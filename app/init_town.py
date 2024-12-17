from app.db.db import db, Person
from app.utils.citizen_gen.generator import CitizenGen
import random

db.connect()

generator = CitizenGen()


def gen_town():
    with db.atomic():  # Wrap all insertions in a single transaction
        for _ in range(1000):  # Simplified loop
            gender = "male" if random.random() < 0.5 else "female"
            new_citizen = generator.generate_citizen(gender, 21,89)

            # Create a Person instance and save it
            Person.create(
                first_name=new_citizen["first_name"],
                last_name=new_citizen["last_name"],
                gender=gender,
                age=new_citizen["age"],
                occupation=new_citizen["occupation"]
            )


if __name__ == "__main__":
    gen_town()
