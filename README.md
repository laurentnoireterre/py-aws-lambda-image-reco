# Description

Simple python program to experiment image recognition using Keras machine learning framework and Tensorflow.
This has to be deployed within a AWS Lambda function. The function posts the result in an SNS topic.

# Packaging

Clone the repository and zip its content
```
cd py-aws-lambda-image-reco
zip -r ../py-aws-lambda-image-reco.zip .
```

# Installation & Usage 

Connect to AWS console and create a Lambda having this properties:
   - Runtime: `Python 3.6`
   - Trigger: `S3 bucket`
   - Role:
```
Allow: lambda:GetLayerVersion
Allow: lambda:GetLayerVersionPolicy 
Allow: logs:CreateLogGroup
Allow: logs:CreateLogStream
Allow: logs:PutLogEvents
Allow: s3:*

Resource: *
```
   - Layers:
     - Add the Tensorflow-Kera-Pillow layer using this ARN `arn:aws:lambda:us-east-1:347034527139:layer:tf_keras_pillow:3` 
        (see details https://github.com/antonpaquin/Tensorflow-Lambda-Layer)
   - Environment variables: 
     - Add an environment variable named `snsTopicArn` and containing the SNS topic ARN where to post the recognition result

Deploy the function code by uploading the zip package.

To trigger the function, just upload an image in the S3 bucket configured within the function
You can use the `test-sample.json`file to test the function.