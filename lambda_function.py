from keras.applications.mobilenet import MobileNet, decode_predictions
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from keras.models import load_model

import numpy as np
from PIL import Image

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
    img = np.asarray(Image.open(BytesIO(s3Img)))
    
    X = np.reshape(img, [1, 224, 224, 3])

    preds = model.predict(X)

    print(decode_predictions(preds, top=5)[0])
