class AllPicks:
    def __init__(self, allowedModels):
        self.allowedModels = allowedModels
        self.picks = {}
        self.sports = []

    def PrintPicks(self):
        for sport in self.sports:
            print("----------------"+sport+"----------------")
            for pick in self.picks[sport]:
                print(pick)
            print("\n")
            
    def AddPick(self, pick):
        if pick.modelType in self.allowedModels:
            if not pick.sport in self.sports:
                self.sports.append(pick.sport)
                self.picks[pick.sport] = [pick]
            else:
                self.picks[pick.sport].append(pick)
    


class Pick:
    def __init__(self, modelType, sport, probability, line, lineType, player):
        self.modelType = modelType
        self.sport = sport
        self.probability = probability
        self.line = line
        self.lineType = lineType
        self.player = player

    def __str__(self):
        return f" {self.probability} - {self.line} {self.lineType} {self.player}"


patchNotes = "------NEW FEATURES (V0.01)------\n - Users can now select which model(s) they would like to use\n--------------------------------\n"


print(patchNotes)


_ = input("Start? (Enter Any Input) \n>")

keepGoing_count = 0
keepGoing = "Y"
while keepGoing == "Y":
    print("\n\n")
    #UPDATE MODEL SETTINGS
    settings_needHelp = True
    while settings_needHelp:
        settings_options = " 0: Recent Performance \n 1: Projections \n 2: EV Plus \n 3: Webscraped \n (Enter 'help' for more information on models)"
        settings_rawInput = input("Which of the following models would you used: \n" + settings_options + "(EX: 1,3)\n>")
        if settings_rawInput == "help":
            settings_help = "\nDESCRIPTIONS OF MODELS:\n(0) Recent Performance looks at the last 5 games for the player\n(1) Projections looks at projections for the stats for a player\n(2) EV Plus looks at the given odds of a line to determine is chance of hitting\n(3) Webscrapped used picks webscraped from the internet.\n\n"
            print(settings_help)
        else:
            settings_needHelp = False
            settings = [int(x) for x in settings_rawInput.split(',')]


    print("\n\n\n")

    slate = AllPicks(settings)
    slate.AddPick(Pick(0,"NFL","80%","O 275.5","Passing Yards", "Brock Purdy"))
    slate.AddPick(Pick(1,"NFL","60%","U 245.5","Passing Yards", "Patrick Mahomes"))
    slate.AddPick(Pick(2,"NBA","75%","O 21.5","P+R+A", "Buddy Heild"))
    slate.AddPick(Pick(3,"NBA","65%","U 8.5","Rebounds", "Trae Young"))

    #PRINT PICKS
    print("----------------PICKS----------------\n")
    slate.PrintPicks()

    if keepGoing_count >=5:
        keepGoing_prompt = f"\nWould you like to try different models? (Enter 'Y' or 'N') [You have tried a different model {keepGoing_count} times]\n"
    else:
        keepGoing_prompt = "\nWould you like to try different models? (Enter 'Y' or 'N')\n>"
    keepGoing_count += 1
    keepGoing = input(keepGoing_prompt)

print("End Program")
