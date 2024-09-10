from flask import render_template, request 
from twilio.rest import Client

# Twilio configuration
account_sid = 'ACbd2cdc6aaa0af2d3670fd4fd2d7e410d'
auth_token = 'e1163f37d5be98a748b044364a9763b7'
twilio_phone_number = '+16318304712'

client = Client(account_sid, auth_token)

def send_sms_from_mobile_route():
    phone_number = request.form['phone_number']
    message = request.form['message']
    
    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=phone_number
        )
        return render_template('success.html')
    except Exception as e:
        return f"Failed to send message: {str(e)}"