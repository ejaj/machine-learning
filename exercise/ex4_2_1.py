
import numpy as np
import xlrd

doc = xlrd.open_workbook('data/iris.xls').sheet_by_index(0)

attributeNames = doc.row_values(0,0,4)
classLabels = doc.col_values(4,1,151)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames,range(len(classNames))))
y = np.array([classDict[value] for value in classLabels])
X = np.empty((150,4))
for i in range(4):
    X[:,i] = np.array(doc.col_values(i,1,151)).T
N = len(y)
M = len(attributeNames)
C = len(classNames)

