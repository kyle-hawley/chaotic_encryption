import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
from math import floor

def iterateLogMap(x_n, a):
  return a * x_n * (1 - x_n)

x0 = 0.2
minA = 1
maxA = 4
steps = 1000
beginningBuffer = 1000
numRecordedPoints = 1000

aList = []
xList = []

for a in tqdm(np.linspace(minA, maxA, steps)):
  currentX = x0
  # Go through the buffer points
  for _ in range(beginningBuffer):
    # newX = iterateLogMap(currentX, a)
    newX = iterateLogMap(currentX, a)
    currentX = newX  

    # print(currentX)

  # Record behavior after buffer
  for _ in range(numRecordedPoints):
    # newX = iterateLogMap(currentX, a)
    newX = iterateLogMap(currentX, a)
    aList.append(a)
    xList.append(newX)
    currentX = newX

    # print(currentX)

# s controls the size of the dots
sns.scatterplot(x=aList, y=xList, s=1)
plt.ylim(0, 1)
plt.xlabel("a")
plt.ylabel("x")
plt.show()

# print(set(xList))

sns.histplot(x=xList, bins=256)
plt.show()