import classifiers,matplotlib,data

import matplotlib.pyplot as plt
import numpy as np

# plot the dataset in "data.py"
def plot(X,T):
	plt.figure()
	plt.plot(X[T==True ,0],X[T==True ,1],'o',color='blue')
	plt.plot(X[T==False,0],X[T==False,1],'s',color='red')
	plt.legend(['t=1','t=-1'])
	plt.xlabel('x1')
	plt.ylabel('x2')
	plt.axis([-5,5,-5,5])
	plt.savefig('plot.png')

# find parameters {c,r,p} that  
def learn(X,T):
	classify = classifiers.B

	params = []
	# TODO: complete this list with more possible parameters
	#       hint:
	#        use nested loops to generate a large number
	#        of candidate parameters

	for param in params:

		# return parameter if it satisfies data
		if np.all([classify(x,param)==t for x,t in zip(X,T)]): return param
			
			

plot(data.X,data.T)


param = learn(data.X,data.T)
print("Learned parameter: ",param)

