#import 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import config

#engine 
engine = create_engine(config.database_url,echo=True,pool_pre_ping=True)

#sessionfactory
sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

#sesssion
def get_db():
    with sessionLocal() as session:
        yield session
            