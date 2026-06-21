from sqlalchemy import Column, Integer, Float,Date,ForeignKey
from app.db.database import Base

class EnvironmentalObservation(Base):
    __tablename__ = "environmantal_observation"

    observation_id = Column(
        Integer,
        primary_key=True,
        index = True
    )

    city_id = Column(
        Integer,
        ForeignKey("cities.city_id")
    )

    observation_date = Column(Date)