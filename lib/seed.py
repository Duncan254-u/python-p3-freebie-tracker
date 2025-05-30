from config import Base, engine, SessionLocal
from models import Company, Dev, Freebie

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    print(" Clearing old data...")
    db.query(Freebie).delete()
    db.query(Company).delete()
    db.query(Dev).delete()
    db.commit()

    print("Creating companies...")
    companies = [
        Company(name="TechCorp", founding_year=2000),
        Company(name="DevSoft", founding_year=1995),
        Company(name="CodeMasters", founding_year=2010)
    ]
    db.add_all(companies)

    print("Creating devs...")
    devs = [
        Dev(name="Alice"),
        Dev(name="Bob"),
        Dev(name="Charlie")
    ]
    db.add_all(devs)
    db.commit()

    print("Creating freebies...")
    freebies = [
        Freebie(item_name="T-shirt", value=15, dev=devs[0], company=companies[0]),
        Freebie(item_name="Mug", value=10, dev=devs[0], company=companies[1]),
        Freebie(item_name="Sticker", value=5, dev=devs[1], company=companies[0]),
        Freebie(item_name="Laptop", value=1000, dev=devs[2], company=companies[2])
    ]
    db.add_all(freebies)
    db.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()