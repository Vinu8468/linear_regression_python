def fit_linear_regression(x,y):
    # finds the slope(m) and intercept(c) using the ordinary least square formula.
    n=len(x)

    sumx=sum(x)
    sumy=sum(y)
    sumxy=sum([xi*yi for xi,yi in zip(x,y)])
    sumx2=sum([xi**2 for xi in x])

    # Slope (m)
    m= (n*sumxy -sumx*sumy)/(n*sumx2 - sumx**2)

    # Intercept (c)
    c= (sumy - m*sumx)/n

    return m,c

def predict(x_value,m,c):
    # Returns predicted value for a given x using Y=mX+c
    y_value=m*x_value +c
    return y_value


# example

x_vals=[1,2,3,4,5,6]
y_vals=[10,21,29,38,47,60]

slope,intercept=fit_linear_regression(x_vals,y_vals)

print(f"Slope (m): {slope:.2f} ")
print(f"Intercept (c): {intercept:.2f}")
print(f"Equation: Y= {slope:.2f}X + {intercept:2f}")

# prediction 

new_x_val=10

predicted_value= predict(new_x_val,slope,intercept)

print(f"Predicted Y value for X = {new_x_val}: {predicted_value:.2f}")

