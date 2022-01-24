"""
Wilson Score

References: 
https://www.mikulskibartosz.name/wilson-score-in-python-example/
https://www.simplypsychology.org/confidence-interval.html#:~:text=The%20confidence%20interval%20(CI)%20is,an%20upper%20and%20lower%20interval.
https://www.ucl.ac.uk/english-usage/staff/sean/resources/wilson-distribution.pdf
"""

import sys
import math
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

class WilsonScore:

    def __init__(self, p=737/989, n=989, z=1.96, verbose=False):
        """Constructor

        Keyword arguments:
        p -- sample proportion (e.g passing)
        n -- sample size
        z -- expected confidence interval of Wilson score as a z-score (e.g. 95% = 1.96)
        """
        self.p = p
        self.n = n
        self.z = z

        if verbose:
            self.report()
    
    def wilson(self, reuse=True, p=None, n=None, z=None):
        """ Gets the Wilson Score (range of possible proportions)."""
        if reuse:
            p = self.p
            n = self.n
            z = self.z

        denominator = 1 + z**2 / n
        center_adjusted_probability = p + z * z / (2 * n)
        adjusted_standard_deviation = math.sqrt((p * (1 - p) + z * z / (4 * n)) / n)
        lower_bound = (center_adjusted_probability - z * adjusted_standard_deviation) / denominator
        upper_bound = (center_adjusted_probability + z * adjusted_standard_deviation) / denominator
        return lower_bound, upper_bound
    
    def report(self):
        lower_bound, upper_bound = self.wilson()
        print("(p: %0.3f, z: %0.3f (%0.3f, %0.3f)" % (self.p, self.z, lower_bound, upper_bound))

    def demo(self):
        n = 15
        ps = [0.5, self.p]
        zs = [1.28, 1.96]
        confidence = {1.28: "80CI", 1.96: "95CI"}
        r_values = np.arange(n + 1)
        i = 0

        fig, axs = plt.subplots(len(zs), len(ps), figsize=(15,8))
        axs = axs.flatten()

        for z in zs:
            for p in ps:
                binomial = [binom.pmf(k=r, n=n, p=p) for r in r_values]
                lower_bound, upper_bound = self.wilson(False, p, n, z)
                lower_bound *= n
                upper_bound *= n
                axs[i].plot(r_values, binomial)
                axs[i].bar(r_values, binomial, alpha=0.5)
                axs[i].axvline(lower_bound, color='red')
                axs[i].axvline(upper_bound, color='red')
                axs[i].set_title("%s (n = %i, p = %0.2f)" % (confidence[z], n, p))
                i += 1
        fig.suptitle("Wilson Score Demonstration")
        plt.show()

    def information(self):
        """Describes the purpose of the Wilson Score"""
        description = "Wilson Score - asymmetric estimation of confidence interval for binomial distribution (confidence interval of proportion passing)"
        tolerances = "- small samples\n-skewed observations"
        requirements = ""
        auxiliary = "Confidence Interval - a range of values that's likely to include a population value with a certain degree of confidence"
        print(description)
        print("\nTolerances:")
        print(tolerances)
        print("\nRequirements:")
        print(requirements)
        print("\nOther Notes:")
        print(auxiliary)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 3:
        p = float(sys.argv[1])
        n = float(sys.argv[2])
        z = float(sys.argv[3])
    if len(sys.argv) > 2:
        p = float(sys.argv[1])
        n = float(sys.argv[2])
        z = 1.96
    if len(sys.argv) > 1:
        p = float(sys.argv[1])
        n = 989
        z = 1.96
    else:
        p = 737/989
        n = 989
        z = 1.96
    
    wilson = WilsonScore(p, n, z, True)
    wilson.demo()