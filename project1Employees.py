"""script: project1Employees.py
   action: a. define class Person
           b. define class Employee
           c. define get employees()
           d. define create_menu()
           e. define display_employee_employment_information()
           f. define display_employee_contact_info()
           g, call get_employees
           h. call create_menu()
   author: Mat Bakarich
   date:   03/31/2025 
"""
###########################################################################################################
#    class_person.py
###########################################################################################################
"""
    script: class_person.py
    author: Mat Bakarich
"""

# import abc
from abc import ABC


# class definition
class Person(ABC):
    """
    A class representing a person.

    attributes:
        last_name (str): Last Name
        first_name (str): First Name
        id (4-digit intger): ID Number
        email_address (str): e-mail address
        phone_number (12-character str): Phone Number
    
    methods:
        first_name(): set the first name
        last_name(): set the last name
        email_address(): set the e-mail address
        phone_number(): set the phone number
        *note* the ID number cannot be changed
    
    """

    def __init__(self, last_name, first_name, id, email_address, phone_number):
        """
        Initializes an person object.

        arguments: 
            last_name (str): Last Name
            first_name (str): First Name
            id (4-digit intger): ID Number
            email_address (str): e-mail address
            phone_number (12-character str): Phone Number
        """
        # call ABC's init method
        super().__init__()
        
        # intialize last name
        self.last_name = last_name
        
        # initialize firt name
        self.first_name = first_name
        
        # convert id to integer
        id = int(id)
        # validate the number is 4-digits
        if not 1000 <= id <= 9999:
        # raise ValueError if ID out of range.
            raise ValueError("ID Number must be a 4-digit integer")
        # intialize id
        self._id = id
        
        # initialize e-mail address
        self.email_address = email_address

        # intialize phone number
        self.phone_number = phone_number

    
    
    def __repr__(self):
        """
            Returns a string representation of the Person object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Person object
        
        """
        return (f"Name: {self._first_name} {self._last_name}\nID: {self._id}\nE-mail: {self._email_address}\nPhone Number: {self._phone_number}")
    
    def __str__(self):
       """
            Returns a string representation of the Person object.

            action: returns a string
            input: none
            output: none
            return: string represenation of Person object
        
        """
       return (f"Name: {self._first_name} {self._last_name}\nID: {self._id}\nE-mail: {self._email_address}\nPhone Number: {self._phone_number}")
    
    # first name getter and setter
    @property
    def first_name(self):
        """return the first name"""
        return self._first_name
    
    @first_name.setter
    def first_name(self,first_name):
        """Set first name."""
        self._first_name = first_name


    # last name getter and setter
    @property
    def last_name(self):
        """return the last name"""
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        """Set last name."""
        self._last_name = last_name
    


    # id getter
    @property
    def id(self):
        """return id number."""
        return self._id
     


    # e-mail getter and setter
    @property
    def email_address(self):
        """return the e-mail address."""
        return self._email_address
    
    @email_address.setter
    def email_address(self, email_address):
        """Set the e-mail address."""
        self._email_address = email_address
    


    # phone number getter and setter
    @property
    def phone_number(self):
        """return the phone number."""
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        """Set the phone number."""
        if len(phone_number) != 12:
            raise ValueError("Phone number must be 12 characters including spaces.")
        else:
            self._phone_number = phone_number

###########################################################################################################
#    class_employee.py
###########################################################################################################
"""
    script: class_employee.py
    author: Mat Bakarich
"""

# import datetime
import datetime

