
#################################MINIMAPS###################################
#mini1=Horastead
#mini2=Ancient Ruin
#mini3=Rebel House

#mini4=TRoll cave
#mini5=Dragon cave
#mini6=Morceris castle
#mini7=Morc Town 1
#mini8=Morc Town 2
#mini9=Morc town 3
#mini10= Goblin cave? dont really need
#mini11= Ice Dragon
#mini12= Dalthuur castle
#mini13= Dark elves lair
#mini14= Mountain castle
#mini15= Mountain pass cave
#mini16= Korvorath lair
#mini17 = storm dragon lair
#mini18= Shanzalars castle



my_string='''         _________ _______  _______  _______  _       
|\     /|\__    _/(  ___  )(  ____ )(  ___  )( (    /|
| )   ( |   )  (  | (   ) || (    )|| (   ) ||  \  ( |
| (___) |   |  |  | (___) || (____)|| |   | ||   \ | |
|  ___  |   |  |  |  ___  ||     __)| |   | || (\ \) |
| (   ) |   |  |  | (   ) || (\ (   | |   | || | \   |
| )   ( ||\_)  )  | )   ( || ) \ \__| (___) || )  \  |
|/     \|(____/   |/     \||/   \__/(_______)|/    )_)'''

print(my_string)

#Start Game: # create another start symbol
s=input("PRESS 's' TO START: ")
if s=="s":
    input("Welcome Adventurer! Before you embark on your quest, here is a tutorial PRESS ENTER TO CONTINUE: ")
    #r=int(r)
    
    print("This is your character token: Ꙙ. You can move around the map by pressing: w-move north,s- move south, d-move east, and a-move west.")
        
    input("You can interact with the map by travelling to different areas. ")

        
       
    input("You can move two steps at a time by pressing the button twice: ex) aa, or dd. ")
    
    input("Pressing the a,s,d,w keys three times will move you three spaces, but you will lose 1 stamina. ")
    
    input("PRESS '?' to activate information. PRESS 'i' to bring up your inventory. PRESS 't' to bring up the tutorial in game.")
    
    print("When text appears, PRESS ENTER TO CONTINUE. This game allows you to choose different text options.")
    
    input("Read the dialogue and press the corresponding key. ")
    
    input("This game allows you to make decisions(good or evil) throughout the game in the text dialogue.")
    
    input("Depending on what decision you make, you will be given a unique outcome.")
    
    input("**TO MAKE THE STORYLINE MAKE THE MOST SENSE, STICK WITH EITHER [GOOD {OR} BAD]. NOT BOTH.**")
    
    input("If you land on an enemy token, combat will begin. Press the corresponding keys to attack.")
    
    input("You have five different attack types (spells, weapons, heavy attacks,scrolls, special weapons) and 3-5 different attacks each.")
    
    input("Press either a,s,e,d,w to choose a type of attack. You also have the option to drink a health or magik potion. Press q for potions")
    
    input("After an attack is initialized, press the corresponding number to choose your sub-attack.")
    
    input("If you defeat your enemy, you will be rewarded with loot and xp. type 'yes' to claim the loot and 'no' to not.")
    
    input("You can press 'x' to upgrade your spells and abilities.")
    
    input("All loot can be taken, but some will only work if you choose the evil decision.")
    
    input("If you die in combat or in the map, you will have the chance to regain all of your health, stamina, etc...")
    
    input("...but you will lose 1 of your 10 lives. Once you lose all 10, it is GAME OVER.")
    
    input("There are Merchants scattered around the land. You can buy potions and scrolls from them.")
    
    input("There are Blacksmiths scattered around as well. You can repair your sword and bow here.")#add shield? # hunting dagger?
    
                
input("Now, you are ready to embark on your Journey!")


