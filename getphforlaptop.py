import json
import boto3
import logging

client = boto3.client('iot-data', region_name='us-west-2')
s3 = boto3.client('s3')



def function_handler(event, context):
    response = s3.get_object(Bucket='phfromhottubbucket', Key='phlevelfromhottub.json')
    value = response['Body'].read()
    value = float(value)
    OUTPUT_TOPIC = 'phlevelcheck'
    try:
        if (value >= 2.8 and value <= 2.9):
            response_message = "pH Value of water is good"
        elif  value > 2.9:   
            response_message = "Water is acidic. Add pH increaser"
        elif  value < 2.8:   
            response_message = "Add pH reducer"    
    except Exception as e:
        logging.error(e)
    client.publish(topic=OUTPUT_TOPIC, payload=response_message)
    return

