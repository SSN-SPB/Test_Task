from behave import given, when, then

@given('the username is "{username}"')
def step_given_username(context, username):
    context.username = username

@when('the password is "{password}"')
def step_when_password(context, password):
    context.password = password

@then('login should be successful')
def step_then_login_success(context):
    assert context.username == "admin"
    assert context.password == "1234"