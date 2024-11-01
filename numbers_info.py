import json


num_of_app_users = 0
num_of_drivers = 0
num_of_licenses=0
num_of_editors=0
num_of_fines=0
num_of_inspections=0
num_of_lines=0
num_of_path_stops=0
num_of_paths=0
num_of_purchases=0
num_of_rides=0
num_of_stops=0
num_of_technical_issues=0
num_of_ticket_inspectors=0
num_of_tickets=0
num_of_vehicles=0
num_of_passengers=0
num_of_ticket_types=0


def json_nums():
    with open('numbers.json', 'w') as file:
        json.dump({'app_users': num_of_app_users, 'passengers': num_of_passengers,'drivers': num_of_drivers, 'licenses': num_of_licenses, 'editors': num_of_editors, 'fines': num_of_fines, 'inspections': num_of_inspections, 'lines': num_of_lines, 'path_stops': num_of_path_stops, 'paths': num_of_paths, 'purchases': num_of_purchases, 'rides': num_of_rides, 'stops': num_of_stops, 'technical_issues': num_of_technical_issues, 'ticket_inspectors': num_of_ticket_inspectors, 'tickets': num_of_tickets, 'vehicles': num_of_vehicles, 'ticket_types': num_of_ticket_types}, file)

def load_nums():
    with open('numbers.json', 'r') as file:
        data=json.load(file)
        global num_of_app_users
        global num_of_drivers
        global num_of_licenses
        global num_of_editors
        global num_of_fines
        global num_of_inspections
        global num_of_lines
        global num_of_path_stops
        global num_of_paths
        global num_of_purchases
        global num_of_rides
        global num_of_stops
        global num_of_technical_issues
        global num_of_ticket_inspectors
        global num_of_tickets
        global num_of_vehicles
        global num_of_ticket_types
        global num_of_passengers
        num_of_app_users=data['app_users']
        num_of_drivers=data['drivers']
        num_of_licenses=data['licenses']
        num_of_editors=data['editors']
        num_of_fines=data['fines']
        num_of_inspections=data['inspections']
        num_of_lines=data['lines']
        num_of_path_stops=data['path_stops']
        num_of_paths=data['paths']
        num_of_purchases=data['purchases']
        num_of_rides=data['rides']
        num_of_stops=data['stops']
        num_of_technical_issues=data['technical_issues']
        num_of_ticket_inspectors=data['ticket_inspectors']
        num_of_tickets=data['tickets']
        num_of_vehicles=data['vehicles']
        num_of_ticket_types=data['ticket_types']
        num_of_passengers=data['passengers']