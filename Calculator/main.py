from function import Function
function = Function()


def main():
	a = 0
	while(True):
		print("\n-:Welcome to the calculator:-")
		print("1. To Add.")
		print("2. To Subtract.")
		print("3. To Multiply.")
		print("4. To Divide.")
		print("5. To find Square.")
		print("6. To find Cube.")
		print("7. To find Square Root.")
		print("8. To find Cube Root.")
		print("9. To find Power.")
		print("10. To find Remainder.")
		print("11. To change Sign.")
		print("12. To find exponential of base 2.")
		print("13. To find Sin Function.")
		print("14. To find Cos Function.")
		print("15. To find Tan Function.")
		print("16. Equal to.")
		print("17. Zero.")
		print("18. Exit.")
		choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18): "))

		if(choice == 1):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number: "))
			a = function.add(a, n2)
			print("\n", a)

		elif(choice == 2):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number: "))
			a = function.subtract(a, n2)
			print("\n", a)

		elif(choice == 3):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number: "))
			a = function.multiply(a, n2)
			print("\n", a)

		elif(choice == 4):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number: "))
			a = function.divide(a, n2)
			print("\n", a)
		
		elif(choice == 5):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.square(a)
			print("\n", a)

		elif(choice == 6):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.cube(a)
			print("\n", a)

		elif(choice == 7):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.square_root(a)
			print("\n", a)

		elif(choice == 8):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.cube_root(a)
			print("\n", a)

		elif(choice == 9):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number to which power you want: "))
			a = function.power(a, n2)
			print("\n", a)

		elif(choice == 10):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			n2 = float(input("\nEnter number whose remainder you want: "))
			a = function.modulus(a, n2)
			print("\n", a)

		elif(choice == 11):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.plus_minus(a)
			print("\n", a)

		elif(choice == 12):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.exponent_2(a)
			print("\n", a)

		elif(choice == 13):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.sin_func(a)
			print("\n", a)

		elif(choice == 14):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.cos_func(a)
			print("\n", a)
		
		elif(choice == 15):
			if(a == 0):
				a = float(input("\nEnter number: "))
			else:
				a = a
			a = function.tan_func(a)
			print("\n", a)

		elif(choice == 16):
			print("\nTotal: ", a)

		elif(choice == 17):
			a = 0
			print("\n", a)

		elif(choice == 18):
			print("\nTotal: ", a)
			break

		else:
			print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    main()