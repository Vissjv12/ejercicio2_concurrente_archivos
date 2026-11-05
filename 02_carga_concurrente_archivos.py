import asyncio
import time


async def cargar_archivo(estudiante, archivo, tiempo):
    """Se simula la arga de archivos"""
    print(f"Iniciando carga: {archivo} (estudiante: {estudiante})")
    await asyncio.sleep(tiempo)
    print(f"Carga completada: {archivo}")
    return archivo


async def main():
    print("CARGA DE ARCHIVOS ESCOLARES")
    inicio = time.perf_counter()
    archivos_cargados = await asyncio.gather(
        cargar_archivo("Ana", "tarea_matematicas.pdf", 2.0),
        cargar_archivo("Luis", "ensayo_historia.docx", 3.0),
        cargar_archivo("Maria", "proyecto_fisica.zip", 1.5),
        cargar_archivo("Carlos", "informe_quimica.pdf", 2.5),
    )
    tiempo_total = time.perf_counter() - inicio
    print(f"Archivos cargados: {len(archivos_cargados)}")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print("Las cargas avanzaron durante el mismo periodo de tiempo.")


if __name__ == "__main__":
    asyncio.run(main())
