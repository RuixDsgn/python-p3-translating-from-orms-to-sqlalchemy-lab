from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    joey = Dog(
        name="joey",
        breed="cocker spaniel"
    )

    session.add(joey)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()

    return query


def find_by_id(session, id):
    dog_id = session.query(Dog).filter(Dog.id == id).first()

    return dog_id

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog

def update_breed(session, dog, breed):
    dog.breed=breed
    session.add(dog)
    session.commit()