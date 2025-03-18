from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def whatsapp_webhook():
    # Extract incoming message details from Twilio's POST request
    from_number = request.values.get('From')  # Sender's WhatsApp number
    body = request.values.get('Body')         # Message content
    
    print(f"Received message from {from_number}: {body}")
    
    # Optional: Echo the message back
    resp = MessagingResponse()
    resp.message(f"Echo: {body}")
    
    return str(resp)

if __name__ == '__main__':
    app.run()