# Naive method: Multiplying two matrices using nested loops

X = [[1, 2],
     [3, 4]]

Y = [[2, 3],
     [3, 4]]

result = [[0, 0],
          [0, 0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for end in result:
    print(end)
