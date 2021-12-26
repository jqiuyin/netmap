from . import api
from ..models import DataCenter, NetworkSegment
from flask import request, jsonify, abort
from .errors import bad_request

@api.route('/datacenter')
def get_datacenter():
    if not request.args:
        return bad_request('no network_segment')
    network_segment_name = request.args['network_segment']
    datacenter = DataCenter.query.join(NetworkSegment)\
        .filter(NetworkSegment.network_segment == network_segment_name).first()
    if not datacenter: 
        abort(404)
    return jsonify(datacenter.to_json())
