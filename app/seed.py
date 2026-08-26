from datetime import datetime
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Location, Building, Floor, Room, Sensor

Base.metadata.create_all(bind=engine)

def seed_data():
    db: Session = SessionLocal()

    try:
        loc_building = Location(type="building", name="Общежитие №1", parent_id=None)
        db.add(loc_building)
        db.commit()
        db.refresh(loc_building)

        building = Building(location_id=loc_building.id, address="ул. Ленина, 10")
        db.add(building)

        loc_floor = Location(type="floor", name="4 этаж", parent_id=loc_building.id)
        db.add(loc_floor)
        db.commit()
        db.refresh(loc_floor)

        floor = Floor(location_id=loc_floor.id, number=4)
        db.add(floor)

        loc_room1 = Location(type="room", name="417", parent_id=loc_floor.id)
        loc_room2 = Location(type="room", name="418", parent_id=loc_floor.id)
        db.add_all([loc_room1, loc_room2])
        db.commit()

        room1 = Room(location_id=loc_room1.id, number="417", capacity=3)
        room2 = Room(location_id=loc_room2.id, number="418", capacity=2)
        db.add_all([room1, room2])

        sensor1 = Sensor(location_id=loc_room1.id, type="temperature", name="Temp 1_4_417", unit="C°")
        sensor2 = Sensor(location_id=loc_floor.id, type="electricity", name="Temp 1_4_000", unit="кВт/ч")
        sensor3 = Sensor(location_id=loc_building.id, type="water", name="Water 1_0_000", unit="л/мин")
        db.add_all([sensor1, sensor2, sensor3])
        db.commit()
        print("Test data successfully added")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()