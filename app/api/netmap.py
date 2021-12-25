from . import api
from ..models import DataCenter, NetworkSegment
from flask import request, jsonify

@api.route('/datacenter')
def get_datacenter():
    network_segment_name = request.args['network_segment']
    datacenter = DataCenter.query.join(NetworkSegment)\
        .filter(NetworkSegment.network_segment == network_segment_name).first()
    return jsonify(datacenter.to_json())
