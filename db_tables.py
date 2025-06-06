import json
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Booking(Base):
    __tablename__ = 'tbl_booking'

    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    client_name = Column(String(100), nullable=False)
    client_email = Column(String(200), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'class_id': self.class_id,
            'client_name': self.client_name,
            'client_email': self.client_email
        }