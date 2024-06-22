
# PyBooking 🏨📅

![Build Status](https://img.shields.io/github/actions/workflow/status/danieljoris/py-booking/ci.yml?branch=main)
![Coverage Status](https://img.shields.io/codecov/c/github/danieljoris/py-booking)
![License](https://img.shields.io/github/license/danieljoris/py-booking)


**PyBooking** is a reservation management API built with Python. This API is designed to streamline the booking process for various industries, including hotels, restaurants, and event management. PyBooking aims to provide an efficient and seamless experience for developers integrating reservation systems into their applications.

## Features ✨

- **User Authentication** 🔐: Secure registration and login system using JWT.
- **Reservation Management** 🗂️: Endpoints to create, read, update, and delete reservations.
- **Availability Management** 📆: Real-time tracking of availability for rooms, tables, or event slots.
- **Notification System** ✉️: Automated email notifications for booking confirmations and reminders.
- **Reporting** 📊: Endpoints to generate detailed reports on reservations and user activity.
- **API Documentation** 📜: Comprehensive API documentation using Swagger.

## Technologies 🛠️

- **Backend Framework**: *FastAPI* for building a high-performance, asynchronous API.
- **Database**: *PostgreSQL* for reliable data storage.
- **Authentication**: *JWT (JSON Web Tokens)* for secure user authentication.
- **Deployment**: *Docker* for containerization and easy deployment.
- **CI/CD**: *GitHub Actions* for continuous integration and deployment.

## Getting Started 🚀

1. **Clone the repository:**
   ```sh
   git clone https://github.com/danieljoris/pybooking.git
   cd pybooking
   ```
2. **Set up the environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints 📍

- **Authentication** 🔐:
  - `POST /auth/register`: Register a new user.
  - `POST /auth/login`: Log in a user and receive a JWT.
- **Reservations** 🗂️:
  - `POST /reservations`: Create a new reservation.
  - `GET /reservations`: Retrieve all reservations.
  - `GET /reservations/{id}`: Retrieve a specific reservation by ID.
  - `PUT /reservations/{id}`: Update a specific reservation by ID.
  - `DELETE /reservations/{id}`: Delete a specific reservation by ID.
- **Availability** 📆:
  - `GET /availability`: Check availability for specific dates and times.
- **Notifications** ✉️:
  - `POST /notifications/send`: Send notifications for bookings.
- **Reports** 📊:
  - `GET /reports`: Generate reports on reservations and user activity.

## Contribution 🤝

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
