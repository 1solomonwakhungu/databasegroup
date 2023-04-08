# Hospital Management System
This project is a Java-based database system for a hospital that helps manage patient information, medical records, appointments, billing, and inventory management.

## Requirements
- Java Development Kit (JDK) 8 or higher
- MySQL server
- MySQL Connector/Java

## Installation
- Clone the repository.
- Import the `database.sql` file into your MySQL server to create the required tables and data.
- Edit the `config.properties` file with your MySQL database connection details.
- Build the project with `mvn package` command.

## Usage
To start the system, run `java -jar target/hospital-management-system.jar`. This will start the command-line interface where you can perform the following operations:

- Register a new patient.
- View and update patient information.
- Add and view medical records for a patient.
- Schedule and view appointments.
- Generate billing statements for patients.
- Manage inventory items.
To exit the system, type `exit` or press `Ctrl+C`.
