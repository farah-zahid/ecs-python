from boto3 import client

bucket_name = "nginx-prod-egdfgdfhhs"

bucket_objects = "/ecs/task/nginx"

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(bucket_name)[bucket_objects]:
    print(key['Key'])