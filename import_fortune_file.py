import boto3

class import_fortune_file:

    def s3_read:
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

    def import_file:
        f = open("fortunes.txt","r")

        for line in f:
            pass