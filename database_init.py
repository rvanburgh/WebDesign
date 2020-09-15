from flaskblog import db
from flaskblog import create_app
from flaskblog.models import User, Thought, BurnsDepressionTest

app = create_app()
app.app_context().push()