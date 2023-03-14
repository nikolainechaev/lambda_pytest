import boto3
import json


def runner():
    lambda_client = boto3.client('lambda')
    test_event = dict()
    response = lambda_client.invoke(
        FunctionName='simple_function',
        Payload=json.dumps(test_event),
    )
    print(response['Payload'])
    print(response['Payload'].read().decode("utf-8"))

# If you want to test runner() type in terminal:
# python3 -c "import invoke_lambda; print(invoke_lambda.runner())"
# it will return  status and hello from Lambda message
