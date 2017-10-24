import boto3

def s3_read():
    dyn = boto3.resource('dynamodb')
    table = dyn.Table('fortunes')

    # print(table.creation_date_time)

    # response = table.get_item(
    #     Key={
    #         'fortune_id': 1999
    #     }
    # )

    client = boto3.client('dynamodb')
    response = client.describe_table(
        TableName='fortunes'
    )

    count = response['Table']['ItemCount']
    print(count)

s3_read()
