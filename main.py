import sys
from app_user import generate_users
from drivers_licenses import generate_dl
from driver import generate_drivers
from editors import generate_editors
from passengers import generate_passengers
from purchases import generate_purchases
from stops import generate_stops
from ticket_inspectors import generate_ticket_inspectors
from tickets import generate_tickets
def main():
    print('How many users do you want to generate?')
    while True:
        try:
            users = int(sys.argv[1])
            generate_users(users)
            break
        except IndexError or ValueError:
            print('You must provide a number of users to generate')
            sys.exit(1)
    while True:
        print('How many drivers do you want to generate?')
        try:
            dl = int(sys.argv[2])
            generate_dl(dl)
            break
        except IndexError or ValueError:
            print('You must provide a number of drivers to generate')
            sys.exit(1)
    while True:
        print('How many drivers do you want to generate?')
        try:
            drivers = int(sys.argv[3])
            generate_drivers(drivers)
            break
        except IndexError or ValueError:
            print('You must provide a number of drivers to generate')
            sys.exit(1)
    while True:
        print('How many editors do you want to generate?')
        try:
            editors = int(sys.argv[4])
            generate_editors(editors)
            break
        except IndexError or ValueError:
            print('You must provide a number of editors to generate')
            sys.exit(1)
    while True:
        print('How many passengers do you want to generate?')
        try:
            passengers = int(sys.argv[5])
            generate_passengers(passengers)
            break
        except IndexError or ValueError:
            print('You must provide a number of passengers to generate')
            sys.exit(1)
    while True:
        print('How many purchases do you want to generate?')
        try:
            purchases = int(sys.argv[6])
            generate_purchases(purchases)
            break
        except IndexError or ValueError:
            print('You must provide a number of purchases to generate')
            sys.exit(1)
    while True:
        print('How many stops do you want to generate?')
        try:
            stops = int(sys.argv[7])
            generate_stops(stops)
            break
        except IndexError or ValueError:
            print('You must provide a number of stops to generate')
            sys.exit(1)
    while True:
        print('How many ticket inspectors do you want to generate?')
        try:
            ticket_inspectors = int(sys.argv[8])
            generate_ticket_inspectors(ticket_inspectors)
            break
        except IndexError or ValueError:
            print('You must provide a number of ticket inspectors to generate')
            sys.exit(1)


