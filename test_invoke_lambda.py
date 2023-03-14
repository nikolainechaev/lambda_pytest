from invoke_lambda import runner


def test_invocation():

    # expected_string = '{"statusCode": 200, "body": "\\"Hello from Lambda!\\""}'
    expected_string = '{"statusCode": 200, "body": 300}'
    lambda_result = runner()
    assert lambda_result == expected_string
