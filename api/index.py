import os

from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)


@app.route('/api/webhook/email', methods=['POST'])
@app.route('/webhook/email', methods=['POST'])
def receive_email():
	try:
		# Get email info
		sender = request.form.get('from')
		to = request.form.get('to')
		subject = request.form.get('subject')
		text = request.form.get('text')
		html = request.form.get('html')

		# Build attachment metadata from uploaded files.
		attachments = []
		for field_name, uploaded_file in request.files.items():
			position = uploaded_file.stream.tell()
			uploaded_file.stream.seek(0, os.SEEK_END)
			size = uploaded_file.stream.tell()
			uploaded_file.stream.seek(position)

			attachments.append({
				"field": field_name,
				"filename": uploaded_file.filename,
				"content_type": uploaded_file.content_type,
				"size": size,
			})

		# Print or process the received email information
		print("--- New email received ---")
		print(f"Sender: {sender}")
		print(f"Recipient: {to}")
		print(f"Subject: {subject}")
		print(f"Content (Text): {text}")
		print(f"Attachment count: {len(attachments)}")

		for index, attachment in enumerate(attachments, start=1):
			size_mb = attachment['size'] / (1024 * 1024)
			print(f"Attachment {index}")
			print(f"  Field: {attachment['field']}")
			print(f"  Filename: {attachment['filename']}")
			print(f"  Content-Type: {attachment['content_type']}")
			print(f"  Size (MB): {size_mb:.4f}")

		return jsonify({"status": "success", "message": "Email received"}), 200

	except Exception as e:
		print(f"Error processing email: {e}")
		return jsonify({"status": "error", "message": "Internal server error"}), 500


# Expose Flask app as Vercel Python serverless entrypoint.
application = app


if __name__ == '__main__':
	# Local default is 5000 unless PORT is set in environment.
	port = int(os.getenv('PORT', '5000'))
	debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
	app.run(host='0.0.0.0', port=port, debug=debug)
