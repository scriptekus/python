#Import Required Libraries
import boto3
import json
#Invoke AWS Client Resources
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
#Access S3 Bucket Read JSON Contents
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
#Insert JSON Contents Into Dynamo DB
    table = dynamodb.Table('Transaction')
    table.put_item(Item=jsonDict)
    return 'Hello from Lambda'