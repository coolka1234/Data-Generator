DROP TABLE IF EXISTS Fines CASCADE;
DROP TABLE IF EXISTS Tickets CASCADE;
DROP TABLE IF EXISTS Purchases CASCADE;
DROP TABLE IF EXISTS Ticket_Types CASCADE;
DROP TABLE IF EXISTS Passengers CASCADE;
DROP TABLE IF EXISTS Inspections CASCADE;
DROP TABLE IF EXISTS Ticket_Inspectors CASCADE;
DROP TABLE IF EXISTS Rides CASCADE;
DROP TABLE IF EXISTS Drivers CASCADE;
DROP TABLE IF EXISTS Drivers_Licenses CASCADE;
DROP TABLE IF EXISTS Technical_Issues CASCADE;
DROP TABLE IF EXISTS Vehicles CASCADE;
DROP TABLE IF EXISTS Path_Stops CASCADE;
DROP TABLE IF EXISTS Stops CASCADE;
DROP TABLE IF EXISTS Lines CASCADE;
DROP TABLE IF EXISTS Paths CASCADE;
DROP TABLE IF EXISTS Editors CASCADE;
DROP TABLE IF EXISTS App_Users CASCADE;
DROP TYPE IF EXISTS weekday_enum CASCADE;
DROP TYPE IF EXISTS vehicle_status CASCADE;
DROP TYPE IF EXISTS vehicle_type CASCADE;
DROP TYPE IF EXISTS ticket_discount_type CASCADE;
DROP TYPE IF EXISTS techincal_issue_status CASCADE;
DROP TYPE IF EXISTS fine_status CASCADE;

CREATE TYPE weekday_enum AS ENUM ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');
CREATE TYPE vehicle_type AS ENUM ('Bus','Tram');
CREATE TYPE vehicle_status AS ENUM ('Active','Inactive');
CREATE TYPE ticket_discount_type AS ENUM ('Normal','Discounted');
CREATE TYPE techincal_issue_status AS ENUM ('Reported','Resolved','InProgress');
CREATE TYPE fine_status AS ENUM ('Paid','Unpaid');

CREATE TABLE App_Users (
                        id_user SERIAL PRIMARY KEY,
                        login VARCHAR(255) NOT NULL UNIQUE,
                        password VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL UNIQUE,
                        phone_number VARCHAR(20) NOT NULL, 
                        name VARCHAR(255) NOT NULL,
                        surname VARCHAR(255) NOT NULL,

                        CONSTRAINT valid_email CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$')
);

CREATE TABLE Drivers_Licenses (
                                id_license SERIAL PRIMARY KEY,
                                issued_on TIMESTAMP NOT NULL,
                                expires_on TIMESTAMP NOT NULL,
                                
                                CONSTRAINT valid_dates CHECK (expires_on > issued_on)
);

