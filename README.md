# Booking_app
This is a simple RESTful API built with Flask for a fictional fitness studio that offers classes like Yoga, Zumba, and HIIT. Clients can view available classes, book a slot, and check their bookings by email

# Fitness Studio Booking API

## Setup


## 1. Clone the repository:
   git clone https://github.com/yuvarajrajdata/Booking_app.git
   cd booking-api

## 2 . Install dependencies:
    pip install -r requirements.txt

## 3. Run the app:
    RUN the application using run button or flask run app.py in terminal

## 4.  Postman requests:

    1. Get all fitness classes
       Method : GET
       URL : http://127.0.0.1:5000/api/get_classes_details  # may also run in port 80

    2. Add a booking (book a class)
       Method : POST
       URL : http://127.0.0.1:5000/api/add_booking  # may also run in port 80
       Body : (raw JSON)

       sample :
        payload : {
                    "class_id": 1,
                    "client_name": "Yuvaraj",
                    "client_email": "yuvarajspt1998@gmail.com" }


    3. Get bookings by client email
       Method: GET
       URL : http://127.0.0.1:5000/api/get_booking_details


POST RESPONSE
```bash
POSTMAN/get_classes_details.png

POSTMAN/add bookings.png

POSTMAN/get_booking_details.png

POSTMAN/log.png
