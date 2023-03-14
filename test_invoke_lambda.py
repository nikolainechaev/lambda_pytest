from invoke_lambda import runner


def test_invocation():

    expected = '{"statusCode": 200, "body": "\"Hello from Lambda!\""}'
    lambda_result = runner()
    assert lambda_result == expected
