# Print "Let's calculate your tip".
# Ask for the user amount of the bill.
# Ask for the user for the tip amount. Give them three options to choose from.
# Calculate the total bill including tip
# Ask how many people are going to split the bill.
# Calculate how much each person should pay.

print("Let's calculate your tip!")

bill = float( input("How much was the bill? $"))

tip_percentage = int( input("What percentage tip do you want to leave? 15, 18, 20? "))

total_bill_with_tip = tip_percentage / 100 * bill + bill

final_amount_with_two_decimal_places =  round(total_bill_with_tip, 2)

print(f"The total bill is ${final_amount_with_two_decimal_places}.")

num_of_people_splitting_check = int( input("How many people are splitting the check? "))

each_person_will_pay = round(final_amount_with_two_decimal_places / num_of_people_splitting_check, 2)

print(f"Each person will pay ${each_person_will_pay}")



