## Importar Librerias
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

##  Cargar Dataset
iris = datasets.load_iris()
print(iris)
## Definir cuál es la columna de salida
X, y = iris.data[:, :2], iris.target

## Division del dataset en datos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)

## Standarizacion de los valores
scaler = preprocessing.StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

## Seleccion del algoritmo de macchine learning
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

## Entrenamiento del Modelo
knn.fit(X_train, y_train)

## Prediccion
y_pred = knn.predict(X_test)

# Evaluacion
print(accuracy_score(y_test, y_pred))
##Salida:0.631578947368421