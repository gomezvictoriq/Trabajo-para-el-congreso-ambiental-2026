import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_bootstrap_linear_regression_analysis(X, y, n_iteraciones=100):
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    coeficientes = []
    interceptos = []

    for _ in range(n_iteraciones):
        indices = np.random.choice(len(X), size=len(X), replace=True)
        X_boot = X[indices]
        y_boot = y[indices]

        modelo = LinearRegression().fit(X_boot, y_boot)
        coeficientes.append(modelo.coef_)
        interceptos.append(modelo.intercept_)

    coeficientes = np.array(coeficientes)
    interceptos = np.array(interceptos)

    coef_prom = np.mean(coeficientes, axis=0)
    intercept_prom = np.mean(interceptos)

    # Usar modelo promedio para predecir en X de entrenamiento
    y_pred_prom = X @ coef_prom + intercept_prom
    r2 = r2_score(y, y_pred_prom)
    rmse = np.sqrt(mean_squared_error(y, y_pred_prom))

    #print(f"Análisis de Bootstrapping completado con {n_iteraciones} iteraciones.")
    #print(f"Coeficientes promedio: {coef_prom}")
    #print(f"Intercepto promedio: {intercept_prom:.4f}")
    #print(f"R² del modelo promedio: {r2:.4f}")
    #print(f"RMSE del modelo promedio: {rmse:.4f}")

    return coef_prom, intercept_prom, r2, rmse

