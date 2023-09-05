# arrange()
# range (start, stop)
import numpy as np

a = np.arange(1, 11)
print(a)

# 1-20 ---> 2 d (5*4)
b=np.arange(1,21)
# a= np.arange(1,21).reshape([5,4])
c=b.reshape([5,4])
print(c)
