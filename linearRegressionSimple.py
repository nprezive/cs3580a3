import numpy as np
import matplotlib.pyplot as plt

length = [94,74,147,58,86,94,63,86,69,72,128,85,82,86,88,72,74,61,90,89,68,76,114,90,78]
weight = [130,51,640,28,80,110,33,90,36,38,366,84,80,83,70,61,54,44,106,84,39,42,197,102,57]


fit = np.polyfit(length,weight,1)
fit_fn = np.poly1d(fit) 
# fit_fn is now a function which takes in x and returns an estimate for y

plt.plot(length,weight, 'yo', length, fit_fn(length), '--k')
plt.show()