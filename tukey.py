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
from statsmodels.stats.multicomp import (pairwise_tukeyhsd,
                                        MultiComparison)
import matplotlib.pyplot as plt

class PairwiseTukey:

    def __init__(self, a=0.05, df=None, x=None, y=None, verbose=False):
        """Constructor

        Keyword arguments:
        a -- alpha
        df -- data
        x -- label for x
        y -- label for y
        """
        if df == None:
            df = np.rec.array([
                (  1,   'mental',  2 ),
                (  2,   'mental',  2 ),
                (  3,   'mental',  3 ),
                (  4,   'mental',  4 ),
                (  5,   'mental',  4 ),
                (  6,   'mental',  5 ),
                (  7,   'mental',  3 ),
                (  8,   'mental',  4 ),
                (  9,   'mental',  4 ),
                ( 10,   'mental',  4 ),
                ( 11, 'physical',  4 ),
                ( 12, 'physical',  4 ),
                ( 13, 'physical',  3 ),
                ( 14, 'physical',  5 ),
                ( 15, 'physical',  4 ),
                ( 16, 'physical',  1 ),
                ( 17, 'physical',  1 ),
                ( 18, 'physical',  2 ),
                ( 19, 'physical',  3 ),
                ( 20, 'physical',  3 ),
                ( 21,  'medical',  1 ),
                ( 22,  'medical',  2 ),
                ( 23,  'medical',  2 ),
                ( 24,  'medical',  2 ),
                ( 25,  'medical',  3 ),
                ( 26,  'medical',  2 ),
                ( 27,  'medical',  3 ),
                ( 28,  'medical',  1 ),
                ( 29,  'medical',  3 ),
                ( 30,  'medical',  1 )], dtype=[('idx', '<i4'),
                                                ('Treatment', '|S8'),
                                                ('StressReduction', '<i4')])
            x = 'StressReduction'
            y = 'Treatment'

        self.a = a
        self.df = df
        self.x = x
        self.y = y

        if verbose:
            self.report()
    
    def tukey_pairwise(self, reuse=True, a=0.05, df=None, x=None, y=None):
        """Gets the tukey HSD Score using pairwise_tukeyhsd"""
        if reuse:
            a = self.a
            df = self.df
            x = self.x
            y = self.y
        
        output = pairwise_tukeyhsd(df[x], df[y], a)
        return output
    
    def tukey_mcompare(self, reuse=True, a=0.05, df=None, x=None, y=None):
        """Gets the tukey HSD Score using MultiComparison"""
        if reuse:
            a = self.a
            df = self.df
            x = self.x
            y = self.y
        
        output = MultiComparison(df[x], df[y])
        output = output.tukeyhsd(alpha=a)
        return output
    
    def report(self):
        print('Pairwise')
        output = self.tukey_pairwise(True, self.a, self.df, self.x, self.y)
        print(output)
        print()

        print('MultiComparison')
        output = self.tukey_mcompare(True, self.a, self.df, self.x, self.y)
        print(output)
        print()

    def demo(self):
        output = self.tukey_mcompare()
        df = pd.DataFrame(data=output._results_table.data[1:], 
                            columns=output._results_table.data[0])

        # Plotting Option 1
        output.plot_simultaneous(comparison_name=df['group1'].iloc[0])
                
        
        # Plotting Option 2
        '''                    
        for lower, upper, y in zip(df['lower'], df['upper'], range(len(df))):
            plt.plot((lower, upper), (y,y), 'ro--', color='orange')
        '''
        plt.show()
        
    def information(self):
        """Describes the purpose of the pairwise Tukey HSD"""
        description = "Pairwise Turkey HSD = post hoc test to determine differences between all pairings of groups simultaneously)"
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
    if len(sys.argv) > 1:
        a = float(sys.argv[1])
    else:
        a = 0.05
    
    tukey = PairwiseTukey(a, verbose=True)
    tukey.demo()