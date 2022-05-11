import boto3
import logging
import json

client = boto3.client('iot-data', region_name='us-west-2')
s3 = boto3.client('s3')

def function_handler(event, context):
    response = s3.get_object(Bucket='wlevelfromhottubbucket', Key='wlevelfromhottub.json')
    wlevel_value = response['Body'].read()
    OUTPUT_TOPIC = 'waterlevel'
    try:
        if json.loads(wlevel_value) == "HIGH":
            response_message = "Water level already HIGH"
        elif json.loads(wlevel_value) == "LOW":
            response_message = "SETTING WATER LEVEL"
    except Exception as e:
        logging.error(e)
    client.publish(topic=OUTPUT_TOPIC, payload=response_message)
    return