class Map:
    #generates a map__________________
    def __init__(self, ): 
        self.data=["^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{WAR OF THE ANCIENTS}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
                   "==================================================================================================  ",
                   "|........##############...######....ᴥ.....##Ѻ###............######......###.....###.....######...|  ",
                   "|...########   #ϫ ####ᴥ######◊####.......## Ꙉ ###.........###   §###..##  ##..## ϫ##..##ₒₒ ₒ##...|  ",
                   "|..#  1 ##ᴥ    Ω  ###      ## ##........#.#   ###........# π #    Ƿ ##   ĦŒ ##      ##  Д    ₒ#..|  ",
                   "|..###    ###  #  ####    ###꙲#........#.###₪####.......##     ##      ##        #     # ₒₒ ##..|   ",
                   "|...##   ##       Ψ       ##..........###....‖..##......############# ###   ᴥ############Ŏ####...| ",
                   "|..##       # ##########Ō##...0......#  ##### ###......#Ӿ      ##    ### ##### ₒ ₒ #ₒ ₒ #  ###...|  ",
                   "|...##!##  ## $#ᴥ      ...#........##$         ###....##### #      #        ## ##ₒ##ₒ#ₒ# ₒ###....|  ",
                   "|...## ############# #######.......########ȣ####.......##   ϫ##### #    ##  Ŏ   # ₒ ₒ#ₒ# ##......|  ",
                   "|...###              #ϫ###ᴥ##......#       G Ӿ##........##  ##   # #####  # ####### ш#ₒ#ₒ#.......|  ", 
                   "|....## |H|#     #      #$  Ӿ#.....##     #Σ#   ##........#  *# ##ϫ##     ##       ## ₒ ₒ#.......|  ",
                   "|...####    ### ####  ##### #### ###            ##.........##     ##   ##    ####    ####........|  ",      
                   "|....####Ơ#### ###ϫ######       Φ          #####.............#### ẘ## #ᴥ #  #ϫ# §##     #........|  ",  
                   "|...#ᴥ                        #############.....................##    ##  ##  #   ##  # ##.......|    ",   
                   "|...##############################..............................## ##§###         Ǿ   # #........|         ",  
                   "|....####......##########.....###...............................#  ######   #Ѫ#   ##### #........|      ",               
                   "|...............................................................#  #....####   ###....# ᴥ#.......|   ",
                   "|........########.................#####...........#####........#  #.......###₻###......# ϫ#......|       ",
                   "|....####+Ꙋ ?# #$#####..........###   Ŀ####......#    Ӿ###.....#ϫᴥ#....................#  #......|   ",
                   "|...##  # ####      ######.........#  #   ####..#   #   ##......#ﬦ#.........#.#........#Ӿ#.......|   ",
                   "|....#Ұ  #-  #        ⌂  ######.....#   #    #### ### #  ##......###.......# Ꝋ #.......###.......|  ",
                   "|....##  #?#        <⌂⌂⌂>      #######  ##    #      ##    ###.....##.......###........##........|  ",
                   "|.....#    # Ҵ     <  _  > >           #  ##  #   ## #  ##   ####....#..................#........|      ",
                   "|......##  #    ?  <  M  > >    ### ###     #  ###    #   #      #########.......................|      ",
                   "|........##        <@V   > >   #      #####  #     ## #######        #   #####...................|    ",    
                   "|........##         <V V>@    #  #####....##  #  $####.....####  #      Ѥ  ########..............|        ",
                   "|.........######Ӿ    x  >  ᴥ#####..........#    ###...........###  ######        Ꝍ #.............|        ",
                   "|...............#############...............#####................####..##.#########..............|         ",
                   "==================================================================================================   ", 
                   "+++++++++++++++++++++++++++++++++++++++{Kingdoms of Hjaron}++++++++++++++++++++++++++++++++++++++        "]
                        ##########ADD <,>,^,V TO ISWALL, ADD @ AS A "CAVE TUNNEL"(ANOTHER PORTAL)[MAYBE FOLLLOW A BLOOD TRAIL TO MAKE IT EASIER TO FOLLOW?]
                        #########ADD Ꙋ AS A DIALOGUE BETWEEN YOU AND THE DARK ELVES.ƺ
                        #########ADD A SYMBOL TO THE MAP THAT WILL ACTIVATE (THE DARK ELVES TRAP YOU){TELEPORTS YOU TO JUST BEFORE Ꙋ} MAKE ANOTHER SYMBOL TO TELEPORT YOU BACK
