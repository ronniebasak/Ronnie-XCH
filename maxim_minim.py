from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math




def LocalMax(nums, a):
	#nums is a nparray
	nums = np.array(nums)
	ndiff = np.diff(nums)
	ndiff = np.sign(ndiff)
	n2diff = np.diff(ndiff)
	n2max = np.where(n2diff==-2)
	n2v = np.array( [ nums[x] for x in n2max ][0] )
	n2max = np.array( [ a[x] for x in n2max ][0] )
	#print n2v[0]
	return n2max, n2v
	
def LocalMin(nums, a):
	#nums is a nparray
	nums = np.array(nums)
	ndiff = np.diff(nums)
	ndiff = np.sign(ndiff)
	n2diff = np.diff(ndiff)
	#print n2diff
	n2min = np.where(n2diff==2)
	n2v = np.array( [ nums[x] for x in n2min ][0] )
	n2min = np.array( [ a[x] for x in n2min ][0] )
	#print n2v[0]
	return n2min, n2v



a = np.arange( -math.pi, 3*math.pi, 1/50)
b = np.sin(a)

#print LocalMax(b)

plt.plot(a,b, "g-")

n2max, n2v = LocalMax(b, a)
#print n2max, n2v
plt.plot(n2max, n2v, "ro")

n2min, n2v = LocalMin(b, a)
print n2min, n2v
plt.plot(n2min, n2v, "bo")

plt.axis([-5,11,-6,6])
plt.show()
