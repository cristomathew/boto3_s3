
print("\n\nbefore starting make sure you have configured your aws cli\n\n")
import boto3
#Connect to aws s3 client using boto3
s3=boto3.client('s3')
#Create a bucket in your s3
def create_bucket(bucket_name):
  s3.create_bucket(Bucket=bucket_name)
  print("You have succesfully created a bucket with the name:",bucket_name)
#upload a file to your s3 bucket
def upload_file(filename,bucket_name):
  s3.upload_file(filename,bucket_name,filename)
#upload the file to a specic folder(if the folder does not exist it will create the folder
def upload_file_folder(filename,bucket_name,folder_name):
  s3.upload_file(filename,bucket_name,folder_name+'/{}'.format(filename))
#get the list of buckets created in your account
def bucket_list():
  response = s3.list_buckets()

# Get a list of all bucket names from the response
  buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
  print("Bucket List: %s" % buckets)
#main program to get some minor details
def main_func(m):
  if m=='1':
     print('Enter the following details carefully:')
     bucket_name=input("Enter the name of the bucket you wish to create:")
     create_bucket(bucket_name)
  elif m=='2':
     print("Enter the following details carefully")
     bucket_name=input("Enter the name of the bucket:")
     filename=input("enter name of the file you wish to upload:")
     print("NOTE::the file should be in the same directory as the app your are running")
     upload_file(filename,bucket_name)
  elif m=='3':
     print("Enter the following details carefully;")
     bucket_name=input("Enter the name of the bucket:")
     filename=input("enter name of the file you wish to upload:")
     print("NOTE::the file should be in the same directory as the app your are running")
     folder_name=input("Enter your directory /path:")
     upload_file_folder(filename,bucket_name,folder_name)
  elif m=='4':
     bucket_list()
  else:
     print("Error::Please enter out 1-4")

def main():
  print("Hello")
  print("Choose one of the following options:\n1.Create a new bucket \n 2.Upload a file \n 3.Upload a file to a specific directory \n  4.Print out the bucket list")
  m=input("please enter one of the above options(in terms of no):")
  print("Ypu have choosen option",m)
  print("do you wish to proceed(y/n):")
  n=input("enter your output:")
  if n=='y':
    main_func(m)
  else:
    main()


main()

