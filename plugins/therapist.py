from dataclasses import dataclass

import factory


@dataclass
class Therapist:

    name: str
    specialty: str = "psychedelics"

    def respond(self):
        print(f"I am {self.name} and I am specialized at {self.specialty}!")


def register() -> None:
    factory.register("therapist", Therapist)
