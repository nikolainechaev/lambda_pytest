from invoke_lambda import InvokedLambda


def test_invocation():

    expected = '{"statusCode": 200, "body": "\"Hello from Lambda!\""}'
    lambda_result = InvokedLambda.runner()
    assert lambda_result == expected
