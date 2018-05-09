import time
import datetime


class ToDoList(object):

    to_do_list = {
        }
    current_date = ((datetime.date.today().strftime("%B")) + " " + (datetime.date.today().strftime("%d")))

    def __init__(self, list_name):

        self.name = list_name
        self.date = self.current_date

    def add_item(self):
        
        #adds the inputed item into to_do_list under the correlating datetime
        self.to_do_list[str(datetime.datetime.now())] = str(input("Item: "))

    def print_list(self):

        print ("Date:  Item:")

        for item in self.to_do_list:
            
            #Puts datetime into month/day of month format
            time = str(item)
            time2 = ((time.split("-")))
            time3 = (time2[2].split(" "))

            #prints out the date in month/day format and the item with spaces in between
            print ((time3[0] + "/" + time2[1]) + "  " + self.to_do_list[item])


my_list = ToDoList("My To Do List")

my_list.add_item()
my_list.add_item()

my_list.print_list()

