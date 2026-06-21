from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base

class City(Base):
    __tablename__ = "cities"

    city_id = Column(
        Integer,
        primary_key=True,
        index = True
    )

    city_name = Column(
        String(50),
        nullable = False
    )

    state_name = Column(
        String(50),
        nullable = False
    )
    
    country_name = Column(
        String(50),
        nullable = False,
    )
    
    centroid_lat = Column(Float)

    centroid_lon = Column(Float)

    population = Column(
        Integer,
        nullable = True
    )

    area_sqkm = Column(Float)

    created_at = Column(
        DateTime,
        default = datetime.utcnow
    )