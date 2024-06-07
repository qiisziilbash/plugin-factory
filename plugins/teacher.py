from dataclasses import dataclass

import factory


@dataclass
class Teacher:

    name: str
    specialty: str = "psychedelics"

    def respond(self) -> None:
        print(f"I am {self.name} and I am specialized at {self.specialty}!")


def register() -> None:
    factory.register("teacher", Teacher)
