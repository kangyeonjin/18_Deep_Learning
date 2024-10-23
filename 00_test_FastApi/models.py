from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sqlalchemy베이스클래스생성
Base = declarative_base()

#데이터베이스 모델정의
class Item(Base):
    __tablename__='items'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    
#sqlite데이터베이스 연결
DATABASE_URL ="sqlite:///.test/db" #데이터베이스 url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#테이블생성
Base.metadata.create_all(bind=engine)