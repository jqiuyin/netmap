import os
from app import create_app, db
from flask_migrate import Migrate, upgrade
from app.models import NetworkSegment, DataCenter

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, NetworkSegment=NetworkSegment, DataCenter=DataCenter)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()