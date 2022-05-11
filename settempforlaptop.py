import boto3
import logging
import json

client = boto3.client('iot-data', region_name='us-west-2')
s3 = boto3.client('s3')

def function_handler(event, context):
    response = s3.get_object(Bucket='tempfromhottubbucket', Key='tempfromhottub.json')
    temp_value = json.loads(response['Body'].read())
    temp_value = int(temp_value.strip('F'))
    OUTPUT_TOPIC = 'temperature'
    x = event['set']
    value = int(x)
    try:
        if temp_value >= value:
            response_message = "Temperature already HIGH"
        elif temp_value < value:
            response_message = "SETTING HEATER ON " + str(value)
    except Exception as e:
        logging.error(e)
    client.publish(topic=OUTPUT_TOPIC, payload=response_message)
    return