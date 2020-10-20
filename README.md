# grupo6_pepy

Pasos para ejecutar Docker:

1) posicionarse con la consola en la carpeta env

2) ejecutar el siguiente comando

```bash
docker run -p 19999:8080  -v $PWD/logs:/zeppelin/logs -v $PWD/data:/zeppelin/data --rm --name zeppelin_single apache/zeppelin:0.8.1
```

3) para acceder a la aplicación zeppelin, abrir el navegador 

http://localhost:19999

4) Importar el notebook, deseado.