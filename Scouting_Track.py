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
    num_adds = 0

    num_req_merit_badges = 0
    num_other_merit_badges = 0
    current_scout_rank = None

    def __init__(self, username):

        self.username = username
        self.date = self.current_date

    def add_item(self):

        item = str(input("Item: "))

        #checks if item is already in Achievements.txt
        with open("Achievements.txt", "r") as Achievements:
            completed_achievements = str(Achievements.read())
            completed_achievements = completed_achievements.split("\n")

        if item not in completed_achievements:
            
            
            #adds the inputed item into completed_dict under the correlating time stamp
            item_list = [item]
            self.completed_dict[str(datetime.datetime.now())] = item_list
            

            #adds achievement type of the inputed item (i.e. Merit Badge, Scout Rank, or No Type)
            if item in scout_ranks:
                item_list.append("Scouting Rank")
                
            elif item in req_merit_badges:
                item_list.append("Req Merit Badge")

            elif item in other_merit_badges:
                item_list.append("Other Merit Badge")

            else:
                item_list.append("No Type")

            #writes the inputed item unto Achievements.txt
            with open("Achievements.txt", "r") as Achievements:
                achievements = Achievements.readlines()

            achievements.append(str(item + "\n"))

            with open("Achievements.txt", "w") as Achievements:
                            Achievements.writelines(achievements)
                            

            #counts how many badges of each type (req, other, self.current_scout_rank) are in self's 
            for item_time in self.completed_list.completed_dict:

                item_type = self.completed_list.completed_dict[item_time][1]
                item = self.completed_list.completed_dict[item_time][0]

                if item not in completed_achievements:

                    #checks if item in required merit badges list
                    if item_type == "Req Merit Badge":
                        self.num_req_merit_badges += 1
                    
                    #checks if item in other merit badges list
                    elif item_type == "Other Merit Badge":
                        self.num_other_merit_badges += 1
                        
                    #checks if item in scout ranks list
                    elif item_type == "Scouting Rank":
                        self.current_scout_rank = str(item)


    def print_list(self):

        print ("Date:  Achievement:  Type:")
        
        #prints out each item_time, its correlating item name (stored in index 0) and its item type (stored in index 1)
        for item_time in self.completed_dict:
            
            #Puts time stamp into month/day of month format
            time = str(item_time)
            time2 = ((time.split("-")))
            time3 = (time2[2].split(" "))

            #prints out the date in month/day format and the item_list's first value (which is the original item) with spaces in between
            print ((time2[1] + "/" + time3[0]) + "  " + self.completed_dict[item_time][0] + "  " + self.completed_dict[item_time][1])

    def print_display(self):

        self.num_merit_badges = self.num_req_merit_badges + self.num_other_merit_badges

        #Eagle (21 min merit badges)
        if self.num_req_merit_badges >= 21:
            scaled_num = 10
            self.current_scout_rank = "Eagle Scout"
        else:
            scaled_num = int((self.num_merit_badges/21)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Eagle Scout")

            
        #Life (11 min merit badges)
        if self.num_merit_badges >= 11:
            scaled_num = 10
            if self.num_merit_badges < 21:
                self.current_scout_rank = "Life Scout"
        else:
            scaled_num = int((self.num_merit_badges/11)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Life Scout")

                    
        #Star (6 min merit badges)
        if self.num_merit_badges >= 6:
            scaled_num = 10
            if self.num_merit_badges < 11:
                self.current_scout_rank = "Star Scout"
        else:
            scaled_num = int((self.num_merit_badges/6)*10)
        print ("[" + ("|"*(scaled_num)) + (" "*(10-scaled_num)) + "]  " + "Star Scout")

            
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

        #Detailed descriptions prompt
        print ("Type 'details' to see more...")

    def print_details(self):

            print("Merit Badge Progress Details:")

            #Eagle (21 min merit badges)
            if self.num_req_merit_badges >= 13:
                req_scaled_num = 10
            else:
                req_scaled_num = int((self.num_req_merit_badges/13)*10)
            if self.num_other_merit_badges >= 8:
                other_scaled_num = 10
            else:
                other_scaled_num = int((self.num_other_merit_badges/8)*10)
                
            print ("Eagle Scout  " + "Req:[" + ("|"*(req_scaled_num)) + (" "*(10-req_scaled_num)) + "]" + "  Other:[" + ("|"*(other_scaled_num)) + (" "*(10-other_scaled_num)) + "]")

                
            #Life (11 min merit badges)
            if self.num_req_merit_badges >= 7:
                req_scaled_num = 10
            else:
                scaled_num = int((self.num_req_merit_badges/7)*10)
            if self.num_other_merit_badges >= 4:
                other_scaled_num = 10
            else:
                other_scaled_num = int((self.num_other_merit_badges/4)*10)
                
            print ("Life Scout   " + "Req:[" + ("|"*(req_scaled_num)) + (" "*(10-req_scaled_num)) + "]" + "  Other:[" + ("|"*(other_scaled_num)) + (" "*(10-other_scaled_num)) + "]")

                        
            #Star (6 min merit badges)
            if self.num_req_merit_badges >= 4:
                req_scaled_num = 10
            else:
                scaled_num = int((self.num_req_merit_badges/4)*10)
            if self.num_other_merit_badges >= 2:
                other_scaled_num = 10
            else:
                other_scaled_num = int((self.num_other_merit_badges/2)*10)
                
            print ("Star Scout   " + "Req:[" + ("|"*(req_scaled_num)) + (" "*(10-req_scaled_num)) + "]" + "  Other:[" + ("|"*(other_scaled_num)) + (" "*(10-other_scaled_num)) + "]")

class ScoutTrack(CompletedList):

    def __init__(self):

        self.date = self.current_date
        print ("Welcome to Scout Track! Please choose a username.")
        self.username = str(input("Username:"))
        self.completed_list = CompletedList(str(self.username) + "'s Completed List")
        print ("To add achievements, type add.")
        print ("To see your progress towards ranks, type progress.")
        print ("To see a list of past achievements, type history.")

        #clears achievements
        with open("Achievements.txt", "r+") as Achievements:
            Achievements.truncate()

    def prompt(self):

        #print (self.completed_dict)
        
        self.command = None
        while (not(self.command == "add" or self.command == "details" or self.command == "progress" or self.command == "history")): 
            self.command = input("Prompt:")

        if self.command == "add":
            self.add_item()
            self.prompt()

        if self.command == "progress":
            self.print_display()
            self.prompt()

        if self.command == "details":
            self.print_details()
            self.prompt()
            
        if self.command == "history":
            self.print_list()
            self.prompt()
            
my_scouting = ScoutTrack()
my_scouting.prompt()
