import logging
import boto3
from botocore.exceptions import ClientError


key_id = "AKIA5Z4HQZDU3UAC7IZY"
access_key = "I4sR2a5ixre1BNmtORoS5oBW0y49p/jMyDNcS1tT"

import boto3

def create_bucket(bucket_name, region=None):
    """
        :param bucket_name: Bucket para criar
        :param region: String - Região que é para criar o bucket
        :return: TRUE se o bucket for criado, caso não, retorna FALSE

    """
    try:
        if region is None:
            s3_client = boto3.client('s3',
                                     aws_access_key_id= key_id,
                                     aws_secret_access_key= access_key)
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', 
                                     region_name=region,
                                     aws_access_key_id= key_id,
                                     aws_secret_access_key= access_key)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True

bucket_name = "webscraping2023"
create_bucket(bucket_name)

