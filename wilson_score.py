"""
References: 
https://www.mikulskibartosz.name/wilson-score-in-python-example/
https://www.simplypsychology.org/confidence-interval.html#:~:text=The%20confidence%20interval%20(CI)%20is,an%20upper%20and%20lower%20interval.
https://www.ucl.ac.uk/english-usage/staff/sean/resources/wilson-distribution.pdf
"""

import sys
import math

class WilsonScore:

    def __init__(self, p, n, z=1.96):
        """Constructor

        Keyword arguments:
        p -- sample proportion (e.g passing)
        n -- sample size
        z -- expected confidence interval of Wilson score as a z-score (e.g. 95% = 1.96)
        """
        self.p = p
        self.n = n
        self.z = z
    
    def wilson(self):
        """ Gets the Wilson Score (range of possible proportions)."""
        p = self.p
        n = self.n
        z = self.z

        denominator = 1 + z**2 / n
        center_adjusted_probability = p + z * z / (2 * n)
        adjusted_standard_deviation = math.sqrt((p * (1 - p) + z * z / (4 * n)) / n)
        lower_bound = (center_adjusted_probability - z * adjusted_standard_deviation) / denominator
        upper_bound = (center_adjusted_probability + z * adjusted_standard_deviation) / denominator
        return lower_bound, upper_bound

    def information(self):
        """Describes the purpose of the Wilson Score"""
        description = "Wilson Score - estimates population probability; Proportion of an outcome for a binomial distribution (two possibilities, e.g. pass or fail)"
        confidence_interval = "Confidence Interval - a range of values that's likely to include a population value with a certain degree of confidence"
        print(description)
        print(confidence_interval)

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
    
    wilson = WilsonScore(p, n, z)
    lower_bound, upper_bound = wilson.wilson()
    print("(%0.3f, (%0.3f, %0.3f)" % (p, lower_bound, upper_bound))