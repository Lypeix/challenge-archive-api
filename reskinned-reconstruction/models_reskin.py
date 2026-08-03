from datetime import datetime # imports Python's date n time class

from sqlalchemy import DateTime, String, func # DateTime tells SQLAlchemy that the db column stores date n time values
                                              # String - db-side string
                                              # func gives access to the SQL functions

from sqlalchemy.orm import Mapped, mapped_column # Mapped marks attribute as belonging to the ORM Mapping (python-side)
                                                 # mapped_column defines the db column config for a mapped attribute 

from app.database import Base # imports the declarative base class which marks python models as ORM models