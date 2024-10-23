from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Item

app = FastAPI()

#의존성으로 데이터베이스 세션 제공
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#아이템추가API
@app.post("/items/")
def create_item(item: Item, db: Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
    