from . import db

class NetworkSegment(db.Model):
    __tablename__ = 'network_segments'
    id = db.Column(db.Integer, primary_key=True)
    network_segment = db.Column(db.String(64), unique=True)

    datacenter_id = db.Column(db.Integer, db.ForeignKey('datacenters.id'))

    def __repr__(self) -> str:
        return '<NetworkSegment %r>' % self.network_segment

class DataCenter(db.Model):
    __tablename__ = 'datacenters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    network_segments = db.relationship(NetworkSegment, backref='datacenter',lazy='dynamic')

    def to_json(self):
        json_dataCenter={
            'name': self.name
        }
        return json_dataCenter

    def __repr__(self) -> str:
        return '<DataCenter %r>' % self.name