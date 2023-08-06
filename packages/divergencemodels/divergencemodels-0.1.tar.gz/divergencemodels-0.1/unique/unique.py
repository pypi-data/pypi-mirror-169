from collections import defaultdict
from sklearn.preprocessing import LabelEncoder
from scipy.stats import entropy
from scipy.stats import norm
from numpy.linalg import norm
import plotly.express as px

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class UniqueMerchant(object):
    def __init__(self, global_df):
        self.global_df = global_df

    def outlier_removal(self, dataframe, column: str):

        """
        Outlier remvoal using IQR 

        Args:
            Dataframe: Datframe Object
            Column: Name of the Column that undergoes outlier removal
        Returns:
            Dataframe withouts rows that are removed from IQR computation

        """        
        p75, p25 = dataframe[column].quantile(0.75), dataframe[column].quantile(0.25)
        iqr = p75 - p25
        high, low = p75 + 1.5 * iqr, p25 - 1.5 * iqr

        outlier_filtered = dataframe[(dataframe[column] < high) & (dataframe[column] > low)]
        filtered_percentage = outlier_filtered[column].value_counts()/len(outlier_filtered)

        total_len = len(dataframe)

        #If outlier filtering results in the loss of more than 50% of dataset or random variables less or equal to 5 dont perform outlier filtering
        if (len(outlier_filtered)/total_len) <= 0.5 or len(dataframe[column].value_counts()) <=5:
            if (dataframe[column].value_counts()/len(dataframe)).values[0] >= 0.9:
                return dataframe[dataframe[column] == (dataframe[column].value_counts()/len(dataframe)).index[0]]
            return dataframe
        
        if filtered_percentage.values[0] >= 0.9:
            return outlier_filtered[outlier_filtered[column] == filtered_percentage.index[0]]
        
        return outlier_filtered

    def oversampling(self, df1, df2):

        """ 
        Oversampling the merchant with smaller sample size
        Sampling from uniform distribution to maintain the dataset ratio
        
        Args:
            df1: First Dataframe
            df2: Second Dataframe
        Returns:
            sampled: Oversampled dataset (Equal size as the larger )
            l[idx_large]: Standard sample dataset
        """
        df1 = df1.reset_index(drop = True)
        df2 = df2.reset_index(drop = True)

        l = [df1, df2]
        size = [len(i) for i in l]
        idx_large = size.index(max(size))
        idx_small = size.index(min(size))
        
        difference = size[idx_large] - size[idx_small]

        generate_index = np.random.choice(np.arange(0,size[idx_small]), size = (difference,))

        sampled = l[idx_small].loc[generate_index, :]
        sampled = pd.concat([l[idx_small], sampled])

        return sampled, l[idx_large]

    def kl(self,p, q):

        """
        KL Divergence computation

        Args:
            p: PDF for first distribution
            q: PDF for second distribution
        Returns:
            Similarity measure between p and q distributions
            (P|Q) != (Q|P)
        """
        return np.sum(np.where(p != 0, p * np.log(p / q), 0))

    def jsd(self,p, q):

        """
        Jensen Shannon divergence computation

        Args:
            p: PDF for fist distribution
            q: PDF for second distribution
        Returns:
            Distance measure between two distributions 
            (P|Q) == (Q|P)
        """
        p = p / norm(p, ord=1)
        q = q / norm(q, ord=1)
        m = 0.5 * (p + q)
        return 0.5 * (entropy(p, m) + entropy(q, m))
    
    def encoder(self, dataframe1, dataframe2):
        for i in dataframe1.columns:
            if dataframe1[i].dtypes != 'O':
                continue                
            random_vars = set(np.concatenate([ dataframe1[i].unique() , dataframe2[i].unique() ]))
            random_vars = np.array([i for i in random_vars])

            lb = LabelEncoder()
            lb.fit(random_vars)
            
            dataframe1[i] = lb.transform(dataframe1[i])
            dataframe2[i] = lb.transform(dataframe2[i])

        return dataframe1, dataframe2
    
    def p_distribution(self, dataframe, bin):
        return np.histogram(dataframe, bins = bin, density = True)

    
    def divergence(self, merchant1, merchant2, return_normalized = False):

        def sort_dict(dictionary, rev = False):
            #Sorting Dictionary function 
            return {k:v for k,v in sorted(dictionary.items(), key = lambda item: item[1], reverse= rev)}
        
        def rv_difference(large_df, small_df, col ,for_large = False):
            if for_large:
                rv_difference = list(set(small_df[col]) - set(large_df[col]))
                rv_difference = pd.Series(np.asarray(rv_difference))
                return rv_difference
            else:
                rv_difference = list(set(large_df[col]) - set(small_df[col]))
                rv_difference = pd.Series(np.asarray(rv_difference))
                return rv_difference
             

        self.merchant1 = self.global_df[self.global_df.AppMerchantGroup == merchant1].drop(['AppMerchantGroup', 'AppMerchantIndustry', 'CustomerID'], axis=1)
        self.merchant2 = self.global_df[self.global_df.AppMerchantGroup == merchant2].drop(['AppMerchantGroup', 'AppMerchantIndustry', 'CustomerID'], axis=1)
        
        assert len(self.merchant1.columns) == len(self.merchant2.columns)
        # assert len(self.merchant1.isnull().sum()) == 0 or len(self.merchant1.isnull().sum() == 0)

        #Drop Null values
        self.merchant1.dropna(inplace = True)
        self.merchant2.dropna(inplace = True)
        
        lowest_float = 2.2250738585072014e-308
        #Score Hasmap
        kl_score = {}
        js_score = {}

        merchant1_encode, merchant2_encode = self.encoder(self.merchant1, self.merchant2)
        
        self.valid = {}
        self.df = {}

        for col in self.merchant1.columns:
            m1, m2 = self.outlier_removal(merchant1_encode, col), self.outlier_removal(merchant2_encode, col)
            m1_over, m2_over = self.oversampling(m1, m2)
            
            #Either Larger RV column or Smaller RV Column
            large_rv_df = m1_over if len(m1_over[col].value_counts()) >= len(m2_over[col].value_counts()) else m2_over
            small_rv_df = m2 if len(m1[col].value_counts()) >= len(m2[col].value_counts()) else m1
            
            #Condition for random variables for continuous variables
            if len(m1_over[col].value_counts()) > 20 and m1_over[col].dtype == 'float':
                #For Continuous variables, choose the one with lower rv 
                bin = int(2 * np.cbrt(len(small_rv_df)))
            else:
                #Discrete Cases
                bin = large_rv_df[col].nunique()
            
            #Always the bigger df chosen
            

            #Adding one to the bin count
            small = rv_difference(large_rv_df, small_rv_df, col ,for_large= False)
            large = rv_difference(large_rv_df, small_rv_df, col, for_large= True)
            small_rv_df = pd.concat([small_rv_df[col], small])
            large_rv_df = pd.concat([large_rv_df[col], large])

            self.df[col] = [small_rv_df, large_rv_df]
            #Compute the Probability Distrution function

            pdf1, bin1 = self.p_distribution(large_rv_df, bin)
            p = pdf1 * np.diff(bin1)
            
            pdf2, bin2 = self.p_distribution(small_rv_df, bin1)
            q = pdf2 * np.diff(bin2)

            self.valid[col] = ([p, bin1], [q, bin2])

            #Replace 0 with lowest float (To avoid calculation error in Divergence)
            p[p == 0] = lowest_float
            q[q == 0] = lowest_float
            #calculate jenson shannon divergence
            js = self.jsd(p,q)
            js_score[col] = js

            #Compute both KLD(P||Q) and KLD(Q||P)
            pq, qp = self.kl(p,q), self.kl(q,p)
            # avg = (pq + qp)/2

            kl_score[col] = pq if pq < qp else qp

        if return_normalized:
            w_kl = (list(kl_score.values())/  np.array(list(kl_score.values())).sum())*100
            w_kl = {k:v for k, v in zip(list(kl_score.keys()), w_kl)}
            w_js = (list(js_score.values())/ np.array(list(js_score.values())).sum())*100
            w_js = {k:v for k, v in zip(list(js_score.keys()), w_js)}
            return sort_dict(w_kl, rev = True), sort_dict(w_js, rev = True)
        
        return sort_dict(kl_score, rev=True) , sort_dict(js_score, rev = True)
    
    def validation(self, return_dataframe = False):
        if return_dataframe:
            return self.merchant1, self.merchant2
        return self.valid, self.df


    def compare_graph(self,column1:str, column2:str ,hist = True):
        lowest_float = 2.2250738585072014e-308

        if hist == True:
            #plotting the higher weight column
            plt.figure(figsize=(12,10))
            sns.distplot(self.merchant1[column1], norm_hist =True, kde = True)
            sns.distplot(self.merchant2[column1], norm_hist =True,color = 'red', kde=True, )
            plt.show()

            #lower weight column
            plt.figure(figsize=(12,10))
            sns.distplot(self.merchant1[column2], norm_hist =True,kde = True)
            sns.distplot(self.merchant2[column2], norm_hist =True,color = 'red', kde=True)
            plt.show()
        else:
            sns.boxplot(self.merchant1[column1])
            plt.show()
            sns.boxplot(self.merchant2[column1])
            plt.show()

            sns.boxplot(self.merchant1[column2], color = 'red')
            plt.show()
            sns.boxplot(self.merchant2[column2], color = 'red')
            plt.show()
    
    def merchant_heatmap(self, main_merchant:str, other_merchants:list, divergence_type:str):        
        unique = []
        for merchant in other_merchants:
            if divergence_type == 'KL':
                kl = self.divergence(main_merchant, merchant)[0]
                unique.append(kl)
            elif divergence_type == 'JS':
                js = self.divergence(main_merchant,merchant )[-1]
                unique.append(js)
        
            #Merging dicts (one for each merchant)
        d = defaultdict(list)
        for i in unique:
            for k,v in i.items():
                d[k].append(v)

        #Dict into Dataframe
        final = dict(d)
        df = pd.DataFrame.from_dict(data = final)
        df['Index'] = other_merchants
        #setting index
        data_matrix = df.set_index('Index')

        fig = px.imshow(data_matrix,aspect='atuo', labels=dict(x = 'Features', y='Merchants'),width=1200, height=1000)
        fig.show() 
        

            

        


