from flask import Flask, request, jsonify

app = Flask(__name__)

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
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Local test port is 5000
    app.run(host='0.0.0.0', port=5000, debug=True)