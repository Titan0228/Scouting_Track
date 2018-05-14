import time
import datetime

#creates a list of all non required for Eagle BSA Merit Badges as of 2018 from a text document called Other_Merit_Badge_List.txt:

other_merit_badges = None

with open("Other_Merit_Badge_List.txt", "r") as OtherMeritBadgeList:
    other_merit_badges = str(OtherMeritBadgeList.read())

other_merit_badges = other_merit_badges.split("\n")


#creates a list of all required for Eagle BSA Merit Badges as of 2018 from a text document called Req_Merit_Badge_List.txt:

req_merit_badges = None

with open("Req_Merit_Badge_List.txt", "r") as ReqMeritBadgeList:
    req_merit_badges = str(ReqMeritBadgeList.read())

req_merit_badges = req_merit_badges.split("\n")


#creates a list of all BSA Scout Ranks as of 2018 from a text document called Scout_Ranks.txt:

scout_ranks = None

with open("Scout_Ranks.txt", "r") as ScoutRanks:
    scout_ranks = str(ScoutRanks.read())

scout_ranks = scout_ranks.split("/n")


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
        if item in scout_ranks:
            item_list.append("Scouting Rank")
            
        elif (item in other_merit_badges) or (item in req_merit_badges):
            item_list.append("Merit Badge")

        else:
            item_list.append("No Type")

    def print_list(self):

        print ("Date:  Achievement:  Type:")
        
        #prints out each item_time, its correlating item name (stored in index 0) and its item type (stored in index 1)
        for item_time in self.completed_dict:
            
            #Puts time stamp into month/day of month format
            time = str(item_time)
            time2 = ((time.split("-")))
            time3 = (time2[2].split(" "))

            #prints out the date in month/day format and the item_list's first value (which is the original item) with spaces in between
            print ((time3[0] + "/" + time2[1]) + "  " + self.completed_dict[item_time][0] + "  " + self.completed_dict[item_time][1])



#creates display where one can track progress towards ranks and add completed ranks

class Display(object):

    num_req_merit_badges = 0
    num_other_merit_badges = 0
    current_scout_rank = None

    def __init__(self, username):

        self.username = username
        self.completed_list = CompletedList(str(username) + "'s Completed List")

    def count_ranks(self):

        #counts how many badges of each type (req, other, self.current_scout_rank) are in self's 
        for item_time in self.completed_list.completed_dict:

            item = self.completed_list.completed_dict[item_time][0]
            
            if item in req_merit_badges:
                self.num_req_merit_badges += 1

            elif item in other_merit_badges:
                self.num_other_merit_badges += 1

            elif item in scout_ranks:
                self.current_scout_rank = str(item)
                
    def print_display(self):
        self.num_merit_badges = self.num_req_merit_badges + self.num_other_merit_badges
        
        #Eagle (21 min merit badges)
        if self.num_merit_badges > 21:
            scaled_num = 10
        else:
            scaled_num = int((self.num_merit_badges/21)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Eagle Scout")
        if self.num_merit_badges >= 21:
            self.current_scout_rank = "Eagle Scout"

            
        #Life (11 min merit badges)
        if self.num_merit_badges > 11:
            scaled_num = 10
        else:
            scaled_num = int((self.num_merit_badges/11)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Life Scout")
        if self.num_merit_badges >= 11 and self.num_merit_badges < 21:
            self.current_scout_rank = "Life Scout"

            
        #Star (6 min merit badges)
        if self.num_merit_badges > 6:
            scaled_num = 10
        else:
            scaled_num = int((self.num_merit_badges/6)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Star Scout")
        if self.num_merit_badges >= 6 and self.num_merit_badges < 11:
            self.current_scout_rank = "Star Scout"

            
        #First Class
        if self.current_scout_rank == "Eagle Scout" or self.current_scout_rank == "Life Scout" or self.current_scout_rank == "Star Scout" or self.current_scout_rank == "First Class":
            print ("[" + ("|"*10) + "]  " + "First Class")


        #Second Class
        if self.current_scout_rank == "Eagle Scout" or self.current_scout_rank == "Life Scout" or self.current_scout_rank == "Star Scout" or self.current_scout_rank == "First Class" or self.current_scout_rank == "Second Class":
            print ("[" + ("|"*10) + "]  " + "Second Class")
        else:
            print ("[" + (" "*10) + "]  " + "Second Class")


        #Tenderfoot
        if self.current_scout_rank == "Eagle Scout" or self.current_scout_rank == "Life Scout" or self.current_scout_rank == "Star Scout" or self.current_scout_rank == "First Class" or self.current_scout_rank == "Second Class" or self.current_scout_rank == "Tenderfoot":
            print ("[" + ("|"*10) + "]  " + "Tenderfoot")
        else:
            print ("[" + (" "*10) + "]  " + "Tenderfoot")


        #Scout Rank
        if self.current_scout_rank == "Eagle Scout" or self.current_scout_rank == "Life Scout" or self.current_scout_rank == "Star Scout" or self.current_scout_rank == "First Class" or self.current_scout_rank == "Second Class" or self.current_scout_rank == "Tenderfoot" or self.current_scout_rank == "Scout Rank":
            print ("[" + ("|"*10) + "]  " + "Scout Rank")
        else:
            print ("[" + (" "*10) + "]  " + "Scout Rank")

        #creates endless loop of adding items and seeing progress towards ranks
        self.scout_display()

    def scout_display(self):

        #prints out a prompt to add achievements
        self.completed_list.add_item()
        self.count_ranks()
        self.print_display()
        
            
my_scouting = Display("Nicholas")
my_scouting.scout_display()
