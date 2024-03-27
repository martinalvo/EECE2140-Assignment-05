#Program for basic math operations

#Creatin class with the operations
class BasicMathOperations:

    #Initial method to greet the user given a first and last name
    def greetUser(fname, lname):
        print("Hello ", fname, " ", lname, ", how are you?", sep="")

    #A method to add two numbers together. The number are inputed by the user in the method
    def addNumbers():
        n1 = float(input("Enter a first number: "))
        n2 = float(input("Enter a second number: "))
        sum = n1 + n2

        return sum

    #A method that performs either + - * or / on two numbers. The numbers and the operation are passed as arguments
    def performOperation(num1, num2, op):

        #Conditional to check what the operation inputed was
        if op == "+":
            return num1+num2
        elif op == "-":
            return num1-num2
        elif op == "*":
            return num1*num2
        elif op == "/":
            return num1/num2
        #If an invalid operation is entered, let the user know
        else:
            print("That is not a valid operation")

    #A method two square a number entered into it
    def squareNumber(n1):
        sqr = n1**2
        return sqr

    #A method to find the factorial of a number
    def factorial(n1):
        #initializing the factorial to the number
        fact = n1
        #Then for a range from 2 to the number, multiply fact times the iterator
        for i in range(2, n1):
            fact *= i

        #Return the factorial
        return fact

    #A method to count numbers from an entered start and end range
    def counting(start, end):
        #If the start is greater than the end, then output nothing
        if start > end:
            return
        #For the range from start to end, output the iterator. Make the end of each print statement an emtpy
        #string to have them all print in one line
        for i in range(start, end):
            print(i, ", ", sep="", end="")
            #print the last element seperately to have a new line and shorten loop
        print(end)

    #CalculateSquare is the same as the method from before

    #Method to calculate the hypotenuse of a right triangle triangle with two sides entered
    def calculateHypotenuse(l1, l2):
        #Using pythagorean theorem and squareNumber method to find hypotenuse
        hyp = (BasicMathOperations.squareNumber(l1) + BasicMathOperations.squareNumber(l2))**.5

        return hyp

    #Method for finding the area of a rectangle given a width and a height. Just multiplying them
    def areaOfSquare(w, h):
        area = w*h
        return area

    #Method for finding a number to the power of another number. Just a**b
    def powerOfNumber(base, exp):
        pow = base**exp
        return pow

    #Method for finding the type of a passed in argument. Just using type()
    def typeOfArgument(arg):

        return type(arg)

#Main function
def main(): 

    #Creating instance of the Basic operations class
    mathOps = BasicMathOperations
    #Printing the available tasks for the user to perform
    print("""The list of available Tasks: 
          1. Greet the user
          2. Add Number
          3. Perform Operation
          4. Square Number
          5. Factorial of Number
          6. Count between range
          7. Calculate Hypotenuse of right triangle
          8. Calculate Area of Square
          9. Calculate a^b
          10. Output type of an argument
          11. End program""")
    #While loop that runs indefinetly until the user stops the program in order to ask for multiple tasks
    run = True
    while run:

        #Asking for user input of task number
        userInput = input("Select the number of the task you want to perform: ")
        #A try except that makes sure that the user has inputed valid inputs for any of the numbers asked for in each task.
        #If they dont input something valid, the except at the end of this lets them know, and the program dosent crash
        try:
            #A conditional to check what task the user wants to perform. The necessary inputs from the user are asked
            #In each specific conditional. Also, any values inputs that need to be turned into integers or floats are done so
            if userInput == "1":
                first = input("Enter your first name: ")
                last = input("Enter your last name: ")
                print("=============================")
                mathOps.greetUser(first, last)
            elif userInput == "2":
                print(mathOps.addNumbers())
            elif userInput == "3":
                n1 = float(input("Enter a first number: "))
                n2 = float(input("Enter a second number: "))
                op = input("Enter the operation: ")
                print("=============================")
                print(mathOps.performOperation(n1, n2, op))
            elif userInput == "4":
                n1 = float(input("Enter a number: "))
                print("=============================")
                print(mathOps.squareNumber(n1))
            elif userInput == "5":
                n1 = int(input("Enter a number: "))
                print("=============================")
                print(mathOps.factorial(n1))
            elif userInput == "6":
                n1 = int(input("Enter a start number: "))
                n2 = int(input("Enter an end number: "))
                print("=============================")
                mathOps.counting(n1, n2)
            elif userInput == "7":
                l1 = float(input("Enter side 1 lenght: "))
                l2 = float(input("Enter side 2 length: "))
                print("=============================")
                print(mathOps.calculateHypotenuse(l1, l2))
            elif userInput == "8":
                w = float(input("Enter width lenght: "))
                h = float(input("Enter height length: "))
                print("=============================")
                print(mathOps.areaOfSquare(w, h))
            elif userInput == "9":
                b = float(input("Enter base number: "))
                e = float(input("Enter exponent: "))
                print("=============================")
                print(mathOps.powerOfNumber(b, e))
            elif userInput == "10":
                ar1 = input("Enter argument: ")
                print("=============================")
                print(mathOps.typeOfArgument(ar1))
            elif userInput == "11":
                run =  False
            #If the user does not enter a valid task number, let them know
            else:
                print("That is not a valid input")
        #Except that lets user know if their input for any number was invalid
        except:
            print("Operation could not be perfomed (Invalid input)")

#Running main
main()