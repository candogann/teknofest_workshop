# Title: Module Mail
# Description: Mail module for sending emails autamatically using Python and AWS Lambda
# You can send emails to mail lists using this module.

import smtplib, ssl, logging, json
from email.message import EmailMessage

# I will comment this out for now because i dont want to add layer to lambda function. I will add this later when i add the layer.
#from pymongo import MongoClient 

# MongoDB connection

#client = MongoClient('') # MongoDB connection string, added for future use 
# db = client[''] # MongoDB database name, added for future use

# Email configuration


port = 465  # For starttls
smtp_server = "smtp.gmail.com" 
email = "YOUR-EMAIL" # 
password = "YOUR-PASS" 
# Logger

logging.basicConfig()
logging.root.setLevel(logging.INFO)
logger = logging.getLogger("ETTA-Mail Module Log")

##
#
# This function is the main function of the module. It is called by the lambda function. When lambda function triggers, this function is called. 
# Basically a main method in terms of java/c++.
# @param event: Event object for lambda, check lambda docs for more info
# @param context: Context object for lambda
# @return: Returns a JSON object with status code and body
#
##
def lambda_handler(event, context):
    print(event)
    msg = EmailMessage()
    logger.info("Event body load has started.")
    print(event)
    bodyJson = event # This is for API Gateway
    #bodyJson = event['body'] # This is for local testing
    

    ###
    logger.info("Mail initialization has started.")
    msg['From'] = email
    msg['Subject'] = bodyJson.get('mailSubject') # this is subject of mail
    msg.set_content(bodyJson.get('mailContents'), subtype='html') # this is contents of mail @TODO: Add html support.
    msg['To'] = bodyJson.get("mailList") # This is array of mail addresses 

    ###

    logger.info("The mail to be sent is: \n" + str(msg))

    ###


    logger.info("Mail sending has started.")

    sslContext = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = sslContext) as server:
        server.login(email, password)
        server.send_message(msg, from_addr=email, to_addrs=bodyJson.get('mailList'))
        server.quit()

    logger.info("Mail sending has finished.")


    return {"statusCode": 200, "body": "Mail has been sent."}

#testevent = { "body": { "mailList": ["ulworddev@gmail.com", "cannezih09@gmail.com"], "mailSubject": "Test", "mailContents": "Test"}} # This is event body

#lambda_handler(testevent, None) # This is for local testing
