# Instantiate employee list
employee = {}

# Instantiate income tax list
incomeTax = {
    "AL": 2.0,
    "AK": 0.0,
    "AZ": 2.59,
    "AR": 2.0,
    "CA": 1.0,
    "CO": 4.55,
    "CT": 3.0,
    "DC": 4.0,
    "DE": 0.0,
    "FL": 0.0,
    "GA": 1.0,
    "HI": 1.4,
    "ID": 1.125,
    "IL": 4.95,
    "IN": 3.23,
    "IA": 0.33,
    "KS": 3.1,
    "KY": 5.0,
    "LA": 1.85,
    "ME": 5.8,
    "MD": 2.0,
    "MA": 5.0,
    "MI": 4.25,
    "MN": 5.35,
    "MS": 0.0,
    "MO": 1.5,
    "MT": 1.0,
    "NE": 2.46,
    "NV": 0.0,
    "NH": 5.0,
    "NJ": 1.4,
    "NM": 1.7,
    "NY": 4.0,
    "NC": 4.99,
    "ND": 1.1,
    "OH": 0.0,
    "OK": 0.25,
    "OR": 4.75,
    "PA": 3.07,
    "RI": 3.75,
    "SC": 0.0,
    "SD": 0.0,
    "TN": 0.0,
    "TX": 0.0,
    "UT": 4.95,
    "VT": 3.35,
    "VA": 2.0,
    "WA": 0.0,
    "WV": 3.0,
    "WI": 3.54,
    "WY": 0.0
}


# ** Define first function for case 1 **
def case1():

  # Prints prompt to notify user of option picked
  print("You selected Option 1 (Input Hours Worked")

  # Prompts user to enter employee ID
  employee_id = input("Enter Employee ID: ")

  # Loop until the input is a valid float
  while True:
      # Prompts user to enter hours worked
      try:
          hours = input("Enter your hours worked: ")

          # Check if the input ends with a decimal point and append '0' if necessary
          if hours.endswith('.'):
              hours += '0'

          hours = float(hours)  # Try converting the input to a float

          # Break the loop if conversion to float is successful
          break  

      # If the input is not a valid float, print an error message and continue the loop
      except ValueError:
          print("Error, Please enter a valid wage rate (Numbers Only)")

  # Instantiates a new list to store hours worked
  newHoursList = []

  # Appends hours worked to new list
  newHoursList.append('{:.2f}'.format(hours))

  # Calls the addValue function to add hours worked to employee ID to employee list
  addValue(employee_id, newHoursList)


# ** Define addValue function with 2 parameters (employee ID, hours worked) **
def addValue(id, hours):

  # Checks if employee ID is in employee list, if true append hours to employee list
  if id in employee:
    employee[id].append(hours)

  # If employee ID is not in employee list add new employee ID to employee list
  else:
    employee[id] = [hours]
    print(employee[id])


# ** Define second function for case 2 **
def case2():

  # Prints prompt to notify user of option picked
  print("You selected Option 2 (Show Hours Worked) \n")

  # Prompts user to enter employee ID
  selected_employee_id = input("Enter Employee ID: ")
  
  # Loops until user enters valid ID
  while not selected_employee_id.isdigit():
    selected_employee_id = input("Error, Enter Employee ID: ")

  # Saves the employee list to a variable
  employee_hours = (employee.get(selected_employee_id))

  # Checks if the employee hours list is not empty
  if employee_hours is not None:
    print(
        f"\nEmployee ID: {selected_employee_id} \nHours Worked: {employee_hours}"
    )
  else:
    print("No hours found for this employee.")


