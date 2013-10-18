import numpy as np

# classifier A
def A(x,(a)):
	assert(a[0] > 0)
	return a[0]**x[0] > x[1]	
	
# classifier B
def B(x,(w,b)):
	return np.dot(w,x) + b > 0

# classifier C
def C(x,(c,r,p)):
	assert(p == 1 or p == 2)
	assert(r > 0)
	return (np.abs(x-c)**p).sum() >= r**p

# classifier D
def D(x,(A,w,b)):
	assert(A.shape == (2,2))
	return (np.dot(np.dot(np.transpose(x),A),x) + np.dot(w,x) + b) > 0 

# classifier "ring"
#  x: data point
#  c: center of the ring
#  r: radius of the ring
#  w: width of the ring
def ring(x,(c,r,w)):
	assert(r > 0)
	assert(w < r)
	return C(x,(c,r-w,2)) and (not C(x,(c,r+w,2)))

def point(x,(p)):
	return not(np.array(x) == p).all()

# classifier "triangle"
#  x: data point
#  c: center of the rectangle
#  s: size of the rectangle
def rect(x,(c,s)):
	vertical = B(x,(np.array([1,0]),s[0] / 2 - c[0])) and B(x,(np.array([-1,0]),s[0] / 2 + c[0]))
	horizontal = B(x,(np.array([0,1]),s[1] / 2 - c[1])) and B(x,(np.array([0,-1]),s[1] / 2 + c[1]))
	return horizontal and vertical








