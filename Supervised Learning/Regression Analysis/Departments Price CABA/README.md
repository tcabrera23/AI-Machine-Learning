El objetivo de este modelo de regresión lineal consistió en predecir los precios en dólares de los distintos departamentos de CABA en función de distintas variables.

Como primer paso, aunque no del todo necesario, me encargué de dejar el archivo preparado para cualquier tipo de operación o análisis. Hay bloques de código que podría no haberlos realizado e igualmente llegaría al mismo resultado, pero decidí hacerlos para practicar la limpieza de los datos. 

La columna de Comunas la traté como una variable categórica debido a que el número hace referencia a el lugar de pertenencia del departamento, no a una cantidad cuantitativa.
El modelo resultante indica ser de buena precisión ya que obtuvo un R^2 alto y un MSE relativamente bajo. Por lo tanto, en la gran mayoría de los casos explicará y tratará de predecir correctamente la variabilidad de los datos y se acercará a los valores reales.

El modelo lo ajusté en un intervalo de metros cuadrados correspondiente a un departamento residencial, con el objetivo de aumentar la precisión del modelo. Con ello logré pasar de un 0.69 de R-Squared a un valor de 0.89 y reducir considerablemente el margen de volatilidad. De todas formas, se qué si sigo ajustando puedo conseguir mejores resultados pero no quería descartar demasiados datos del dataset.

Queda por mejorar el desvío estándar del modelo. Un desvío de casi $38.000 USD es bastante alto y hay margen de mejora por realizar. Por último intenté replicar el modelo en varios random forest pero tuve problemas con la capacidad de la memoria y de momento lo dejaré así y continuaré con otros temas. 

Fuente: https://data.buenosaires.gob.ar/dataset/departamentos-venta
