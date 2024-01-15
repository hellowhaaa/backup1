


TICKET_PRICE = 10
tickets_remaining = 100
# How many ticket are remaining

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}?".format(name))
    #  Expect ValueError to happen and handle it!
    try:
        num_tickets = int(num_tickets)
        # Raise the ValueError! 若張數不夠
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("error, we ran to the issue. {} Please try again".format(err))
    else:

        amount_due = num_tickets * TICKET_PRICE
        print("The total due is ${}".format(amount_due))

        should_proceed = input("Do you want to proceed? Y/N ")
        if should_proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you".format(name))
print("sorry ~ no ticket!")




# prompt the user by name and ask how many tickets they would like



# Output the price


# Prompt user if they want to proceed Y/N?
