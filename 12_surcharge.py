import re
import pandas


# Function goes here
# WARNING: The response is returned in Title Case
def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name of the snack
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the response is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


# Main routine

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# loop until exit code...
name = ""
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    # Ask for payment method
    how_pay = string_check("Choose a payment method (cash / credit)", pay_method)

    # Ask for subtotal (for testing purposes)
    subtotal = float(input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | "
          "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))

# Calculate surcharge






