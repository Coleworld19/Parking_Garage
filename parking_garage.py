# Your parking gargage class should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount of time from the user and store it in a variable
# - Show them how much they have to pay
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class Parking_Garage():

    all_tickets = {
        # 1 : "Paid"
        # 2 : "Unpaid"
        # 2 : "Unpaid"
    }

    active_tickets = []
    available_tickets = 0

    def __init__(self, parking_spaces, cost_per_hour):
        self.parking_spaces = parking_spaces
        self.cost_per_hour = cost_per_hour

    def takeTicket(self): #Cole's Baby

        #Ask the user if they want to take a ticket

        #Make sure there's enough tickets to give them

        #"Give them a ticket" - decrease available tickets and available spaces by 1

        pass

    def payForParking(self): #David's Baby

        #Ask the user how much time they spent in the garage

        #Show them their total

        #Ask if they want to "pay"

        #Tell them "thank you for your payment"

        #Update the dictionary to paid status
        pass

    def leaveGarage(self): #Felix's Baby
        
        #Make sure their ticket is paid, if it is display "thank you, have a nice day"

        #If ticket is not paid, bring them back to payment

        #Update the parking spaces + 1

        #Update the available tickets + 1

        #Take their ticket out of the active_tickets list
        pass


def main():

    takeTicket()
    payForParking()
    leaveGarage()


garage = Parking_Garage(50, 10)
main()

