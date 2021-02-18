"""
Crowd Computing:
Proposed by Francis Galton
The wisdom of crowd is the collective opinion of a group of individuals rather than that of a single expert.
A large group's aggregate answers to questions involving quantity estimation, general world knowledge, and spatial
reasoning has generally been found to be as good as, but often superior to, the answer given by any of the individuals
within the group.

Collective opinion > Expert opinion

Trimmed Mean:
* 10% Trimmed mean
* Remove 10% smallest and 10% largest values from the sample.
* Calculate the mean of the sample obtained.
"""

from statistics import mean
import statistics
from scipy import stats
import matplotlib.pyplot as plt

Estimates = [1570, 275, 350, 150, 1500, 650, 321, 958, 654, 325, 451, 987, 1005, 1500, 1200, 275, 561, 350, 251, 250,
             156, 987, 2000, 360, 650, 351, 200, 150, 650, 750, 985, 850, 1300, 1200, 1550, 654, 330, 375, 456, 450,
             275, 350, 150, 1500, 650, 321, 958, 654, 325, 451, 987, 1005, 1500, 1200, 275, 561, 350, 360, 890, 750,
             156, 987, 2000, 360, 750, 985, 850, 1300, 1200, 1550, 654, 330, 375, 456, 450]
Estimates.sort()

# Method - 1  from scipy import stats
m = stats.trim_mean(Estimates, 0.1)
print(m)

# Method -2  from statistics import mean
tv = int(0.1 * len(Estimates))  # tv - trimmed value
Estimates = Estimates[tv:]
Estimates = Estimates[:len(Estimates) - tv]
print(mean(Estimates))

# plt.plot([1, 2, 3, 4])  # In python, it automatically generates x values if we don't pass any
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g^')
# plt.ylabel("Squares")
# plt.xlabel("Numbers")
# plt.show()

y = []
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates, y, 'r--')
plt.plot([statistics.mean(Estimates)], [5], 'b+')
plt.plot([statistics.median(Estimates)], [5], 'b+')
plt.plot([375], [5], 'g^')

plt.show()


