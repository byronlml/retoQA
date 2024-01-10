import os
import subprocess
import argparse


def run_behave_and_generate_report(feature_directory):
    # Añadir la variable de entorno `allure_result_folder`
    os.environ["allure_result_folder"] = "./src/reports/"

    # Ejecutar Behave con el formato Allure y el directorio de resultados definido
    result = subprocess.run(f"behave -f allure_behave.formatter:AllureFormatter -o {os.environ['allure_result_folder']} {feature_directory}", shell=True)
    if result.returncode != 0:
        raise Exception("Error al ejecutar Behave")

    # Luego de que las pruebas se hayan ejecutado, ejecutamos Allure serve
    subprocess.run(f"allure serve {os.environ['allure_result_folder']}", shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ejecutar pruebas Behave en un directorio específico')
    parser.add_argument('feature_directory', help='Directorio de los features a ejecutar')
    args = parser.parse_args()

    run_behave_and_generate_report(args.feature_directory)
