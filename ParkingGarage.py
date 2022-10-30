class ParkingGarage():
    """
        Your parking garage class should have the following methods:
        - takeTicket
            - This should decrease the amount of tickets available by 1
            - This should decrease the amount of parkingSpaces available by 1
        - payForParking
            - Display an input that waits for an amount from the user and store it in a variable
            - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
            - This should update the "currentTicket" dictionary key "paid" to True
        -leaveGarage
            - If the ticket has been paid, display a message of "Thank You, have a nice day"
            - If the ticket has not been paid, display an input prompt for payment
            - Once paid, display message "Thank you, have a nice day!"
            - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
            - Update tickets list to increase by 1 (meaning add to the tickets list)

        You will need a few attributes as well:
        - tickets -> list
        - parkingSpaces -> list
        - currentTicket -> dictionary
    """

    tickets = [i for i in range(20)]
    parkingSpaces = [i for i in range(20)]
    currentTicket = {'paid': False}

    def takeTicket(self):
            self.tickets.pop()
            self.parkingSpaces.pop()

    def payForParking(self):
        paid = input("Have you paid for your parking? (be honest!) ")
        if paid != '':
            print("Excellent! Your ticket has been paid, you have 15 minutes to leave the parking garage.")
            self.currentTicket['paid'] = True

    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print("Thank You, have a nice day")
        else:
            paid = input("Please pay your ticket! ")
            print("Thank you, have a nice day!")
        self.parkingSpaces.append(len(self.parkingSpaces)+1)
        self.tickets.append(len(self.parkingSpaces)+1)
