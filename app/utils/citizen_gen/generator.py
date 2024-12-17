import json
import os
import random


class CitizenGen:
    def __init__(self, file_path=None, probability_source=None) -> None:
        """
        Initializes the NameGen class.

        Args:
            file_path: Path to the names file.
            probability_source: A callable or object to dynamically retrieve probabilities.
        """
        # Get the directory of the current file
        base_path = os.path.dirname(os.path.abspath(__file__))
        # Use the default file path if none is provided
        file_path = file_path or os.path.join(base_path, "names.json")

        # Load data from the names file
        with open(file_path) as f:
            self.data = json.load(f)

        self.boys = self.data["boys"]
        self.girls = self.data["girls"]
        self.surnames = self.data["surnames"]
        self.weird = self.data["weird"]
        self.occupations = self.data["occupations"]

        # Set the probability source (a callable or object)
        self.probability_source = probability_source or self.default_probability

    def default_probability(self) -> dict:
        """
        Default probability values.
        Override this in simulation or pass a callable to fetch probabilities dynamically.
        """
        return {
            "first_names": {
                "gender_match": 990,
                "gender_opposite": 7,
                "weird": 3,
            },
            "surnames": {
                "hyphenated": 240,
                "first_person": 750,
                "invented": 10,
                "weird": 0.01,
            },
            "town": {"unemployment": 0.2, "retirement_age": 65},
        }

    def get_probabilities(self, category: str) -> dict:
        """
        Fetches probabilities dynamically for the given category.
        """
        probabilities = self.probability_source()
        return probabilities.get(category, {})

    def generate_citizen(self, gender="neutral", min_age=1, max_age=101):
        first_name = self.generate_first_name(gender)
        last_name = self.generate_last_name()
        age = self.generate_age(min_age, max_age)
        occupation = self.generate_occupation()
        return {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "occupation": occupation,
        }

    def generate_full_name(self, gender="neutral", surname="invented") -> dict:
        first_name = self.generate_first_name(gender)
        last_name = self.generate_last_name()
        formatted_first = first_name.capitalize()
        formatted_last = last_name.capitalize()

        # Print full name for display/debugging
        print(f"{formatted_first} {formatted_last}")

        return {"first_name": formatted_first, "last_name": formatted_last}

    def generate_first_name(self, gender: str) -> str:
        probabilities = self.get_probabilities("first_names")
        choice = self.weighted_choice(probabilities)

        match choice:
            case "gender_match":
                if gender == "male":
                    return random.choice(self.boys)
                elif gender == "female":
                    return random.choice(self.girls)
                else:
                    return random.choice(self.boys + self.girls)
            case "gender_opposite":
                if gender == "female":
                    return random.choice(self.boys)
                elif gender == "male":
                    return random.choice(self.girls)
                else:
                    return random.choice(self.boys + self.girls)
            case "weird":
                return random.choice(self.weird)
            case _:  # Default case to handle unexpected choices
                return "Unknown"

    def generate_last_name(self) -> str:
        probabilities = self.get_probabilities("surnames")
        if random.random() < probabilities.get("weird", 0):
            return random.choice(self.weird)
        else:
            return random.choice(self.surnames)

    def weighted_choice(self, probabilities) -> str:
        """
        Take a dictionary of options and weights, and return one key based on the weights.
        """
        options, weights = zip(*probabilities.items())
        return random.choices(options, weights=weights, k=1)[0]

    def generate_age(self, min=1, max=102):
        return random.randint(min, max)

    def generate_occupation(self):
        probabilities = self.get_probabilities("town")
        if random.random() < probabilities.get("unemployment", 0):
            return "unemployed"
        else:
            return random.choice(self.occupations)


# Example dynamic probability source
def dynamic_probabilities():
    """
    Simulate dynamic probabilities. This can pull from a database, table, or any other source.
    """
    return {
        "first_names": {
            "gender_match": 500,  # Updated probabilities
            "gender_opposite": 400,
            "weird": 100,
        },
        "surnames": {
            "hyphenated": 50,
            "first_person": 30,
            "invented": 20,
            "weird": 0.05,
        },
    }


# Example usage
if __name__ == "__main__":
    # Pass the dynamic probability source to the NameGen class
    # generator = CitizenGen(probability_source=dynamic_probabilities)
    generator = CitizenGen()

    generator.generate_citizen()
