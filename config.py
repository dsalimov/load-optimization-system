# Configuration Management for Python 3.14

class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = 'your_secret_key_here'
    ALLOWED_HOSTS = ['localhost']

# You can create additional classes for different environments like Production, Development, etc.
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'mysql://user@localhost/foo'