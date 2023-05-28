Siempre me pareció que las herramientas para realizar aplicaciones de escritorio con las que había trabajado eran bastante limitadas en cuanto al apartado estético, hace un tiempo descubrí la existencia de ElectronJS que es un framework para hacer aplicaciones de escritorio usando HTML, JS y CSS, decidí usarla para mi proyecto ya que abre las posibilidades a realizar cosas más atractivas, quería específicamente ver como animar cosas con CSS, pensé que seria un proyecto pequeño de esta manera, entonces pensé que seria bueno agregar algo de inteligencia artificial ya que será algo que empezare a ver los próximos semestres y me sería útil un primer acercamiento.

Entonces necesitaba una idea que me permitiera recolectar datos y poder hacer animaciones, decidí realizar un juego de toma de decisiones que se basa en 100 selecciones de 4 mazos de cartas. Lo primero que hice fue el front, directamente fui a diseñar la pantalla de juego que quedo en lo siguiente: 

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/imagen%201.png)

Después de diseñar esto empecé a realizar la animación, quería lograr que la carta fuera al centro y se volteara para ver su contenido, esto lo logré con el atributo “transform” de CSS, hice 2 partes de la carta, el dorso y la parte frontal al hacer el “giro” se intercambian estas partes:

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/GIF1.gif)

Posteriormente decidí agregar algunos efectos al fondo para darle más énfasis estos los logre con la herramienta “@keyframes” de CSS, hice que el fondo se hiciera borroso y se oscureciera un poco cuando seleccionas una carta:

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/GIF2.gif)

Teniendo esto hice la base de datos en postgres que tiene la siguiente estructura:

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/modelo%20ER.png)

Hice la pantalla de registro de usuario:

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/registro.png)

Con esto ya tenia cubierta la primera parte de mi proyecto, los usuarios se registraban y podían jugar, sus resultados se guardaban en la base de datos, entonces me puse a investigar sobre que podía ser algo de IA para principiantes y vi que uno de los mejores lenguajes para esto es Python, en este lenguaje encontré la librería scikitlearn, lo único que había escuchado yo sobre IA era redes neuronales entonces me fui por ahí, la documentación de la librería es bastante amplia y eso me ayudo bastante, lo primero que tuve que hacer fue tomar los datos de la DB y pasarlos en un formato correcto para la interpretación, para mi esta fue la parte mas complicada ya que requirió de bastantes horas de investigación de sentencias SQL, al final pude hacer una sentencia que me daba los datos como los necesitaba. El primer paso fue convertir esta información de la consulta a un DataFrame con la librería de pandas, con esto ya tenía la información lista para usarse, solo faltaba agregar las etiquetas para la clasificación, los resultados se dividen en 2: Bueno o Malo, esto dependiendo de las elecciones que hagas. Realice unos cuantos registros para poder entrenar la red neuronal esto lo realice con la ayuda de la documentación de scikitlearn. Después hice el método para clasificar las pruebas de los usuarios que también fue apoyándome de la documentación.
De este modo el flujo del programa resulta de la siguiente forma:

1.- Registro de usuario

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/registro2.png)

2.- Aplicación Juego

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/GIF3.gif)

3.- Final y cálculo de resultados

![Imagen](https://github.com/franco-e-s-c/Sem-Traductores2/blob/72cf9307f7c051c8544863e9f6e97d5f1842febc/ProyectoFin/imagenes/GIF4.gif)
