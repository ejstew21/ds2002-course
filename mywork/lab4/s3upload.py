import boto3
import urllib

s3 = boto3.client('s3', region_name='us-east-1')
bucket_name  = 'ds2002-ryb8jt'
file_url = input('URL of file?: ')
local_file = input('File name for saving?: ')
urllib.request.urlretrieve(file_url, local_file)
object_name = local_file

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket_name,
    Key = local_file
)

expires_in = 604800
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )
print(response)

# Presigned URL
# https://ds2002-ryb8jt.s3.amazonaws.com/dog.gif?AWSAccessKeyId=ASIAXYKJSVMX2J44D5XA&Signature=JOpiANz65dzX1%2FZkcEOnIeWHNDU%3D&x-amz-security-token=FwoGZXIvYXdzEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDK365OC%2BC%2FXxTvuYWCLEAWzh39AFrRuF9t9ih%2BteoUSICTANhfuCc4z2MyxXyhwSatioWdfsNETkTPrWLMntkn6%2BKmbTEh3CFGH%2FmFqR1OOSBUsjoBnCZPbaMHGMyY687WOmnv0g4wI4v%2BLuA5Quic55sWytk%2Fzbv4%2FDUos2n0fRd3F3Dm7SD6ILx3stQ49IjkulV3%2FF3s2Qmu2T4pO8Q%2BuKHdQusxIEVE4FgoFR3uJOBgVmRY3bb%2Fy2j5JActwcxNvsq8lg3AgbiAImNWEIwS1FhO8o9IjSrwYyLRzDEuzT%2FhyqKlSmitEgmaI95vpLuyufzx%2F83U9enzab3lFquGFOe6meWLImGQ%3D%3D&Expires=1711131305

