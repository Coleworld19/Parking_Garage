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


    def __init__(self, parking_spaces, cost_per_hour):
        self.parking_spaces = parking_spaces
        self.cost_per_hour = cost_per_hour
        self.available_tickets = parking_spaces
        self.available_spaces = parking_spaces

    all_tickets = {}

    active_tickets = []


    def takeTicket(self): #Cole's Baby
        while True:
            #Ask the user if they want to take a ticket
            ask=input("Do you want a ticket?")
            if ask.lower()=="no":
                break
            elif ask.lower()=="yes":
            #Make sure there's enough tickets to give them
                if self.available_tickets >=1:
                    

                    #"Give them a ticket" - decrease available tickets and available spaces by 1
                    new_ticket_num = len(self.all_tickets.keys()) + 1
                    self.all_tickets[new_ticket_num] = "Unpaid"
                    self.active_tickets.append(new_ticket_num)
                    self.available_tickets = self.available_tickets -1
                    self.available_spaces = self.available_spaces -1 
                    break
                else:
                    print("Not enough Tickets")
                    break

        return new_ticket_num


    def checkTicket(self): #David's Baby

       #set up a loop to validate ticket number
        while True:

        #Ask which ticket they're paying
            current_ticket = int(input("Please enter your ticket number: "))

            #check to see if the ticket is valid, else ask for their ticket number again
            if current_ticket in self.active_tickets:
                break
            else:
                print("Please enter a valid ticket number")

        #Ask the user how much time they spent in the garage
        time = int(input("How many total minutes did you spend in the garage? "))
        total = (time / 60) * self.cost_per_hour

        #Show them their total
        total = round(total, 2)
        total = str(total)
        if total[-2:] == ".0":
            total = total + "0"
        print(f"Your total for {time} minutes is ${total}")

        return current_ticket


    def payForParking(self): #David's Baby

        #Run the check ticket function to figure out how much they owe and bring it over here
        current_ticket = self.checkTicket()

        #Ask if they want to "pay"
        pay = input("Would you like to pay? y/n ").lower()

        #Tell them "thank you for your payment"
        if pay == "y":
            print("Processing your payment...")
            print("Success!")
            print("Thank you for your payment")
        
        #Update the dictionary to paid status
            self.all_tickets[current_ticket] = "Paid"

        return current_ticket # can remove this once the take ticket function is returning the ticket number


    def leaveGarage(self, ticket): #Felix's Baby

        #check to see if they've even taken a ticket yet
        if ticket == 0:
            print("You have not taken a ticket yet")
        else:
            #Make sure their ticket is paid, if it is display "thank you, have a nice day"
            if self.all_tickets[ticket] == "Paid":
                print("Thank you, have a nice day")
                #Update the parking spaces + 1
                self.available_spaces = self.available_spaces + 1

                #Update the available tickets + 1
                self.available_tickets = self.available_tickets + 1

                #Take their ticket out of the active_tickets list
                self.active_tickets.remove(ticket)

            else:
                #If ticket is not paid, bring them back to payment
                print("You have an unpaid balance. Please select the 'pay for parking' option and try again")
                

    

def main():

    ticket = 0

    while True:
        ask = input("What would you like to do? You can say 'take ticket', 'pay for parking', 'check my ticket', 'leave garage', or 'quit': ").lower()
        if ask == "quit":
            break
        if ask == "pay for parking":
            garage.payForParking()
        if ask == "check my ticket":
            garage.checkTicket()
        if ask == "take ticket":
            ticket = garage.takeTicket()
        if ask == "leave garage":
            garage.leaveGarage(ticket)

        #TO DO
        #Assign ticket variable when it's taken, not when it's paid


garage = Parking_Garage(50, 10)
main()
