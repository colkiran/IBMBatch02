
from flask import Flask, request, jsonify

app = Flask(__name__)# Create a dummy database
users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
]

# Define the PATCH endpoint
@app.route('/users/<int:id>', methods=['PATCH'])
def patch_user(id):
    # Get the user from the database
    user = next((user for user in users if user['id'] == id), None)

    # If the user doesn't exist, return a 404 error
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Get the data from the request body
    data = request.get_json()

    # Update the user's name
    user['name'] = data['name']

    # Save the changes to the database
    # ...

    # Return the updated user
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
