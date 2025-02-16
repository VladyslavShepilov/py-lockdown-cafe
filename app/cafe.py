import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError

        vaccine_expiration_date = visitor["vaccine"].get("expiration_date")
        if (vaccine_expiration_date
                and vaccine_expiration_date < datetime.date.today()):
            raise OutdatedVaccineError

        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
