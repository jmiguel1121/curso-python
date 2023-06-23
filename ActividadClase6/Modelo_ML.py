import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
#
def true_fun(X):
    return np.cos(1.5 * np.pi * X)
#
# Semilla 
np.random.seed(0)

# Cantidad de muestras
n_samples = 30

# Grados de polinomios usados
degrees = [1,2,3, 4, 7,15,21]

# Multiplicador
k = 1
#
X = np.sort(np.random.rand(n_samples)) * k 
y = true_fun(X) + np.random.randn(n_samples) * 0.3
#
plt.plot(X, y, color = 'red', label="Actual")
plt.plot(X, true_fun(X), label="True function")
plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.show()
#
# Tamáño del grafico
plt.figure(figsize=(30, 7))

# import pandas as pd 
# df = pd.DataFrame(columns = ['Degrees', 'Mean', 'Stdev'])


#itera por la cantidad de polinomios 
for i in range(len(degrees)):
    
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    #Estas son las transformaciones y el modelo que se aplican a los datos
    polynomial_features = PolynomialFeatures(degree=degrees[i],include_bias=False)
    linear_regression = LinearRegression()
    
    #Arma el pipeline con las tuplas que componen las trasnformaciones y el modelo
    pipeline = Pipeline(
        [("polynomial_features", polynomial_features), 
         ("linear_regression", linear_regression)]
    )
    
    # arma la matriz de entrenamiento
    x0 = X[:, np.newaxis]
    
    #Aplica el pipeline a los datos y entrena el modelo
    pipeline.fit(x0, y)

    # Evalua el modelo mediante cross_val_score
    scores = cross_val_score(pipeline, x0, y,scoring="neg_mean_squared_error", cv=10)

    # Muestra los resultados
    X_test = np.linspace(0, k, 100)
    
    y_poly_pred = pipeline.predict(X_test[:, np.newaxis])
    plt.plot(X_test, y_poly_pred, label="Model")
    plt.plot(X_test, true_fun(X_test), label="True function")
    plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, k))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
    
 
    plt.title("Degree {}\nMSE = {:.2e}(+/- {:.2e})".format(degrees[i], -scores.mean(), scores.std()))
    
    #df.append(pd.DataFrame([degrees[i],-scores.mean(), scores.std()]).T)
    
plt.show()
#
#print(df)