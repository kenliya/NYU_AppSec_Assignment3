from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker

#from app import db

engine = create_engine('sqlite:///app.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
 
class User(Base):
    __tablename__ = 'users'
    username = Column(String(32), unique=True, primary_key=True)
    password = Column(String(120), nullable=False)
    phone = Column(String(15), unique=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# create tables
#def db_init():
Base.metadata.create_all(engine)