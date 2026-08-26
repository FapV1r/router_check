from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Location, Building, Floor, Room, Sensor

def test_hierarchy():
    db: Session = SessionLocal()

    try:
        loc_building = db.query(Location).filter(Location.type == "building").first()
        print(f"Building: {loc_building.name}")
        print(f"    ID: {loc_building.id}")
        print(f"    Parent_ID: {loc_building.parent_id}")
        print()

        floors = db.query(Location).filter(Location.parent_id == loc_building.id).all()
        print("building floors")
        for loc_floor in floors:
            print(f" - {loc_floor.name} (ID: {loc_floor.id})")

            rooms = db.query(Location).filter(Location.parent_id == loc_floor.id).all()
            print("     rooms")
            for loc_room in rooms:
                print(f"    -{loc_room.name} (ID: {loc_room.parent.id})")
        print()

        print("relationship check")
        loc_room = db.query(Location).filter(Location.type == "room").first()
        print(f"    Room: {loc_room.name}")
        print(f"    parent through relationships: {loc_room.parent.name if loc_room.parent else None}")
        if loc_room.parent:
            print(f" Gandfather: {loc_room.parent.parent.name if loc_room.parent.parent else None}")
        print()

        print("Sensors")
        sensors = db.query(Sensor).all()
        for sensor in sensors:
            loc = db.query(Location).filter(Location.id == sensor.location_id).first()
            print(f" - {sensor.name}")
            print(f"    Type: {sensor.type}")
            print(f"    Location: {loc.name}")
            print(f"    hierarchi ", end="")

            path = []
            current = loc
            while current:
                path.append(current.name)
                current = current.parent
            print(" → ".join(reversed(path)))
    finally:
        db.close()

if __name__ == "__main__":
    test_hierarchy()