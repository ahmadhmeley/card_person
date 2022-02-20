from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:123456@localhost/abo_Mohammed", echo=True)

base = declarative_base()

sessionLocal = sessionmaker(bind=engine)



