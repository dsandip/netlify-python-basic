from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/.netlify/functions/api')
def hello_world():
    # Create the JSON response
    response_data = {
        'user_id': 1,
        'email': 'test@test.com',
        'name': 'sandip'
    }

    # Return the JSON response
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()

