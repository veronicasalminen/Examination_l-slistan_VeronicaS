from behave import given, when, then

URL = "https://tap-ht25-testverktyg.github.io/exam/"

@given('the book catalog contains books')
def step_impl(context):
    context.page.goto(URL)

@when('I open the book catalog')
def step_impl(context):
    context.page.goto(URL)

@then('I should see a list of all books')
def step_impl(context):
    assert context.page.locator("body").is_visible()