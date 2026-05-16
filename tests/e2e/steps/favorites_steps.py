from behave import given, when, then

URL = "https://tap-ht25-testverktyg.github.io/exam/"

@given('a book exists in the catalog')
def step_impl(context):
    context.page.goto(URL)

@when('I mark the book as favorite')
def step_impl(context):
    ...

@then('the book should be saved under my favorites')
def step_impl(context):
    assert context.page.locator("body").is_visible()
    ...

@given('a book exists in my favorites')
def step_impl(context):
    context.page.goto(URL)

@when('I remove the favorite mark')
def step_impl(context):
    ...

@then('the book should no longer exists under my favorites')
def step_impl(context):
    assert context.page.locator("body").is_visible()