from selenium import webdriver


def before_all(context):
    context.root_url = 'https://test-bees.herokuapp.com'
    context.driver = webdriver.Firefox(keep_alive=False)


def after_all(context):
    context.driver.delete_all_cookies()
    context.driver.quit()
    