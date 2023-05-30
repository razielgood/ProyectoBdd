from behave import given, when, then
from selenium import webdriver
from adidad_page import AdidasPage

# Configuración inicial
@given('I am on the Adidas website')
def step_open_website(context):
    context.driver = webdriver.Firefox()
    context.adidas_page = AdidasPage(context.driver)
    context.adidas_page.open_page()

@when('I close the cookies notification')
def step_close_cookies(context):
    context.adidas_page.close_cookies()

@when('I search for "{product}"')
def step_search_product(context, product):
    context.adidas_page.search(product)

@when('I close the modal')
def step_close_modal(context):
    context.adidas_page.close_modal()

@then('I should see the search results')
def step_check_search_results(context):
    assert "adidas Online Shop | adidas.es" in context.adidas_page.get_title()

@then('I add a product to the cart')
def step_add_product_to_cart(context):
    context.adidas_page.add_product_to_cart()

@then('I check the price of the product')
def step_check_product_price(context):
    # Implementar lógica para verificar el precio del producto
    pass

# Finalización
def after_scenario(context, scenario):
    context.driver.quit()
