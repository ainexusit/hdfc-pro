import json
import boto3

aws_access_key_id = 'AKIAQI5GDLR6ZOMLLNZJ'
aws_secret_access_key = '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'

client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

sourcebucket = 'offline9-s3tos3-using-lambda'
destinationbucket = 'offline9-destination-bucket'

def copy_to_destination_bucket(filename):
    response = client.copy_object(Bucket='{}'.format(destinationbucket),CopySource='/{}/{}'.format(sourcebucket,filename),Key='{}'.format(filename))


def delete_from_source_bucket(filename):
    response = client.delete_object(Bucket='{}'.format(sourcebucket), Key='{}'.format(filename))


def main():
    print("*"*100)
    response = client.list_objects(Bucket='{}'.format(sourcebucket))
    for temp in response['Contents']:
        copy_to_destination_bucket(temp['Key'])
        delete_from_source_bucket(temp['Key'])
    print("*"*100)

if __name__=='__main__':
    main()