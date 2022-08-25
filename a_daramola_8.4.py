#Akinola Daramola Jr
#Programming Exercise
#Due Date: 08/03/2022


"""
Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers.
The program should store the numbers in a list then display the following data:
The lowest number in the list
The highest number in the list
The total of the numbers in the list
The average of the numbers in the list
"""


#Main() function
def main():
    #numberAnalysis() function to invoke program
    numberAnalysis()
    


#numberAnalysis() function
def numberAnalysis():
    
    #Initializing empty list
    number_container = []

    #Initializing variables
    lowest_number = 0
    highest_number = 0
    list_of_elements = 0
    list_total = 0
    average = 0

    #For loop to iterate through range of 20 numbers
    for number in range(20):

        #Prompts user to enter number
        user_input = float(input("Enter a number: "))

        #Stores user_input value in list
        number_container.append(user_input)

        #Organizes list from least to greatest balue
        number_container.sort()

        #Defines value of lowest number to zero index position in list
        lowest_number = number_container[0]

        #Defines highest number to highest index position in list
        highest_number = number_container[-1]
        #Calculating sum of all number input
        list_total += user_input
        #Incrementing 1 unit for each element in list
        list_of_elements +=1

    #Value of list_total divided by numer_of_elements in list
    average = list_total/list_of_elements 
    
    #Displays list of elements
    print('List:', number_container)

    #Displays lowest value in list
    print(f"Lowest number: {lowest_number:,.2f}")

    #Displays highest value in list
    print(f"Highest number: {highest_number:,.2f}")

    #Displays total value of list items input
    print(f"Total: {list_total:,.2f}")

    #Displays average value of items in list
    print(f"Average: {average:,.2f}")



#Calling Main() function to start program
main()
