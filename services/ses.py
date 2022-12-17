import logging

import boto3


class SESService():
    

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
