import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))

current = os.path.dirname(os.path.realpath(__file__))
#print("current",current)

parent = os.path.dirname(current)
sys.path.append(parent)
#print("parent",parent)


#print("image_store",store_img)


class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    

#configuration of application
class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "testdb.db")
    DEBUG = True
    SECRET_KEY =  "really superrrr secret"

