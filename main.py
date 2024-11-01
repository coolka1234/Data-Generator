import sys
# from numbers_info import *
from app_user import generate_users
from drivers_licenses import generate_dl
from driver import generate_drivers
from editors import generate_editors
from passengers import generate_passengers
from purchases import generate_purchases
from stops import generate_stops
from ticket_inspectors import generate_ticket_inspectors
from ticket_types import load_ticket_types
from tickets import generate_tickets
from vehicles import generate_vehicles
from fines import generate_fines
from rides import generate_ride
from paths import generate_paths
from lines import generate_line
from path_stops import generate_path_stops
from inspections import generate_inspections
from technical_issue import generate_ti
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

def main():
    load_ticket_types()
    print('How many users do you want to generate?')
    while True:
        try:
            users = int(input())
            generate_users(users)
            num_of_app_users = users
            break
        except IndexError or ValueError:
            print('You must provide a number of users to generate')
            # sys.exit(1)
    while True:
        print('How many drivers licenses do you want to generate?')
        try:
            dl = int(input())
            generate_dl(dl)
            num_of_licenses = dl
            break
        except IndexError or ValueError:
            print('You must provide a number of drivers licenses to generate')
            # sys.exit(1)
    while True:
        print('How many drivers do you want to generate?')
        try:
            drivers = int(input())
            generate_drivers(drivers,num_of_users=num_of_app_users, num_of_licenses=num_of_licenses)
            num_of_drivers = drivers
            break
        except IndexError or ValueError:
            print('You must provide a number of drivers to generate')
            # sys.exit(1)
    while True:
        print('How many editors do you want to generate?')
        try:
            editors = int(input())
            generate_editors(editors, num_of_app_users)
            num_of_editors = editors
            break
        except IndexError or ValueError:
            print('You must provide a number of editors to generate')
            # sys.exit(1)
    while True:
        print('How many passengers do you want to generate?')
        try:
            passengers = int(input())
            generate_passengers(passengers, num_of_app_users)
            num_of_passengers = passengers
            break
        except IndexError or ValueError:
            print('You must provide a number of passengers to generate')
            # sys.exit(1)
    while True:
        print('How many purchases do you want to generate?')
        try:
            purchases = int(input())
            generate_purchases(purchases)
            num_of_purchases = purchases
            break
        except IndexError or ValueError:
            print('You must provide a number of purchases to generate')
            # sys.exit(1)
    while True:
        print('How many stops do you want to generate?')
        try:
            stops = int(input())
            num_of_stops = stops
            generate_stops(stops)
            break
        except IndexError or ValueError:
            print('You must provide a number of stops to generate')
            # sys.exit(1)
    while True:
        print('How many ticket inspectors do you want to generate?')
        try:
            ticket_inspectors = int(input())
            generate_ticket_inspectors(ticket_inspectors, num_of_app_users)
            num_of_ticket_inspectors = ticket_inspectors
            break
        except IndexError or ValueError:
            print('You must provide a number of ticket inspectors to generate')
            # sys.exit(1)
    while True:
        print('How many tickets do you want to generate?')
        try:
            tickets = int(input())
            generate_tickets(tickets, num_of_passengers=num_of_passengers, num_of_purchases=num_of_purchases, num_of_ticket_types=num_of_ticket_types)
            num_of_tickets = tickets
            break
        except IndexError or ValueError:
            print('You must provide a number of tickets to generate')
            # sys.exit(1)
    while True:
        print('How many vehicles do you want to generate?')
        try:
            vehicles = int(input())
            generate_vehicles(vehicles)
            num_of_vehicles = vehicles
            break
        except IndexError or ValueError:
            print('You must provide a number of vehicles to generate')
            # sys.exit(1)
    while True:
        print('How many fines do you want to generate?')
        try:
            fines = int(input())
            generate_fines(fines, num_of_passengers=num_of_passengers, num_of_ticket_inspectors=num_of_ticket_inspectors)
            num_of_fines = fines
            break
        except IndexError or ValueError:
            print('You must provide a number of fines to generate')
            # sys.exit(1)
    while True:
        print('How many paths do you want to generate?')
        try:
            paths = int(input())
            generate_paths(paths)
            num_of_paths = paths
            break
        except IndexError or ValueError:
            print('You must provide a number of paths to generate')
            # sys.exit(1)
    while True:
        print('How many lines do you want to generate?')
        try:
            lines = int(input())
            generate_line(lines, num_of_paths=num_of_paths)
            num_of_lines = lines
            break
        except IndexError or ValueError:
            print('You must provide a number of lines to generate')
            # sys.exit(1)
    while True:
        print('How many rides do you want to generate?')
        try:
            rides = int(input())
            generate_ride(rides, num_of_drivers=num_of_drivers, num_of_lines=num_of_lines, num_of_paths=num_of_paths, num_of_vehicles=num_of_vehicles)
            num_of_rides = rides
            break
        except IndexError or ValueError:
            print('You must provide a number of rides to generate')
            # sys.exit(1)
    while True:
        print('How many path stops do you want to generate?')
        try:
            path_stops = int(input())
            generate_path_stops(path_stops, num_of_paths=num_of_paths, num_of_lines=num_of_lines)
            num_of_path_stops = path_stops
            break
        except IndexError or ValueError:
            print('You must provide a number of path stops to generate')
            # sys.exit(1)
    while True:
        print('How many inspections do you want to generate?')
        try:
            inspections = int(input())
            generate_inspections(inspections, num_of_rides=num_of_rides, num_of_ticket_inspectors=num_of_ticket_inspectors)
            num_of_inspections = inspections
            break
        except IndexError or ValueError:
            print('You must provide a number of inspections to generate')
            # sys.exit(1)
    while True:
        print('How many technical issues do you want to generate?')
        try:
            ti = int(input())
            generate_ti(ti, num_of_drivers=num_of_drivers, num_of_vehicles=num_of_vehicles)
            num_of_ti = ti
            break
        except IndexError or ValueError:
            print('You must provide a number of technical issues to generate')
            # sys.exit(1)
    # json_nums()

if __name__ == '__main__':
    main()
    

