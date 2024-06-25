x = [0.87, 0.88, 0.80, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96]
y = [3.35, 3.62, 4.21, 4.5, 4.9, 5.3, 5.8, 6.11, 6.3, 6.1]
X = np.array(x).reshape(-1, 1)
y = np.array(y)
model = LinearRegression()
model.fit(X, y)
x_new = 1.25
y_pred = model.predict([[x_new]])
print(f"Спрогнозированное количество патентов при x=1.25: {y_pred[0]:.2f}")
