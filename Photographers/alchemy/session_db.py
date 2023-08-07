from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://postgres:123@localhost/store')
autocommit_engine = engine.execution_options(isolation_level='AUTOCOMMIT')
__session = sessionmaker(autocommit_engine)
session: Session = __session()
