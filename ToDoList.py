import time
import datetime

#creates a list of all 137 BSA Merit Badges as of 2018 from a text document called Merit_Badge_List.txt:

merit_badges = None

with open("Merit_Badge_List.txt", "r") as MeritBadgeList:
    merit_badges = str(MeritBadgeList.read())

merit_badges = merit_badges.split("\n")


#creates class for achievement lists (lists of completed ranks)

class CompletedList(object):

    completed_dict = {
        }
    current_date = ((datetime.date.today().strftime("%B")) + " " + (datetime.date.today().strftime("%d")))

    def __init__(self, list_name):

        self.name = list_name
        self.date = self.current_date

    def add_item(self):
                                 
        #adds the inputed item into completed_dict under the correlating time stamp
        item = str(input("Item: "))
        item_list = [item]
        self.completed_dict[str(datetime.datetime.now())] = item_list

        #adds achievement type of the inputed item (i.e. Merit Badge, Scout Rank, or No Type)
        if (item == "Tenderfoot" or item == "Second Class" or item == "First Class" or item == "Star Scout" or item == "Life Scout" or item == "Eagle Scout"):
            item_list.append("Scout Rank")
            
        elif (item in merit_badges):
            item_list.append("Merit Badge")

        else:
            item_list.append("No Type")

    def print_list(self):

        print ("Date:  Achievement:  Type:")

        for item_time in self.completed_dict:
            
            #Puts time stamp into month/day of month format
            time = str(item_time)
            time2 = ((time.split("-")))
            time3 = (time2[2].split(" "))

            #prints out the date in month/day format and the item_list's first value (which is the original item) with spaces in between
            print ((time3[0] + "/" + time2[1]) + "  " + self.completed_dict[item_time][0] + "  " + self.completed_dict[item_time][1])




my_list = CompletedList("My To Do List")

my_list.add_item()
my_list.print_list()
