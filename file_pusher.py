import boto3
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import pytz
import glob
import os
from connectivity_checker import connect
s3_client = boto3.client('s3')

storage_directory ='/Users/BayoOlawumi/Desktop/monitor_me'
# Creating the Buckets
#s3_client.create_bucket(Bucket = 'camsec-futa',CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

# Listing all the available buckets
df = pd.DataFrame(s3_client.list_buckets()['Buckets'])
print(df)

# Upload files to your S3
"""
    file_name: The name of the file on your computer
    bucket_name : The name of the bucket you want to store the file
    object_name : The name you want the file to take on the AWS server, if set to none, then the object name will be seen as the file_name, hence, you can pass another name
    args : custom args,example timestamp
"""

def upload_files(file_name, bucket_name, object_name, date_created, date_sent):

    if object_name is None:
        object_name = file_name
    # Main File Uploader
    response = s3_client.upload_file(file_name, bucket_name, object_name, ExtraArgs = {
        'ACL': 'public-read',
        'Metadata':{
            'creation date': date_created,
            'time-sent': date_sent,
        }})
    print(response)

target_folder = glob.glob(storage_directory+'/*')
#file_path = 'testing_folder\dark_mode.jpg'

if connect():
    for each_file in target_folder:
        tz_NG = pytz.timezone('Africa/Lagos')
        time_sent = dt.now(tz_NG).strftime("%H: %M: %S")
        time_created = (dt.now(tz_NG) - timedelta(days=20)). strftime("%H: %M: %S")
        # Check File File format, ensure it is jpg
        if os.path.isfile(each_file) and os.path.splitext(each_file)[-1].lower() == '.jpg':
            upload_files(each_file,'camsec-futa',"picture"+str(time_sent),time_created, time_sent)
        else:
            print(each_file + " is a wrong File Format in this Folder")
else:
    print("Server is down!")


