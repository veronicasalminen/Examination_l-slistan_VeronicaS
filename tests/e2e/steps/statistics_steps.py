from behave import given, when, then

URL = "https://tap-ht25-testverktyg.github.io/exam/"

@given('there are books in the catalog')
def step_impl(context):
    context.page.goto(URL)

@when('I open the statistics page')
def step_impl(context):
    context.page.goto(URL)

@then('I should see statistics about the books')
def step_impl(context):
    assert context.page.locator("body").is_visible()