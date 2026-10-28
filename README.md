# Webhook Demo

A simple Flask application that receives email webhook data and prints the email details to the console.

## Overview

This project is intended to demonstrate how to receive incoming email data from a webhook, such as SendGrid Inbound Parse, and process it in a Python backend.

It currently reads fields like:

- sender
- recipient
- subject
- text content

Then it returns a JSON success response and logs the values.

## Features

- Flask-based webhook endpoint
- Accepts HTTP POST requests
- Reads standard email form fields
- Logs incoming email details
- Returns a success or error response
- Ready to be deployed on Vercel

## Project Structure

```text
.
├── app.py
├── api/
│   └── index.py
├── requirements.txt
├── vercel.json
├── README.md
└── .venv/   # local virtual environment (optional)
```

## Local Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate it:

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

The app runs on:

```text
http://0.0.0.0:5000
```

## Webhook Endpoint

```text
POST /webhook/email
```

Example form fields:

- from
- to
- subject
- text
- html

## Deployment

This project includes Vercel configuration in `vercel.json` and exposes the Flask app through `api/index.py`.

After deployment, the webhook URL will be similar to:

```text
https://<your-vercel-domain>/webhook/email
```

## Notes

- This is a basic demo and does not include persistent storage, authentication, or production-grade security checks.
- It is suitable for testing webhook behavior and logging incoming email payloads.
- For production use, you should add validation, database storage, and monitoring.
