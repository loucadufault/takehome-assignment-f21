from typing import Counter, Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.
    
    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/shows", methods=['GET'])
def get_all_shows():
    shows = db.get('shows')

    if "minEpisodes" in request.args:
        minEpisodes = int(request.args["minEpisodes"])
        return create_response({"shows": [show for show in shows if show["episodes_seen"] >= minEpisodes]}) # returns an empty list if there are no matching shows

    return create_response({"shows": shows})
    

@app.route("/shows/<id>", methods=["GET"])
def get_show(id):
    show = db.getById("shows", int(id)) # todo handle non-digit string
    if show is None:
        return create_response(status=404, message="No show with this id exists")

    return create_response(data={"show": show})

@app.route("/shows", methods=["POST"])
def create_show():
    print(request.json.get("name"))
    if "name" not in request.json or "episodes_seen" not in request.json:
        return create_response(status=422, message="Request must send a 'name' and 'episodes_seen' parameter")

    newShow = db.create("shows", {
        "name": request.json["name"],
        "episodes_seen": request.json["episodes_seen"]
    })

    return create_response(status=201, data={"show": newShow})

@app.route("/shows/<id>", methods=["PUT"])
def update_show(id):
    updatedShow = db.updateById(
        "shows", 
        int(id), 
        { allowedAttributeKey: request.json[allowedAttributeKey] for allowedAttributeKey in ["name", "episodes_seen"] if allowedAttributeKey in request.json }) # todo handle non-digit string

    if updatedShow is None:
        return create_response(status=404, message="No show with this id exists")
    
    return create_response(data={"show": updatedShow})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('shows', int(id)) is None:
        return create_response(status=404, message="No show with this id exists")
    db.deleteById('shows', int(id))
    return create_response(message="Show deleted")


# TODO: Implement the rest of the API here!

"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
