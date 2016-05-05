from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base()
engine = create_engine('mysql+pymysql://root:45223@localhost/learn_python')
DBSession = sessionmaker(bind=engine)

class Code(Base):
    __tablename__ = 'code'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(32), unique=True)

if __name__ == '__main__':
    session = DBSession()
    metadata.create_all(engine)
    with open('../0001/codes.txt', 'r') as f:
        for code in f.readlines():
            new_code = Code(code=code)
            session.add(new_code)
    session.commit()
    session.close()
