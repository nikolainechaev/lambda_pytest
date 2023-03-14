import boto3
iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')
with open('lambda.zip', 'rb') as f:
    zipped_code = f.read()

role = iam_client.get_role(RoleName='LambdaBasicExecution')
response = lambda_client.create_function(
    FunctionName='helloWorldLambda',
    Runtime='python3.9',
    Role=role['Role']['Arn'],
    Handler='handler.lambda_handler',
    Code=dict(ZipFile=zipped_code),
    Timeout=300,  # Maximum allowable timeout
    # Set up Lambda function environment variables
    Environment={
        'Variables': {
            'Name': 'helloWorldLambda',
            'Environment': 'prod'
        }
    },
)
print(response)
# import boto3
# import json

# AWS_REGION = "us-east-1"
# lambda_client = boto3.client("lambda", region_name=AWS_REGION)
# iam = boto3.client('iam')
# role_policy = {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Sid": "",
#             "Effect": "Allow",
#             "Principal": {
#                 "Service": "lambda.amazonaws.com"
#             },
#             "Action": "sts:AssumeRole"
#         }
#     ]
# }

# response = iam.create_role(
#     RoleName='LambdaBasicExecution',
#     AssumeRolePolicyDocument=json.dumps(role_policy)
# )
