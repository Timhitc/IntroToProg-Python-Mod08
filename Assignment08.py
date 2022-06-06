# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# THitch, 6.6.22, Scrapped original and started changes over
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    totalcount = 0
    def __init__(self, prod_name, prod_price):
        self.__name = prod_name
        self.__price = prod_price
        Product.totalcount +=1

    def __str__(self):
        return  self.name + ", " + str(self.price)

    @property
    def name(self):
        return str(self.__name).title()

    @property
    def price(self):
        return float(self.__price)

    @name.setter
    def name(self, value):
        if str(value).isnumeric()==False:
            self.__name = value
        else:
            raise Exception("Product name cannot start with a number")

    @price.setter
    def price(self, value):
        if isinstance(value,(int, float))==True:
            self.__price = value
        else:
            raise Exception("Product price bust be numeric")



# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) index of products filled with file data:
        :return: (list)
        """
        list_of_rows.clear()
        try:
            file = open(file_name, "r")
            for line in file:
                name, price = line.split(",")
                globals()[name.strip()] = Product(name, price.strip("\n"))
                list_of_rows.append(name)
            file.close
        except FileNotFoundError:
            print("No saved file found")
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """ Saves product objects to file

        :param file_name: (string) name of file
        :param list_of_rows : (list) index of Product object to be recorded
        :return: none
        """
        objfile = open(file_name, "w")
        for row in list_of_rows:
            objfile.write(str(globals()[row].name) +", "+ str(globals()[row].price) + '\n')
        objfile.close()
        return


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
        Provides input and output to the user

        properties:

        methods:
        print_menu_Products
        input_menu_choice
        input_new_name_and_price -> strname, strprice

        changelog: (When,Who,What)
        THitch, 6.6.22, (re)Created Class
    """
    pass

    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
                Menu of Options
                1) Add a new Product
                2) Remove an existing Product 
                3) Save Data to File        
                4) Reload Data from File
                5) Exit Program
                ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (choice) string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_Products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in list_of_rows:
            print("Product Name: " + globals()[row].name + "   Price: $" + str(globals()[row].price))
        print("*******************************************")

    @staticmethod
    def input_new_name_and_price():
        while (True):
            strname = str(input("What is the Product Name?"))
            if (str(strname).isnumeric() == True):
                print("Product Name cannot contain any numbers")
                continue
            else:
                while (True):
                    strprice = str(input("What is the Product Price?"))
                    try:
                        float(strprice)
                        break
                    except Exception:
                        print("Product Price must be numeric")
                        continue
            globals()[strname] = Product(strname, strprice)
            lstOfProductObjects.append(strname)
            print(str(globals()[strname].name) + " added.")
            break

        return

    @staticmethod
    def delete_product():
        strremove = ""
        strremove = input("What product would you like to remove?")
        for row in lstOfProductObjects:
            if row.lower() == strremove.lower():
                lstOfProductObjects.remove(row)
                del globals()[row]
                print("Product removed")


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
# Load data from file into a list of product objects when script starts
while True:
    IO.print_current_Products_in_list(lstOfProductObjects)
    # Show user current data in the list of product objects
    IO.print_menu_Products()
    # Show user a menu of options
    strchoice = IO.input_menu_choice()
    # Get user's menu option choice

    if strchoice.strip() == "1":
        # Let user add data to the list of product objects
        IO.input_new_name_and_price()

        continue


    if strchoice.strip() == "2":
        IO.delete_product()


    if strchoice.strip() == "3":
        # let user save current data to file and exit program
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        input("Data saved, press enter to continue")

    if strchoice.strip() == "4":
        print("WARNING: Unsaved data will be lost!")
        strchoice = input("Are you sure y/n")
        if strchoice.lower() == 'y':
            FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
        else:
            print("Action canceled")
            continue

    if strchoice.strip() == "5":
        input("Goodbye")
        break






# Main Body of Script  ---------------------------------------------------- #


