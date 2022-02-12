"""
ANOVA (Analysis of Variance)

References: 
"""

import sys
import math
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

class ANOVA:

    def __init__(self, df=None, x=None, y=None, verbose=False):
        """Constructor

        Keyword arguments:
        df -- data
        x -- label for x (array)
        y -- label for y
        """
        if df == None:
            df = sm.datasets.statecrime.load_pandas()
            df = df.data
            x = ['hs_grad', 'urban', 'poverty', 'single']
            y = 'murder'
        
        self.df = df
        self.x = x
        self.y = y

        if verbose:
            self.report()
    
    def anova(self, reuse=True, df=None, x=None, y=None):
        """Gets the ANOVA p-value using sm.stats.anova_lm"""
        if reuse:
            df = self.df
            x = self.x
            y = self.y
        
        print(df)
        model_val = y + ' ~'
        for val in x:
            model_val += val + ' +'
        model_val = model_val[:-1]
        model = ols(model_val, data=df).fit()
        table = sm.stats.anova_lm(model, typ=2)
        return model, table
        
    
    def report(self):
        model, table = self.anova()

        # Print output
        print(model.summary())
        print()
        print(table)

        # Saves figures
        fig = plt.figure(figsize=(8, 6))
        sm.graphics.plot_regress_exog(model, 'poverty', fig=fig)

    def demo(self):
        fig = plt.figure(figsize=(8, 6))
        model, table = self.anova()
        sm.graphics.plot_regress_exog(model, 'poverty', fig=fig)
        plt.show()
        
    def information(self):
        """Describes the purpose of the ANOVA"""
        description = "ANOVA identifies if the differences between groups of data are statistically significant"
        tolerances = ""
        requirements = ""
        auxiliary = ""
        print(description)
        print("\nTolerances:")
        print(tolerances)
        print("\nRequirements:")
        print(requirements)
        print("\nOther Notes:")
        print(auxiliary)

if __name__ == "__main__":
    anova = ANOVA(verbose=True)
    anova.demo()