from flask import Blueprint as bp
from flask import request as rq
from flask import jsonify as jf
from src.views.http_types.http_request import HttpRequest as hr
from src.views.tag_creator_view import TagCreatorView as tc

tags_routes_bp = bp('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    tag_creator_view = tc()

    http_request = hr(body=rq.json)
    response = tag_creator_view.validate_and_create(http_request)

    return jf(response.body), response.status_code
