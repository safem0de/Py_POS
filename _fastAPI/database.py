from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///_fastAPI/database.sqlite"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# from pysqlcipher import dbapi2 as sqlite
# # # https://stackoverflow.com/questions/30314882/using-pysqlcipher-with-sqlalchemy
# engine = create_engine(
#     'sqlite+pysqlcipher://:{0}@/{1}?'
#     'cipher=aes-256-cfb&kdf_iter=64000'.format('testtest', 'database.sqlite'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()