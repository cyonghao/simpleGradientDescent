#Implementation of Gradient Descent on Linear Regression

##Intro to Gradient Descent
- y = mx + b
- m = slope
- b = intercept
- m, b = unknowns
- finding line of best fit on set of data points
- gradient descent = adjusting values of m, b using partial derivatives, step size to get to optimal (local minima) = sum of squared errors closest to 0
- using gradient to descend to the lowest point in the loss function (sum of the squared residuals)
- gradient descent will stopped when either the step size is very small or completes number of tries specified

##Steps of Gradient Descent
1. find partial derivative form of linear line
2. initialise random m, b values
3. calculate partial derivative with respect to m, b
4. calculate new step size with respect to m, b
5. repeat step 3 to 5 until either step size is very small or completes number of tries specified