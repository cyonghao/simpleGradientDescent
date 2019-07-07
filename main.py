'''
Assume finding relationship between height and weight of people based on 3 data points
y-axis = height
x-axis = weight
(x, y)
(0.5, 1.4)
(2.3, 1.9)
(2.9, 3.2)
'''

data = [(0.5, 1.4), (2.3, 1.9), (2.9, 3.2)]

learningRate = 0.01
slope = 1
intercept = 0
derIntercept = 0
derSlope = 0
tries = 1
sumError = 1

while sumError > 0.45:
    sumError = 0
    for point in data:
        actualY = point[1]
        x = point[0]
        sumError += (actualY - (slope*x + intercept))**2
        # partial derivative of squared error with respect to intercept
        derIntercept += -2 * (actualY - (slope*x + intercept))
        # partial derivative of squared error with respect to slope
        derSlope += (-2*x) * (actualY - (slope*x + intercept))

    print(f"sum of error: {sumError}")
    stepSizeIntercept = derIntercept * learningRate
    stepSizeSlope = derSlope * learningRate
    print(f"sum of stepSizeSlope: {stepSizeSlope}")

    intercept = intercept - stepSizeIntercept
    slope = slope - stepSizeSlope

    tries += 1

print(f"sum of slope: {slope}")
print(f"sum of intercept: {intercept}")
print(f"sum of tries: {tries}")