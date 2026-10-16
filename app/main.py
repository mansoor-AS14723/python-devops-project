from flask import Flask, jsonify

from app.services import get_all_items, get_item_by_id

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Python DevOps Demo API",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/items", methods=["GET"])
def list_items():
    return jsonify(get_all_items()), 200


@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = get_item_by_id(item_id)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)