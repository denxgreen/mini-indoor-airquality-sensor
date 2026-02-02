from models.udataclasses import BaseModel, validator
from utils.measurements import TemperatureUnit

class Settings(BaseModel):
    units: str = TemperatureUnit.STANDARD
    
    @validator('units')
    def check_units(self, value: str) -> None:
        if value not in (TempUnit.METRIC, TempUnit.STANDARD, TempUnit.IMPERIAL):
            raise ValueError(f'Unit "{value}" is invalid.')
