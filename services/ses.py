import logging

import boto3


class SESService():
    def __init__(self):
        self.client = boto3.client(
            'ses',
            aws_access_key_id='AKIA6BZMFCPEFH5GCQPX',
            aws_secret_access_key="AKIA6BZMFCPEFH5GCQPX,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",
            region_name="us-east-1",
        )

    def send_email(self, email):
        logging.info("Starting email sending process")
        response = self.client.send_email(
            Source='zhelyazkomd@gmail.com',
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to our website',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'Welcome to our website. Now you are registered. Enjoy!',
                        'Charset': 'UTF-8'
                    },
                }
            },
        )
        logging.info(f'Email sent {response}')
