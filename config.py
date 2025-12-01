import os 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database location 
    SQLALCHEMY_DATABASE_URI = "sqlite:///cms.db"

    # Disable modification tracking for performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False