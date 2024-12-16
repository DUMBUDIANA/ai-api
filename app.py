# import os
# from dotenv import load_dotenv
# from groq import Groq

# client = Groq(
#   api_key=os.environ.get("GROQ_API_KEY"),
#  )

# chat_completion = client.chat.completions.create(
#   messages=[
#          {
#             "role": "user",
#              "content": "Explain the importance of fast language models",
#         }
#     ],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)

# from dotenv import load_dotenv
# import os
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()

# # Initialize the Groq client with the API key from the environment variable
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# try:
#     # Make a chat completion request
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Explain the importance of fast language models",
#             }
#         ],
#         model="llama3-8b-8192",  # Ensure the model name is correct
#     )

#     # Print the response from the model
#     print(chat_completion.choices[0].message.content)

# except Exception as e:
#     print(f"An error occurred: {e}")
# import os
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()

# # Print the API key to ensure it's being loaded correctly
# print("API Key Loaded:", os.environ.get("GROQ_API_KEY"))

# # Create the client with the loaded API key
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

# chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "user",
#         "content": "Explain the importance of fast language models",
#     }],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)



# import os
# from dotenv import load_dotenv
# from groq import Groq

# # Load environment variables from the .env file
# load_dotenv()

# # Now, Groq API client can access the environment variable
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")  # Use getenv to safely access the API key
# )

# chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "user",
#         "content": "Explain the importance of fast language models",
#     }],
#     model="llama3-8b-8192",
# )

# print(chat_completion.choices[0].message.content)


# from flask import Flask, request, jsonify
# from dotenv import load_dotenv
# import os
# from groq import Groq

# # Load environment variables from the .env file
# load_dotenv()

# app = Flask(__name__)

# # Initialize Groq client with API key from environment variables
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # Define the '/api/chat' route to handle POST requests
# @app.route('/api/chat', methods=['POST'])
# def chat():
#     try:
#         # Extract the user's message from the POST request's body
#         message = request.json.get('message')
#         if not message:
#             return jsonify({'error': 'No message provided'}), 400

#         # Call the Groq API for chat completion
#         chat_completion = client.chat.completions.create(
#             messages=[{"role": "user", "content": message}],
#             model="llama3-8b-8192",  # Use the correct model
#         )

#         # Return the response from Groq API
#         return jsonify({"response": chat_completion.choices[0].message.content})

#     except Exception as e:
#         # Handle exceptions and return a generic error message
#         return jsonify({'error': str(e)}), 500

# # Start the Flask server on port 5000
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

# from flask import Flask, request, jsonify
# from flask_cors import CORS  # Import Flask-CORS for handling CORS issues

# # Initialize Flask app
# app = Flask(__name__)

# # Enable CORS to allow requests from React frontend
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, 
#      supports_credentials=True,
#      methods=["GET", "POST", "OPTIONS"],
#      allow_headers=["Content-Type", "Authorization"])

# @app.route('/api/chat', methods=['POST'])
# def chat():
#     # Log request data for debugging
#     print("Request received:", request.json)

#     # Extract the message from the request body
#     user_message = request.json.get('message')

#     # Generate a simple response
#     response_message = f"Echo: {user_message}"  # Mock response for testing

#     # Return the response as JSON
#     return jsonify({'response': response_message})


# if __name__ == '__main__':
#     # Run Flask app on localhost with debugging enabled
#     app.run(debug=True)


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
