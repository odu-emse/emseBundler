import paramiko
import boto3
import os

host = "51.222.87.170"
s3 = boto3.resource('s3')

def fetchCourses():
    courses = []
    client = boto3.client("s3")
    pag = client.get_paginator('list_objects')
    result = pag.paginate(Bucket='almpmodules', Delimiter='/')
    for prefix in result.search('CommonPrefixes'):
        print(prefix.get('Prefix'))
        courses.append(prefix.get('Prefix'))

    return courses

def fetchModules(courseName):
    bucket = s3.Bucket("almpmodules") 
    for obj in bucket.objects.filter(Prefix = courseName):
        remotePath = obj.key[obj.key.find('/')+1:]
        if not os.path.exists(os.path.dirname("interface/assets/" + remotePath)):
            os.makedirs(os.path.dirname("interface/assets/" + remotePath))
        print(remotePath)
        bucket.download_file(obj.key, "interface/assets/" + remotePath) # save to same path
        # bucket.download_file(obj.key, obj.key) # save to same path