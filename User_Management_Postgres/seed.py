from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
import app.models as models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_data = [
    {"username": "admin", "email": "admin@example.com", "password": "admin123"},
    {"username": "user1", "email": "user1@example.com", "password": "password1"},
    {"username": "user2", "email": "user2@example.com", "password": "password2"},
]

def seed_db():
    models.Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()
    
    try:
        for user in users_data:
            existing_user = db.query(models.User).filter(models.User.email == user["email"]).first()
            if not existing_user:
                hashed_password = pwd_context.hash(user["password"])
                new_user = models.User(
                    username=user["username"],
                    email=user["email"],
                    hashed_password=hashed_password,
                )
                db.add(new_user)
        db.commit()
        print("Base de datos inicializada con datos de prueba.")
    except Exception as e:
        db.rollback()
        print(f"Error al poblar la base de datos: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()