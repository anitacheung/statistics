"""
Linear Regression

References: 

"""

import sys
import math
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class LinReg:

    def __init__(self, df=None, x=None, y=None, verbose=False):
        """Constructor

        Keyword arguments:
        a -- alpha
        df -- data
        x -- label for x
        y -- label for y
        """
        if df == None:
            df = sns.load_dataset('anscombe').query("dataset=='I'")
            x = 'x'
            y = 'y'

        self.df = df
        self.x = x
        self.y = y

        if verbose:
            self.report()
    
    def linregress_scipy(self, reuse=True, df=None, x=None, y=None):
        """Gets the linear regression equation using scipy"""
        if reuse:
            df = self.df
            x = self.x
            y = self.y
        
        output = stats.linregress(df[x], df[y])
        return output
    
    def linregress_smodels(self, reuse=True, df=None, x=None, y=None):
        """Gets the linear regression equation using statsmodels"""
        if reuse:
            df = self.df
            x = self.x
            y = self.y
        
        x = df[x].to_numpy().reshape((-1,1))
        y = df[y].to_numpy()
        output = LinearRegression().fit(x, y)
        return output
    
    def report(self):
        print('Scipy')
        output = self.linregress_scipy(True, self.df, self.x, self.y)
        print('r^2: %0.2f, y = %0.2fx + %0.2f'% (output[2], output[0], output[1]))
        print()

        print('Statsmodels')
        output = self.linregress_smodels(True, self.df, self.x, self.y)
        x = self.df[self.x].to_numpy().reshape((-1,1))
        y = self.df[self.y].to_numpy()
        print('r^2: %0.2f, y = %0.2fx + %0.2f' % (output.score(x, y),
                output.coef_, output.intercept_))
        print()

    def demo(self):
        output = self.linregress_scipy()
        x = self.df[self.x]
        y = output[0] * x + output[1]

        
        sns.regplot(data=self.df, x=self.x, y=self.y)
        sns.lineplot(x, y, color='red', linestyle='--')
        
        plt.show()
        
    def information(self):
        """Describes the purpose of the linear regression"""
        description = "Linear regression describes a relationship between x and y using y = mx+b"
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
    print(sys.argv)
    
    linreg = LinReg(verbose=True)
    linreg.demo()