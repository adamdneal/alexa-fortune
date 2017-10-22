import boto3

def s3_read():
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

def import_file():
    f = open("fortunes.txt", "r")
    i = 0
    author = quote = ""

    for line in f:
        i += 1
        line = line.strip()

        if line.startswith("~"):
            author = line
        elif line == "%":
            insert_record(i, quote, author)
        else:
            quote = line.strip('"')

def insert_record(id, quote, quthor):
    pass

#s3_read()
import_file()
