import json
from datetime import datetime
from flask import Blueprint, request
from log_setup import logger
from time_zone import convert_class_time
from models import add_booking_detail, get_bookings



route = Blueprint('route', __name__)

@route.route('/api/add_booking', methods=['POST'])
def add_bookings():
    content = request.get_json()
    class_id = content['class_id']
    client_name = content['client_name']
    client_email = content['client_email']

    if not class_id or not client_name or not client_email:
        logger.info("Missing required fields for booking.")
        return json.dumps({"error": "Missing required fields"}),400

    classes_data = load_classes()
    class_list = classes_data.get("classes_details", [])

    try:
        selected_class = next((c for c in class_list if c["id"] == class_id), None)

        if selected_class["available_slots"] <= 0:
            logger.info(f"No slots available for {class_id}.")
            return json.dumps({"error": "No slots available"}), 400

        add_booking_detail(class_id, client_name, client_email)


        selected_class["available_slots"] -= 1
        save_classes(classes_data)

        logger.info(f"Booking added successfully for {class_id}.")
        return json.dumps({"message": "Booking added successfully"},), 200

    except Exception as e:
        return f"Error: {e}", 500



@route.route('/api/get_classes_details', methods=['GET'])
def get_classes_details():
    try:
        classes_details = load_classes()
        current_date = datetime.now().isoformat() # IST
        upcoming_classes = [c for c in classes_details["classes_details"] if c["datetime"] > current_date]
        logger.info(f"Classes details fetched.")
        return json.dumps({"class_details": upcoming_classes}), 200

    except Exception as e:
        return f"Error: {e}", 500


@route.route('/api/get_booking_details', methods=['GET'])
def get_booking_details():
    try:
        content = request.get_json()
        email = content['email']
        classes_details = get_bookings(email)
        # check email exists in db

        booked_classes = [c for c in classes_details if c["client_email"] == email]
        if not booked_classes:
            logger.info(f"No booking details found for {email}.")
            return json.dumps({"error": "No booking details found"}), 400

        logger.info(f"Booking details fetched for {email}.")
        return json.dumps({"booking_details": classes_details}), 200

    except Exception as e:
        return f"Error: {e}", 500



@route.route('/api/change_timezone', methods=['POST'])
def get_classes():
    content = request.get_json()
    user_tz = content['timezone']
    classes_data = load_classes()
    class_list = classes_data.get("classes_details", [])

    for c in class_list:
        c["datetime"] = convert_class_time(c["datetime"], user_tz)

    save_classes(classes_data)
    logger.info(f"Timezone changed to {user_tz}")
    return json.dumps({"message":"Timezone Applied","classes": class_list}), 200



def load_classes():
    with open("sample_data.json", "r") as file:
        return json.load(file)

def save_classes(data):
    with open("sample_data.json", "w") as file:
        json.dump(data, file, indent=2)