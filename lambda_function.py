from keras.applications.mobilenet import MobileNet, decode_predictions, preprocess_input
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.models import load_model
from keras.preprocessing import image

import numpy as np

import boto3
from io import BytesIO

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    print('Reading {} from S3 bucket {}'.format(file_key, bucket_name))
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    model = MobileNet()

    s3Img = obj['Body'].read()
    img = image.load_img(BytesIO(s3Img), target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    pImg = preprocess_input (img)

    preds = model.predict(pImg)

    print(decode_predictions(preds, top=5)[0])
