from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data for demonstration purposes
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": 'Welcome to the Rest API'})

#Route that gets user data
@app.route('/user', methods=['GET'])
def get_user():
    user = {
        "id":1,
        "name":"John Doe",
        "email": "john@example.com"
    } 
    return jsonify(user)

#Route that creates new user data
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User created!", "data":data}),201 

if __name__ == '__main__':
    app.run(debug=True)

