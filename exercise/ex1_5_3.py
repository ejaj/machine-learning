import numpy as np
from scipy.io import loadmat
iris_mat = loadmat('data/iris.mat', squeeze_me=True)
X = iris_mat['X']
y = iris_mat['y']
M = iris_mat['M']
N = iris_mat['N']
C = iris_mat['C']
attributeNames = iris_mat['attributeNames']
classNames = iris_mat['classNames']
