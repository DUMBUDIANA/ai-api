
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call Groq API to generate a response
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message}
            ],
            model="llama3-8b-8192"
        )
        # Extract the AI's response
        response_message = chat_completion.choices[0].message.content
        return jsonify({"response": response_message})

    except Exception as e:
        print(f"Error communicating with Groq API: {e}")
        return jsonify({"error": "Failed to generate a response"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
