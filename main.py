"""The main module of the application."""

from flask import Flask, jsonify, request
from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController

app = Flask(__name__) # pylint: disable=invalid-name

@app.route("/ticket")
def get_ticket_list():
    """Get a list of tickets."""
    tickets_array = TicketController.get_tickets()
    return jsonify(tickets_array)

@app.route("/ticket/<int:ticket_id>")
def get_single_ticket(ticket_id):
    """Get the details of a single ticket."""
    tickets_array = TicketController.get_ticket_by_id(ticket_id)
    return jsonify(tickets_array.conv_ticket_to_dict())

@app.route("/ticket", methods=["POST"])
def create_ticket():
    """Create a new ticket."""
    ticket_data = request.get_json()
    new_ticket = TicketController.create_ticket(ticket_data)
    return jsonify(new_ticket.conv_ticket_to_dict())

@app.route("/ticket/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    """Delete a ticket."""
    TicketController.delete_ticket(ticket_id)
    response = success_response_body({})
    return response

@app.route("/ticket/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    """Update a ticket."""
    ticket_data = request.get_json()
    put_ticket = TicketController.update_ticket(ticket_id, ticket_data)
    return jsonify(put_ticket)

@app.route("/user")
def get_user_list():
    """Get a list of users."""
    user_array = UserController.get_users()
    return jsonify(user_array)

@app.route("/user/<int:user_id>")
def get_single_user(user_id):
    """Get the details of a of user."""
    user_array = UserController.get_users_by_id(user_id)
    return jsonify(user_array)

@app.route("/user", methods=["POST"])
def create_user():
    """Create a new user."""
    user_data = request.get_json()
    new_user = UserController.create_user(user_data)
    return jsonify(new_user)

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user."""
    del_user = UserController.delete_ticket(user_id)
    return jsonify(del_user)

@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update a user."""
    user_data = request.get_json()
    put_user = UserController.update_user(user_id, user_data)
    return jsonify(put_user)

@app.errorhandler(404)
def not_found(_error):
    """Return the notfound page for missing paths."""
    my_404_str = {
        "code": 404,
        "error": "This API call does not exist",
        "result": False
    }
    return jsonify(my_404_str), 404

def success_response_body(data):
    """Return a successful message."""
    return {"result": True, "data": data}    

if __name__ == "__main__":
    app.run()
