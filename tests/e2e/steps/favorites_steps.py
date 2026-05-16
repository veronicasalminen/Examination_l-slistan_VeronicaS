from behave import given, when, then

@given('a book exists in the catalog')
def step_impl(context):
    context.page.goto("http://localhost:3000")

@when('I mark the book as favorite')
def step_impl(context):
    context.page.click("[data-testid='favorite-button']")

@then('the book should be saved under my favorites')
def step_impl(context):
    context.page.goto("http://localhost:3000/favorites")
    assert context.page.locator("li").count() > 0


@when('I remove the favorite mark')
def step_impl(context):
    context.page.click("[data-testid='favorite-button']")

@then('the book should no longer exists under my favorites')
def step_impl(context):
    context.page.goto("http://localhost:3000/favorites")
    assert context.page.locator("li").count() == 0