# class definition
class Employee(Person):
    """
    A class representing an Employee(Person)

    attributes:
        last_name (str): Last Name
        first_name (str): First Name
        id (4-digit intger): ID Number
        email_address (str): e-mail address
        phone_number (12-character str): Phone Number
        hire_date (str): hire date date object
        classification_person (str): full-time or part-time classification
        role_pereson (str): staff or faculty role
        annual_salary (float): annual salary, must be positive float to 2 decimal places 
    
    methods:
        first_name(): set the first name
        last_name(): set the last name
        email_address(): set the e-mail address
        phone_number(): set the phone number
        *note* the ID number cannot be changed
    
    """

    # class variables
    role_dictionary = {'001': 'Staff', '002': 'Faculty'}  
    classification_dictionary =	{'001': 'Full-time', '002': 'Part-time'}  

    # init method
    def __init__(self, last_name, first_name, id, email_address, phone_number, hire_date, classification_person, role_person, annual_salary ):
        super().__init__(last_name, first_name, id, email_address, phone_number)
         
        # store hire date in a local variable
        hire_string = hire_date
        # strip backslashes from hire date and intialize date object
        try:
            hire_date = datetime.datetime.strptime(hire_string, "%m/%d/%Y").date()
        except ValueError:
            print("Hire date must be a valid string in 'MM/DD/YYYY' format.")
        # set hire date
        self._hire_date = hire_date
        
                    
        # intialize role_person        
        self.role_person = role_person

        # initalize classification_person   
        self.classification_person = classification_person 
        
        # set annual salary
        self.annual_salary = annual_salary
    
    # def repr() method
    def __repr__(self):
        classification = self._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        role = self._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value
        return (f"{super().__repr__()} \nHire date: {self._hire_date} \nRole: {role} \nClassification: {classification} \nAnnual Salary: ${self._annual_salary}")
    
    # def str() method
    def __str__(self):
        classification = self._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        role = self._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value
        return (f"{super().__str__()} \nHire date: {self._hire_date} \nRole: {role} \nClassification: {classification} \nAnnual Salary: ${self._annual_salary}")
                     
    # hite date getter
    @property
    def hire_date(self):
        """return the hire date"""
        return self.hire_date
    
    #@hire_date.setter
    # hire date may not be changed once initialized.
    
    # classification_person getter and setter
    @property
    def classification_person(self):
        """return the  employee classification"""
        return self._classification_person
    
    @classification_person.setter
    def classification_person(self,classification_person):
        """set the employee classification"""
        # adjust classification strings to match format
        classification_person = classification_person.lower()
        if classification_person == 'full':
                classification_person = 'Full-time'
        elif classification_person == 'part':
                classification_person = 'Part-time'
        else:
            raise ValueError("classification_person must be 'Full' or 'Part'.")
        
        # iterate over classification dictionary
        for key, value in Employee.classification_dictionary.items():          
            # check for classification in values
            if classification_person == value:
                # store the dictionary key in local variable 
                classification_person = key
        # set classification person
        self._classification_person = classification_person


    # role_person getter and setter
    @property
    def role_person(self):
        """return the employee role"""
        return self._role_person
    
    @role_person.setter
    def role_person(self,role_person):
        """set the employee role"""
        # check if employee role is in role_dictionary
        for key, value in Employee.role_dictionary.items():
            if role_person == value:
                # store the dictionary key in local variable 
                role_person = key 
                self._role_person = role_person
        if role_person not in Employee.role_dictionary.keys():    
                raise ValueError("Employee role not found.")
     

    # annual_salary getter and setter
    @property
    def annual_salary(self):
        """return the annual salary"""
        return self._annual_salary
    
    @annual_salary.setter
    def annual_salary(self, annual_salary):
        """validate and set the annual salary"""
        try:
            annual_salary = float(annual_salary)

        except ValueError:
            print("Annual Salary must be a float.")
        
        if annual_salary <= 0:
            raise ValueError("Annual salary can't be negative.")     
        else:
            annual_salary = f"{annual_salary:.2f}"
            self._annual_salary = annual_salary


###########################################################################################################
## Get Employees
###########################################################################################################

# intialize employee list
employee_list = []

