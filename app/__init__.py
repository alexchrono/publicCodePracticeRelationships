from .factory import create_app
from .config import Configuration
from flask_migrate import Migrate
from .models import db  # Import db once
app = create_app()
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)

# from . import selfmade_queries  # Import your routes (selfmade_queries) here

if __name__ == "__main__":
    app.run()
