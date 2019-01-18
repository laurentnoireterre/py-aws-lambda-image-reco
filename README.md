# Description

Simple python programm to experiment image recognition using Keras machine learning framework and Tensorflow backend.
This has to be deployed on a AWS Lambda function.

# Packaging

Clone the reposotory and launch zip its content
```
cd py-aws-lambda-image-reco
zip -r ../py-aws-lambda-image-reco.zip .
```

# Installation & Usage 

Connect to AWS console and create a Lambda having this properties:
   - Trigger: `S3 bucket`
   - Roles:
```
Allow: lambda:GetLayerVersion
Allow: lambda:GetLayerVersionPolicy 
Allow: logs:CreateLogGroup
Allow: logs:CreateLogStream
Allow: logs:PutLogEvents
Allow: s3:*
```
   - Layers:
     - Add the Tensorflow-Kera-Pillow layer using this ARN `arn:aws:lambda:us-east-1:347034527139:layer:tf_keras_pillow:3` 
        (see details https://github.com/antonpaquin/Tensorflow-Lambda-Layer)

Deploy the function code using the zip packaged. Runtime: `Python 3.6`

To trigger the function, just upload an image having a size of 224*224px in the S3 bucket configured with the function