def get_employees():
    """opens the employees.txt file
       reads the file line by line
       for each line, creates and Employee object and adds it to the Employee list.
    """
    # print a startup line
    print("Starting Application....")

    # open employees.txt
    with open('employees.txt', mode='r') as employees:
        for line in employees:
            # Strip whitespace and split the line into parts (adjust delimiter as needed)
            data = line.split()
            classifications = ('full', 'part',)
            roles = ('staff', 'faculty')
            classification = data[6].lower()
            role_current = data[7].lower()
            
            #check for header line
            if len(data) == 9  and (data[6]).lower() in classifications and data[7].lower() in roles and not 'ID' in data:
            
                # create a class instance    
                obj = Employee(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],)
                # add employee object to employee list
                employee_list.append(obj)
                # concatenate firstname and lastname strings
                name = obj.first_name + " " + obj.last_name
                # print a line confirming the Employee was initialized
                print(f"Added employee {name}...")
            # skip the header line of the text file
            elif len(data) == 0:
               print("Skipping blank line.")
            elif 'ID' in data:
                print("Skipping header line.")
            # skip lines with incorrect numbers of attributes
            elif classification not in classifications or role_current not in roles:
                print(f"Skipping entry: {data} due to invalid role or classification.")
            else:
                print(f"Skipping line: {line.strip()} - Incorrect number of attributes")
        
###########################################################################################################
## MENU
###########################################################################################################

def create_menu():
    
    # add menu options here, use this format
    menu_options = ('1. Quit', 
                    '2. Display Employee Employment Information', 
                    '3. Display Employee Contact Information',
                   #'4. Enter a new menu option followed by a comma here'
                    )
    # sentinel variable for loop
    keep_going = 0

    # print the menu options
    while keep_going != 1:
        print("\nPlease select an option below.\n")
        for item in menu_options:
            print(item)

        # get user input
        while True:
            # ensure user input is a menu option
            try:
                user_selection = int(input())
                if not user_selection in range(len(menu_options) + 1) or user_selection == 0 :
                    raise ValueError(f"Please choose an option between 1 and {len(menu_options)}")
                break
            except ValueError:
                print(f"Please choose an option between 1 and {len(menu_options)}.")


    ####################################
    # add new menu selection code here #
    ####################################    
        if user_selection == 1:
            print('\nThank you for using the system. \nNow exiting the program…')
            # terminate the menu loop using the sentinel value
            keep_going = 1
        if user_selection == 2:
            display_employee_employment_information() 
        if user_selection == 3:
            display_employee_contact_information() 
      # if user_selection == 4:
            

###########################################################################################################
## employee employment info
###########################################################################################################
def display_employee_employment_information():
    
    # print a header line
    print(f"\nEmployee Employment Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'E-mail' : <33}{'Phone Number ' : <12}{'Hire Date' : <12}{'Classification' : <15}{'Role' : <12}{'Salary' : <12}")
    
    # iterate over employee list and set attributes to variables
    for item in employee_list:
        employee = item
        last_name = employee.last_name
        first_name = employee.first_name
        id = employee.id
        email = employee.email_address
        phone_number = str(employee.phone_number)
        hire_date = str(employee._hire_date)
        
        # convert stored value back to classification
        classification = employee._classification_person
        for key, value in Employee.classification_dictionary.items():
            if classification == key:
                classification = value
        # convert stored value back to role
        role = employee._role_person
        for key, value in Employee.role_dictionary.items():
            if role == key:
                role = value  
        salary = float(employee._annual_salary)
        salary = f"{salary:.2f}"
        salary = str(salary)
        
        # print Employee Employment information
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}   {phone_number : <12} {hire_date : <12}{classification : <15}{role : <12}{salary : <12}")
         
        


###########################################################################################################
## employee contact info
###########################################################################################################
def display_employee_contact_information():
    # print a header line
    print(f"\nEmployee Contact Information:\n\n{'Last Name' : <15}{'First Name' : <15}{'ID' : <6}{'Email' : <30}{'Phone' : <12}")
    # iterate over empplooyee_list and set attributes to variables
    for item in employee_list:
        employee = item
        last_name = employee.last_name
        first_name = employee.first_name
        id = employee.id
        email = employee.email_address
        phone_number = str(employee.phone_number)
        # print the employee contact information
        print(f"{last_name : <15}{first_name : <15}{id : <6}{email : <30}{phone_number : <12}")




# call get_employees
get_employees()


# call create_menu
create_menu()  
