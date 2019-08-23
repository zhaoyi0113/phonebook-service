import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.environ['POSTGRES_USER']
pwd = os.environ['POSTGRES_PASSWORD']
db = os.environ['POSTGRES_DB']

db_url = 'postgresql://'+user+':'+pwd+'@db:5432/'+db
print('connect to db ' + db_url)
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()
print('Created db connection.')