"""
Tukey's Honest Significant Difference

References: 
- http://jpktd.blogspot.com/2013/03/multiple-comparison-and-tukey-hsd-or_25.html
- https://sikflow.io/projects/tukey-test
"""

import sys
import math
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.stats import weightstats
from statsmodels.stats.weightstats import (DescrStatsW,
                                            CompareMeans)
import matplotlib.pyplot as plt

class EquivalenceTest:

    def __init__(self, x1=None, x2=None, low=None, upp=None, verbose=False):
        """Constructor

        Keyword arguments:
        x1 -- first independent sample set
        x2 -- second independent sample set
        low -- equivalence interval low
        upp -- equivalence interval high
        """
        if x1 == None:
            df = sns.load_dataset('iris')
            x1 = df['sepal_length'] / 2
            x2 = df['sepal_width']
            low = -0.3
            upp = 0.3

        self.x1 = x1
        self.x2 = x2
        self.low = low
        self.upp = upp

        if verbose:
            self.report()
    
    def equivalence(self, reuse=True, x1=None, x2=None, low=None, upp=None):
        """Gets the equivalence test"""
        if reuse:
            x1 = self.x1
            x2 = self.x2
            low = self.low
            upp = self.upp
        
        output = weightstats.ttost_ind(x1, x2, low, upp)
        return output
    
    def report(self):
        output = self.equivalence(True, self.x1, self.x2, self.low, self.upp)
        p = output[0]
        pl = output[1][1]
        pu = output[2][1]
        print('p-value: %0.3f, \np-value (lower): %0.3f, \np-value(upper): %0.3f' % (p, pl, pu))

    def demo(self):
        output = self.equivalence()

        fig, axs = plt.subplots(1, 2)
        axs = axs.flatten()
        axs[0].hist(self.x1, color='red', alpha=0.5)
        axs[0].hist(self.x2, color='blue', alpha=0.5)

        y = 'CI Difference'
        a = 0.05 * 2
        diff_ci = weightstats.CompareMeans(DescrStatsW(self.x1), DescrStatsW(self.x2))
        diff_ci = diff_ci.tconfint_diff(alpha=a)
        
        axs[1].axvline(self.low, linestyle='--', color='red')
        axs[1].axvline(self.upp, linestyle='--', color='red')
        axs[1].plot((diff_ci[0], diff_ci[1]), (y,y), 'ro--', color='gray')
        axs[1].text(0.3, 0.5, 'CI of Difference: \n(%0.3f, %0.3f)' % (diff_ci[0], diff_ci[1]), transform=axs[1].transAxes)
        fig.tight_layout()
        plt.show()
        
    def information(self):
        """Describes the purpose of the Equivalence Test"""
        description = "Test of (non-) equivalence for two independent samples where test rejects if the 2*alpha confidence interval for the difference is contained in the (low, upp) interval"
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
    
    equiv = EquivalenceTest(verbose=True)
    equiv.demo()