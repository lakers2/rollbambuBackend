from sqlalchemy.orm import Session
from app.db.database import SessionLocal, create_tables
from app.models.fortune import Fortune

def init_db():
    create_tables()
    db = SessionLocal()

    fortunes = [
        {"name": "大吉", "interpretation": "运气很好，诸事顺利。"},
        {"name": "中吉", "interpretation": "运气不错，可以期待好事发生。"},
        {"name": "小吉", "interpretation": "运气稍好，保持积极态度。"},
        {"name": "吉", "interpretation": "运气一般，努力会有回报。"},
        {"name": "末吉", "interpretation": "运气平平，不必太过担心。"},
        {"name": "凶", "interpretation": "运气欠佳，需要谨慎行事。"},
        {"name": "大凶", "interpretation": "运气不佳，最好避免重要决定。"},
    ]

    for fortune in fortunes:
        db_fortune = Fortune(**fortune)
        db.add(db_fortune)

    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()