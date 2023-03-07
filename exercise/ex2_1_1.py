
import numpy as np
import xlrd
doc = xlrd.open_workbook('data/nanonose.xls').sheet_by_index(0)

attributeNames = doc.row_values(0, 3, 11)

classLabels = doc.col_values(0, 2, 92)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(5)))

y = np.asarray([classDict[value] for value in classLabels])

# Preallocate memory, then extract excel data to matrix X
X = np.empty((90, 8))
for i, col_id in enumerate(range(3, 11)):
    X[:, i] = np.asarray(doc.col_values(col_id, 2, 92))
N = len(y)
M = len(attributeNames)
C = len(classNames)
