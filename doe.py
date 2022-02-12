"""
DOE (Design of Experiments)

References:
- https://pythonhosted.org/pyDOE/
- https://en.wikipedia.org/wiki/Box%E2%80%93Behnken_design
"""

import sys
from pyDOE import *
from xml_python import NoneType

class DOE:

    def __init__(self, numLevels=None, verbose=False):
        """Constructor

        Keyword arguments:
        numLevels -- dimensions for factorial (array or generator string)
        """

        self.numLevels = numLevels

        if verbose:
            self.report()

    def full_factorial(self, numLevels=None):
        """"""
        if numLevels == None:
            if self.numLevels == None:
                # Number of levels per factor
                numLevels = [2,3]
            else:
                numLevels = self.numLevels
       
        setup = fullfact(numLevels)
        return setup

    def two_level_full_factorial(self, numLevels=None):
        """"""
        if numLevels == None:
            if self.numLevels == None:
                # Number of factors
                numLevels = 2
            else:
                numLevels = self.numLevels

        setup = ff2n(numLevels)
        return setup
    
    def two_level_fractional_factorial(self, numLevels=None, folding=True, foldcol=None):
        """"""
        if numLevels == None:
            if self.numLevels == None:
                # generator string of symbolic charactors
                numLevels = 'a b ab c ac bc abc'
                foldcol = 2
            else:
                numLevels = self.numLevels

        setup = fracfact(numLevels)

        # Fold to reduce confounding: estimate main effects clear of two-factor interactions
        if folding:
            setup = fold(setup, columns=[foldcol])
        return setup
        
    
    def plackett_burman(self, numLevels=None):
        """
        Plackett Burman (Factorial)

        experimental design where each combination of levels for any pair of factors appears the same number of times, throughout all the experimental runs; multiples of four 
        """
        if numLevels == None:
            if self.numLevels == None:
                # number of factors
                numLevels = 3
            else:
                numLevels = self.numLevels

        setup = pbdesign(numLevels)
        return setup
    
    def box_behnken(self, numLevels=None):
        """
        Box Behnken (Response Surface)
        
        Each factor, or independent variable, is placed at one of three equally spaced values that can fit a quadratic model
        """
        if numLevels == None:
            if self.numLevels == None:
                # numver of factors, number of center points
                numLevels = [4, 1]
            else:
                numLevels = self.numLevels

        setup = bbdesign(numLevels)
        return setup
    
    def central_composite(self, numLevels=None):
        """
        Central Composite (Response Surface)
        """
        if numLevels == None:
            if self.numLevels == None:
                # number of factors, center tuple, 'o':'orthogonal' or 'r':'rotatable'; 'ccc':'circumscribed', 'cci':'inscribed', 'ccf':'faced'
                numLevels = [3, (1,1), 'r', 'cci']
            else:
                numLevels = self.numLevels
        
        setup = ccdesign(numLevels)
        return setup
    
    def randomized_designs(self, numLevels=None):
        """
        Randomized designs (Randomized Design)
        """
        if numLevels == None:
            if self.numLevels == None:
                # number of factors, samples, criterion ('c': 'center'; 'm':'maximin', 'cm':'centermaximin', 'corr':'correlation')
                numLevels = [4, 10, 'center']
            else:
                numLevels = self.numLevels

        setup = lhs(numLevels)
        return setup
    
    def report(self):
        """"""
        if numLevels == None:
            numLevels = self.numLevels

        setup = fullfact(numLevels)

    def demo(self):
        """"""
        print('Full Factorial')
        print(self.full_factorial())
        print()

        print('Two Level Full Factorial')
        print(self.two_level_full_factorial())
        print()

        print('Two Level Fractional Factorial')
        print(self.two_level_fractional_factorial())
        print()

        print('Plackett Burmann')
        print(self.plackett_burman())
        print()

        print('Box Behnken')
        #print(self.box_behnken())
        print()

        print('Composite Design')
        #print(self.central_composite())
        print()

        print('Randomized Design')
        #print(self.randomized_designs())
        print()
    
    def information(self):
        """Describes the purpose of the DOE"""
        description = ""
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
    doe = DOE()
    doe.demo()