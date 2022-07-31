from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    context.root_url = 'https://test-bees.herokuapp.com'
    driver_manager = GeckoDriverManager()
    context.driver = webdriver.Firefox(
        executable_path=driver_manager.install())
    context.driver.maximize_window()


def after_all(context):
    context.driver.delete_all_cookies()
    context.driver.quit()
