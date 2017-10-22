import boto3

dyn = boto3.resource('dynamodb')
table = dyn.Table('fortunes')

#print(table.creation_date_time)

response = table.get_item(
    Key={
        'fortune_id': 2
    }
)

item = response['Item']
print(item)