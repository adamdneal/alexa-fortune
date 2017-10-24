import boto3

def import_file():
    f = open("fortunes.txt", "r")
    i = 0
    author = quote = ""

    for line in f:
        line = line.strip()

        if line.startswith("~") or line.startswith("-"):
            author = line.strip("~- ")
        elif line == "%":
            i += 1
            insert_record(i, quote, author)
            author = quote = ""
        else:
            quote += " " + line.strip('"')


def insert_record(fortune_id, quote, author):
    quote = quote.strip()

    if not quote:
        return

    dyn = boto3.resource('dynamodb')
    table = dyn.Table('fortunes')

    fortune = {
        'fortune_id': fortune_id,
        'quote': quote
    }

    if author:
        fortune['author'] = author

    print('inserting item {}'.format(fortune_id))
    table.put_item(Item=fortune)

import_file()
