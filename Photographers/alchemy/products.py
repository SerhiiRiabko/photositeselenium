from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, INTEGER, VARCHAR

Base = declarative_base()

class Products(Base):
    __tablename__ = 'users'
    id = Column(INTEGER, primary_key=True)
    product_name = Column(VARCHAR(25))
    price = Column(INTEGER)
