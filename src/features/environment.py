from behave import fixture, use_fixture
from src.config import config
from selenium import webdriver


@fixture
def browser_setup(context):
    # Crear el driver del navegador
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.base_url = config("BASE_URL")

    context.driver.get(context.base_url)

    yield context.driver  # Permitir la ejecución de los tests

    # Cerrar el driver al finalizar los tests
    context.driver.quit()


def before_scenario(context, scenario):
    print("Before scenario:", scenario.name)
    use_fixture(browser_setup, context)


def after_scenario(context, scenario):
    print("After scenario:", scenario.name)
    context.driver.quit()

