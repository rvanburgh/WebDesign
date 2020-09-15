from flaskblog import create_app, db
from flaskblog.models import User, Thought, BurnsDepressionTest, DysfunctionalAttitudeScale, Gratitude
import os

KEY= os.environ.get('SECRET_KEY')
app = create_app()
app.config['SECRET_KEY']=str(KEY)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Thought=Thought, BurnsDepressionTest=BurnsDepressionTest, DysfunctionalAttitudeScale=DysfunctionalAttitudeScale, Gratitude=Gratitude)

if __name__ == '__main__':
    app.run(debug=True)
