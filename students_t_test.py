"""
Student's T Test

References
- https://www.youtube.com/watch?v=pTmLQvMM-1M
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html
- https://pdf.sciencedirectassets.com/272610/1-s2.0-S0741521400X00249/1-s2.0-S0741521402000307/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLWVhc3QtMSJGMEQCIEMLn%2FILeSpazr6P5rCpASekrSdGDPqWb060kIU8wbJAAiBGnNyHBwOmARxWmKgmGKRq36gfdBYkrkrk7cZLFLUMiCr6Awh3EAQaDDA1OTAwMzU0Njg2NSIMTTT7ZsnOWU3CHC7fKtcDoKYZXGLaUjVxop1kgvIFmKNDqBWL%2FkgXySa2EZQLGejMnX6t%2FsAQg08JW6U3uo1R5Ff124rJ2U3pSz6kT5%2F37HsVEg%2BxuweF6M%2FA%2Bqb8XsdWCw5nbyRl%2B3997F0zYgURLiSHQ%2F89h0FxdNAgjyLmVuU%2Fz5pfGLAjgnH9XD7DS5Ymtl4kLAfrqCwrbNgJM16I8APsBRyWeg04o2JHWTNDTEAvcEAOrjKc50ucIa97xiktgVwVxm42YwN2eK4Q%2BYC0FJI48m%2BQMWcsVUexgp8WIDXQccwMbN2DdKht9A1JmjrQsySyzETf4zDI0R5Uy3FqT8Wqk0e9DOhurehpOR5Fqpkq1a8OTYukfiiGDCajyFkmXja8ncdgvQ19SZrNwzSnxsZwW93x%2BKM7Y3pogJnT5aRF6%2BEd7YvHZt2KNMjdyYAh0Ffn83vAoQOPZTRySVPh%2FLFDHCrIR7d%2B7XsqrxIQmYXqZOYk3DhmNINTf207jutSen21b62KJRGrz00tR3T7U%2BLvSCFZnby41hyc3r%2F3RtmZyBfP%2FjXilYoU2KfC%2F2veW2IkXKvcHq%2BfRq%2BVUUwpPmkxkWAQui9xXPQlfgfLHdWI%2Fd3Tr7MQhRNPd2LRrlYH86W%2FTB6IMPXPuo8GOqYB9KPRVt5A2%2B74rTaZVf8Nxl8WF2grqDBeMpfBxDK4JsQ1tUrAW6%2BGgTS%2BxOcMqN7v1AxSEtDzd6SKBVyGu%2Bf%2B2i%2FbRsqZEyhv%2Fds3wMilkWhHJ664pdxNYcHRuFaqoxeC6JNQNx7AytfY4waTsaMGdrNNeS6Y7HiQr23ND47wDi8lhn6lZ80f9XMELq5IoJvwbML%2FxqUXa%2FwXp%2FXozhTj2ilTae9mlQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220124T145425Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXFBB66VI%2F20220124%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=fbc08b5d5be351cc199968847c834c156ae6637ea746a616a5ac300b806fed10&hash=a9ddf209a644bbfb8d7ac9a3c984693a4ad58d699ef4305b74860402440958fd&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0741521402000307&tid=spdf-d327446a-6d91-45c2-af5d-d3409555afdd&sid=b81c187a3491a54691788445d5256ed2d7e7gxrqa&type=client
"""

import scipy.stats as stats
from scipy.stats import ttest_ind
from scipy.stats import norm
from scipy.stats import levene
from scipy.stats import shapiro
import numpy as np
from matplotlib import pyplot as plt
import math

class StudentsT:

    def __init__(self, sampleA=None, sampleB=None, verbose=False):
        """Constructor"""
        self.sampleA = sampleA
        self.sampleB = sampleB

        if verbose:
            self.report()

    def verify(self):
        """Confirm applicability of use of student's t test"""
        alpha = 0.05

        # Sample Size

        # Homogeneity of Variance
        statisticsh, ph = levene(y1, y2, center='median')

        # Normality: normally distributed
        statisticn1, pn1 = shapiro(self.sampleA)
        statisticn2, pn2 = shaprio(self.sampleB)

        if ((ph < alpha) & (pn1 > alpha) & (pn2 > alpha)):
            return True
        else:
            return False

    def pvalue(self)
        """Calculates p value of students t test"""
        statistics, p = ttest_ind(self.sampleA, self.sampleB)
        return p

    def report(self):
        """Print output of students t test"""
        p = self.pvalue()
        print("0.2f%" % (t))

    
    def demo(self):
        """Demonstrates the distributions of significant difference using student's t test"""
        n = 200
        ms1 = [10, 10, 10, 30]
        ms2 = [30, 30, 10, 30]
        s1s = [300, 15, 8, 8]
        s2s = [300, 15, 3, 3]
        xslower = [-1000, -50, -50, -50]
        xsupper = [1000, 150, 150, 150]
        ns = [3*n, n, 2*n, 2*n]
        titles = ['Require higher variance to overcome differences in central tendency',
                    'Insufficient ',
                    '',
                    '']

        rows = 2
        cols = int(len(ms1)/rows)
        fig, axs = plt.subplots(rows, cols, figsize=(15,8))
        axs = axs.flatten()

        for i in range(len(ms1)):
            m1 = ms1[i]
            s1 = s1s[i]
            m2 = ms2[i]
            s2 = s2s[i]
            n = ns[i]

            x = np.linspace(xslower[i], xsupper[i], n)
            y1 = norm.rvs(m1, s1, n)
            y2 = norm.rvs(m2, s2, n)
            pdf1 = norm.pdf(x, m1, s1)
            pdf2 = norm.pdf(x, m2, s2)
            axs[i].plot(x, pdf1, label="(%d, %i)" %(m1, s1))
            axs[i].plot(x, pdf2, label="(%d, %i)" %(m2, s2))

            std_lim = 1.96
            low1 = m1 - std_lim * s1
            low2 = m2 - std_lim * s2
            high1 = m1 + std_lim * s1
            high2 = m2 + std_lim * s2
            axs[i].fill_between(x, pdf1, where=(low1 < x) & (x < high1), alpha=0.8)
            axs[i].fill_between(x, pdf2, where=(low2 < x) & (x < high2), alpha=0.5)

            statistics, p = ttest_ind(y1, y2)
            t = (m2-m1)/np.sqrt((s1**2/n)+(s2**2/n))
            statisticsh, ph = levene(y1, y2, center='median')
            axs[i].text(0.8, 0.8, "p: %0.3f\nt: %0.3f\nLevene p:%0.3f" %(p, t, ph),  transform=axs[i].transAxes)
            axs[i].legend(loc="upper left")
            axs[i].set_title(titles[i])
        fig.suptitle("Student's T Test: Significance")
        plt.show()

    def demo2(self):
        xslower = -1000
        xsupper = 1000
        m1 = 30
        m2 = 10
        s1 = 300
        s2 = 300
        n = 200
        x = np.linspace(xslower, xsupper, n)
        y1 = norm.rvs(m1, s1, n)
        y2 = norm.rvs(m2, s2, n)

        std_lim = 1.96
        low1 = m1 - std_lim * s1
        high1 = m1 + std_lim * s1

        mdiff = m1 - m2
        pooledstd = np.sqrt((s1**2 + s2**2)/2)

        pdf = norm.pdf(x, mdiff, pooledstd)
        plt.plot(x, pdf)
        plt.fill_between(x, pdf, where=(low1 < x) & (x < high1), alpha=0.8)
        plt.show()

if __name__ == "__main__":
    student = StudentsT()
    #student.demo()
    student.demo2()