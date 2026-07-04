### Linear regression

## 1. Basic
Model the relationship between a dependent variable and independent variables. 

Minimize square sum of residuals:

$SSE = \sum_{i=1}^n (y_i - \hat{y}_i)^2$

OLS problem: there is a closed-form solution: 

$\beta = \beta = (X^T X)^{-1} X^T y$

Where:
X: features matrix with added column full 1 represent the intercept
y: observed value correspond to each row of feature matrix X

By fitting the data, we can solve for the beta. Then we can use the beta to new data and predict it. 

## 2. Evaluation
There are various metrics to evaluate the algorithm:

2.1 Mean squared error: the most popular one.
$MSE = 1/n \sum_{i=1}^n (y_i - \hat{y}_i)^2$

Good: non negative, easily derived and find maximum/minimum

Bad: sensitive to outlier: since the error is squared, it will affect the sum a lot if the error is large. The unit is squared so cannot be used to compare with the predicting value. 

2.2 Mean absolute error (MAE)

$MAE = \frac {1} {n} \sum_{i=1}^n |y_i - \hat{y}_i|$

Good: same unit with the variable. Robust with outlier. 

Bad: undifferentiable at 0 is a hard challenge for calculation

2.3. Mean percentage error (mape)

$MAPE = \frac {1} {n} \sum_{i=1}^n | \frac {y_i - \hat{y}_i} {y_i} |$

2.4. $R^2$ score
- Coefficient of determination.
- Intuitively, this is the comparison of how a simple estimation model compare with the mse of the model we created. 
- We use a simple estimation model, normally the average of the observed value 
$\bar{y} = \frac {1} {n} \sum_{i=1}^n y_i$ 
- Then compare the mse of the simple model with real value AND mse of our model with real value.
$$
R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
$$
3. Interpreting the evaluation metrics