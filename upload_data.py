import os
import boto3

s3_resource = boto3.resource('s3')

BUCKET_NAME_SOURCE = os.environ.get('SRC_BKT_NAME')
BUCKET_NAME_OUTPUT = os.environ.get('OUTPUT_BKT')
PREFIX = 'input/data/training/'

s3_resource.Bucket(BUCKET_NAME_SOURCE).upload_file("data/iris.csv", PREFIX + 'iris.csv')