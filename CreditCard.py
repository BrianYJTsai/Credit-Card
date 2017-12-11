#  File: CreditCard.py

#  Description: Program determines whether a credit card number is valid or not. User inputs a credit card and 
#  output is whether the credit card is valid and if it is, what type of card it is.

#  Student Name: Brian Tsai

#  Student UT EID: byt76	

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4/7/17

#  Date Last Modified: 4/7/17

# This function checks if a credit card number is valid
def is_valid (cc_num):
	
	# The length of the card number
	card_length = len(str(cc_num))

	#Check if the card number length is of length 15 or 16 
	if (card_length == 15 or card_length ==16):
		return True
	# Else return False
	else:
		return False		

# This function returns the type of credit card
def cc_type (cc_num):
	card_number = str(cc_num)
	card_type = ""

	# Comparisons determine what type of card is passed based on the first few numbers
	if (card_number[0:2] == "34" or card_number[0:2] == "37"):
		card_type = "American Express"
	elif (card_number[0:4] == "6011" or card_number[0:3] == "644" or card_number[0:2] == "65"):	
		card_type = "Discover"
	elif (card_number[0:2] >= "50" and card_number[0:2] <= "55"):
		card_type = "MasterCard"
	elif (card_number[0:1]  == "4"):
		card_type = "Visa"
	else:
		card_type = ""
	return card_type				

# Used to determine the luhn sum of a 16 number length card
def luhn16(num):
	# Return 0 when the card length is zero
	if (num == 0):
		return 0	
	else:
		# If the length is even then add the value of the last digit to the sum
		if (len(str(num)) % 2 == 0):
			return (num % 10) + luhn16(num // 10)
		# Else, add sum of the digits of twice the last digit
		else:
			return ((2 * (num % 10)) // 10) + ((2 * (num % 10)) % 10) + luhn16(num // 10)

# Used to determine the luhn sum of a 15 number length card
def luhn15(num):
	# Return 0 when the card length is zero
	if (num == 0):
		return 0	
	else:
		# If the length is odd then add the value of the last digit to the sum
		if (len(str(num)) % 2 == 1):
			return (num % 10) + luhn15(num // 10)
		# Else, add sum of the digits of twice the last digit
		else:
			return ((2 * (num % 10)) // 10) + ((2 * (num % 10)) % 10) + luhn15(num // 10)



def main():
	# Input the card number
	credit_card = int(input("Enter 15 or 16-digit credit card number: "))
	
	# Output if the card number is not the correct length 
	if (not is_valid(credit_card)):
		print("Not a 15 or 16-digit number")
		return


	# Calculate the luhn sum for a 15 number long card
	if (len(str(credit_card)) % 2 == 1):
		luhn_test = luhn15(credit_card)

		# Output if the luhn test fails
		if (luhn_test % 10 != 0):
			print("Invalid credit card number")

		# Output if the luhn test passes	
		else:
			card_type = cc_type(credit_card) 
			
			# Identify the card type if it is valid
			if (len(card_type)!= 0):
				print("Valid", card_type, "credit card number")
			else:
				print("Valid credit card number")	
	
	# Calculate the luhn sum for a 16 number long card				 
	else:	
		luhn_test = luhn16(credit_card)
		# Output if the luhn test fails
		if (luhn_test % 10 != 0):
			print("Invalid credit card number") 
		
		# Output if the luhn test passes
		else:
			card_type = cc_type(credit_card) 
			
			# Identify the card type if it is valid
			if (len(card_type)!= 0):
				print("Valid", card_type, "credit card number")
			else:
				print("Valid credit card number") 
main()