################################################# smiths: L = low, R = med, D = med-high, U = high   # SHADOVAR(Ұ Ҵ Ꚅ Ꜻ ѿ ₾ ꝙ Ꝝ Ʊ Ԭ-------ѿ Ҵ Ұ Ԭ ẟ  ₾ ⌂ Ꙃ Ꙋ Ꚅ Ꜻ ꝙ Ꝝ ꬲ) Ω Ψ Ξ Φ Σ ₪ 
        self.enemies=[] #Enemy combat
        #merchant
    def playerCollidesEnemy(self): #Enemy combat
        for e in self.enemies:
            if self.player.x==e.x and self.player.y==e.y:
                return e
        return None
    
    def addEnemies(self, e): #Enemy combat
        self.enemies=self.enemies+[e]
    
    def setPlayer(self,player):
        self.player=player
####################################### NEW LOCATIONS WILL GO HERE #############################



######################################## ^^^^^^^^^^^^^^^^^^^^^^^^^ #############################



        
#determine if coordinate is a grove of poison trees
    def isWall(self, x, y):
        locationSymbol= self.data[y][x]
        if "#"== locationSymbol:
            return True
        else:
            return False
    def isCaveWall(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꙮ"== locationSymbol:
            return True
        else:
            return False
    def isCave2(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꬽ"== locationSymbol:
            return True
        else:
            return False
    def isCave3(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꬲ"== locationSymbol:
            return True
        else:
            return False

    def isTown (self, x, y):
        locationSymbol= self.data[y][x]
        if "H"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isRuins (self, x, y):
        locationSymbol= self.data[y][x]
        if "꙲"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isRuinRoom(self, x, y):
        locationSymbol= self.data[y][x]
        if "%"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isEntrance (self, x, y):
        locationSymbol= self.data[y][x]
        if "["== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isExit (self, x, y):
        locationSymbol= self.data[y][x]
        if "]"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False

    def isEntrance2 (self, x, y):
        locationSymbol= self.data[y][x]
        if "{"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isExit2 (self, x, y):
        locationSymbol= self.data[y][x]
        if "}"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isEntrance3 (self, x, y):
        locationSymbol= self.data[y][x]
        if "‾"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isExit3 (self, x, y):
        locationSymbol= self.data[y][x] 
        if "˽"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isDoor(self, x, y):
        locationSymbol= self.data[y][x]
        if "Π"== locationSymbol:
            return True
        else:
            return False
    def isPedestal (self, x, y):
        locationSymbol= self.data[y][x]
        if "^"== locationSymbol:
            return True
        else:
            return False
    
###########PORTALS#######33      
    def PortalM(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ѻ"== locationSymbol:
            return True
        else:
            return False
    def PortalA(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ꝍ"== locationSymbol:
            return True
        else:
            return False
    def PortalS(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ꝋ"== locationSymbol:
            return True
        else:
            return False

#########SMITH AND MAGICAL RESTORATION
    def Smith(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ӿ"== locationSymbol:
            return True
        else:
            return False
    def magicRest(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꙮ"== locationSymbol:
            return True
        else:
            return False


    
    
#determine if the player is on a boundary: dont let them pass      
    def isBoundary1(self, x, y):
        locationSymbol= self.data[y][x]
        if "|"== locationSymbol:
            return True
        else:
            return False

    def isBoundary2(self, x, y):
        locationSymbol= self.data[y][x]
        if "="== locationSymbol:
            return True
        else:
            return False
    def isBoundary3(self, x, y):
        locationSymbol= self.data[y][x]
        if "_"== locationSymbol:
            return True
        else:
            return False
    def isWall2(self, x, y):
        locationSymbol= self.data[y][x]
        if "/"== locationSymbol:
            return True
        else:
            return False

    def isWall3(self, x, y):
        locationSymbol= self.data[y][x]
        if "\\"== locationSymbol:
            return True
        else:
            return False
    def isMountian1(self, x, y):
        locationSymbol= self.data[y][x]#movingleft
        if "<"== locationSymbol:
            return True
        else:
            return False
    def isMountian2(self, x, y):
        locationSymbol= self.data[y][x]#movingright
        if ">"== locationSymbol:
            return True
        else:
            return False
    def isMountian3(self, x, y):
        locationSymbol= self.data[y][x]#movingup
        if "⌂"== locationSymbol:
            return True
        else:
            return False
    def isMountian4(self, x, y):
        locationSymbol= self.data[y][x]#movingdown
        if "˅"== locationSymbol:
            return True
        else:
            return False
    
    def isMountian5(self, x, y):
        locationSymbol= self.data[y][x]#movingdown
        if "˄"== locationSymbol:
            return True
        else:
            return False
    def isMtnCave(self, x, y):
        locationSymbol= self.data[y][x]#move the player 1 space down and 4 spaces right
        if "@"== locationSymbol:
            return True
        else:
            return False
    def isBlood(self, x, y):
        locationSymbol= self.data[y][x]#does not do anything. maybe print(you find more blood)(write in that someone is bleeding and there is recently dropped blood
        if ","== locationSymbol:
            return True
        else:
            return False
    def isDarkElf(self, x, y):
        locationSymbol= self.data[y][x]#move the player 1 space down and 4 spaces right
        if "?"== locationSymbol:
            return True
        else:
            return False

#determine if the coordinate is a cave
    def isCave (self, x, y):
        locationSymbol= self.data[y][x]
        if "Ō"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def isDragCave(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ơ"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
        
    def isSerpentDead(self, x, y):
        locationSymbol= self.data[y][x]
        if "0"== locationSymbol:
            return True
            
        else:
            return False
   
    def isGobCave(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ŏ"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def trapGold(self, x, y): #st [ﬦ] trap chest [
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 25 gold
        if "ш"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def iceLair(self, x, y): #st [ﬦ] trap chest [
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 25 gold
        if "*"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def iceLair2(self, x, y): #st [ﬦ] trap chest [
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 25 gold
        if "ẘ"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    
    def invisGoblin(self, x, y):
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 300 gold
        if ","== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def realGold(self, x, y):
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 300 gold
        if "ﬦ"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    def largeChest(self, x, y):
        locationSymbol= self.data[y][x]#subtracts 20 health, gives 300 gold
        if "□"== locationSymbol:
            return True
            print("Enter Cave")
        else:
            return False
    
    
        
#determine if the coordinate is a ruin
    
#determine if coordinate is water
    def isWater(self, x, y):
        locationSymbol= self.data[y][x]
        if "."== locationSymbol:
            return True
        else:
            return False

#determine if coordinate is a MainQuest 
    def MainQuest1(self, x, y):
        locationSymbol= self.data[y][x]
        if "1"== locationSymbol:
            return True
        else:
            return False
        
    def MainQuest2(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ω"== locationSymbol:
            return True
        else:
            return False
    def MainQuest3(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ψ"== locationSymbol:
            return True
        else:
            return False
    def isCave2(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꬽ"== locationSymbol:
            return True
        else:
            return False
    def isCave3(self, x, y):
        locationSymbol= self.data[y][x]
        if "ꬲ"== locationSymbol:
            return True
        else:
            return False
    def MainQuest4(self, x, y):
        locationSymbol= self.data[y][x]
        if "Ξ"== locationSymbol:
            return True
        else:
            return False
    def MainQuest4a(self, x, y):
        locationSymbol= self.data[y][x]
        if "ѳ"== locationSymbol:
            return True
        else:
            return False
    def SerpentMission(self, x, y):
        locationSymbol= self.data[y][x]
        if "Φ"== locationSymbol:
            return True
        else:
            return False
    
    
    def MainQuest5(self, x, y):
        locationSymbol= self.data[y][x]
        if "Σ"== locationSymbol:
            return True
        else:
            return False

    def MorcerisBridge(self, x, y):
        locationSymbol= self.data[y][x]
        if "‖"== locationSymbol:
            return True
        else:
            return False
    def MorcerisDoor(self, x, y):
        locationSymbol= self.data[y][x]
        if "₪"== locationSymbol:
            return True
        else:
            return False
    
    def MorcerisCastle(self, x, y):
        locationSymbol= self.data[y][x]
        if "§"== locationSymbol:
            return True
        else:
            return False  
#determine if coordinate is a side quest     
    
    def BanditGate(self, x, y):
        locationSymbol= self.data[y][x]
        if "!"==locationSymbol:
            return True
        else:
            return False
    def GuardDecision (self, x, y):
        locationSymbol= self.data[y][x]
        if "ȣ"==locationSymbol:
            return True
        else:
            return False
    def FinalDecision (self, x, y):
        locationSymbol= self.data[y][x]
        if "Ꙉ"==locationSymbol:
            return True
        else:
            return False
    def Morzana (self, x, y):
        locationSymbol= self.data[y][x]
        if "◊"==locationSymbol:
            return True
        else:
            return False

#determine if coordinate is a health potion
###MERCHANTS (1-10) $ ₡ ₿ ₵ ₴ € ฿ Ŀ § ¥
    def coins(self, x, y):
        locationSymbol= self.data[y][x]
        if "ₒ"==locationSymbol:
            return True
        else:
            return False

    def Merchant1(self, x, y):
        locationSymbol= self.data[y][x]
        if "$"==locationSymbol:
            return True
        else:
            return False
        
    def Merchant2(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "₡"==locationSymbol:
            return True
        else:
            return False
    def Merchant3(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "₿"==locationSymbol:
            return True
        else:
            return False
    def Merchant4(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "₵"==locationSymbol:
            return True
        else:
            return False
    def Merchant5(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "₴"==locationSymbol:
            return True
        else:
            return False
    def Merchant6(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "€"==locationSymbol:
            return True
        else:
            return False
    def Merchant7(self, x, y):
        locationSymbol= self.data[y][x]#use as special merchants
        if "฿"==locationSymbol:
            return True
        else:
            return False
    def Merchant8(self, x, y):
        locationSymbol= self.data[y][x]###$delete
        if "Ŀ"==locationSymbol:
            return True
        else:
            return False


    def Merchant9(self, x, y):
        locationSymbol= self.data[y][x]#use as special merchants
        if "asjfh"==locationSymbol:
            return True
        else:
            return False

    def Merchant10(self, x, y):
        locationSymbol= self.data[y][x]# dont have###$delete
        if "¥"==locationSymbol:
            return True
        else:
            return False

###POTIONS TO PICK UP
    def hpotion(self, x, y):
        locationSymbol= self.data[y][x]
        if "ᴥ"==locationSymbol:
            return True
        else:
            return False
    def mpotion(self, x, y):
        locationSymbol= self.data[y][x]
        if "ϫ"==locationSymbol:
            return True
        else:
            return False
   

#MORCENGARDE EXCLUSIVES MISSIONS:
        ##MISSIONS
    def morcIntro(self,x,y):
        locationSymbol= self.data[y][x]
        if "π"==locationSymbol:
            return True
        else:
            return False
    def morcMission1(self,x,y):
        locationSymbol= self.data[y][x]
        if "Œ"==locationSymbol:
            return True
        else:
            return False
    def StrǾmvar(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ƿ"==locationSymbol:
            return True
        else:
            return False
    def Horastead(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ħ"==locationSymbol:
            return True
        else:
            return False
    def Surtestead(self,x,y):
        locationSymbol= self.data[y][x]
        if "Д"==locationSymbol:
            return True
        else:
            return False
    
    def morcMission6(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ѫ"==locationSymbol:
            return True
        else:
            return False
    def morcMission7(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ǿ"==locationSymbol:
            return True
        else:
            return False
    
    def dalFinalDec(self,x,y):
        locationSymbol= self.data[y][x]
        if "₻"==locationSymbol:
            return True
        else:
            return False
        
    ###SHADOVAR MISSIONS # SHADOVAR(ѿ Ҵ Ұ Ԭ   ₾ ⌂  Ꙋ Ꚅ Ꜻ ꝙ Ꝝ ꬲ)  Ұ Ҵ Ꚅ Ꜻ ѿ ₾ ꝙ Ꝝ Ʊ Ԭ
    
    def shadMission1(self,x,y):
        locationSymbol= self.data[y][x]# arrive in shadovar
        if "Ұ"==locationSymbol:
            return True
        else:
            return False
    
    def shadMission2(self,x,y):
        locationSymbol= self.data[y][x]#dark elf hide out
        if "Ҵ"==locationSymbol:
            return True
        else:
            return False
    def shadMission3(self,x,y):
        locationSymbol= self.data[y][x]#frosken
        if "Ꚅ"==locationSymbol:
            return True
        else:
            return False
    def shadMission4(self,x,y):
        locationSymbol= self.data[y][x]#
        if "Ꜻ"==locationSymbol:
            return True
        else:
            return False
    def shadMission5(self,x,y):
        locationSymbol= self.data[y][x]#torum
        if "ѿ"==locationSymbol:
            return True
        else:
            return False
    def shadMission6(self,x,y):
        locationSymbol= self.data[y][x]
        if "₾"==locationSymbol:
            return True
        else:
            return False
    def shadMission7(self,x,y):
        locationSymbol= self.data[y][x]
        if "ꝙ"==locationSymbol:
            return True
        else:
            return False
    def shadMission8(self,x,y):
        locationSymbol= self.data[y][x]#
        if "Ꝝ"==locationSymbol:
            return True
        else:
            return False
    def shadMission9(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ʊ"==locationSymbol:
            return True
        else:
            return False
    
    def shadMission10(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ԭ"==locationSymbol:
            return True
        else:
            return False
    def sGate(self,x,y):
        locationSymbol= self.data[y][x]
        if "Ѥ"==locationSymbol:
            return True
        else:
            return False
    


#SHADOVAR EXCLUSIVES

    ########^^#def Victory##################
        
    
    def display(self, character):
        # place the @ in the right place
        #Get the x and y  coordinates of the character
        #find the matching index

        x=character.getX()
        y=character.getY()
        #Get the row to edit as player moves
        firstRows=self.data[0:y]
        rowToChange=self.data[y]
        lastRows=self.data[y+1:len(self.data)]
        #edit the row
        firstCols=rowToChange[0:x]
        lastCols=rowToChange[x+1:len(rowToChange)]
        newRow=firstCols+character.getSymbol()+lastCols
        #Glue them back together
        mapToDraw=firstRows + [newRow] +lastRows
        
        #draw enemies on map
        for e in self.enemies:
            x=e.getX()
            y=e.getY()
            #Get the row to edit
            firstRows=mapToDraw[0:y]
            rowToChange=mapToDraw[y]
            lastRows=mapToDraw[y+1:len(mapToDraw)]
            #edit the row
            firstCols=rowToChange[0:x]
            lastCols=rowToChange[x+1:len(rowToChange)]
            newRow=firstCols+e.getSymbol()+lastCols
            #Glue the rows back together
            mapToDraw=firstRows + [newRow] +lastRows
            #@@@@@@
       
  
        
        # loop over the data, printine each entry o  aline
        for line in mapToDraw:
            print(line)


###############################
#           #####             #
#          MINIMAPS           #
#           #####             #
###############################

class miniMap1(Map):
    def __init__(self,  ):#KORIFSTEAD
        super().__init__()
        self.data=["/============\\",
                   "[      \\=====|",
                   "|   •   \\   $|",
                   "|        == =|",
                   "|•    •      |",
                   "|       |Ξ|==|",
                   "|Ӿ      |    ]",
                   "\\============/"]
    

            
class miniMap1a(Map):
    def __init__(self, ):#REBEL HOUSE
        super().__init__()
        self.data=["/========\\",
                   "{  /     |",
                   "|ѳ/| |  ϫ|",
                   "| \\|ѳ|= =|",
                   "|  ѳ |   }",
                   "\\========/"]#ꙮꬽ
    
     
class miniMap2(Map):
    def __init__(self, ):#ANCIENT RUIN
        super().__init__()
        self.data=["|==========\\",
                   "[ %        #|",
                   "|==   =     |       /======",
                   "|  \\|◊|  |= |       |      ]",
                   "|#       |ﬦ |      |   ====", 
                   "|====Π==============  ==|",
                   "\\     ====            □|",
                   " ===\\        == =  ====/",
                   "     \\=====\\     ᴥ====/",
                   "            \\=====/      "]
        #V is a door. 
    
class miniMap3(Map):
    def __init__(self, ):#CAVE TROLL
        super().__init__()
        self.data=["ꙮꙮꙮ  ꙮꙮꙮ  ꙮꙮꙮ      ",
                   "[   ꙮꙮ  ꙮꙮꙮꙮ ꙮꙮꙮꙮ ꙮꙮꙮ ",
                   "ꙮ  ϫꙮ    ꬽ  ꙮ   ꙮꙮꙮ   ꙮ",
                   "ꙮ  ꙮ ꙮ   ꙮ    ꙮ       ꙮ",
                   "ꙮ ꬽ ꙮ   ꙮ    ꙮ   ꙮ ꙮꙮ",
                   "ꙮꙮ      ꙮ    ꙮ  ꙮ  ]",
                   " ꙮꙮꙮ     ꙮ  ꙮ   ꙮꙮꙮ",
                   "    ꙮꙮꙮ ꙮ       ꙮꙮ",
                   "       ꙮꙮꙮꙮꙮꙮꙮꙮꙮ"]#ꙮꬽꬽꬲꬾ
    
class miniMap4(Map):
    def __init__(self, ):#DRAGON CVAE
        super().__init__()
        self.data=["ꙮꙮꙮ  ꙮꙮꙮ  ꙮꙮꙮ    ꙮꙮ  ",
                   "[   ꙮꙮ  ꙮꙮꙮꙮ ꙮꙮꙮꙮ ꙮꙮꙮ ",
                   "ꙮ  ϫꙮ    ꬽ  ꙮ   ꙮꙮ     ꙮ",
                   "ꙮ  ꙮꙮ                  ꙮ",
                   "ꙮ ꬽ   ꙮ          ꙮ  ꙮꙮ",
                   "ꙮꙮꙮꙮ       ꙮ     ꙮ  ]",
                   " ꙮ ꙮꙮ       ꙮꙮ  ꙮꙮꙮ",
                   "    ꙮꙮꙮ ꙮ  ꙮ  ꙮꙮ ꙮꙮ",
                   "       ꙮꙮꙮꙮꙮ   "]#ꙮꬽꬽꬲꬾ

class miniMap5(Map):
    def __init__(self, ):#Bridge to the castle of morceris
        super().__init__()
        self.data=["#######.##",
                   "##ꙮ ...  #  ",
                   "+˄=˄=˄=˄=˄=˄\\|",
                   "[            ₪",
                   "+˅=˅=˅=˅=˅=˅/|",
                   "ꙮ## . ## #",
                   "#####..###"]
                   
                   

                   
class miniMap5a(Map):
    def __init__(self, ):#Morceris Castle
        super().__init__()
        self.data=["##ꙮꙮꙮ  ##     ",
                   "ꙮꙮꙮ  #####...   ",
                   "ꙮꙮ<==˄==˄===",
                   "ꙮ=/          \\",
                   "˄| + + + +|   \\>    ",
                   "₪ §       MꙈ Ѻ}>   ",
                   "˅| + + + +|   />    ",
                   "ꙮ=\\          /",
                   "ꙮꙮ<==˅==˅==="]


# Move the portal to moveRight
# Move door to move right
# Move text to moveRight



###############################
#           #####             #
#         INVENTORY           #
#           #####             #
###############################


class Inventory:#all self.inv used to be self.stuff
    def __init__(self):
        self.inv=["Iron Sword", "Hunting Bow", "Hunting Knife", "Iron Shield"]#player starts with  a bow and sword

    def store(self, item):
        self.inv.append(item) #Stores an item in Inventory by adding it to self.stuff
        
    def display(self):
        print("ITEMS: %s"%(self.inv)) #shows the inventory in the game. the inventory will display more items as the player collects them

    def checkItem(Inventory, item):
        x=0
        while x<len(Inventory):
        
            if Inventory[x]==item:
                return True 
            else:
                pass
            
            
            x=x+1
        return False

#add shops and merchants: work on buying first: work on subtracting things from inventroy (this will be difficult
#-----Got this to work a different way
#-----Need to add 10 Merchants: (3) per island and each needs to have a new item that the other one didn't
#------So 6 or 10 different types of MERCHANTS
#1 hp,mag, arrows, stam
#2 hp, mag, arrows, stam,
#3 hp, mag, arrows, stam, scroll of inferno
#4 hp, mag, arrows, stam, scroll of healing
#5 hp, mag, arrows, stam, scroll of blizzard
#6 hp, mag, arrows, stam, scroll of inferno, scroll of blizzard
#7 hp, mag, arrows, stam, Souls
#8 hp, mag, arrows, stam, umbra arrows
#9 hp, mag, arrows, stam, scroll of the thunder, umbra arrows
#10 hp, mag, arrows, stam, 

#THE MOUNTAINS ON EITHER SIDE SCRAPE THE SKIES ABOVE YOU AND ARE ALMOST ENTIRELY COVERED IN SNOW.")
            #input("THE COLD, MOUNTAIN AIR BLOWS SNOW INTO THE BACK OF YOUR NECK, SENDING SHIVERS DOWN YOUR SPINE.") 
            #input("THE COLD WIND CONTINUES FOR MANY MILES UNTIL ")
