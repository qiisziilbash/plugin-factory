from dataclasses import dataclass

import factory


@dataclass
class Patient:

    name: str
    specialty: str = "depressed"

    def respond(self) -> None:
        print(f"I am {self.name} and I am specialized at being {self.specialty}!")


def register() -> None:
    factory.register("patient", Patient)
