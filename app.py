import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

@app.route('/api/webhook/email', methods=['POST'])
@app.route('/webhook/email', methods=['POST'])
def receive_email():
    try:
        # SendGrid Inbound Parse form
        sender = request.form.get('from')
        to = request.form.get('to')
        subject = request.form.get('subject')
        text = request.form.get('text')
        html = request.form.get('html')
        
        # Print or process the received email information
        print("--- New email received ---")
        print(f"Sender: {sender}")
        print(f"Recipient: {to}")
        print(f"Subject: {subject}")
        print(f"Content (Text): {text}")
        
        # You can add your business logic here (for example, saving to a database or sending a notification)

        return jsonify({"status": "success", "message": "Email received"}), 200

    except Exception as e:
        print(f"Error processing email: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Local default is 5000 unless PORT is set in environment.
    port = int(os.getenv('PORT', '5000'))
    debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)