
## Carga concurrente de archivos escolares

Aqui se simula a cuatro estudiantes que cargan sus tareas a una plataforma escolar. Usando `asyncio` se hace que las cargas continuen concurrentemente hasta dar una respuesta para el programa.

Cada carga dura 9 segundo pero como es ejecucion concurrente el proceso tarda aproximadamente 3 segundos.

Ejecutar con Docker Compose:

```bash
docker compose -f docker-compose.extras.yml run --rm carga-escolar
```

Ejecutar sin Docker:

```bash
python 07_carga_concurrente_archivos.py
```