# ** Define third function for case 3 **
def case3():

  # Prints prompt to notify user of option picked
  print("You selected Option 3 (Calculate Wage)")

  # Prompts user to enter employee state
  selected_state = input(
      "Please enter your State (Two Letters Only i.e. MN)").upper()

  # Loops until user enters valid state
  while not incomeTax.__contains__(selected_state):
    selected_state = input(
        "Error, Please enter your State (Two Letters Only i.e. MN)").upper()

  # Gets the tax rate from the user selected state
  taxRate = incomeTax.get(selected_state)

  # Prompts user to enter employee ID
  selected_employee_id = input("Enter Employee ID: ")

  # Loops until user enters valid ID
  while not selected_employee_id.isdigit():
    selected_employee_id = input("Error, Enter Employee ID: ")

  # Loops until the input is a valid float
  while True:
    
    # Prompts user to enter hours worked
    try:
      wageRate = float(input("Please enter your wage rate(Numbers Only): "))
      
      # Break the loop if conversion to float is successful
      break  

    # If the input is not a valid float, print an error message and continue the loop
    except ValueError:
      print("Error, Please enter a valid wage rate (Numbers Only)")

  # Gets the employee hours worked from the employee list
  employee_hours = (employee.get(selected_employee_id))

  # Instantiates a new variable for total hours worked
  totalHours = 0

  # Checks if the employee hours list is not empty
  if employee_hours is not None:

    # Loops through the employee hours list and adds the hours worked to the total hours
    for hours_list in employee_hours:

      # Converts the hours worked to a float and adds it to the total hours
      for hours in hours_list:
        totalHours += float(hours)

  # If no hours worked, print error message
  else:
    print("No hours found for this employee.")

  # Checks if the tax rate is not 0
  if taxRate is not None:
    
    # Calculates gross total wage
    grossTotal = float(wageRate) * totalHours

    # Calculates net total wage
    netTotal = grossTotal - (grossTotal * float(taxRate) / 100)

    # Formats the total hours worked, wage rate, gross total wage, and net total wage
    totalHours = format(totalHours, ".2f")
    wageRate = format(wageRate, ".2f")
    grossTotal = format(grossTotal, ".2f")
    netTotal = format(netTotal, ".2f")

    # Prints out a table structure of the calculated wage
    print(
        "_____________________________________________________________________ \n"
    )
    print("\033[4mCALCULATED WAGE\033[0m \n")
    print(f"Total Hours: {totalHours} \n")
    print(f"Wage Rate: $ {wageRate}  \n")
    print(f"Tax Rate: {taxRate}%  \n")
    print(f"Gross Total Wage: ${grossTotal} \n")
    print(f"Net Total Wage: ${netTotal} \n")
    print(
        "_____________________________________________________________________ \n"
    )


# ** Defining fourth function for case 4 **
def case4():

  # Prints prompt to notify user of option picked
  print("You selected Option 4 (Delete Hours Worked)")

  # Prompts user to enter employee ID
  selected_employee_id = input("Enter Employee ID: ")

  # Loops until user enters valid ID
  while not selected_employee_id.isdigit():
    selected_employee_id = input("Error, Enter Employee ID: ")

  # Prompts user to enter hours worked
  employee_hours = (employee.get(selected_employee_id))

  # Checks if the employee hours list is not empty
  if employee_hours is not None:

    # Prints out list of employee hours with a index number
    for i in range(len(employee_hours)):
      print(f"ID: {i} | Hours: {employee_hours[i]}")

    # Loops until a valid index is entered
    while True:

      # Prompts user to enter index number
      delete_index = input("Enter the index of the hours you want to delete: ")

      # Checks if the input is a valid integer
      if delete_index.isdigit():
          delete_index = int(delete_index)
          
          # Check if the index is within range
          if 0 <= delete_index < len(employee_hours):  

              # Deletes the hours from the employee list using the index
              del employee_hours[delete_index]

              # Prompts confirmation of hour deletion
              print("Hours deleted successfully.")
              
              # Breaks the loop
              break

          # If the index is not within range, print an error message and continue the loop
          else:
              print("Error: Index out of range. Please enter a valid index.")
      
      # If the input is not a valid integer, print an error message and continue the loop
      else:
          print("Error: Invalid input. Please enter a valid index.")

  # If the employee hours list is empty, print an error message
  else:
    print("No hours found for this employee.")


# ** Define fifth function for case 5 **
def default():
  print("You Exited The Program")


# ** Defines the function for the menu
def menu():
  print("\n")
  print("1. Input Hours")
  print("2. Show Hours")
  print("3. Calculate Wage")
  print("4. Delete Hours")
  print("#. Any Number Other Than The Stated To Exit The Program")


# ** Defines the menu selections
def selection(selection):
  if selection == 1:
    case1()
  elif selection == 2:
    case2()
  elif selection == 3:
    case3()
  elif selection == 4:
    case4()
  elif selection < 1 or selection > 4:
    default()


# ** Main Program **

#  Insantiate a variable to a default of 1
selection_input = 1

# Loop until the user enters a valid selection
while selection_input >= 1 and selection_input <= 4:

  # Try to execute the program
  try:
    # Calls the menu function
    menu()

    # Prompts user to enter a selection
    selection_input = int(input("\nEnter Your Selection (1-4): "))
    
    # Calls the selection function by passing the selection_input variable
    selection(selection_input)

  # If the input is not a valid integer, print an error message and continue the loop
  except ValueError:
    print("Incorrect input. Please Enter the Proper Selection: ")
