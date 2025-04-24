import os
import subprocess
from pathlib import Path


def get_latest_report_dir(base_dir="Reports"):
    # Obtener todos los directorios en la carpeta base
    report_dirs = [d for d in Path(base_dir).iterdir() if d.is_dir()]
    if not report_dirs:
        raise FileNotFoundError("No se encontraron directorios de reportes en 'Reports'")

    # Ordenar por fecha de modificación (el más reciente primero)
    latest_dir = max(report_dirs, key=lambda x: x.stat().st_mtime)
    return latest_dir


def run_allure_serve():
    try:
        # Obtener el directorio más reciente
        latest_report_dir = get_latest_report_dir()
        allure_results_dir = latest_report_dir / "allure-results"

        if not allure_results_dir.exists():
            raise FileNotFoundError(f"No se encontró el directorio 'allure-results' en {latest_report_dir}")

        # Ejecutar el comando allure serve
        print(f"Ejecutando Allure serve para: {allure_results_dir}")
        subprocess.run(["allure", "serve", str(allure_results_dir)], check=True)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_allure_serve()