CREATE TABLE Drivers (
                    id_driver SERIAL PRIMARY KEY,
                    fk_license INT NOT NULL,
                    fk_user INT NOT NULL,
                    FOREIGN KEY (fk_license) REFERENCES Drivers_Licenses(id_license) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Stops (
                    id_stop SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL UNIQUE,
                    type VARCHAR(50) NOT NULL,
                    longitude FLOAT NOT NULL,
                    latitude FLOAT NOT NULL,
                    seating_available BOOLEAN NOT NULL,
                    shelter BOOLEAN NOT NULL,

                    CONSTRAINT valid_longitude CHECK (longitude BETWEEN -180 AND 180),
                    CONSTRAINT valid_latitude CHECK (latitude BETWEEN -90 AND 90)
);

CREATE TABLE Paths (
                    id_path SERIAL PRIMARY KEY,
                    distance DECIMAL(10, 2) NOT NULL,
                    number_of_stops INT NOT NULL,
                    estimated_travel_time INT NOT NULL,

                    CONSTRAINT valid_distance CHECK (distance > 0),
                    CONSTRAINT valid_number_of_stops CHECK (number_of_stops > 2),
                    CONSTRAINT valid_estimated_travel_time CHECK (estimated_travel_time > 0)
);

CREATE TABLE Lines (
                    id_line SERIAL PRIMARY KEY,
                    number VARCHAR(10) NOT NULL UNIQUE,
                    fk_main_path INT NOT NULL,
                    avg_frequency INT NOT NULL,
                    FOREIGN KEY (fk_main_path) REFERENCES Paths(id_path) ON DELETE SET NULL ON UPDATE CASCADE,

                    CONSTRAINT valid_frequency CHECK (avg_frequency > 0)
);

CREATE TABLE Path_Stops (
                        id_path INT NOT NULL,
                        id_stop INT NOT NULL,
                        path_minute INT NOT NULL,
                        PRIMARY KEY (id_path, id_stop),
                        FOREIGN KEY (id_path) REFERENCES Paths(id_path) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (id_stop) REFERENCES Stops(id_stop) ON DELETE CASCADE ON UPDATE CASCADE,

                        CONSTRAINT valid_path_minute CHECK (path_minute > 0)
);

CREATE TABLE Vehicles (
                        id_vehicle SERIAL PRIMARY KEY,
                        vehicle_number INT NOT NULL UNIQUE,
                        last_technical_inspection TIMESTAMP NOT NULL,
                        production_date TIMESTAMP NOT NULL,
                        capacity INT NOT NULL,
                        type vehicle_type NOT NULL,
                        status vehicle_status NOT NULL,
                        air_conditioning BOOLEAN NOT NULL,

                        CONSTRAINT valid_capacity CHECK (capacity > 0)
);

CREATE TABLE Technical_Issues (
                                id_technical_issue SERIAL PRIMARY KEY,
                                description VARCHAR(255) NOT NULL,
                                report_date TIMESTAMP NOT NULL,
                                resolve_date TIMESTAMP,
                                fk_driver INT NOT NULL,
                                fk_vehicle INT NOT NULL,
                                status techincal_issue_status NOT NULL,
                                repair_cost DECIMAL(10, 2) NOT NULL,
                                FOREIGN KEY (fk_driver) REFERENCES Drivers(id_driver) ON DELETE SET NULL ON UPDATE CASCADE,
                                FOREIGN KEY (fk_vehicle) REFERENCES Vehicles(id_vehicle) ON DELETE CASCADE ON UPDATE CASCADE,

                                CONSTRAINT valid_repair_cost CHECK (repair_cost > 0),
                                CONSTRAINT valdid_dates CHECK (resolve_date >= report_date)
);

CREATE TABLE Rides (
                    id_ride SERIAL PRIMARY KEY,
                    fk_line INT NOT NULL,
                    fk_path INT NOT NULL,
                    fk_vehicle INT NOT NULL,
                    fk_driver INT NOT NULL,
                    weekday weekday_enum NOT NULL,
                    start_time TIMESTAMP NOT NULL,
                    FOREIGN KEY (fk_line) REFERENCES Lines(id_line) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (fk_path) REFERENCES Paths(id_path) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (fk_vehicle) REFERENCES Vehicles(id_vehicle) ON DELETE SET NULL ON UPDATE CASCADE,
                    FOREIGN KEY (fk_driver) REFERENCES Drivers(id_driver) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Ticket_Inspectors (
                                id_inspector SERIAL PRIMARY KEY,
                                fk_user INT NOT NULL,
                                FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Inspections (
                        id_inspection SERIAL PRIMARY KEY,
                        fk_ride INT NOT NULL,
                        fk_inspector INT NOT NULL,
                        date TIMESTAMP NOT NULL,
                        FOREIGN KEY (fk_ride) REFERENCES Rides(id_ride) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (fk_inspector) REFERENCES Ticket_Inspectors(id_inspector) ON DELETE CASCADE ON UPDATE CASCADE,

                        CONSTRAINT valid_date CHECK (date <= CURRENT_TIMESTAMP)
);

CREATE TABLE Passengers (
                           id_passenger SERIAL PRIMARY KEY,
                           fk_user INT NOT NULL,
                           FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ticket_Types (
                            id_ticket_type SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL UNIQUE,
                            type ticket_discount_type NOT NULL,
                            price DECIMAL(10, 2) NOT NULL,
                            validity_duration INT NOT NULL,
                            is_discounted BOOLEAN NOT NULL,

                            CONSTRAINT valid_price CHECK (price > 0),
                            CONSTRAINT valid_validity_duration CHECK (validity_duration > 0)
);

CREATE TABLE Purchases (
                          id_purchase SERIAL PRIMARY KEY,
                          date TIMESTAMP NOT NULL,
                          amount DECIMAL(10, 2) NOT NULL,

                          CONSTRAINT valid_amount CHECK (amount > 0),
                          CONSTRAINT valid_date CHECK (date <= CURRENT_TIMESTAMP)
);



CREATE TABLE Tickets (
                        id_ticket SERIAL PRIMARY KEY,
                        fk_passenger INT NOT NULL,
                        fk_purchase INT NOT NULL,
                        fk_ticket_type INT NOT NULL,
                        FOREIGN KEY (fk_passenger) REFERENCES Passengers(id_passenger) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (fk_purchase) REFERENCES Purchases(id_purchase) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (fk_ticket_type) REFERENCES Ticket_Types(id_ticket_type) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Fines (
                    id_fine SERIAL PRIMARY KEY,
                    fk_passenger INT NOT NULL,
                    fk_inspector INT NOT NULL,
                    amount DECIMAL(10, 2) NOT NULL,
                    issue_date TIMESTAMP NOT NULL,
                    status fine_status NOT NULL,
                    deadline TIMESTAMP NOT NULL,
                    FOREIGN KEY (fk_passenger) REFERENCES Passengers(id_passenger) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (fk_inspector) REFERENCES Ticket_Inspectors(id_inspector) ON DELETE CASCADE ON UPDATE CASCADE,

                    CONSTRAINT valid_deadline CHECK (deadline > issue_date),
                    CONSTRAINT valid_amount CHECK (amount > 0)
);

CREATE TABLE Editors (
                        id_editor SERIAL PRIMARY KEY,
                        fk_user INT NOT NULL,
                        FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

