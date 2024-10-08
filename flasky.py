import os
from app import create_app, db
from app.templates.models import User, Role  # Importação ajustada para a nova localização
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Role': Role}

if __name__ == '__main__':
    app.run()
