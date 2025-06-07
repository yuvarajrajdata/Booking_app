import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from db_tables import Booking
from db_tables import Base

engine = create_engine('sqlite:///bookings.db', echo=False, future=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def add_booking_detail(class_id, client_name, client_email):
    session = Session()
    print(Booking)
    try :
        new_booking = Booking(class_id=class_id, client_name=client_name, client_email=client_email)
        session.add(new_booking)
        session.commit()

    except ValueError as ve:
        print(f"Validation Error: {ve}")

    except SQLAlchemyError as sae:
        session.rollback()
        print(f"Database Error: {sae}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


def get_bookings(email):
    session = Session()

    try:
        bookings = session.query(Booking).filter_by(client_email=email).all()
        return [booking.to_json() for booking in bookings]

    except ValueError as ve:
        print(f"Validation Error: {ve}")

    except SQLAlchemyError as sae:
        session.rollback()
        print(f"Database Error: {sae}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return []

    finally:
        session.close()