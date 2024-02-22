# Example to do together: String Slicing, uncomment lines 3 - 5 to debug

a_long_string = "This is a very long string"
last_letter_sliced = a_long_string[-1] 
print(f"The last letter sliced from the sentence {a_long_string} is {last_letter_sliced.upper()}") 

# Problem 1: Mathematical Operations, uncomment lines 9 - 14 to debug

gift_card_balance = 45
price_of_entree = 20
price_of_drink = 7.50
gift_card_balance -= price_of_entree
gift_card_balance -= price_of_drink
print(f"The remaining balance for the gift card is: ${gift_card_balance}")

# Problem 2: Use string interpolation to print a sentence, uncomment lines 19 and 22 to debug

# store the name of a pet in a variable
pet_name = "Felix"

# Fix the line of code below so that the program prints: "FELIX is the best!"
print(f"{pet_name.capitalize()} is the best!")