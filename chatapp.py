from flask import Flask, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

app = Flask(__name__)

def get_completion(prompt, model="gpt-3.5-turbo-0125"):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return completion.choices[0].message.content


@app.route('/get_department_suggestion', methods=['POST'])

def get_department_suggestion():

    data = request.get_json()

    query = data.get('query')

    if not query:
        return jsonify({'error': 'Query parameter is missing'}), 400

    details = f"""
    You are helpful assistant, designed to suggest the respective department
    based on user query
    provide output in JSON format

    '''{query}'''

    """

    department = get_completion(details)
    return jsonify({"department": department})

if __name__ == '__main__':
    app.run(debug=True)
