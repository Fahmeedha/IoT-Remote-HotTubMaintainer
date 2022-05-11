import boto3
import logging
import json

client = boto3.client('iot-data', region_name='us-west-2')
s3 = boto3.client('s3')

def function_handler(event, context):
    response = s3.get_object(Bucket='wlevelfromhottubbucket', Key='wlevelfromhottub.json')
    value = response['Body'].read()
    wlevel_value = json.loads(value)
    OUTPUT_TOPIC = 'waterlevel'
    try:
        response_message = json.dumps(wlevel_value)
    except Exception as e:
        logging.error(e)
    client.publish(topic=OUTPUT_TOPIC, payload=response_message)
    return
