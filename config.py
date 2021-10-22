import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 1) gives us access to this projects location in any
#    OS we find ourselves in.
# 2) allows us access to other folders to be added into
#    project from external sources.

class Config:
    """
    Sets the configuration variables for our flask app
    Eventually we will use hidden variable items, 
    but for now we'll leave them exposed.
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Decreases unneccessary output in terminal
    