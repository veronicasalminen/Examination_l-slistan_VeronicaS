from behave import given, when, then

@given('there are books in the catalog')
def step_impl(context):
    context.page.goto("http://localhost:3000")

@when('I open the statistics page')
def step_impl(context):
    context.page.click("[data-testid='statistics']")

@then('I should see statistics about the books')
def step_impl(context):
    stats = context.page.locator("[data-testid='stats']")
    assert stats.count() > 0