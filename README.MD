## Streamlit en docker

He construido este **streamlit** de prueba y lo he subido a docker

Para que funcione en docker hay que realizar lo siguiente en la terminal de pycharm:

`docker build -t nombreimagen .`

Para ver las imagenes creadas:

`docker images`

para ejecutar el contenedor:

`docker run -p 8501:8501 --name nombre_contenedor idimagen`

En el navegador escribir http://localhost:8501
