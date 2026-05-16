from behave import given, when, then

# Navigerar till katalogen och verifierar att böckerna visas
@given('the book catalog contains books')
def step_impl(context):
    context.page.goto("http://localhost:3000")

@when('I open the book catalog')
def step_impl(context):
    context.page.click("[data-testid='catalog']")

@then('I should see a list of all books')
def step_impl(context):
    books = context.page.locator("li")
    assert books.count() > 0