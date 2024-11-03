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

CREATE TABLE App_Users (
                          id_user SERIAL PRIMARY KEY,
                          login VARCHAR(255) NOT NULL UNIQUE,
                          password VARCHAR(255) NOT NULL CHECK (LENGTH(password) >= 8),
                          email VARCHAR(255) NOT NULL UNIQUE,
                          phone_number VARCHAR(20) NOT NULL,
                          name VARCHAR(255) NOT NULL,
                          surname VARCHAR(255) NOT NULL
);

CREATE TABLE Drivers_Licenses (
                                 id_license SERIAL PRIMARY KEY,
                                 issued_on TIMESTAMP NOT NULL,
                                 expires_on TIMESTAMP NOT NULL,
                                 CHECK (expires_on > issued_on)
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
                      longitude FLOAT NOT NULL CHECK (longitude BETWEEN -180 AND 180),
                      latitude FLOAT NOT NULL  CHECK (latitude BETWEEN -90 AND 90),
                      seating_available BOOLEAN NOT NULL,
                      shelter BOOLEAN NOT NULL
);

CREATE TABLE Paths (
                      id_path SERIAL PRIMARY KEY,
                      distance DECIMAL(10, 2) NOT NULL CHECK (distance > 0),
                      number_of_stops INT NOT NULL CHECK (number_of_stops > 2),
                      estimated_travel_time INT NOT NULL CHECK (estimated_travel_time > 0)
);

CREATE TABLE Lines (
                      id_line SERIAL PRIMARY KEY,
                      number VARCHAR(10) NOT NULL UNIQUE,
                      fk_main_path INT NOT NULL,
                      avg_frequency INT NOT NULL CHECK (avg_frequency > 0),
                      FOREIGN KEY (fk_main_path) REFERENCES Paths(id_path) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE Path_Stops (
                            id_path INT NOT NULL,
                            id_stop INT NOT NULL,
                            path_minute INT NOT NULL CHECK (path_minute > 0),
                            PRIMARY KEY (id_path, id_stop),
                            FOREIGN KEY (id_path) REFERENCES Paths(id_path) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (id_stop) REFERENCES Stops(id_stop) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Vehicles (
                         id_vehicle SERIAL PRIMARY KEY,
                         vehicle_number INT NOT NULL UNIQUE,
                         last_technical_inspection TIMESTAMP NOT NULL,
                         production_date TIMESTAMP NOT NULL,
                         capacity INT NOT NULL CHECK (capacity > 0),
                         type VARCHAR(50) NOT NULL,
                         status VARCHAR(50) NOT NULL,
                         air_conditioning BOOLEAN NOT NULL
);

CREATE TABLE Technical_Issues (
                                 id_technical_issue SERIAL PRIMARY KEY,
                                 description VARCHAR(255) NOT NULL,
                                 report_date TIMESTAMP NOT NULL,
                                 resolve_date TIMESTAMP,
                                 fk_driver INT NOT NULL,
                                 fk_vehicle INT NOT NULL,
                                 status VARCHAR(50) NOT NULL,
                                 repair_cost DECIMAL(10, 2) NOT NULL CHECK (repair_cost > 0),
                                 FOREIGN KEY (fk_driver) REFERENCES Drivers(id_driver) ON DELETE SET NULL ON UPDATE CASCADE,
                                 FOREIGN KEY (fk_vehicle) REFERENCES Vehicles(id_vehicle) ON DELETE CASCADE ON UPDATE CASCADE,
                                 CHECK (resolve_date >= report_date)
);

CREATE TABLE Rides (
                      id_ride SERIAL PRIMARY KEY,
                      fk_line INT NOT NULL,
                      fk_path INT NOT NULL,
                      fk_vehicle INT NOT NULL,
                      fk_driver INT NOT NULL,
                      weekday VARCHAR(50) NOT NULL,
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
                            date TIMESTAMP NOT NULL CHECK (date <= CURRENT_TIMESTAMP),
                            FOREIGN KEY (fk_ride) REFERENCES Rides(id_ride) ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (fk_inspector) REFERENCES Ticket_Inspectors(id_inspector) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Passengers (
                           id_passenger SERIAL PRIMARY KEY,
                           fk_user INT NOT NULL,
                           FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Ticket_Types (
                             id_ticket_type SERIAL PRIMARY KEY,
                             name VARCHAR(255) NOT NULL UNIQUE,
                             type VARCHAR(50) NOT NULL,
                             price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
                             validity_duration INT NOT NULL CHECK (validity_duration > 0),
                             is_discounted BOOLEAN NOT NULL
);

CREATE TABLE Purchases (
                          id_purchase SERIAL PRIMARY KEY,
                          date TIMESTAMP NOT NULL CHECK (date <= CURRENT_TIMESTAMP),
                          amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0)
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
                      amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
                      issue_date TIMESTAMP NOT NULL,
                      status VARCHAR(50) NOT NULL,
                      deadline TIMESTAMP NOT NULL CHECK (deadline > issue_date),
                      FOREIGN KEY (fk_passenger) REFERENCES Passengers(id_passenger) ON DELETE CASCADE ON UPDATE CASCADE,
                      FOREIGN KEY (fk_inspector) REFERENCES Ticket_Inspectors(id_inspector) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Editors (
                        id_editor SERIAL PRIMARY KEY,
                        fk_user INT NOT NULL,
                        FOREIGN KEY (fk_user) REFERENCES App_Users(id_user) ON DELETE CASCADE ON UPDATE CASCADE
);
