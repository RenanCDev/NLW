from flask import Blueprint as bp
from flask import request as rq
from flask import jsonify as jf

tags_routes_bp = bp('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    print(rq.json)
    return jf({ "resp": "ok" }), 200
