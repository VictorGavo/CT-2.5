from ParkingGarage import ParkingGarage
from IPython.display import clear_output

print("Welcome to Victor's Vehicular Vault! Please take a ticket before parking your car!")
vvv = ParkingGarage()
while True:
    # print(f"There are {len(vvv.parkingSpaces)} spots left and {len(vvv.tickets)} tickets available\n")
    if len(vvv.tickets) == 20:
        print("[T] Take a ticket")
    elif vvv.currentTicket['paid'] == False:
        print("[P] Pay for your ticket\n"
              "[L] Leave the garage")
    else:
        print("[L] Leave the garage")
    
    response = input("What would you like to do? ")
    clear_output()
    if response.lower() == 't':
        if len(vvv.tickets) < 20:
            print("You already have a ticket")
        else:
            vvv.takeTicket()
            print("Thank you for choosing Victor's Vehicular Vault! Please keep your ticket with you at all times!")
        # print(f"There are {len(vvv.parkingSpaces)} spots left and {len(vvv.tickets)} tickets available\n")
    elif response.lower() == 'p':
        if len(vvv.tickets) == 20:
            print("You need a ticket first!")
        elif vvv.currentTicket['paid'] == True:
            print("You've already paid for your ticket!")
        else:
            vvv.payForParking()
            # print(f"There are {len(vvv.parkingSpaces)} spots left and {len(vvv.tickets)} tickets available\n")

    elif response.lower() == 'l':
        if len(vvv.tickets) == 20:
            print("You need a ticket first!")
        else:
            vvv.leaveGarage()
            # print(f"There are {len(vvv.parkingSpaces)} spots left and {len(vvv.tickets)} tickets available\n")
            break