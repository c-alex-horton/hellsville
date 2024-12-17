from app.db.db import db, Person, TownStats

class TownManager:
    def __init__(self):
        pass

    def get_population(self):
        """
        Count up all the people still alive in the person table and make that 
        the value of 'population' in the townstats table.
        """
        # Step 1: Count the people alive
        alive_count = Person.select().where(Person.alive == True).count()

        # Step 2: Update or insert the 'population' stat in TownStats
        # Check if the stat exists
        population_stat, created = TownStats.get_or_create(stat="population",
                                                           defaults={'value': alive_count})

        # If it already exists, update its value
        if not created:
            population_stat.value = alive_count
            population_stat.save()

        print(f"Population updated to {alive_count}")