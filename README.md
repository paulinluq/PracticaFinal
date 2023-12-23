# Práctica final programación II

   Paula Piña Luque
   Practica Final Programación II
   23/12/2023

   Para esta practica he utilizado una base de datos la cual contenía información sobre distintas bebidas de starbucks y sus valores nutricionales. Esta base de datos la he obtenido de kaggle. me ha parecido interesante esta base de datos no solo porque me encante el cafe sino porque al indicar los valores nutricionales de cada bebida podría resultar muy interesante hacer un estudio sobre dichos valores nutricionales, sobre todo desde el punto de vista médico/dietetico. 

   Toda esta practica se ha desarrollado a traves de una terminal de ubuntu y vscode donde hemos programado nuestra aplicación de streamlit. Ahí encontramos 4 páginas principales: 

      - Home: es la página principal, nos da una vision general de lo que nos vamos a encontrar en este trabajo

      - Analisis: aqui es donde muestro los distintos gráficos (casi todos los graficos se pueden modificar con las opciones que aparece a la izquierda para ver dichos graficos solo con los tipos de bebidas que selecciones)
         ~ Calorias por bebida: con este grafico pretendo ver la media de calorias que contiene cada tipo de bebida. hay que resaltar que la bebida con menos calorias es la de cafe solo y la que más los smoothies seguido de muy cerca de frapucchino blended coffee. la media de calorias de bebida ronda entre las 5 y 300 kcal.
         ~ analisis nutricional de las bebidas: aqui muestro las distintas bebidas ofrecidas por starbucks y el usuario puede seleccionar si quiere ver la grasa, el azucar, la proteina o la cafeina dependiendo de sus necesidades dietéticas.
         ~ calorías por tipo de leche: como en el primer grafico observamos que el cafe solo apenas tenia calorias, pensé que podría haber alguna relación entre el tipo de leche y la cantidad de calorias por lo que me parecio interesante comparar la media de calorias por cada tipo de leche utilizada para las bebidas. Aqui volvemos a observar que el cafe solo es el que menos calorias tiene y la leche entera la que más.
         ~ numero de bebidas por tipo de bebidas: a traves del csv observe que los nombres de las bebidas se repetian, por lo que quise ver cuantas bebidas había por cada tipo de bebida.
         ~ bebidas de starbucks por contenido de sodio: investigando sobre el cafe y los problemas médicos, encontré que muchos de dichos problemas vienen por la cantidad de sodio contenida en las bebidas, por lo que me pareció interesante hacer un grafico que muestre la suma de sodio que contenian las diferentes bebidas. el usuario puede seleccionar un rango de sodio contenido por cada bebida.

      - Historia: aqui cuento un poco la historia de starbucks.

      -Feedback: aqui se puede poner una reseña sobre las paginas de la app. 

   Para este trabajo lo primero que hice fue buscar una base de datos que me resultase interesante. Una vez ya la encontré me enfrenté a varios problemas a la hora de empezar a programar. No sabía si hacer una partición de mi disco, descargarme un simulador de terminal de ubuntu o hacerlo a traves de una máquina virtual. Después de ver los problemas que habian experimentado mis compañeros para hacer una partición del disco (era mi idea original de proceder), decidí que no era una buena opción. A la vez, vi que claudia tuvo muchos problemas al intentar hacerlo a traves de una máquina virtual, por lo que opté por la aplucación que simulaba una terminal de ubuntu. Me encontre con muchos errores (la mayoría porque tenia que instalarme paquetes para que funcionase bien el código) pero poco a poco los fui solucionando.

   Me cree una carpeta nueva y me clone el repositorio de github. A partir de ahí primero analice tu código e intenté entenderlo. Una vez ya me vi lo suficientemente enterada, empecé a cambiar tu código para adaptarlo a mis necesidades. Cuando ya tuve todos los gráficos que me parecían pertinentes pasé a intentar hacer un back end con el método Post. Primero me informé sobre lo que era y para qué servia. 

      Para ello vi que lo mejor era hacerlo con flask. Para que el trabajo estuviese dividido en contenedores cree otra carpeta donde se encuentra todo el código para el back end. En la práctica lo he utilizado para el feedback. 

   Posteriormente vi lo que era una jerarquia de clases y como implementarlo junto con el manejo de errores. La manera más simple que vi de incluir esto a la practica era a traves del feedback tambien. Poniendo que tipo de datos esperar. además cree un archivo para comprobar que funcionaba correctamente el manejo de errores (test_server).

   Para que todo funcionase correctamente con docker-compose tuve que añadir el servicio de flask al .yml y crear un archivo de texto con los requerimientos necesarios. 


   He de admitir que al principio me agobie con el trabajo, sobre todo al ver la magnitud que abarcaba y todo lo que se pedía. 
   Una vez solucione los primeros problemas que me encontré (fue lo que más tarde con esta práctica) fui poco a poco construyendo el código y dandole estructura. A medida que iba avanzando con el proyecto me iba gustando más y más y buscaba la manera de hacerlo más bonito o de otras maneras que me parecían mejores. Por lo que puedo decir que he sufrido bastente con este trabajo pero a la vez me lo he pasado muy bien. 
   Debido al tiempo que tarde intentando solucionar los primeros errores y a mi mala gestión del tiempo no he podido implementar una base de datos como servicio adicional. Me da mucha rabia porque creo que podría ser muy interesante y podría aprender un montón intentándolo. Aunque te haya entregado este proyecto sin utilizar la base de datos voy a intentar hacerlo posteriormente. ¿podría mandartelo cuando crea que lo haya conseguido? Sé que no me contaria como nota para este trabajo, no pretendo que lo sea, pero me gustaría tener un feedback sobre lo que voy a intentar. 

   Espero que te parezca interesante el proyecto que he hecho. 

