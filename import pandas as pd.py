
# Importar las bibliotecas necesarias
import pandas as pd  # Manejo de datos en formato de tablas (similar a Excel)
import numpy as np  # Cálculos numéricos avanzados
import matplotlib.pyplot as plt  # Para crear gráficos y visualizaciones
from sklearn.model_selection import train_test_split  # Dividir el conjunto de datos en entrenamiento y prueba
from sklearn.preprocessing import StandardScaler  # Normalizar las características
from sklearn.metrics import mean_squared_error, mean_absolute_error  # Métricas para evaluar el modelo
from tensorflow.keras.models import Sequential  # Crear modelos secuenciales de redes neuronales
from tensorflow.keras.layers import Dense  # Capa densa (totalmente conectada) para las redes neuronales

# Cargar el dataset de precios de casas en California
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()  # Cargar los datos

# Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(housing.data, housing.target, test_size=0.2, random_state=42)

# Normalizar las características (promedio 0 y desviación estándar 1)
scaler = StandardScaler()  # Crear un objeto StandardScaler para normalizar los datos
X_train = scaler.fit_transform(X_train)  # Ajustar el escalador a los datos de entrenamiento y transformarlos
X_test = scaler.transform(X_test)  # Transformar los datos de prueba usando el mismo escalador (sin re-ajustar)

# Construir el modelo de regresión lineal en TensorFlow
model = Sequential([  # Crear un modelo secuencial (capas ordenadas una tras otra)
    Dense(units=1, input_shape=(X_train.shape[1],))  # Añadir una capa densa con 1 unidad (neuron) de salida
])

# Compilar el modelo, especificando el optimizador y la función de pérdida
model.compile(optimizer='adam', loss='mean_squared_error')  # Optimización con Adam y pérdida MSE (error cuadrático medio)

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train, epochs=100, validation_data=(X_test, y_test))  # Entrenamiento durante 100 épocas con validación

# Hacer predicciones con los datos de prueba
y_pred = model.predict(X_test)  # Generar predicciones usando el modelo entrenado

# Evaluar el modelo calculando métricas de error
mse = mean_squared_error(y_test, y_pred)  # Calcular el error cuadrático medio (MSE)
rmse = np.sqrt(mse)  # Calcular la raíz del error cuadrático medio (RMSE)
mae = mean_absolute_error(y_test, y_pred)  # Calcular el error absoluto medio (MAE)

# Mostrar en pantalla las métricas de evaluación del modelo
print('RMSE:', rmse)  # Imprimir RMSE (error cuadrático medio)
print('MAE:', mae)  # Imprimir MAE (error absoluto medio)

# Visualización de las predicciones comparadas con los valores reales
plt.scatter(y_test, y_pred)  # Crear un gráfico de dispersión entre valores reales y predicciones
plt.xlabel('Valores reales')  # Etiqueta para el eje X
plt.ylabel('Predicciones')  # Etiqueta para el eje Y
plt.title('Comparación entre valores reales y predicciones')  # Título del gráfico
plt.show()  # Mostrar el gráfico
