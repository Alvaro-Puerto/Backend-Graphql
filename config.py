import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    DEGUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://" + os.environ['DB_USER'] \
                            + ":" + os.environ['DB_PASSWORD'] + "@" \
                            + os.environ['DB_HOST'] + ":" \
                            + os.environ['DB_PORT'] + "/" \
                            + os.environ['DB_NAME']
    JWT_SECRET_KEY=os.environ['JWT_SECRET_KEY']