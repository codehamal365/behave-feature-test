from behave import then, given, when


@given('you are happy')
def step_impl(context):
    pass


@when('someone says {s}')
def step_impl(context, s):
    context.message = s
    print("THIS IS NEVER DISPLAYED IN THE CONSOLE")
    pass


@then('you smile')
def step_impl(context):
    assert (context.message == "hi")
