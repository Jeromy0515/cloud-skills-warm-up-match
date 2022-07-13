import json
import os
import sys


def handler(event, context):

    return {
        'statusCode': 200,
        'body': json.dumps({
            'version': sys.version,
            'region': os.environ['AWS_REGION'],
            'status': 'OK'
        })
    }
