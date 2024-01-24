El objetivo de este programa es predecir si a una persona se le aprobaría o no un crédito en base a determinadas variables, tales como edad, score crediticio, si es cliente bancario, entre varias otras. Excluí los valores menores a |0.01|ya que los consideré menos relevantes a la hora de realizar el modelo. Las variables categóricas no las tuve en cuenta ya que obtenía valores muy bajos al hacer la matriz de correlación con la variable dependiente. 

Para llevar a cabo la predicción, decidí basarme en un árbol de decisión ya que mi output debe ser por si o por no. El modelo en el 93% de los casos no aprobará correctamente el crédito a las personas. Es decir, fallará en un 7% en los casos de rechazar a personas que si estén aptas para un crédito. En contraparte, aprobará con una eficacia del 80% a los clientes, y tendrá un 20% de margen de error al aprobar créditos a personas que no deberían. Podría hacerse foco en el último dato ya que el banco no querrá dar préstamos a personas no aptas o que no estén en condiciones de lidiar con una deuda futura.

En cuanto al recall, la proporción del 83% de los que no aprobamos estuvieron bien rechazados. Y el 91% de los que aprobamos estuvieron bien aprobados (muy importante). F1-Score comparó los valores esperados con los reales.

En conclusión, la exactitud del modelo es del 86%. Es decir que acierta 86 de 100 predicciones realizadas, siendo este un modelo bien trabajado. 

Fuente: https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction
