from sqlalchemy import Column, String, Float, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from country_etl_project.db import Base
from sqlalchemy.orm import sessionmaker

class CountryModel(Base):
    __tablename__ = 'countries'

    id = Column(Integer,primary_key=True)
    country_name =  Column(String)
    country_code = Column(String) 
    independence_status = Column(Boolean) 
    country_currency = Column(String)
    country_capital = Column(String)
    country_region = Column(String)
    country_subregion = Column(String)
    country_languages = Column(String)
    country_latitude = Column(String)
    country_longitude = Column(String)
    country_landlock_status = Column(Boolean)
    country_borders = Column(String)
    country_area = Column(Float)
    country_location = Column(String)
    country_population = Column(String)
    country_car_sign = Column(String)
    country_car_side = Column(String)
    country_timezones = Column(String)
    country_continents = Column(String)
    country_flag = Column(String)
    country_ltd = Column(String)
    created_at = Column(DateTime(timezone=True),default=func.now())
