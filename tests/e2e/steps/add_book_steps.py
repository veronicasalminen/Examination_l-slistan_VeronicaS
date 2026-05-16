from behave import given, when, then

@given('the book does not exist in the catalog')
def step_impl(context):
    context.page.goto("http://localhost:3000")

@when('I add the book')
def step_impl(context):
    context.page.click("[data-testid='add-book']")
    context.page.fill("[data-testid='title']", "Test")
    context.page.fill("[data-testid='author']", "Test")
    context.page.click("[data-testid='submit']")

@then('the book should be added in the catalog')
def step_impl(context):
    assert context.page.locator("li").count() > 0