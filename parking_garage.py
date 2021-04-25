
class Parking_Garage():


    def __init__(self, parking_spaces, cost_per_hour):
        self.parking_spaces = parking_spaces
        self.cost_per_hour = cost_per_hour
        self.available_tickets = parking_spaces
        self.available_spaces = parking_spaces

    all_tickets = {}

    active_tickets = []


    def takeTicket(self): #Cole's Baby

        #Make sure there's enough tickets to give them
        if self.available_tickets >=1:
                    

            #"Give them a ticket" - decrease available tickets and available spaces by 1
            new_ticket_num = len(self.all_tickets.keys()) + 1
            self.all_tickets[new_ticket_num] = "Unpaid"
            self.active_tickets.append(new_ticket_num)
            self.available_tickets = self.available_tickets -1
            self.available_spaces = self.available_spaces -1
            print("Ticket printed")
            print(f"Your ticket number is: {new_ticket_num}")
            
        else:
            print("Not enough tickets")
            return
            

        return new_ticket_num


    def checkTicket(self): #David's Baby

        #set up a loop to validate ticket number
        while True:
            #Ask which ticket they're paying
            current_ticket = int(input("Please enter your ticket number: "))

            #check to see if the ticket is valid
            if current_ticket in self.active_tickets:
                if self.all_tickets[current_ticket] == "Paid":
                    print("Your ticket is paid")
                    return current_ticket
                else:
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
            elif current_ticket in self.all_tickets.keys():
                print(f"Your ticket is not active and is {self.all_tickets[current_ticket]}")
            else:
                print("Please enter a valid ticket number")
                break

        return current_ticket


    def payForParking(self): #David's Baby

        #Run the check ticket function to figure out how much they owe and bring it over here
        current_ticket = self.checkTicket()

        #check to see if the ticket they entered is valid
        if current_ticket not in self.active_tickets:
            return

        #Ask if they want to "pay"
        pay = input("Would you like to pay? y/n ").lower()

        #Tell them "thank you for your payment"
        if pay == "y" or pay == "yes":
            print("Processing your payment...")
            print("Success!")
            print("Thank you for your payment")
        
            #Update the dictionary to paid status
            self.all_tickets[current_ticket] = "Paid"

        return


    def leaveGarage(self): #Felix's Baby

        #check to see if they've even taken a ticket yet
        if len(self.active_tickets) == 0:
            print("You have not taken a ticket yet")
        else:
            #Make sure their ticket is paid, if it is display "thank you, have a nice day"
            current_ticket = int(input("Please enter your ticket number: "))
            if current_ticket not in self.active_tickets:
                print("This is not a valid ticket number")
                return

            if self.all_tickets[current_ticket] == "Paid":
                print("Thank you, have a nice day")
                #Update the parking spaces + 1
                self.available_spaces = self.available_spaces + 1

                #Update the available tickets + 1
                self.available_tickets = self.available_tickets + 1

                #Take their ticket out of the active_tickets list
                self.active_tickets.remove(current_ticket)

            else:
                #If ticket is not paid, bring them back to payment
                print("You have an unpaid balance. Please select the 'pay for parking' option and try again")
                

    

def main():

    while True:
        ask = input("What would you like to do? You can say 'take ticket', 'pay for parking', 'check my ticket', 'leave garage', or 'quit': ").lower()
        if ask == "quit":
            break
        if ask == "pay for parking":
            garage.payForParking()
        if ask == "check my ticket":
            garage.checkTicket()
        if ask == "take ticket":
            garage.takeTicket()
        if ask == "leave garage":
            garage.leaveGarage()

    

garage = Parking_Garage(50, 10)
main()
