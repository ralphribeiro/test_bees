from selenium import webdriver


def before_all(context):
    context.root_url = 'https://test-bees.herokuapp.com'
    context.driver = webdriver.Firefox(keep_alive=False)


def after_scenario(context, scenario):
    context.driver.quit()