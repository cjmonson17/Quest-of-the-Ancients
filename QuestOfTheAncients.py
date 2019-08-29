#Action/Adventure RPG
mapA='''
^^^^^^^^^^^^^^^^^^{Kingdom of Hjaron}^^^^^^^^^^^^^^^
====================================================                {LEGEND}",
|........##############...####............####.....|  Ꙙ=Player,           Ѯ=Serpent",
|...########   #  #### ##########.......### ◊ ###..|  1=Mission One       0=Serpent Egg",
|..#  1 ##  ɷ  Ω  ### Ḯ   ##꙲###.......####   ##..|  Ω=Mission Two        ꙲=Ancient Ruins",
|..###  ɷ ###  #  ###    #.............#####₪####..|  Ψ=Mission Three     Ꚛ=The Guard ",
|...##   ## ᴥ     Ψ  ɷ    ##...0......##      ᴥ#...|  Ξ=Mission Four      ȣ=Guard Decision",
|..##       #  ######### ##..........#   ɷ    Ḯ##..|  Φ=Side Mission      Ꙛ=Morceris",
|...##!##Ḯɷ ####      ꙰...#........##  ##ȣ#####...|  Σ=Mission Five,      ◊=Morceris Decision",
|...## ########## ##########.......#####   ###.....|  ₪=Morceris's Castle  ᴥ=Magic Potion",
|...####      ɷ  Ḯ  # ## ɷ##.......#    #Σ#  ###...|  !=Bandit Gate        ɷ=Health Potion", 
|.......#Ξ#        ᴥ   #    #.....##           ##..|  ѧ=Bandit Camp       Ḯ=Arrows",
|...#####҉######  ##  ##### #### ###            #..|  ꙰=Cave              #=Poison Trees",      
|....#.....### ### ######       Φ           ####...|  ¤=Cave Troll         .=Water",  
|...#..... ....ᴥ     ɷ    Ḯ   ##########.##........|  ҉=Dragon Cave",   
|...##############################.................|  ṽ=Drago,  
|....####......##########.....###..................|               
==================================================== 
++++++++++++++++++++++{Hjaron}++++++++++++++++++++++'''




##############################
#INITIAL GAME
##############################

my_string2=[" _______  _______  _______  _______  _______  _        _______  _______  _______  ______   _______ ",
            "(       )(  ___  )(  ____ )(  ____ \(  ____ \( (    /|(  ____ \(  ___  )(  ____ )(  __  \ (  ____ \\",
            "| () () || (   ) || (    )|| (    \/| (    \/|  \  ( || (    \/| (   ) || (    )|| (  \  )| (    \/",
            "| || || || |   | || (____)|| |      | (__    |   \ | || |      | (___) || (____)|| |   ) || (__    ",
            "| |(_)| || |   | ||     __)| |      |  __)   | (\ \) || | ____ |  ___  ||     __)| |   | ||  __)   ",
            "| |   | || |   | || (\ (   | |      | (      | | \   || | \_  )| (   ) || (\ (   | |   ) || (      ",
            "| )   ( || (___) || ) \ \__| (____/\| (____/\| )  \  || (___) || )   ( || ) \ \__| (__/  )| (____/\\",
            "|/     \|(_______)|/   \__/(_______/(_______/|/    )_)(_______)|/     \||/   \__/(______/ (_______/"]
        

#print(my_string2)
#############THINGS TO ADD AND IMPROVE################
    #ADD MORE LOCATIONS TO MAP
        #MORCENGARDE
        #WINTERFELL
        #MORZANA
        #SHADOVAR
    #ADD MORE ENEMIES
        #DARK ELVES: lightning arrow, poison dagger, whirlwind fury
        #ELECTRO: lightning storm( chain lightning(always does damage, less if player dodges it), electro claw, breath of electricity
        #AND FROST DRAGONS: Blizzard(decrease dmamge with increased radius, ice claw, frost bite
        #ADD stamina: if stamina>0, yada yada. stamina=0 cant use sword =)
        #TREE CREATURES: poison, absorb health?, 
        #DALTHUUR: rasies undead skeletons(high chance), raises undead cavetroll (med chance), raises undead dragon(very low chance), 
        #SHANZALAR: switch with morceris: poison, illusion(makes player attack himself/followers), absorb health
        #GOBLIN: steals arrows from inventory, poison dagger, throwing knives
        #Ghost of the tomb: Fires of Morcengarde, ethereal(player cant damage him, if ghost attack==ethereal, player's attack does nothing), possession[player attacks himself]
    ##ADD ALLIES: rebel and spared guard
    ##ADD FOLLOWERS THAT ATTACK IN BATTLE
    #ADD MORE TOWNS AND USE A NEW ICON
        #CAPITOL CITIES
        #SMALL TOWNS
    #CHANGE THE PLAYER SYMBOL TO SOMETHING MORE NOTICEABLE :)
    #make code so that player can choose their race/class.
        #p=input("CHOOSE A CLASS: 'o'=orc, 'd'=dark elf, 'h'=human, etc.
        #if p=='o':
            #max health=10
            #max magik=10
###############IMPORTANT CODE##########
#NEED TO:
    #CREATE A WAY TO RESPAWN IF PLAYER DIES :) I DID IT!!! all on my phone during a hike
    #CREATE A WAY FOR THE NEW ITEMS TO DEAL DAMAGE :) I GOT IT. thought of the idea on a hike
    #CREATE A WAY TO HAVE COMPANIONS JOIN YOU. :( have not tried. no ideas. not as necessary/dont think it would work well
    #CREATE A WAY TO MAKE MAPS FOR TOWNS AND HAVE THEM APPEAR INSTEAD OF THE MAIN MAP :( working on it, but not much progress
        ##ONCE WE DO THIS, WE CAN ADD MORE SIDE MISSIONS, AND FAST TRAVEL TO AND FROM OTHER TOWNS
        ##CREATE NAMES FOR THE TOWNS AND ADD THINGS LIKE: ENTERING ---- TOWN
    #CREATE A WAY TO BUY THINGS FROM A MERCHANT :) did it
    #CREATE A WAY TO HAVE ARMOR AND RESISTANCES
        #STILL NOT SURE HOW TO DO, TRY TO FIGURE IT OUT AFTER TOWNS ARE MADE.

'''#MAKE SURE TO CHANGE THE MISSIONS FROM BEING WALK THROUGH ABLE TO SOLID WHEN WE ARE ACTUALLY DONE WITH THE GAME'''
import random
import time

##########IMPORT MAP AND INVENTORY#
from MapInv import *              #
###################################


#########
#Defining combative classes
#########
class Entity:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,Map):
        pass
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getSymbol(self):
        return self.symbol
    def applyAttack(self,damage):
        '''to recieve damage from another entity'''
        self.hp=self.hp-damage
        if damage>0:
            True #hit
        else:
            False #miss
        return
    def isAlive(self):
        '''keeps track of whether entity is alive'''
                                                
        if self.hp>0:
            return True
        else:
            return False

##################################player class
          
class Player(Entity):
    def __init__(self,x,y):
        super().__init__(x,y) 
        self.inv=Inventory()#used to be self.inv=
        name=input("Enter your name: ")
        if name == "":
            name = "Prisoner"
        self.x=x
        self.y=y
        self.story=20
        self.lydiaStory = 1
        self.symbol='Ꙙ'
        self.name = name
        self.lives = 100
        self.quick=0
        if self.quick>4:
            self.quicks='   SPECIAL ATTACK [x]:'
        if self.quick<5:
            self.quicks=':'
        self.moral=0
        self.mine=0
        if self.x>1 and self.x<51 and self.y>1 and self.y<17:
            self.island='Amodera'
        if self.x>57  and self.x<100 and self.y>1 and self.y<22:
            self.island='Morcengarde'
        if self.x>4  and self.x<92 and self.y>19 and self.y<31:
            self.island='Shadovar'
        #else:
            #print("IN BETWEEN ISLANDS")
        if self.moral==0: #make different classes of good and evil, change neutral to mysterious, unknown, nameless, secret, unsung
            self.morals=''
            
            #good
        if self.moral==1:
            self.morals='the Defender'
        if self.moral==2:
            self.morals='the Guardian'
        if self.moral==3:
            self.morals='the Savior'
        if self.moral==4:
            self.morals='the Hero'
        if self.moral==5:
            self.morals='the Morzana'
            
            #evil
        if self.moral==-1:
            self.morals='the Corrupt'
        if self.moral==-2:
            self.morals='the Soulless'
        if self.moral==-3:
            self.morals='the Betrayer'
        if self.moral==-4:
            self.morals='the Damned'
        if self.moral==-5:
            self.morals='the Morthuurzar'
        ###HEALTH, MAGIK, STAMINA, ARROWS, GOLD
        self.maxmagik=20
        self.magik=self.maxmagik
        self.maxhp=25 #10
        self.hp=self.maxhp
        self.maxstam=20 #10
        self.stam=self.maxstam
        self.maxarrows=20 #10
        self.arrows=20
        self.gold=500
        self.maxgold=500
        ###COMBAT POTIONS
        ##health potion
        self.hpotion=0
        self.hpotionCount=0
        self.maxhpotion=3
        self.mpotionCount=0
        self.mpotion=0
        self.maxmpotion=3
        ######SMITH AND STUFF THAT NEEDS REPAIR
        self.maxsword=10 #fiire and normal
        self.sword=5
        self.bow=7
        self.maxbow=20#triple shot and normal
        #self.shield=5
        #self.maxshield=10
        
        #UNLOCKABLE SPELLS
        
        #SPELLS
        self.fire=1
        if self.fire==0:
            self.fires='<LOCKED>'
            self.firess='<LOCKED>'
        if self.fire>0:
            self.fires='Fireball {-5mag}'
            self.firess='Fireball'
        self.heal=1
        if self.heal==0:
            self.heals='<LOCKED>'
            self.healss='<LOCKED>'
        if self.heal>0:
            self.heals='Healing Spell {-3mag}'
            self.healss='Healing Spell'
        self.snow=1
        if self.snow==0:
            self.snows='<LOCKED>'
            self.snowss='<LOCKED>'
        if self.snow>0:
            self.snows='Snow Storm {-5mag}'
            self.snowss='Snow Storm'
        self.lightning=1
        if self.lightning==0:
            self.lightnings='<LOCKED>'
            self.lightningss='<LOCKED>'
        if self.lightning>0:
            self.lightnings='Chain Lightning {-5mag}'
            self.lightningss='Chain Lightning'
        self.mystic=1
        if self.mystic==0:
            self.mystics='<LOCKED>'
            self.mysticss='<LOCKED>'
        if self.mystic>0:
            self.mystics='Mystic Arrow {-1mag}'
            self.mysticss='Mystic Arrow'
            
        #HEAVY SPELLS
        self.iBlast=1
        if self.iBlast==0:
            self.iBlasts='<LOCKED>'
            self.iBlastss='<LOCKED>'
        if self.iBlast>0:
            self.iBlasts='Ice Blast {-10mag}'
            self.iBlastss='Ice Blast'
        self.fBlast=1
        if self.fBlast==0:
            self.fBlasts='<LOCKED>'
            self.fBlastss='<LOCKED>'
        if self.fBlast>0:
            self.fBlasts='Fire Blast {-10mag}'
            self.fBlastss='Fire Blast'
        self.tBlast=1
        if self.tBlast==0:
            self.tBlasts='<LOCKED>'
            self.tBlastss='<LOCKED>'
        if self.tBlast>0:
            self.tBlasts='Thunderbolt {-10mag}'
            self.tBlastss='Thunderbolt'
            
        #ABILITIES
        self.fSword=1
        if self.fSword==0:
            self.fSwords='<LOCKED>'
            self.fSwordss='<LOCKED>'
        if self.fSword>0:
            self.fSwords='Flame Sword {-5mag, -5stam}'
            self.fSwordss='Flame Sword'
        self.tArrow=1
        if self.tArrow==0:
            self.tArrows='<LOCKED>'
            self.tArrowss='<LOCKED>'
        if self.tArrow>0:
            self.tArrows='Triple Arrows {-3arrows}'
            self.tArrowss='Triple Arrows'


#SCROLLS>     {Tidal Wave: 0/5 Scrolls} {Maximum Healing: 0/5 Scrolls}   {Blizzard: 0/5 Scrolls}   {Thunderstorm: 0/5 Scrolls}
 
#ARTIFACTS OF POWER>  {ShadowBow: 0/20 Umbra Arrows}   {Mask of Morzana: 0/5 Souls}   {Morceris's Staff: 0/10 Energy}   {Dalthuur's Cloak: 0/6 Energy}
                     #{Shanzalar's Staff: 0/1 Energy}


            ######SPECIAL ATTACKS
        
        #SPECIAL WEAPONS
        self.morc=0
        self.maxmorc=10 #absorb the life of 5 enemies or summon 2 flaming cobras
        self.dalthuur=0
        self.maxdalthuur=6 #summon an undead army 6 times or an undead dragon 2 times
        self.shan=0
        self.maxshan=1 # create the maelstrom that destroys anything in its path 1 use
        self.umbra=0
        self.maxumbra=20 # creates shadow arrows. can be collected agiain if you kill another dark elf
        self.morzana=0
        self.maxmorzana=5 # creates the fire of morzana
        #UPGRADES
        self.Morc=0
        '''
        if self.Morc==0:
            self.Morcs='<LOCKED>'
            self.Morcss='<LOCKED>'##do this for all scrolls and special weapons
        if self.Morc>0:
            self.Morcs="Morceris's Staff"
            self.Morcss=" {Morceris's Staff: %d/10 Energy}"%(self.morc) ##do this for all scrolls and special weapons
        '''  
        self.Dalthuur=0
        '''
        if self.Dalthuur==0:
            self.Dalthuurs='<LOCKED>'
            self.Dalthuurss='<LOCKED>'##do this for all scrolls and special weapons
        if self.Dalthuur>0:
            self.Dalthuurs="Dalthuur's Cloak"
            self.Dalthuurss=" {Dalthuur's Cloak: %d/6 Energy}"%(self.dalthuur) ##do this for all scrolls and special weapons
          '''  
        self.Shan=0
        '''
        if self.Shan==0:
            self.Shans='<LOCKED>'
            self.Shanss='<LOCKED>'##do this for all scrolls and special weapons
        if self.Shan>0:
            self.Shans="Shanzalar's Staff"
            self.Shanss=" {Shanzalar's Staff: %d/1 Energy}"%(self.shan) ##do this for all scrolls and special weapons
'''
        self.Umbra=0
        '''
        if self.Umbra==0:
            self.Umbras='<LOCKED>'
            self.Umbrass='<LOCKED>'##do this for all scrolls and special weapons
        if self.Umbra>0:
            self.Umbras="Shadowbow {-1 Umbra Arrow}"
            self.Umbrass=" {Shadowbow: %d/20 Umbra Arrows}"%(self.umbra) ##do this for all scrolls and special weapons
'''
        self.Morz=0
        '''
        if self.Morz==0:
            self.Morzs='<LOCKED>'
            self.Morzss='<LOCKED>'##do this for all scrolls and special weapons
        if self.Morz>0:
            self.Morzs="Mask of Morzana {-5souls}"
            self.Morzss=" {Mask of Morzana: %d/5 Souls}"%(self.morzana) ##do this for all scrolls and special weapons
        
        '''
        #SCROLLS
        self.inferno=0
        self.maxinferno=5
        self.wave=0
        self.maxwave=5
        self.ultimhp=0
        self.maxultimhp=5
        self.blizzard=0
        self.maxblizzard=5
        self.thunder=0
        self.maxthunder=5
        #SCROLLS
        self.Inferno=0
        self.Wave=0
        self.Ultimhp=0
        self.Blizzard=0
        self.Thunder=0
        

        #SPECIAL WEAPONS:
        
            
        #WEAPONS
        self.iSword=1
        self.iArrows=1

        ###UPGRADES and LEVELS
        self.perks=10
        #Spells
        self.fireBallLvl=1
        self.snowStormLvl=1
        self.cLightLvl=1
        self.healLvl=1
        self.mArrowsLvl=1
        #Weapons
        self.iSwordLvl=1
        self.iArrowsLvl=1
        self.fSwordLvl=1
        self.tArrowLvl=1
        #Heavy spells
        self.fBlastLvl=1
        self.iBlastLvl=1
        self.tBlastLvl=1

        ##RINGS
        self.ring1=0
        self.ring2=0
        self.ring3=0
        
        
    def checkItem(Inventory, item): ##this thing not working. tried moving it here
        x=0
        while x<len(Inventory):
        
            if Inventory[x]==item:
                return True 
            else:
                pass
            
            x=x+1
        return False
    def receiveItem(self,loot):
        a=input("MISSION COMPLETE: Do you want %s?  [yes or no]:  "%loot)
        if a=="yes":
            self.inv.store(loot)
             #if an item is the loot, then hp and magik and arrows increase
            #########################AMODERA###############
            if loot=="Bandit's Quiver":
                print("--Max arrow storage raised to 20 arrows")
                self.maxarrows=20
                self.arrows=self.maxarrows
            if loot=="Steel Armor Set":
                print("--Max health raised to 20 hp")
                self.maxhp=20
                self.hp=self.hp
            if loot=="Armor of the Destroyer":
                print("--Max health raised to 25 hp")
                self.maxhp=25
                self.hp=self.maxhp
                self.maxstam=20
                self.stam=self.maxstam
                self.mine=1
            
            if loot=="Scroll of the Inferno":
                print("--Max magik raised to 25 magik")
                print("++5 Inferno Scrolls added")
                self.maxmagik=30
                self.magik=self.magik
                self.Inferno=1
                self.inferno=self.maxinferno
            
            if loot=="Scroll of the Tide":
                print("--Max health raised to 40 hp")
                print("++5 Tidal Wave Scrolls added")
                self.maxhp=35
                self.hp=self.hp
                self.Wave=1
                self.wave=self.maxwave
            if loot=="Mask of Morzana": #special weapon
                print("--Max magik raised to 50 magik")
                print("--Max health raised to 45 hp")
                print("--Max stamina raised to 30 stamina")
                print("COLLECT 5 SOULS TO USE")
                self.maxmagik=50
                self.maxhp=45
                self.maxstam=30
                self.Morz=1
                self.morzana=self.morzana
                #print(self.Morz)
            if loot=="Helm of the Corrupted":
                print("--Max health raised to 45 hp")
                print("--Max stamina  raised to 40 stamina")
                self.maxstam=40
                self.stam=self.stam
                self.maxhp=45
                self.hp=self.hp
            if loot=="The Staff of Morceris": #special weapon (might add a light ending weapon as well to balance this)
                print("--Max health raised to 55 hp")
                print("--Max magik raised to 55")
                print("--Max stamina raised to 45")
                print("You can absorb the life of 5 enemies or summon a flaming cobra 2 times")
                self.morc=self.maxmorc
                self.Morc=1
                self.maxhp=55
                self.maxmagik=55          
                self.maxstam=45
                ################MORCENGARDE
            if loot=="Heart of the Forest":
                print("++5 Scrolls of Maximum Healing added")
                self.Ultimhp=1
                self.ultimhp=self.maxultimhp
                
            if loot=="Goblin's Bag of Gold":
                print("--Max gold storage raised to 2000")
                self.maxgold=2000
                self.gold=500
            
            
            if loot=="Scroll of the Blizzard":
                print("--Max magik raised to 60")
                self.maxmagik=60
                print("++5 Scrolls of the Blizzard added")
                self.Blizzard=1
                self.blizzard=self.maxblizzard
            if loot=="Chestplate of the Revenant":
                print("--Max Stamina raised to 50")
                print("--Max Health raised to 60")
                self.maxhp=60
                self.maxstam=50
                
            if loot=="The Cloak of Dalthuur": #special weapon
                print("You can ressurect an undead army 3 times or an undead dragon 1 time")
                print("Max magik raised to 70")
                self.Dalthuur=1
                self.dalthuur=maxdalthuur #self.A-1 #self.D-3
                self.maxmagik=70

                #################SHADOVAR################
            if loot=="Pelt of the Hoarfrost":
                print("--Max Stamina raised to 55")
                self.maxstam=55

            if loot=="Shadowbow of the Umbra":###
                print("Shadowbow added")
                print("++10 Umbra arrows added")
                self.Umbra=1
                self.umbra=10
                self.maxbow=30
            if loot=="Umbra Arrows":
                print("++5 Umbra arrows added")
                
                self.umbra=self.umbra+5
                if self.umbra>self.maxumbra:
                    self.umbra=self.maxumbra
            if loot=="Scroll of the Thunderstorm":
                print("++5 Scrolls of the Thunderstorm added")
                self.Thunder=1
                self.thunder=self.maxthunder
                
            if loot=="Goblin King's Hoard of Gold":
                print("--Max gold storage raised to 5000")
                print("--Gold=2000")
                self.maxgold=5000
                
                self.gold=2000
            #add loot from new enemies
            if loot=="Ring of the Firestorm":
                print("--Max Health raised to 70")
                print("++3 Scrolls of the Inferno")
                self.ring1=1
                self.inferno=self.inferno+3
                if self.inferno>5:
                    self.inferno=5
                self.maxhp=70
            if loot=="Ring of the Snowstorm":
                print("--Max Stamina raised to 60")
                print("++3 Scrolls of the Blizzard")
                self.ring2=1
                self.maxstam=60
                self.blizzard=self.blizzard+3
                if self.blizzard>5:
                    self.blizzard=5
            if loot=="Ring of the Maelstrom":
                print("--Max Stamina raised to 60")
                print("++3 Scrolls of the Thunderstorm")
                self.ring3=1
                self.maxmagik=80
                self.thunder=self.thunder+3
                if self.thunder>5:
                    self.thunder=5
            
                
            if loot=="The Staff of Shanzalar":#################special weapon
                print("You can create a maelstrom that will destroy anything in your path.")
                self.Shan=1
                self.shan=self.maxshan
                ###########################PLAYER CAN CHOOSE WHETHER THEY WANT THE ITEM##########################
            
        else:
            pass
        
    
    def getAttack(self):
        '''to give damage to another entity'''
        if self.quick>4:
            self.quicks='<<SPECIAL ATTACK>> [x]:'
        if self.quick<5:
            self.quicks=':'
        print("-<>-HEALTH: %d"%(self.hp), "  MAGIK: %d"%(self.magik), "  STAMINA: %d"%(self.stam) , "  QUIVER: %d"%(self.arrows), " POWER-UP: %d/5"%(self.quick)) 
        i=input("Potions [q]   Spells [s]   Weapon [w]   Heavy Attacks [e]   Special Scrolls [d]  Special Weapon [a]%s  "%(self.quicks))#input from player to attack
        q=random.randint(1,2)
        if i=='x' and self.quick>4:
            if self.quick>5:
                self.quick = 5
            n=input("Type 'a': ")
            if n=='a':
                print("yay")
                y=1
            else:
                y=0
                print("nah")
            n=input("Type 's': ")
            if n=='s':
                print("yes")
                z=2
            else:
                z=0
                print("nope")
            n=input("Type 'e': ")
            if n=='e':
                print("yes")
                t=3
            else:
                t=0
                print("nope")
            n=input("Type 'y': ")
            if n=='y':
                print("yes")
                p=3
            else:
                p=0
                print("nope")
            n=input("Type 'o': ")
            if n=='o':
                print("yes")
                o=3
            else:
                o=0
                print("nope")
            x=y+z+t+p+o
            self.quick=0
        elif i=='x' and self.quick<5:
            x=0
            print("ATTACK FAILED")
        elif i=="q":
            n=input("press: 1) Use Health Potion {+10 Health, +10 Stamina}   2) Use Magik Potion {+10 Magik}: ")
            #n=int(n)
            if n=='1':
                if self.hpotion>0:
                    self.hp=self.hp+10
                    self.stam=self.stam+10
                    print("YOU USED 1 HEALTH POTION")
                    print("Your health potion gave you +10 Health and +10 Stamina")
                          
                    if self.hp>self.maxhp:
                        self.hp=self.maxhp
                    if self.stam>self.maxstam:
                        self.stam=self.maxstam
                    self.hpotion=self.hpotion-1
                    x=0
                else:
                    print("**----OUT OF HEALTH POTIONS!----**")
                    x=0
            elif n=='2':
                if self.mpotion>0:
                    self.magik=self.magik+10
                    
                    print("YOU USED 1 MAGIK POTION")
                    print("Your magik potion gave you +10 Magik")
                          
                    if self.magik>self.maxmagik:
                        self.magik=self.maxmagik
                    
                    self.mpotion=self.mpotion-1
                    x=0
                else:
                    print("**----OUT OF MAGIK POTIONS!----**")
                    x=0
            else:
                print("YOU REACH FOR A POTION YOU DO NOT HAVE AND GIVE THE ENEMY A CHANCE TO ATTACK")
                #print("YOU LOST 3 HEALTH")
                #self.hp=self.hp-3
                x=0
            
        elif i=="s": #spells
            n=input("press: 1)Fireball{-5mag}   2) %s   3) %s   4) %s   5) %s:  "%(self.snows,self.lightnings,self.heals,self.mystics))
            #n=int(n)
            r=random.randint(1,4)
            
                
            if n=='1':#fireball: does a lot if it hits, but none if it misses
                
                if self.magik>4:
                
                    if r<4:
                        
                        self.magik=self.magik-5
                        print("Your Fireball hits target")
                        print("YOU USED 5 MAGIK")
                        self.quick=self.quick+1
                        if self.fireBallLvl==1:
                            x=5
                        if self.fireBallLvl==2:
                            x=10
                        if self.fireBallLvl==3:
                            x=13
                            
                    if r==4:
                        
                      
                        self.magik=self.magik-5
                        print("Your Fireball misses")
                        print("YOU USED 5 MAGIK")
                        x=0
                    
                else:
                    print("**----NOT ENOUGH MAGIK!----**")
                    x=0
            elif n=='2':#snow: always hits but does little damage
                if self.snow==1:
                    self.quick=self.quick+1
                    if self.magik>4:
                
                        if r<4:
                        
                            self.magik=self.magik-5
                            print("Snow and Ice rain down from the sky, freezing everything in their path")
                            print("YOU USED 5 MAGIK")
                            if self.snowStormLvl==1:
                                x=3
                            if self.snowStormLvl==2:
                                x=5
                            if self.snowStormLvl==3:
                                x=7
                                
                        if r==4:
                        
                      
                            self.magik=self.magik-5
                            print("Snow and Ice rain down from the sky, freezing everything in their path")
                            print("YOU USED 5 MAGIK")
                            
                            if self.snowStormLvl==1:
                                x=3
                            if self.snowStormLvl==2:
                                x=5
                            if self.snowStormLvl==3:
                                x=7
                    
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        x=0
                else:
                    print("SPELL LOCKED!!")
                    x=0
            elif n=='3':#lightning: chain effects
                if self.lightning==1:
                    self.quick=self.quick+1
                    if self.magik>4:
                
                        if r==1:
                        
                            self.magik=self.magik-5
                            print("Lightning scatters in every direction; nearly every bolt hits the enemy")
                            print("YOU USED 5 MAGIK")
                            if self.cLightLvl==1:
                                x=5
                            if self.cLightLvl==2:
                                x=7
                            if self.cLightLvl==3:
                                x=10
                            
                            
                        if r==2 or r==3:
                                         
                            self.magik=self.magik-5
                            print("Lightning scatters in every direction; many bolts hit the enemy")
                            print("YOU USED 5 MAGIK")
                            if self.cLightLvl==1:
                                x=3
                            if self.cLightLvl==2:
                                x=5
                            if self.cLightLvl==3:
                                x=7
                            
                        if r==4:
                            self.magik=self.magik-5
                            print("Lightning scatters in every direction; but only a few bolts hit the enemy")
                            print("YOU USED 5 MAGIK")
                            if self.cLightLvl==1:
                                x=1
                            if self.cLightLvl==2:
                                x=3
                            if self.cLightLvl==3:
                                x=5
                        
                    
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        x=0
                else:
                    print("SPELL LOCKED")
                    x=0
                
            elif n=='4':#Healing Spell
                if self.heal==1:
                    if self.magik>2:
                        self.magik=self.magik-3
                        if self.healLvl==1:
                            self.hp=self.hp+5
                            self.stam=self.stam+5

                        if self.healLvl==2:
                            self.hp=self.hp+7
                            self.stam=self.stam+7

                        if self.healLvl==3:
                            self.hp=self.hp+10
                            self.stam=self.stam+10

                            
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        if self.stam>self.maxstam:
                            self.stam=self.maxstam
                        print("Your healing spell healed your wounds and revitalized you: [+5 health, +5 stamina]")
                        print("YOU USED 3 MAGIK")
                        x=0
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        self.hp=self.hp+0
                        x=0
                else:
                    print("SPELL LOCKED!!")
                    x=0
            elif n=='5':#Mystic Arrow: does very little damage and costs 1 magik
                if self.mystic==1:
                    if self.magik>0:
                
                        if r<4:
                        
                            self.magik=self.magik-1
                            print("Your Mystic Arrow hits its target")
                            print("YOU USED 1 MAGIK")
                            if self.mArrowsLvl==1:
                                x=2
                            if self.mArrowsLvl==2:
                                x=3
                            if self.mArrowsLvl==3:
                                x=5                    

                            
                            
                        if r==4:
                        
                      
                            self.magik=self.magik-1
                            print("Your Mystic Arrow misses")
                            print("YOU USED 1 MAGIK")
                            x=0
                    
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        x=0
       
                    #else:
                        #print("YOU TRY TO PERFORM A SPELL THAT DOES NOT EXIST AND WASTE AN ATTACK.")
                        #x=0
                if self.mystic==0:
                    print("SPELL LOCKED!!")
                    x=0
            else:
                print("YOU TRY TO PERFORM AN ATTACK THAT YOU DONT KNOW AND WASTE AN ATTACK.")
                x=0
            
        
                
        elif i=="w": #weapon
            w=input("press: 1) Shoot Arrow 2) Swing Sword{-4stm}  3) Use Hunting Knife{-1stm}:  ")
            #w=int(w)
            
            if w=='1':#Bow and arrow
                r=random.randint(1,7)
                if self.arrows>0 and self.bow>0:
                    self.quick=self.quick+1
                    if r<6:
                        y=random.randint(1,3)
                        if y==1:
                            self.arrows=self.arrows-1
                            self.bow=self.bow-1
                            print("[CRITICAL HIT] Your arrow hits the enemy in the head")
                            print("YOU USED: 1 ARROW")
                            if self.iArrowsLvl==1:
                                x=5
                            if self.iArrowsLvl==2:
                                x=7
                            if self.iArrowsLvl==3:
                                x=10          
                            
                        if y==2:
                            self.arrows=self.arrows-1
                            self.bow=self.bow-1
                            print("[CRITICAL HIT] Your arrow hits the enemy in the stomach")
                            print("YOU USED: 1 ARROW")
                            if self.iArrowsLvl==1:
                                x=2
                            if self.iArrowsLvl==2:
                                x=4
                            if self.iArrowsLvl==3:
                                x=6      
                            #x=4
                        if y==3:
                            self.arrows=self.arrows-1
                            self.bow=self.bow-1
                            print("Your arrow hits the enemy in the leg")
                            print("YOU USED: 1 ARROW")
                            if self.iArrowsLvl==1:
                                x=1
                            if self.iArrowsLvl==2:
                                x=3
                            if self.iArrowsLvl==3:
                                x=4      
                            #x=3
                    if r>5:
                        self.arrows=self.arrows-1
                        print("Your arrow did not fly true and missed the enemy")
                        print("YOU USED: 1 ARROW")
                        x=0
                else:
                    print("**----QUIVER OUT OF ARROWS!----**")
                    x=0
            elif w=='2':# swing sword
                r=random.randint(1,3)
                if self.stam>3:
                    if self.sword>0:
                        if r<3:
                            self.quick=self.quick+1
                            self.stam=self.stam-4
                            
                            self.sword=self.sword-1
                            print("Your Sword slices through enemy's flesh")
                            print("YOU USED: 4 STAMINA")
                            if self.iSwordLvl==1:
                                x=3
                            if self.iSwordLvl==2:
                                x=5
                            if self.iSwordLvl==3:
                                x=7          
                            
                            if self.stam<0:
                                self.stam=0
                                
                            
                            
                        if r==3:
                            self.stam=self.stam-4
                            print("Enemy dodges Sword")
                            print("YOU USED: 4 STAMINA")
                            x=0
                            if self.stam<0:
                                self.stam=0
                    else:
                        print("**----SWORD IS BROKEN----**")
                        x=0
                else:
                    print("**----NOT ENOUGH STAMINA----**")
                    x=0
            elif w=='3':#Use hunting knife
                r=random.randint(1,7)
                if self.stam>0:
                    if r<7:
                        self.stam=self.stam-1
                        print("You use your hunting knife and stab your enemy's stomach")
                        print("YOU USED: 1 STAMINA")
                        x=2
                    if r>6:
                        self.stam=self.stam-1
                        print("You use your hunting knife but your enemy blocks it")
                        print("YOU USED: 1 STAMINA")
                        x=0
                else:
                    print("**----NOT ENOUGH STAMINA!----**")
                    x=0
    
            else:
                print("YOU REACH FOR A WEAPON YOU DONT HAVE AND WASTE AN ATTACK.")     
                x=0
                
        elif i=="e": #Heavy Attacks (magic and weapons)
            n=input("press: 1)%s   2)%s   3)%s  4)%s  5)%s :  "%(self.fBlasts,self.iBlasts,self.tBlasts,self.fSwords,self.tArrows))
            #n=int(n)
            r=random.randint(1,4)
            if n=='1':#fireball: does a lot if it hits, but none if it misses
                if self.fBlast==1:
                    
                    if self.magik>9:
                
                        if r<4:
                            self.quick=self.quick+1
                        
                            self.magik=self.magik-10
                            print("Your Fire Blast incinerates everything in its path")
                            print("YOU USED 10 MAGIK")
                            if self.fBlastLvl==1:
                                x=5
                            if self.fBlastLvl==2:
                                x=7
                            if self.fBlastLvl==3:
                                x=10
                            
                        if r==4:
                        
                      
                            self.magik=self.magik-10
                            print("Your Fire Blast incinerates everything in its path")
                            print("YOU USED 10 MAGIK")
                            if self.fBlastLvl==1:
                                x=5
                            if self.fBlastLvl==2:
                                x=7
                            if self.fBlastLvl==3:
                                x=10
                    
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        x=0
                else:
                    print("SPELL LOCKED!!")
                    x=0
            elif n=='2':#Ice Blast: does decreased damage at increased range
                if self.iBlast==1:
                    if self.magik>9:
                        self.quick=self.quick+1
                
                        if r==1:
                            
                        
                            self.magik=self.magik-10
                            print("Your Ice Blast sends Ice Spikes flying out ever direction. The enemy was in close proximity to you and was hit by many of them")
                            print("YOU USED 10 MAGIK")
                            if self.iBlastLvl==1:
                                x=5
                            if self.iBlastLvl==2:
                                x=7
                            if self.iBlastLvl==3:
                                x=10
                            
                            
                        if r==2 or r==4:
                        
                      
                            self.magik=self.magik-10
                            print("Your Ice Blast sends Ice Spikes flying out ever direction. The enemy was not too close and was not hit by many ice spikes")
                            print("YOU USED 10 MAGIK")
                            if self.iBlastLvl==1:
                                x=3
                            if self.iBlastLvl==2:
                                x=4
                            if self.iBlastLvl==3:
                                x=6
                            
                        if r==3:
                        
                      
                            self.magik=self.magik-10
                            print("Your Ice Blast sends Ice Spikes flying out ever direction. The enemy was far away and was only hit by a few ice spikes")
                            print("YOU USED 10 MAGIK")
                            if self.iBlastLvl==1:
                                x=1
                            if self.iBlastLvl==2:
                                x=2
                            if self.iBlastLvl==3:
                                x=3
                            
                    
                    else:
                        print("**----NOT ENOUGH MAGIK!----**")
                        x=0
                else:
                    print("SPELL LOCKED")
                    x=0
                    
            elif n=='3':#lightning: single hit
                if self.tBlast==1:
                    
                    if self.magik>9:
                
                        if r==1 or r==2:
                            self.quick=self.quick+1
                        
                            self.magik=self.magik-10
                            print("You cast a large thunderbolt from your hands, and it hits the enemy in the chest")
                            print("YOU USED 10 MAGIK")
                            if self.tBlastLvl==1:
                                x=7
                            if self.tBlastLvl==2:
                                x=10
                            if self.tBlastLvl==3:
                                x=15
                            
                            
                    
                        if r==3 or r==4:
                            self.magik=self.magik-10
                            print("You cast a large thunderbolt from your hands, but the enemy dodges it")
                            print("YOU USED 10 MAGIK")
                            x=0
                        
                    
                    else:
                        print("**----OUT OF MAGIK!----**")
                        x=0
                else:
                    print("SPELL LOCKED!!")
                    x=0
                
            elif n=='4':#Flame Sword: decreases magik and stamina
                if self.fSword==1:
                    if self.magik>4 and self.stam>4:
                        if r==1 or r==2:
                            self.quick=self.quick+1
                        
                            self.magik=self.magik-5           
                            self.stam=self.stam-5
                            print("You raise your sword and endue it with fire magic. You slice your enemy's chest and burn it")
                            print("YOU USED 5 MAGIK")
                            print("YOU USED 5 STAMINA")
                            if self.fSwordLvl==1:
                                x=6
                            if self.fSwordLvl==2:
                                x=8
                            if self.fSwordLvl==3:
                                x=12
                            
                            
                    
                        if r==3 or r==4:
                            self.magik=self.magik-5
                            self.stam=self.stam-5
                            print("You raise your sword and endue it with fire magic. The enemy dodges it but is still burned in the process")
                            print("YOU USED 5 MAGIK")
                            print("YOU USED 5 STAMINA")
                            if self.fSwordLvl==1:
                                x=2
                            if self.fSwordLvl==2:
                                x=3
                            if self.fSwordLvl==3:
                                x=5
                            
                    
                    
                    else:
                        print("**----NOT ENOUGH MAGIK and/or NOT ENOUGH STAMINA!----**")
                        self.hp=self.hp+0
                        x=0
                else:
                    print("SKILL NOT ACQUIRED!!")
            elif n=='5':#Triple Shot bow decreases arrows and stamina
                if self.tArrow==1:
                    
                    if self.arrows>2: #and self.bow>2:
                        self.quick=self.quick+1
                        if r==1:
                            self.bow=self.bow-3
                            self.arrows=self.arrows-3
                            print("You load three arrows onto your bow. All three arrows hit the enemy")
                            print("YOU USED 3 ARROWS")
                            if self.tArrowLvl==1:
                                x=6
                            if self.tArrowLvl==2:
                                x=9
                            if self.tArrowLvl==3:
                                x=12
                            
                            
                        if r==2:
                            self.bow=self.bow-3
                            self.arrows=self.arrows-3
                            print("You load three arrows onto your bow. Two arrows hit the enemy")
                            print("YOU USED 3 ARROWS")
                            if self.tArrowLvl==1:
                                x=4
                            if self.tArrowLvl==2:
                                x=6
                            if self.tArrowLvl==3:
                                x=8
                            
                            
                              
                        if r==3:
                            self.bow=self.bow-3
                            self.arrows=self.arrows-3
                            print("You load three arrows onto your bow. One arrow hits the enemy")
                            print("YOU USED 3 ARROWS")
                            if self.tArrowLvl==1:
                                x=2
                            if self.tArrowLvl==2:
                                x=3
                            if self.tArrowLvl==3:
                                x=4
                            
                            
                        if r==4:
                            self.bow=self.bow-3
                            self.arrows=self.arrows-3
                            print("You load three arrows onto your bow. The enemy dodges every arrow")
                            print("YOU USED 3 ARROWS")
                            x=0
                    
                   
                    else:
                        print("**----QUIVER OUT OF ARROWS!----**")
                        self.hp=self.hp+0
                        x=0
                else:
                    print("SKILL NOT ACQUIRED!!")
                    x=0
       
            else:
                print("YOU TRY TO PERFORM AN ATTACK THAT YOU DONT KNOW AND WASTE AN ATTACK.")
                x=0
        
        elif i=="d": #scrolls 
            d=input("press: 1)%s 2)%s 3)%s 4)%s 5)%s:  "%(self.Infernos,self.Waves,self.Ultimhps,self.Blizzards,self.Thunders))
            #d=int(d)
            r=random.randint(1,10)
            if d=='1':#INFERNO
                if self.inferno>0:
                    if r<10:
                        self.inferno=self.inferno-1
                        print("You create a raging inferno")
                        print("YOU USED: 1 Scroll")
                        x=10
                    if r==10:
                        self.inferno=self.inferno-1
                        print("You create a raging inferno but the enemy avoids it")
                        print("YOU USED: 1 Scroll")
                        x=0
                else:
                    print("**----YOU ARE OUT OF SCROLLS OF THE INFERNO!----**")
                    x=0
            elif d=='2':#TIDAL WAVE
                if self.wave>0:
                
                    if r<10:
                        self.wave=self.wave-1
                        print("You create a tidal wave of water")
                        print("YOU USED: 1 Scroll")
                        x=7
                    if r==10:
                        self.wave=self.wave-1
                        print("Enemy dodges tidal wave")
                        print("YOU USED: 1 Scroll")
                        x=0
                else:
                    print("**----YOU ARE OUT OF SCROLLS OF THE TIDE!----**")
                    x=0
        
            
            elif d=='3': #MAX HEALING
                if self.ultimhp>0:
                    if r<10:
                        self.ultimhp=self.ultimhp-1
                        print("You healed yourself of all wounds")
                        print("YOU USED: 1 Scroll")
                        self.hp=self.maxhp
                        x=0
                    if r==10:
                        self.ultimhp=self.ultimhp-1
                        print("SPELL FAILED")
                        print("YOU USED: 1 Scroll")
                        self.hp=self.hp
                        x=0
                else:
                    print("**----YOU ARE OUT OF SCROLLS OF MAXIMUM HEALING!----**")
                    x=0
            elif d=='4': #BLIZZARD
                if self.blizzard>0:
                    if r<10:
                        self.blizzard=self.blizzard-1
                        print("You create a torrent of ice spikes within a whirlwind of snow.")
                        print("YOU USED: 1 SCROLL")
                        x=8
                    if r==10:
                        self.blizzard=self.blizzard-1
                        print("SPELL FAILED")
                        print("YOU USED: 1 SCROLL")
                        x=0
                else:
                    print("**----YOU ARE OUT OF SCROLLS OF THE BLIZZARD!----**")
                    x=0
            elif d=='5': #THUNDERSTORM
                if self.thunder>0:
                    if r<10:
                        self.thunder=self.thunder-1
                        print("You create a massive storm of lightning bolts that crash down on the enemy.")
                        print("YOU USED: 1 SCROLL")
                        x=8
                    if r==10:
                        self.thunder=self.thunder-1
                        print("SPELL FAILED")
                        print("YOU USED: 1 SCROLL")
                        x=0
                        
                else:
                    print("**----YOU ARE OUT OF SCROLLS OF THE THUNDERSTORM!----**")
                    x=0
            else:
                print("YOU REACH FOR A SCROLL THAT DOESNT EXIST AND WASTE AN ATTACK.")
                x=0
        elif i=="a": #superweapons (ADD WHAT HAPPENS IF YOU DO NOT HAVE THE STAFF
            a=input("press: (1)%s  (2)%s (3)%s  (4)%s  (5)%s:   "%(self.Morcs,self.Morzs, self.Dalthuurs, self.Umbras, self.Shans))
            #a=int(a)
            r=random.randint(1,3)
            if a=='1':#Shadowbow
                if self.umbra>0:
                    if r<3:
                        self.umbra=self.umbra-1
                        print("You use the Shadowbow and the umbra arrow hits the enemy. The enemy writhes in pain for several seconds")
                        print("YOU USED: 1 UMBRA ARROW")
                        x=5
                    if r==3:
                        self.umbra=self.umbra-1
                        print("You use the ShadowBow but the umbra arrow did not fly true and missed the enemy")
                        print("YOU USED: 1 UMBRA ARROW")
                        x=0
                else:
                    print("**----SHADOWBOW OUT OF UMBRA ARROWS!----**")
                    x=0
            elif a=='2': #mask of morzana$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4
                if self.morzana<self.maxmorzana:
                    print("**----MASK OF MORZANA OUT OF POWER! COLLECT 5 SOULS TO RECHARGE----**")
                    x=0 
                if self.morzana==self.maxmorzana:#to charge this up self.morzana>99
                    #if r<3:
                    self.morzana=0#self.morzana-100
                    print("You cast Fires of Morcengarde. Tornadoes of green fire leap from your fingertips and wrap themselves like vines around your enemy")
                    print("The green fire intensifies and consumes your enemy.")
                    print("--MASK OF MORZANA HAS BEEN USED. COLLECT 5 SOULS TO RECHARGE--")
                    x=20
                    self.morzana=0
                
                    
                
            elif a=='3': #Morceriss Staff self.morc
                if self.morc>0:
                    m=input("PRESS: 1) suck the lifeforce out of your enemy (-1 Staff Energy), 2) create a flaming cobra (-5 Staff Energy): ")
                    if m=='1': #drain life
                        if self.morc>1:
                            self.morc=self.morc-1
                            print("You drain the life force out of your enemy and revitalize yourself")
                            print("YOU GAIN +5 HEALTH")
                            self.hp=self.hp+5
                            if self.hp>self.maxhp:
                                self.hp=self.maxhp
                            print("YOU USED: 1 STAFF ENERGY")
                            x=5
                        else:
                            print("**--MORCERIS'S STAFF DOES NOT HAVE ENOUGH POWER--**")
                            x=0
                #else:
                    #print(
                    if m=='2': #flaming cobra
                        
                        if self.morc>5:
                            self.morc=self.morc-5
                            print("A colossal flaming cobra emerges from the ground and spews fire at your opponent. When killed, it explodes.")
                            print("YOU USED: 5 STAFF ENERGY")
                            x=2+2+5
                        else:
                            print("**--MORCERIS'S STAFF DOES NOT HAVE ENOUGH POWER--**")
                            x=0
                    else:
                        print("WHOOPS, THAT IS NOT AN ATTACK.")
                        x=0
                else:
                    print("**----MORCERIS'S STAFF IS USELESS----**")
                    x=0
            elif a=='4': #Dalthuurs Staff/cloak 3 undead armies 1 undead dragon 6 total
                if self.dalthuur>0:
                    d=input("PRESS: 1) Summon an batallion of undead warriors (-2 Cloak Energy, 2) Summon an undead dragon (-6 Cloak Energy).")
                    if d=='1':# undead army
                        self.dalthuur=self.dalthuur-2
                        print("You lift your hands and summon a dozen undead warriors. Each warrior weilds a sword and axe. ")
                        print("The undead warriors swarm your enemy and slice and hack at it with their swords and axes.")
                        print("YOU USED: 2 CLOAK ENERGY")
                        x=7
                    if d=='2': # undead dragon
                        if self.dalthuur==6:
                            
                            self.dalthuur=self.dalthuur-6
                            print("You lift you hands in the air and create a vortex of black smoke. As the vortex dissipates, a dragon made of bones emerges.")
                            print("The dragon opens its mouth and chomps down on your enemy. It then claws and rips at your enemy.")
                            print("YOU USED: 6 CLOAK ENERGY ")
                            x=5+3+3
                        else:
                            print("**--DALTHUUR'S CLOAK DOES NOT HAVE ENOUGH POWER--**")
                            x=0
                    else:
                        print("WHOOPS, THAT IS NOT AN ATTACK.")
                        x=0
                else:
                    print("**----DALTHUUR'S CLOAK IS USELESS----**")
                    x=0
            elif a=='5': #Shanzalar's Staff you create a 1 maelstrom
                if self.shan>0:
                    s=input("PRESS: 1) Release all of the Shanzalar's Energy and lay waste to your enemy (ONLY CAN BE USED 1 TIME)")
                    if s=='1':
                        self.shan=0
                        print("You raise the staff to the sky. The clouds swirl overhead and decend down upon you, creating a vortex around you.")
                        print("You feel the power of the enter your body. You have the power to destroy entire worlds.")
                        print("You slam the staff into the ground and release all of its energy at once.")
                        print("A sphere of energy radiates out from the staff and destroys everything in its path.")
                        print("YOU USED ALL OF THE STAFF'S ENERGY")
                        x=1000
                    else:
                        print("WHOOPS, THAT IS NOT AN ATTACK.")
                        x=0
                    #if r==3:
                        #self.shan=self.shan-4
                        #print("Enemy dodges Sword")
                        #print("YOU USED: 2 STAMINA")
                        #x=0
                else:
                    print("**----SHANZALAR'S STAFF IS USELESS----**")
                    x=0
            else:
                print("YOU REACH FOR A MAGICAL WEAPON THAT DOES NOT EXIST AND WASTE AN ATTACK.")
                x=0
        else:
            print("INSTEAD OF USING THE WEAPONS AND MAGICAL ABILITIES YOU HAVE NOW, YOU DECIDE THE BEST COURSE OF ACTION IS TO THROW A BALL OF DIRT AT YOUR ENEMY")
            x=0
        print("ENEMY LOST: %s Health"%(x)) #MAKE ELSES ELIFS TO SEE IF THAT WORKS
    
        return x #how much damage is dealt
        #return y   
            
          
        
    ##########            
    ###MOVE UP
    ##########
    def moveUp(self, world):
        self.y=self.y-1
        self.hp=self.hp
        
       
        
        #########################################MERCHANT 4
        if world.Merchant4(self.x, self.y): ###MERCHANT 4
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                   (5) BUY 1 MAXIMUM HEALING  SCROLL {250 GOLD}:  ")
               # f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2': 
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam:
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")

        if world.Merchant6(self.x, self.y): ###MERCHANT 6
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD}  (4) BUY 1 STAMINA POTION {50 GOLD}                  (5) BUY 1 INFERNO SCROLL {250 GOLD}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                   
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.ultimhp=self.ultimhp+1
                        if self.ultimhp>self.maxultimhp: #does not go over max health
                            self.ultimhp=self.maxultimhp
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        if world.Merchant7(self.x, self.y): ###MERCHANT 7
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                               (5) BUY 1 INFERNO SCROLL {250 GOLD}  (6) BUY 1 SOUL {150}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:########               
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.blizzard=self.blizzard+1
                        if self.blizzard>self.maxblizzard: #does not go over max health
                            self.blizzard=self.maxblizzard
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                c=400
                if f=='6':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.morzana=self.morzana+1
                        if self.morzana>self.maxmorzana: #does not go over max health
                            self.morzana=self.maxmorzana
                        print("YOU PURCHASED 1 SOUL FOR 150 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")

        if world.Merchant8(self.x, self.y): ###MERCHANT 8
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                                (5) BUY 1 INFERNO SCROLL {100 GOLD}:  ")
               # f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.blizzard=self.blizzard+1
                        if self.blizzard>self.maxblizzard: #does not go over max health
                            self.blizzard=self.maxblizzard
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
#####################################################################
                
  ##########      #Player hits a wall "#"
        if world.isWall(self.x, self.y):
            print("ouch! You have been poisoned")
            self.hp=self.hp-1
            self.y=self.y+1
        if world.isWall2(self.x, self.y):
            self.y=self.y+1
        if world.isWall3(self.x, self.y):
            self.y=self.y+1
        if world.isCaveWall(self.x, self.y):
            self.y=self.y+1
    #######MOUNTAIN
        if world.isMountian1(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y+1
        if world.isMountian2(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y+1
        if world.isMountian3(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y+1
        if world.isMountian4(self.x, self.y):
            print("You cannot go that way")
            self.y=self.y+1
        if world.isMountian5(self.x, self.y):
            print("You cannot go that way")
            self.y=self.y+1
        if world.isDarkElf(self.x, self.y):
            input("You see dark shadows moving through the trees. Suddenly, you feel a knife at your throat. Then everything goes black")
            self.x=self.x-1
            self.y=self.y-3

       
        #Player goes Out of Bounds
        if world.isBoundary1(self.x, self.y):
            
            self.y=self.y+1
        if world.isBoundary3(self.x, self.y):
            
            self.y=self.y+1
        if world.isBoundary2(self.x, self.y):
            
            self.y=self.y+1
        #Player is underwater
        if world.isWater(self.x,self.y):
            print("You are Underwater")
            self.hp=self.hp

        if world.Smith(self.x, self.y):
            y=input("YOU HAVE ENTERED THE FORGE. PRESS 'e' TO EXIT")
            p='yay'
            p=input("[Hjorvein the Blacksmith] Arlo there, Adventurer! Werd you like me to fix yer weapons or improve 'em? [fix='f' or improve='i' or exit='e']: ")
            while p is not 'e':
                
                
                if p=='f':
                    print("[Hjorvein] Ah, now what needs fixing?")
                    b=self.maxbow-self.bow
                    x=10*b
                    c=self.maxsword-self.sword
                    y=10*c
                    print("PRESS: (1) FIX BOW COMPLETELY  (%d GOLD)   (2) FIX ENOUGH FOR 5 USES(50 GOLD)"%(x))
                    print(" ")
                    f=input("PRESS: (3) FIX SWORD COMPLETELY (%d GOLD)   (4) FIX ENOUGH FOR 5 USES(50 GOLD)  (5) EXIT:  "%(y))
            #f=int(f)
                    b=self.maxbow-self.bow
                    if f=='1':
                        a=10*b
                        if self.gold>a or self.gold==a:
                    
                            self.gold=self.gold-a
                            self.bow=self.bow+b
                            if self.bow>self.maxbow:
                                self.bow=self.maxbow
                        else:
                            print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
                    if f=='2':
                        self.bow=self.bow+5
                        self.gold=self.gold-50
                    c=self.maxsword-self.sword  
                    if f=='3':
                        a=10*c
                        if self.gold>a or self.gold==a:
                    
                            self.gold=self.gold-a
                            self.sword=self.sword+c
                            if self.sword>self.maxsword:
                                self.sword=self.maxsword
                        else:
                            print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
                    if f=='4':
                        self.sword=self.sword+5
                        self.gold=self.gold-50
                    else:
                        pass
                if p=='i':
                    y=input("[Hjorvein] Which item o' yers werd you like me to improve fer ya? ['b'=bow, 's'=sword]: ")
                    if y=='s':
                        if self.iSword>0:
                                if self.iSwordLvl==1:
                                    c=100
                                if self.iSwordLvl==2:
                                    c=300
                                if self.iSwordLvl==3:
                                    print("IRON SWORD AT MAX LEVEL!")
                                if self.iSwordLvl<3:
                                    p=input("Upgrade Iron Sword to Level %d (%d Gold)? [yes,no]"%(self.iSwordLvl+1, c))
                                    if p=='yes':
                                        if self.gold<c:
                                            print("NOT ENOUGH GOLD TO UPGRADE!!")
                                        if self.gold>c or self.gold==c:
                                            if self.iSwordLvl+1>2:
                                                self.gold=self.gold-c
                                                self.iSwordLvl=self.iSwordLvl+1
                                                print("Iron Sword Upgraded to Max Level")#make this happen at lvl 3
                                                print("Gold: %d Gold"%(self.gold))
                                                self.iSwordLvl=3
                                            if self.iSwordLvl+1<3:
                                                self.gold=self.gold-c
                                                self.iSwordLvl=self.iSwordLvl+1
                                                print("Iron Sword Upgraded to Level %d"%(self.iSwordLvl))
                                                print("Gold: %d Gold"%(self.gold))
                                    if p=='no':
                                        pass
                    if y=='b':
                        if self.iArrows>0:
                                if self.iArrowsLvl==1:
                                    c=100
                                if self.iArrowsLvl==2:
                                    c=300
                                if self.iArrowsLvl==3:
                                    print("IRON BOW AT MAX LEVEL!")
                                if self.iArrowsLvl<3:
                                    p=input("Upgrade Iron Bow to Level %d (%d Gold)? [yes,no]"%(self.iArrowsLvl+1, c))
                                    if p=='yes':
                                        if self.gold<c:
                                            print("NOT ENOUGH GOLD TO UPGRADE!!")
                                        if self.gold>c or self.gold==c:
                                            if self.iArrowsLvl+1>2:
                                                self.gold=self.gold-c
                                                self.iArrowsLvl=self.iArrowsLvl+1
                                                print("Iron Bow Upgraded to Max Level")#make this happen at lvl 3
                                                print("Gold: %d Gold"%(self.gold))
                                                self.iArrowsLvl=3
                                            if self.iArrowsLvl+1<3:
                                                self.gold=self.gold-c
                                                self.iArrowsLvl=self.iArrowsLvl+1
                                                print("Iron Bow Upgraded to Level %d"%(self.iArrowsLvl))
                                                print("Gold: %d Gold"%(self.gold))
                                    if p=='no':
                                        pass
                p=input("Is der anything else you werd like me to fix or improve, Adventurer? [fix='f' or improve='i' or exit='e']: ")
                
                
                      
                
            
        #Player finds a health or magik potion ##POTIONS AND GOLD
        if world.hpotion(self.x, self.y): 
            print("+1 Health Potion")
            self.hpotion=self.hpotion+3
            if self.hpotion>self.maxhpotion:
                self.hpotion=self.maxhpotion
        if world.mpotion(self.x, self.y):  
            print("+1 Magik Potion")
            self.mpotion=self.mpotion+1
            if self.mpotion>self.maxmpotion:
                self.mpotion=self.maxmpotion
            
            
        if world.coins(self.x, self.y):
            self.gold=self.gold+5
            if self.gold>self.maxgold:
                self.gold=self.maxgold
            
                
                
            #print(my_string2)

        if world.Horastead(self.x, self.y):
            xCoord = self.x
            yCoord = self.y
            self.x = 1
            self.y = 1
            playGame(mini_world1, self)
            self.x = xCoord
            self.y = yCoord
        if world.MainQuest4(self.x, self.y):
            xCoordH = self.x
            yCoordH = self.y
            self.xCoordH = self.x
            self.yCoordH = self.y
            self.x = 1
            self.y = 1
            playGame(game_worlda1, self)
            self.x = xCoordH
            self.y = yCoordH
        if world.MainQuest4a(self.x, self.y) and self.lydiaStory == 2:
            input("LYDIA STOPS. SHE TURNS TOWARDS YOU AND TAKES A DEEP BREATH.")
            input("[Lydia] Morceris killed him with poison. A slow acting potion that slowly dissolves the internal organs. Took him several days of agony for it to finally take him.")
            input("[Lydia] I was forced to watch as his organs dissolved and red mist came from his mouth. Once he died...Morceris let me live. I do not know why.")
            input("[%s] Can he be stopped?"%(self.name))
            input("[Lydia] My husband and I heard of a prophecy that someone from a different world would arrive. They call him the Morzana.")
            input("That's why I brought you here.")
            input("[%s] You think I'm this Morzana?"%(self.name))
            input("[Lydia] There is only one way to find out: you will have to defeat an ancient serpent that lives in Emerald Cove...")
            input("...You will then have to enter the Ancient Ruins.")
            input("If you can defeat the serpent and enter the ruins, then you will be powerful enough to stop Morceris. The only way to get there is")
            input("through Broken Skull Cave. It contains a fearsome dragon. It has killed all who have tried to enter its lair.")
            input("[%s] I'll do it."%(self.name))
            input("[Lydia] Here, come with me. I will get you a few items for your quest.")
            print("Lydia GIVES YOU 50 GOLD AND A HEALTH POTION")
            self.hpotion=self.hpotion + 1
            if self.hpotion > self.maxhpotion:
                self.hpotion = self.maxhpotion
            self.gold=self.gold+50
            if self.gold>self.maxgold:
                self.gold=self.maxgold
            input("[Lydia] There's more in my storage room. Take what you need.")
            input("MISSION 4 COMPLETE")
            input("NEW MISSION: ENTER THE DRAGON'S LAIR(ṽ) AND TRAVEL TO THE OTHER SIDE TO DEFEAT THE GUARD(Ꚛ)")
            self.story=5
            
        
        ##########SERPENT EGG
        if world.isSerpentDead(self.x, self.y) and self.story>6:
            input("AFTER DEFEATING THE SERPENT, YOU LOOK OVER TO THE WESTERN SHORE AND SEE AN ABANDONED RUIN. IT SEEMS THAT THE SERPENT WAS TRYING TO PROTECT IT.")
            input("MISSION: THE ANCIENT RUINS")
            input("SWIM OVER TO THE ABANDONED RUINS(꙲) TO DISCOVER WHY THE SERPENT WAS PROTECTING IT.")
            self.story=8

       
        
        ####################ISRUIN
        if world.isRuins(self.x, self.y) and self.story>7:
            input("MISSION: THE ANCIENT RUINS")
            input("YOU ARRIVE AT THE ENTRANCE TO AN ABANDONED TEMPLE. MOST OF THE STONE WALLS HAVE COLLAPSED AND VINES WIND AROUND THE BROKEN COBBLESTONE.")
            input("YOU WALK AROUND THE TEMPLE, LOOKING FOR ANY HINT OF WHAT THIS TEMPLE USED TO BE LIKE OR WHY THE SERPENT WAS GUARDING IT.")
            
            input("AS YOU CIRCUMNAVIGATE THE RUIN, YOU HEAR A SOFT, LOW VOICE COME FROM THE RUIN. YOU WALK TOWARDS THE VOICE AND FIND A NARROW OPENING.")
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 1
            self.y = 1
            playGame(game_worldb, self)
            self.x = xCoord
            self.y = yCoord
            '''
        if world.isTemple (self.x, self.y) and self.story>7:
            
            input("YOU CRAWL THROUGH THE OPENING AND FIND YOURSELF IN A ROOM FILLED WITH A SOFT GREEN LIGHT. IN THE CENTER OF THE ROOM LIES A LARGE BLACK OBELISK.")

            input("YOU WALK TOWARDS THE OBELISK NOTICE CRACKS ALONG THE SURFACE. AS YOU PEER CLOSER YOU SEE GREEN LIGHT RADIATING OUT FROM THEM.")
            input("YOU PLACE YOUR HAND ON THE OBELISK AND THE VOICE RETURNS. IT GETS LOUDER AND LOUDER AND THE ROOM BEGINS TO SHAKE.")
            input("THE CRACKS ON THE OBELISK GROW UNTIL THE ENTIRE OBELISK CRUMBLES, REVEALING AN OCTAHEDRON. IT LEVITATES ABOVE THE GROUND, UNMOVING.")
            input("THE OCTAHEDRON BURSTS OPEN. YOU ARE SENT FLYING BACKWARDS BY THE POWER OF IT. YOU LOOK BACK AND SEE A GREEN TINTED GHOST EMERGE FROM IT.")
            input("YOUR HANDS BECOME ENGULFED IN FLAMES AS YOU PREPARE TO FIGHT IT.")
            input("[STEP FORWARDS TO FIGHT THE GHOST]")
            self.story=9
            '''
            
       
         ####################MQ5   
        if world.MainQuest5(self.x,self.y) and self.story>9:
            input("MISSION 5")
            input("NIGHT HAS FALLEN, AND ALL YOU CAN SEE IS THE SILHOUETTE OF THE GUARD IN THE MOONLIGHT.")
            input("AS YOU WALK TOWARDS THE GUARD, YOU SEE HIS JAGGED, BLACK ARMOR. THE ARMOR IS ENCHANTED AND GLOWS RED AROUND THE CHEST.")
            print("THE GLOW PULSES WITH THE HEARTBEAT OF THE GUARD. AS THE RED GLOW INCREASES, YOU NOTICE HE IS")
            input("HOLDING A LARGE SWORD WITH THE END OF THE BLADE IN THE GROUND.")
            print("THE GUARD'S HEAD IS FACING TOWARDS THE GROUND, BUT AS YOU WALK CLOSER, HE LIFTS HIS HEAD AND YOU SEE")
            input("BRIGHT RED EYES STARING AT YOU. HE SPEAKS IN A DARK, POWERFUL VOICE.")
            input("[The Guard] HALT!! You are trespassing in Morceris's land. Flee now, or you will be killed.")
            input("[Player] Step aside. I must defeat Morceris and restore peace to this land.")
            input("[The Guard] I will not step aside. My loyalty is to Morceris. Take one more step, and I will be forced to kill you.")
            input("PRESS 'w' TO BATTLE THE GUARD, PRESS 's' TO FLEE: ")
            self.story=11
            ################GUARD DECISION
        if world.GuardDecision(self.x,self.y) and self.story>10:
            print("AFTER YOUR FINAL ATTACK, THE GUARD WAS DEFEATED AND LIES ON THE GROUND. HE IS STILL BREATHING BUT CAN NO LONGER ATTACK YOU.")
            input("YOU LOOK DOWN AT THE GUARD. HIS RED EYES STARE INTO YOURS. YOU KNOCK OFf HIS HELM WITH YOUR SWORD TO SEE WHAT HORRID CREATURE WAS BEHIND IT.")
            input("BUT ALL YOU SEE IS A YOUNG WOMAN. HER LONG RED HAIR COVERS MOST OF HER FACE, BUT SHE LOOKS JUST LIKE THE TOWNSFOLK YOU SAW EARLIER.")
            print("THE GUARD IS NOT A HORRID CREATURE, BUT RATHER JUST A NORMAL WOMAN. DESPITE HER INNOCENT APPEARANCE, SHE WORKS FOR")
            input("MORCERIS AND HAS KILLED EVERY MAN WHO OPPOSED HER.")
            s=input("MORALITY> PRESS (1) Spare her life or PRESS (2) Kill the Guard and be one step closer to bringing peace to the land:  ")
            #s=int(s)
            if s=='1':
                self.moral=self.moral+1
                if self.moral==1:
                    self.morals='the Forgiving'
                input("YOUR DECISION HAS INCREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                input("YOU STEP AWAY FROM THE GUARD AND MOTION FOR HER TO GET UP. SHE GETS UP, LOOKS AT YOU, AND LIMPS AWAY INTO THE FOREST.")
                
            else:
                self.moral=self.moral-1
                if self.moral==-1:
                    self.morals='the Anti-Hero'
                input("%s YOUR DECISION HAS DECREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.name,self.morals))
                input("YOU TAKE YOUR SWORD AND RAM IT THROUGH THE RED GLOW OF HER CHEST. THE RED GLOW SLOWLY FADES TO BLACK AND YOU SEE THE LIGHT LEAVES HER EYES.")
                
            input("NOW THAT THE GUARD IS NO LONGER A THREAT, YOU CONTINUE TOWARDS MORCERIS'S CASTLE.")
            input("END OF MISSION 5 HEAD TO MORCERIS'S CASTLE(₪)")
            self.story=12
            ###############MORCERIS'S CASTLE

        if world.MorcerisBridge(self.x,self.y) and self.story> 11:
            print("AS YOU WALK TO THE END OF THE CLEARING, YOU SEE A WALL OF TREES IN FRONT OF YOU. TOWERING ABOVE THEM IS A MASSIVE CASTLE.")
            input("THE CASTLE BLOCKS OUT THE BACKGROUND STARS AND HAS A DARK ORANGE GLOW EMINATING FROM ITS WINDOWS. IT HAS FOUR SPIKED TOWERS...")
            print("...THAT EXTEND INTO THE SKY. AS YOU LOOK BACK DOWN TO THE TREES, YOU SEE A CLEARING LEADING UP TO THE CASTLE. YOU WALK TOWARDS IT.")
            input("YOU SEE THAT THERE IS A BRIDGE THAT SPANS A MASSIVE CHASM. A SMALL RIVER RUNS BENEATH IT. ")
            print("PRESS 'w' TO CROSS THE BRIDGE.")
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 1
            self.y = 3
            playGame(game_worlde, self)
            self.x = xCoord
            self.y = yCoord
            
                  
        if world.MorcerisDoor(self.x,self.y) and self.story> 11:
            
            input("YOU ARRIVE AT THE DOOR TO THE CASTLE. THE DOORS ARE BLACK WITH DARK RED CRACKS THAT JUT ACROSS IT LIKE ROOTS FROM A TREE.")
            print("THE RED CRACKS PULSE; GROWING BRIGHTER AND THEN DIMMER. YOU CAN FEEL THE POWER RESONATING FROM IT.")
            print("YOU PLACE YOUR HAND ON THE DOOR AND IT OPENS IMMEDIATELY. YOU WALK IN AND UNSHEATH YOUR SWORD.")
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 2
            self.y = 3
            playGame(game_worlde1, self)
            self.x = xCoord
            self.y = yCoord
        if world.MorcerisCastle(self.x,self.y) and self.story> 11:
            print("MORCERIS SITS ON A THRONE MADE OUT OF HUMAN BONES. HE WEARS A DARK RED CLOAK WITH ARCHAIC SYMBOLS ETCHED INTO THE FABRIC.")
            input("HE HOLDS A CURVED, BLACK STAFF TOPPED WITH A FLAMING COBRA'S HEAD. HE OPENS HIS MOUTH AND SPEAKS WITH A LOW, RASPY VOICE.")
            input("[Morceris] I see you have found me, %s. It would appear that my Guard has failed me. Pity, I put a lot of work into the mind-control spell."%(self.name))
            input("[Morceris] Poor innocent girl, I was going to set her free if she was able to kill you; give her back to that rebel mother of hers.")
            input("[Morceris] But no matter, I can always find a new Guard. There are plenty of potential servants in this realm.")
            input("[Morceris] I assume you have come to kill me then? Rid the kingdom of me and restore peace to it?")
            input("[Player] Yes, I have. I am the Morzana and I'm destined to destroy you. I will bring peace to this land.")
            input("[Morceris] Very well. Step forward and seal your destiny.")
            input("PRESS 'w' TO ATTACK MORCERIS.")
            self.story=13
            ############FINAL DECISION
        if world.FinalDecision(self.x,self.y) and self.story>12:
            input("MORCERIS'S BODY LIES CRUMPLED ON THE GROUND. YOU REMOVE HIS HOOD WITH THE TIP OF YOUR SWORD TO SEE THE FACE OF YOUR ENEMY.")
            input("[Player] No, it cant be.")
            input("YOU REALIZE THE OLD MAN AND MORCERIS ARE THE SAME PERSON. IN ANGER, YOU RAISE YOUR SWORD TO STRIKE HIM DOWN.")
            input("[Morceris] WAIT!! Before you strike me down, you must know who you truly are. You are me.")
            input("[Morceris] When you arrived, I was visiting the place that brought me to this wretched world. I was expecting you.")
            input("[Morceris] As I was walking towards it, I saw you materialize on the ground before me.")
            input("[Morceris] Just like you, I was greeted by an old man. And now, you are confronted with the same decision that I had to make.")
            input("[Morceris] As you can see, I am old and sick. You must take my place and find Dalthuur. You must awaken Shanzalar and retake the kingdom.")
            input("[Morceris] This is your destiny. Take my staff and live the life you were meant for.")
            input("YOU CAN TAKE MORCERIS'S STAFF AND CONTINUE THE RULE OF MORCERIS.")###
            input("BUT THAT MEANS CONDEMNING THE ENTIRE KINGDOM TO LIVE UNDER A TYRRANICAL RULE. IN ORDER TO END THIS CYCLE OF TERROR, YOU MUST KILL MORCERIS.")###
            print(">MORALITY PRESS 1: Kill Morceris now and end his reign of terror, knowing that you might end up just like him later, OR")
            s=input("Do you--PRESS 2: Take his staff and unite with Dalthuur and Shanzalar to rule over the kingdom?: ")
            #s=int(s)
            if s=='1':#good ending
                self.moral=self.moral+1
                if self.moral==2:
                    self.morals='the Guardian'
                input("YOUR DECISION HAS INCREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                print("YOU THRUST YOUR BLADE THROUGH HIS CHEST. AS THE LIFE SEEPS AWAY FROM MORCERIS, YOU SEE HIM FADE INTO NOTHING.")
                print("ALL YOU CAN DO IS HOPE THAT YOU NEVER END UP LIKE HIM. YOU MUST DO EVERYTHING POSSIBLE TO NOT TURN INTO MORCERIS AND STOP THE CYCLE.") 
                print("YOU SEE HIS STAFF ON THE GROUND. IT NO LONGER HAS THE FIRE AND APPEARS POWERLESS. YOU TAKE THE STAFF FOR SAFE KEEPING.")##THIS IS SORT OF DUMB, BUT OHWELL
                input("YOU REMEMBER THE RUIN AND NOW UNDERSTAND WHAT COULD HAPPEN IF DALTHUUR AND SHANZALAR ARE AWAKENED.")
                input("YOU MUST TRAVEL TO MORCENGARDE AND DEFEAT DALTHUUR.")
                
                #self.hp=0##############DESCRIBE WHY THE PLAYER WOULD HAVE THE STAFF IF THEY DIDNT TAKE THE STAFF
                #########MAYBE, YOU TAKE THE STAFF, BUT ONLY IF YOU CHOOSE THE BAD ENDING DO YOU GET ITS POWER
                self.hp=self.maxhp                
                self.magik=self.maxmagik              
                self.arrows=self.maxarrows
                self.stam=self.maxstam
                self.morc=0
            else: #bad ending
                self.moral=self.moral-1
                if self.moral==-2:
                    self.morals='the Corrupt'
                input("YOUR DECISION HAS DECREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                print("YOU TAKE MORCERIS'S STAFF, AND YOU FEEL THE POWER OF IT FLOW THROUGH YOUR VEINS. YOU FEEL DIFFERENT.")
                print("THE ITEM HAS TURNED EVERY LAST BIT OF GOOD IN YOU INTO DARKNESS.")
                print("EVERYTHING BECOMES CLEAR TO YOU. THE CYCLE MUST CONTINUE IN ORDER TO MAKE YOU AND YOUR REIGN OF TERROR IMMORTAL.")
                input("YOUR PAST SELF MUST BE BROUGHT TO THE FUTURE AND CORRUPTED, JUST AS YOU WERE.")
                input("AS YOU TOUCH THE TOP PART OF THE STAFF, YOU SEE A VISION OF THE SAME STRANGE LAND YOU SAW IN THE RUIN.")
                input("THIS TIME IS DIFFERENT, IT SHOWS DALTHUUR IN HIS TOMB. YOU SEE HIS DARK PURPLE EYES OPEN AND THE TOMB EXPLODES.")
                input("YOU MUST FIND THE TOMB AND JOIN DALTHUUR.")
                
                
                self.hp=self.maxhp                
                self.magik=self.maxmagik              
                self.arrows=self.maxarrows
                self.stam=self.maxstam
                self.morc=self.maxmorc
            input("YOU START TO LEAVE THE CASTLE, BUT YOU HERE A LOUD CRACK COME FROM THE BACK OF THE ROOM.")
            input("--PRESS ENTER TO INVESTIGATE.")
       # if world.PortalM(self.x,self.y):
            input("YOU TURN TOWARDS THE SOUND AND SEE LARGE CRACKS FORM A SPIDERWEB-LIKE PATTERN ON THE BACK WALL.")
            input("SUDDENLY, THE WHOLE WALL BREAKS REVEALING A PURPLE VORTEX. YOU TRY TO EVADE IT BUT ARE SUCKED INTO IT ALONG WITH MUCH OF THE CASTLE...")
            input("AND THEN EVERYTHING GOES BLACK.")
            input("*-----{AMODERA QUESTLINE COMPLETE}-----*")
            input("PRESS ENTER AND THEN 'w' TO TRAVEL TO MORCENGARDE")
            self.story=14
        if self.moral==0: #make different classes of good and evil, change neutral to mysterious, unknown, nameless, secret, unsung
            self.morals=''
            
            #good
        if self.moral==1:
            self.morals='the Defender'
        if self.moral==2:
            self.morals='the Guardian'
        if self.moral==3:
            self.morals='the Savior'
        if self.moral==4:
            self.morals='the Hero'
        if self.moral==5:
            self.morals='the Morzana'
            
            #evil
        if self.moral==-1:
            self.morals='the Corrupt'
        if self.moral==-2:
            self.morals='the Soulless'
        if self.moral==-3:
            self.morals='the Betrayer'
        if self.moral==-4:
            self.morals=' the Damned'
        if self.moral==-5:
            self.morals='the Morthuurzar'
           
         
            
        

    #Repeat For all four directions
                                
   ############################################################3 #Move South (s)                          
    def moveDown(self, world):
        
        self.y=self.y+1
        self.hp=self.hp
        
        ####################################MERCHANT 5
        if world.Merchant5(self.x, self.y): ###MERCHANT 5
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                    (5) BUY 1 BLIZZARD SCROLL {250 GOLD}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.blizzard=self.blizzard+1
                        if self.blizzard>self.maxblizzard: #does not go over max health
                            self.blizzard=self.maxblizzard
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        #Player hits a wall "#"
        if world.isWall(self.x, self.y):
            print("ouch! You have been poisoned")
            self.hp=self.hp-1
            self.y=self.y-1
        if world.isWall2(self.x, self.y):
            self.y=self.y-1
        if world.isWall3(self.x, self.y):
            self.y=self.y-1
        if world.isCaveWall(self.x, self.y):
            self.y=self.y-1
        #Mountain
        if world.isMountian1(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y-1
        if world.isMountian2(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y-1
        if world.isMountian3(self.x, self.y):
            print("That cliff is not climbable")
            self.y=self.y-1
        if world.isMountian4(self.x, self.y):
            print("You cannot go that way")
            self.y=self.y-1
        if world.isMountian5(self.x, self.y):
            print("You cannot go that way")
            self.y=self.y-1
        if world.isMtnCave(self.x, self.y):
            input("You enter the cave and travel through a secret tunnel")
            self.y=self.y+1
            self.x=self.x+5
            
        
        #Player goes Out of Bounds
        if world.isBoundary3(self.x, self.y):
            
            self.y=self.y-1
        if world.isBoundary2(self.x, self.y):
            
            self.y=self.y-1
        if world.isBoundary1(self.x, self.y):
            
            self.y=self.y-1
        #Player is underwater
        if world.isWater(self.x,self.y):
            print("You are Underwater")
            self.hp=self.hp
        if world.Smith(self.x, self.y):
            print("YOU HAVE ENTERED THE FORGE.")
            print(" ")
            print("{MAX BOW POINTS=%d} PRESS: (1) FIX BOW COMPLETELY  (10 GOLD PER POINT)   (2) FIX ENOUGH FOR 5 USES(50 GOLD)"%(self.maxbow))
            print(" ")
            f=input("{MAX SWORD POINTS= %d} PRESS: (3) FIX SWORD COMPLETELY  (10 GOLD PER POINT)   (4) FIX ENOUGH FOR 5 USES(50 GOLD)  (5) EXIT:  "%(self.maxsword))
            #f=int(f)
            b=self.maxbow-self.bow
            if f=='1':
                a=10*b
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.bow=self.bow+b
                    if self.bow>self.maxbow:
                        self.bow=self.maxbow
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='2':
                self.bow=self.bow+5
                self.gold=self.gold-50
            c=self.maxsword-self.sword  
            if f=='3':
                a=10*c
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.sword=self.sword+c
                    if self.sword>self.maxsword:
                        self.sword=self.maxsword
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='4':
                self.sword=self.sword+5
                self.gold=self.gold-50
            else:
                pass
         #Player finds a health or magik potion or arrows #POTIONS AND GOLD
        if world.hpotion(self.x, self.y): 
            print("+1 Health Potion")
            self.hpotion=self.hpotion+1
            if self.hpotion>self.maxhpotion:
                self.hpotion=self.maxhpotion
        if world.mpotion(self.x, self.y): 
            print("+1 Magik Potion")
            self.mpotion=self.mpotion+1
            if self.mpotion>self.maxmpotion:
                self.mpotion=self.maxmpotion
        
        if world.coins(self.x, self.y):
            self.gold=self.gold+1
            if self.gold>self.maxgold:
                self.gold=self.maxgold
                ###########################portal to shadovar
        if world.PortalS(self.x, self.y):
            input("YOU HAVE ENTERED SHADOVAR")
            self.x=self.x-70
            self.y=self.y-1
        
        
        ##################MQ4
        
            ###########BANDIT
        if world.BanditGate(self.x,self.y):
            print("[Bandit] Well, look what we have here. And here I thought I made it clear that anyone who crossed me would find a")
            input("sword in their chest. Guess not. Get lost fool, or I may use you as archery practice.")
            input("[%s] I'm not from around here. I must not have gotten the message. I'm here to rid the land of your filth."%(self.name))
            input("[Bandit] Have you now? Prepare to die, fool.")
            self.story=1
        if world.isTown(self.x, self.y):######################use this one
            input("MISSION 4")
            input("YOU GO INTO THE VILLAGE OF KORIFSTEAD, MOST OF THE PEOPLE HERE ARE LOYAL TO A SORCERER NAMED MORCERIS. WALK AROUND THE TOWN AND FIND THE REBEL")
            input("{OPTIONAL MISSION} THERE ARE MANY MORCERIS LOYALISTS (•). TALK TO THEM.") 
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            
            self.x = 1
            self.y = 1
            playGame(game_worlda, self)
           
            self.x = xCoord
            self.y = yCoord
        if world.MainQuest4(self.x,self.y) and self.story>3:
            input("YOU FIND A WORN DOWN HOUSE. THE WALLS ARE MADE OF METAL AND STONE AND THERE ARE JUST A FEW SMALL WINDOWS. YOU WALK UP TO THE METAL DOOR AND KNOCK.")
            input("[Rebel]Who goes there? Are you one of Morceris's followers? I thought I made it clear that none of you were welcome here.")
            input("[%s] No, I am not from this land. I know of no Morceris."%(self.name))
            input("[Rebel]Not from this land, huh?")
            input("[%s] Who is this Morceris? Why do you hate him so much?"%(self.name))
            input("[Rebel] I can't speak about him in the open, he has followers everywhere. Quick come inside.")
            input("PRESS ENTER TO ENTER REBEL'S HOUSE.")
            xCoordH = self.x
            yCoordH = self.y
            self.xCoordH = self.x
            self.yCoordH = self.y
            self.x = 1
            self.y = 1
            playGame(game_worlda1, self)
            self.x = xCoordH
            self.y = yCoordH

        if world.MainQuest4a(self.x,self.y) and self.story>3:
            input("THE INTERIOR OF THE HOUSE IS JUST AS WORN DOWN AS THE EXTERIOR. THE HOUSE IS LIT BY A LANTERNS HANGING ON THE WALLS. THEY CAST A SHADOW ON THE REBEL.")
            input("THE REBEL HAS GREY HAIR AND A DARK GREY SKIN TONE. HER BRIGHT ORANGE EYES STARE INTO YOURS.")
            input("[Rebel] What is your name, traveller?")
            print("[%s] My name is %s."%(self.name,self.name))  
            print("[Rebel] My name is Lydia Mercer. Now, why have you come here, %s?"%(self.name))
            input("[%s] I want to know more about this Morceris."%(self.name))
            print("[Lydia] He is an immortal sorceror. He has two brothers: Dalthuur the Necromancer and Shanzalar the Destroyer.")
            input("[Lydia] They brought terror and tyranny to this land for hundreds of years. A millenia ago, Shanzalar and Dalthuur were defeated and imprisoned.")
            input("[%s] What of Morceris? Did he escape?"%(self.name))
            input("LYDIA LOOKS AWAY AND WALKS DOWN THE DIMLY LIT HALLWAY.")
            
            
            
            
            ############DRAG CAVE
        if world.isDragCave(self.x,self.y) and self.story>4:
            print("YOU ENTER THE CAVE. YOUR HANDS ENGULF IN FLAMES AS YOU CAST A FIREBALL. YOU LOOK AROUND AND NOTICE THE WALLS ARE COMPLETELY BLACK.")
            input("YOU PLACE YOUR HAND AGAINST IT AND YOUR HAND BLACKENS WITH SOOT. AS YOU CONTINUE DEEPER INTO THE CAVE, YOU HEAR A CRUNCH UNDERE YOUR FEET.")
            input("YOU LOOK DOWN AND SEE A BROKEN RIB CAGE. AS YOUR EYES GLANCE AROUND THE CAVE, YOU SEE MORE AND MORE BROKEN BONES AND CRUMPLED CHESTPLATES.")
            input("YOU HEAR A SOFT GROWL FROM FARTHER IN. YOU IMMEDIATELY SNUFF OUT YOUR FLAMES, BUT AS YOU DO SO, YOU SEE A RUSH OF FLAMES COME FROM BEHIND THE CORNER.")
            input("YOU SNEAK AROUND THE CORNER AND SEE A BLACK AND RED DRAGON WITH LARGE WINGS, ORANGE SPINES GOING DOWNS ITS BACK, AND A MOUTH FULL OF RAZOR SHARP TEETH.")
            print("THE DRAGON SLOWLY MOVES ITS HEAD TOWARDS YOU. YOU SEE ITS BRIGHT YELLOW EYES STARE DIRECTLY INTO YOURS.")
            print("IT REARS IT HEAD AND BOMBARDES YOU WITH FIREBALLS.")
            input("YOU LOST 5 HEALTH")
            self.hp=self.hp-5
            self.story=6
        if world.isCave(self.x,self.y):
            if self.story>2:
                print("YOU WALK TO THE CAVE'S MOUTH AND ENTER IT.")
               
                xCoord = self.x
                yCoord = self.y - 1
                self.xCoord = self.x
                self.yCoord = self.y
            
                self.x = 1
                self.y = 1
                playGame(game_worldc, self)
            else:
                print("PATH BLOCKED!")
                self.y = self.y - 1
           
            #self.x = xCoord
            #self.y = yCoord
            #fself.y = self.y - 1
            
        if world.isCave2(self.x,self.y):
            print("AS YOU GO DEEPER, IT BECOMES IMPOSSIBLE TO SEE ANYTHING. YOU CAST A FIREBALL AND HOLD THE FLAME IN YOUR HAND")
            input("THE FIREBALL CASTS A WARM GLOW ON THE CAVE WALLS. AS YOU WALK FARTHER INWARD, YOU HEAR A LOW GROWL.")
        
        if world.Morzana(self.x,self.y) and  self.story>8:
            #self.Morz = self.Morz + 1
            #if self.Morz>0:
               # self.Morzs="Mask of Morzana {-5souls}"
               # self.Morzss=" {Mask of Morzana: %d/5 Souls}"%(self.morzana) ##do this for all scrolls and special weapons
            input("AFTER THE GHOST IS DEFEATED, THE OCTAHEDRON REFORMS AND LAYS ON THE GROUND BEFORE YOU.")
            input("YOU PICK UP THE OCTAHEDRON AND LIGHT, GLOWING GREEN RUNES APPEAR ON THE SIDE. YOU HAVE NEVER SEEN THEM BEFORE, BUT SOMEHOW YOU KNOW WHAT THEY MEAN")
            input("THE OCTAHEDRON TRANSFORMS INTO A EMERALD MASK WITH GREEN FIRE ERUPTING FROM THE BACK OF IT.")
            print("YOU PUT IT ON AND YOU SEE FLASHES OF A STRANGE NEW LAND.")
            
            input("[THE LOW VOICE] '%s, YOU HAVE DEFEATED THE ANCIENT MORZANA AND CLAIMED THE MASK OF THE MORZANA."%(self.name))
            print("..NOW YOU MUST TAKE HIS PLACE AS THE MORZANA, THE PROTECTOR OF REALMS..")
            input("..THE EVIL NECROMANCER, DALTHUUR, HAS AWOKEN. MORCERIS HAS JUST RESURECTED HIM AFTER MANY CENTURIES OF PREPARATION..")
            input("..DALTHUUR WILL SURELY ESCAPE HIS PRISON SOON. THERE IS NOTHING YOU CAN DO TO STOP IT..")
            input("[%s] THEN WHAT CAN I DO?"%(self.name))
            
            input("..ONLY YOU CAN STOP DALTHUUR FROM RESURRECTING THE THIRD BROTHER, SHANZALAR. THIS YOU MUST DO.. ")
            input("..WHILE IT MAY HAVE TAKEN MORCERIS SEVERAL GENERATIONS TO RESURRECT DALTHUUR, IT WILL BE A MATTER OF DAYS BEFORE..")
            print("..SHANZALAR IS RESURRECTED. THIS MUST NOT HAPPEN.")
            input("[%s] WHERE IS DALTHUUR? HOW CAN I STOP HIM?"%(self.name))
            input("[THE LOW VOICE] 'DALTHUUR WILL BE IN HIS CASTLE AT THE SOUTHERN MOST PART OF MORCENGARDE, THE KINGDOM OF THE DEAD..")
            print("..GO THROUGH THIS PORTAL (Ѻ) AND YOU WILL TRANSPORTED TO THE NORTHERN PART OF THE KINGDOM.")
            input("..AS THE MORZANA, YOU CAN ABSORB THE SOULS OF YOUR ENEMIES, ALIVE OR DEAD. THE MASK CAN CHANNEL THE SOULS' ENERGY INTO A POWERFUL ATTACK.")
            print("..BUT DO NOT GIVE INTO THE POWER OR YOU WILL BECOME A CORRUPTED GHOST, JUST LIKE ASHIR TARON, WHOSE GHOST YOU DESTROYED.")
            input("[%s] WHY CANT YOU TRANSPORT ME CLOSER TO DALTHUUR?"%(self.name))
            input("[THE LOW VOICE] 'YOU ARE NOT STRONG ENOUGH TO KILL HIM. YOU MUST FIND AND DEFEAT HIS MINIONS TO GAIN THE POWER TO DEFEAT DALTHUUR..")
            input("..NOW, YOU MUST GO. DEFEAT MORCERIS AND WALK THROUGH HIS PORTAL AND YOU WILL BE TRANSPORTED TO MORCENGARDE.")
            print("MISSION COMPLETE")
            input("NEXT MISSION: THE LAND OF MORCENGARDE [AFTER YOU DEFEAT MORCERIS(Ꙛ), TRAVEL TO MORCENGARDE AND CONTINUE YOUR QUEST]")
            self.story=10
        
        if world.isDoor(self.x,self.y):
            #self.Morz = self.Morz
            input("YOU APPROACH A PAIR LARGE WOODEN DOORS. THE DOORS ARE RECTANGULAR, BUT ROUNDED NEAR THE TOP.")
            input("AT THE CENTER, THERE LIES A GREEN RUIN OF A FLAMING MASK. JUST BELOW IT IS A HAND SHAPED INDENT.")
            input("PRESS ENTER TO PLACE YOUR HAND IN THE INDENT")
            if self.Morz<1:
                input("DOOR LOCKED. ONLY THE WEARER OF THE MASK OF MORZANA CAN ENTER")
                self.y = self.y-1
            else:
                input("YOU FEEL A WARMTH AROUND YOUR HAND. THE WARMTH TRAVELS UP YOUR ARM AND ALLAROUND YOUR BODY.")
                input("GREEN FLAMES ERUPT FROM THE MASK AND TRAVEL DOWN YOUR ARM AND INTO THE INDENT. SMALL GREEN STREAMS GROW OUTWARDS FROM THE CENTER...")
                input("TOWARDS THE EDGES. THE DOORS OPEN OUTWARDS AND INTO A DARK CORRIDOR.")
                input("AS YOU STEP INWARDS, LANTERNS ALONG THE CORRIDOR LIGHT AND FILL THE ROOM WITH A GREEN GLOW.")
                  
                  
            
        if world.Horastead(self.x, self.y):
            input("YOU CONTINUE THE NEXT TOWN. YOU FIND A FALLEN OVER SIGN THAT READS, “HORASTEAD”. ")
            input("THIS TOWN IS NOT NEARLY AS DESTROYED, BUT THE FROZEN BODIES ARE JUST AS NUMEROUS. ")
            input("YOU EXPLORE ONE OF THE LARGER HOUSES IN HOPES OF FINDING A FEW CLUES.")
            input("AS YOU SEARCH AROUND THE LOWER FLOOR, YOU HERE CREAKING COMING FROM THE FLOOR ABOVE.")
            input("PRESS ‘W’ TO INVESTIGATE")
            input("YOU SLOWLY, AND QUIETLY WALK UP THE STAIRS; CAREFUL TO AVOID THE MANY HOLES AND UPTURNED NAILS.")
            input("AFTER YOU REACH THE TOP, YOU SEE A FLASH OF BLACK COME FROM AROUND THE CORNER AND EVERYTHING GOES DARK.")
            input("PRESS ENTER TO CONTINUE")
            input("AS YOU REGAIN CONSCIOUSNESS, YOU REALIZE YOU ARE TRAPPED AND UNABLE TO WIGGLE FREE")
            input("YOU TURN YOUR HEAD AROUND AND SEE THE PARTIALLY DECOMPOSED FACE OF A DEAD PERSON. ")
            input("YOU GAG QUIETLY AND FEEL SOME PUKE RISE UP YOUR THROAT. AT THAT MOMENT, YOU SEE A DARK FIGURE COME TOWARDS YOU.")
            input("[Voice] Not a fan of my friend, huh? If you live here long enough, you’ll get to know him more...")
            input("...There wasn’t a single living soul to talk to, so I got by making conversation with the other housemates. They don’t talk much, though.")
            input("YOU STARE AT THE FIGURE BLANKLY. YOU TRY TO GET A LOOK AT ITS FACE, BUT YOUR EYES ARE STILL BLURRY.")
            input("[Voice] Relax. I’m kidding. Well, mostly kidding. Name’s Max.")
            input("AS YOUR VISION IMPROVES, YOU REALIZE WHO THE FIGURE IS.")
            input("We’ve met, you know. Not formally of course. You are quite the fighter. No one had ever defeated me before.")
            s=input("MORALITY> PRESS 1 (GOOD RESPONSE: ASSUMES YOU SPARED THE GUARD PRESS 2 (EVIL RESPONSE: ASSUMES YOU KILLED THE GUARD)")
            if s=='1':
                input("[%s] How did you get here? I thought the only way was through the portal in Morceris’s castle?"%(self.name))
                input("[Max]:Well, if you are the personal Guard of the most powerful alchemist in all the realms, you know how to get through the poison trees and take cross into new lands")
                input("Come to think of it, I was the first human to travel to a new realm in nearly a millenia. I should get a medal.")
                input("[%s] what happened here? What happened to these people?"%(self.name))
                input("The place was destroyed by an Ice dragon. Kinda spooky, huh? How life-like some of them are? Looks like they were frozen yesterday? ")
                input("Nope, frozen many centuries ago. They were probably the last living people until we showed up")
                #input("")

            else:
                input("[%s] I thought I killed you. I stabbed you in the Chest."%(self.name))
                input("That you did. Sort of. Through the years in his servitude, I learned how to brew various potions")
                input("One of which is the Elixir of Life. I’m an alchemy prodigy you could say. ")
                input("I’m totally kidding. I couldn’t even make a proper ale. I stole it from Morceris’s collection.")
                input("Come to think of it, that decision probably spared your life. So, you owe me two lives now. ")
                input("After you stabbed me in the chest, the potion did its work and here I am, minus a few details about how in Oblivion I got here. ")
                input("[%s]: I needed to get passed you. You would have tried to kill me the moment I turned my back on you.% (self.name)")
                input("[Max]: Would I have though? Surely you realize I was under a spell. A spell that, oddly enough, faded after you bested me. ")
                input("Probably something to do with his whole plan with you. By the looks of you, it would appear he succeeded. But whatever, we both did what we had to do. ")
                input("The place was destroyed by an Ice dragon, if you're curious. Kinda spooky, huh? How life-like some of them are? Looks like they were frozen yesterday?")
                input("Nope, frozen many centuries ago. They were probably the last living people until we showed up")
            input("[%s]: So are you going to untie me? Or are you going to leave me here and wait for the ice dragon to come? %(self.name)")
            print("[Max]: I thought about that. I would have a pretty good chance of killing it as it was eating you. But then I figured since you defeated Morceris,")
            input("and me for that matter, you would be more helpful up and about.")
            input("[MAX UNTIES YOU]")
            input("[%s]: You really killed all that opposed you?"%(self.name))
            input("[Max]: Aye, every last one")
            input("[%s]: But that was Morceris’s spell controlling you. So that wasn’t you."%(self.name))
            input("[Max]: Yes and no. I had to kill them, but I was trained to fight by my mother. Whatever skills I had under the spell are the same skills as I have now. ")
            print("[%s]: I met your mother. She’s in Korifstead. I didn’t know at the time, and I do not think she knew you were the Guard."%(self.name))
            input("[%s] She said I had to kill him to get to Morceris."%(self.name))
            input("[Max]: Perhaps. I always thought she would figure it out. I was taken as a teenager by Morceris’s men and my body was never found. ")
            input("[%s]: Has the guard always been here? Surely they would have figured out it was you when the Guard showed up."%(self.name))
            input("[Max]: The Guard is a title and to gain the title you must kill the previous Guard. ")
            input("[%s]: That way each incarnation of me has a personal Guard."%(self.name))
            input("[Max]: Looks like you got stuck with me. Lucky you!")
            input("YOU AND MAX SEE A FLASH OF PURPLE FOLLOWED CLOSELY BY A RUSH OF WIND AND A DEAFENING ROAR.]")
            input("[%s]: What in Oblivion...?"%(self.name))
            input("END OF MISSION 2")
            input("[PRESS ENTER TO WALK OUTSIDE AND START NEXT MISSION(Œ)]")
        if world.isGobCave(self.x, self.y):
            input("AFTER FOLLOWING THE DROPPED COINS, YOU REACH THE MOUTH OF A CAVE.")
            input("[Max] Great. It went into a cave. Definitely won’t be ambushes or anything. We’ll just sneak right in undetected.")
            input("[%s] Come on. We don’t have any other choice."%(self.name))
            input("YOU AND MAX ENTER THE CAVE(Ŏ) AND TRY TO FIND THE GOBLIN AND YOUR SUPPLIES")
        if world.trapGold(self.x, self.y):
            print("WHILE OPENING THE CHEST, YOU ACTIVATED A SPIKE TRAP.")
            print("YOU LOST 10 HEALTH")
            self.hp=self.hp-10
            input("+20 GOLD.")
            self.gold=self.gold+20
            if self.gold > self.maxgold:
                self.gold = self.maxgold
        if world.realGold(self.x, self.y):
            print("WHILE OPENING THE CHEST, YOU ACTIVATED A FLAMETHROWER.")
            print("YOU LOST 20 HEALTH")
            self.hp=self.hp-20
            input("+200 GOLD.")
            self.gold=self.gold+200
            if self.gold > self.maxgold:
                self.gold = self.maxgold
        if world.morcMission6(self.x, self.y):
            input("MISSION 8: OH GOOD, MORE SKELETONS ")
            input("YOU AND MAX SUCCESSFULLY DEFEAT THE GUARD. YOU AND MAX HEAD TOWARDS THE CASTLE TO FIND THE ENTRANCE")
            print("-THE DOORS TO THE CASTLE ARE BLACK WITH GLOWING PURPLE RUNES ALL AROUND THEM.")
            input("SMALL SPIKES COVER THE DOORS AND THE HANDLES ARE MADE OF HUMAN SPINES.")
            input("-YOU TAKE A HOLD OF THE SPINES AND PUSH THE DOORS OPEN.")
            print("THE HALL OF THE CASTLE IS LIT ONLY BY CANDLES WEDGED IN BETWEEN THE TEETH..")
            input("OF DRAGON SKULLS HANGING ON EACH OF THE 8 PILLARS THAT HOLD UP THE TOWERING CEILING. ")
            input("[%s] Guess we’re not the first dragon slayers. "%(self.name))
            input("Max: Not even close.")
            input("AT THE BACK OF THE CASTLE IS A LARGE THROWN MADE OUT OF THE SKULLS OF DRAGONS, HUMANS, GOBLINS, AND TROLLS ALIKE. ")
            input("A BLACK CLOUD FORMS ON THE THRONE AND FADES AWAY TO REVEAL A DARK FIGURE WITH A WHITE CLOAK.")
            input("AS IT STANDS UP OFF THE THRONE, YOU SEE ITS SKIN IS DECAYED AND ROTTEN")
            input(" ITS RIB CAGE AND STERNUM ARE BLACK AND CAN BE EASILY SEEN BEHIND FOLDS OF SKIN")
            input("THE ONLY THING LEFT OF ITS FACE IS A BLACKENED SKULL. ")
            input("AS HE MOVES CLOSER, YOU SEE THAT HIS WHITE CLOAK IS MADE OUT OF SMALL BONES HELD TOGETHER BY BLACK STRINGS AND TISSUE.")
            input("HE SPEAKS WITH A LOW, DARK VOICE")
            print("[Dalthuur] Hello, my brother. Judging by your young appearance, it would appear that your plan has succeeded. ")
            print("I see that you have chosen quite the talented Guard. She made quick work of the Chestplate.")
            s=input("MORALITY> {PRESS 1} (GOOD RESPONSE)     {PRESS 2} (EVIL RESPONSE) ")
            #s=int(s)
            if s=='1':
                
                
                input("[%s] I am not your brother, and I have no memory of my passed life."%(self.name))
                input("[Dalthuur] Pity, I suppose even a successful plan has its flaws. At least the prior generations were able to awaken me")
                input("Strange, though, I have not the faintest idea how the plan would have succeeded if each generation had this flaw. ")
                input("Perhaps some outside event of sorts occurred. ")
                input("[Max] There was, Deadmeat. My mother and my father sabotaged his castle nearly a decade ago. ")
                input("...They must have really messed something up.")
                input("[Dalthuur] Hmmm, Deadmeat. How…clever. And considering that I am awake and have nearly completed the ritual to..")
                input("...bring back my brother Shanzalar, I really do not think your parents were of much consequence.  ")
                input("[%s] Their actions created me; that’s consequence enough. I am the Morzana. I will defeat you and Shanzalar like I defeated Morceris"%(self.name))
                input("[Dalthuur] Well, that is unfortunate. My brother was so close. Just one unforeseen event has created major complications. ")
                input("[%s] You and your brothers are finished. We will defeat you and Shanzalar will never be awoken. I will fulfill my destiny as Morzana."%(self.name))
                input("[Dalthuur] Yes, yes. The Morzana, the protector of light and all that. Tell me: have you seen the true power of the mask? ")
                w=input("EVENT> {PRESS 1} (YOU HAVE USED THE MASK OF MORZANA BEFORE)    {PRESS 2} (YOU HAVE NOT USED THE MASK OF MORZANA)")
                #w=int(w)
                if w=='1':
                    input("[%s] Yes, I used it. The power is enough to kill you."%(self.name))
                    input("[Dalthuur] Not the most heroic of weapons, now is it?")
                    input("[%s] Compared to use it is."%(self.name))

                else:
                    input("[%s] No, I planned to use it on you."%(self.name))
                    input("[Dalthuur] I think you will find it…unnatural. It is not the most heroic of weapons.")
                    input("[%s]  Compared to use it is."%(self.name))
                input("[Dalthuur] Perhaps. Well, let’s end these pleasantries. I have no need of a memoryless meatbag. Prepare to die!")
                input("DALTHUUR SLOWLY RISES INTO THE AIR AND YOU SEE DARK PURPLE ORBS OF ENERGY APPEAR IN HIS HANDS..")
                input("...YOU SEE SKELETONS RISE FROM THE GROUND. ")
                input("[Max] Alright, this is where the fun begins")
                input("YOU AND MAX DESTROY THE SKELETONS AND PREPARE TO FIGHT DALTHUUR")
                
            else:
                self.moral=self.moral-1
                if self.moral==-4:
                    self.morals='the Soulless'
                input("YOUR DECISION HAS DECREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                
                print("[%s] Hello, Brother. Unfortunately, the prior generation of me must have had complications"%(self.name))
                input("...and was unable to provide me with memory of my passed life. ")
                input("...My guess is that my Guard’s rebel mother had something to do with it.")
                input("MAX GLARES AT YOU. SHE NO LONGER TRUSTS YOU")
                input("[Dalthuur] Pity, I suppose even a foolproof plan can be thwarted by outside nuisances. ")
                input("[Max] I trusted you, %s. You can’t betray me and join him."(self.name))
                input("[Dalthuur] Poor girl, [speaking to player] she really has no idea you have been controlling her. ")
                input("[Max] That’s impossible! I told him about this place and led him here. ")
                input("[Dalthuur] Why, Morceris, your powers have grown. You see, darling, Morceris has this ability to plant thoughts into people’s mind. ")
                #input("-	Max: That doesn’t explain anything. He said it himself, he doesn’t even remember who he is.")
                input("[Max] That doesn’t explain anything. He said it himself, he doesn’t even remember who he is; let  alone know how to find this place.")
                #input("-	2Player: True, but you do. I simply had to look inside your mind and I learned all I needed to get you here.")
                input("[%s] True, but you do. After you untied me back in Horastead,  I looked into your eyes and you were under my control."%(self.name))
                input("...You’ve been under my control ever since. All I have to do is flick my wrist and you will do my bidding.")
                input("Or, if I have no more use of your services, inspire you to kill yourself.")
                input("Max: I swear I will kill y-")
                input("YOU FLICK YOUR WRIST AND HER BACK STRAIGHTENS UP. SHE STANDS MOTIONLESS")
                input("[Dalthuur] Now that we have the pleasantries completed; brother, would you enjoy the honor of finishing the final ritual? ")
                input("Once he’s released, we can use the island portal and travel to Shadovar together.")
                input("[%s] I would indeed. Shanzalar has slept long enough."%(self.name))
                input("[Dalthuur]: I-")
                input("[%s]: However, I have no intention of you coming with me"%(self.name))
                input("Dalthuur: What!?")
                input("[%s]: You see, I don’t need you. I need your power. Your cloak should do."%(self.name))
                #input("-	Dalthuur: You will never possess the cloak. I would crumble to dust without it.")
                input("Dalthuur: You will never possess the cloak. I will die before you obtain my cloak.")
                input("[%s] That was the idea. Sorry, brother. "%(self.name))
                input("Dalthuur: Well, brother, COME AND GET IT!")
                input("DALTHUUR SLOWLY RISES INTO THE AIR AND YOU SEE DARK PURPLE ORBS APPEAR IN HIS HANDS")
                input("YOU SEE SKELETONS RISE FROM THE GROUND. THEY EACH HAVE A BLACK SWORD, A SPIKED SHIELD, AND BLACKENED, BRONZE, HORNED HELMETS")
                input("[%s] Come Max. You have work to do. Kill them!"%(self.name))
                input("MAX, STILL IN A TRANCE, GRABS HER SWORD AND STARTS KILLING THE SKELETONS")
                input("YOU AND MAX KILL THE SKELETONS AND PREPARE TO FIGHT DALTHUUR ")
            input("PRESS 's' TO ATTACK DALTHUUR(Ӂ)")
        if world.dalFinalDec(self.x, self.y):
            input("DALTHUUR’S BODY LIES ON THE GROUND. HIS EXPOSED RIB CAGE MOVES UP AND DOWN SLOWLY; HE IS STILL ALIVE. ")
            s=input("MORALITY> {PRESS 1} (GOOD ENDING)     {PRESS 2} (EVIL ENDING) ")
            #s=int(s)
            if s=='1':
                self.moral=self.moral+1
                if self.moral==3:
                    self.morals='the Savior'
                input("YOUR DECISION HAS INCREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                input("[Dalthuur] What…have you…done, brother? What happened to you? We were supposed to travel to Shadovar and awaken Shanzalar.")
                input("[%s]: Again, not your brother. And nothing has happened to me. I’m not Morceris."%(self.name))
                print("[Dalthuur] I…don’t understand. I invented and created the portal to send your past self to the future at will")
                input("... There were no flaws, no oversights. Even with the…complications, you should have your memory.")
                input("Max: It’s been a long time since you invented it. It may not work. Ever thought of that, necromancer?")
                input("Dalthuur: Hush, girl. You haven’t the slightest idea whats really going on. ")
                input("[%s] What!? Whats going on? What aren’t you telling us?"%(self.name))
                input("Dalthuur: What is your name, girl?")
                input("Max: I have no reason to tell you my name. ")
                input("[%s] Just tell him. I’ll cut his head off myself if he has the slightest indication of ill-will."%(self.name))
                input("Max: My name's Maxine.")
                input("DALTHUUR GROANS")
                input("Dalthuur: Not your first name, idiot. Your family name.")
                ####
                input("Max: Mercer")###########
###########################
                input("Dalthuur: Interesting. And what, pray tell, is your mother's family name?")
                input("Max: Tierren")
                print("Dalthuur: A descendant of Alderis Tierren and Xeros Mercer. The Shadovar Elf who successfully lead the armies of man and Elf against us. And the..")
                print("...coward who sent an entire legion of Morzala Bandit's to their deaths. I gladly used some of their bones for my Guard.")
                input("...Quite the turn of events. I see you have Alderis's Shadovar Elf eyes, girl. You clearly do not possess Xeros's cowardice, fortunately.")
                print("Heroics and cowardice aside, your parents knew what they were doing..")
                print("...when they first attacked Morceris’s Castle. Probably damaged part of the portal")
                print("Morceris always enjoyed the phrase, 'keep your allies close and your enemies closer'.")
                input("I suppose that explains why he chose you as his Guard. Or…")
                input("DALTHUUR LOOKS AT MAX AND PAUSES")
                ############################
                print("Dalthuur: Perhaps your mother had something to do with it. A young, mixed-race descendant of Alderis and Xeros on the inside.. ")
                input("...Even after mating with the bandit coward, the Shadovar Elf blood still runs through your veins.")

                input("Max: NO! She lost her husband that night. She would do everything to protect me.")
                input("Dalthuur: Or perhaps she just gave up on you? Decided to give you up in exchange for protection? Her entire bloodline is full of trait--")
                input("MAX YELLS AND SLICES THE MANGLED HEAD OFF OF THE DECAYING BODY. ")
                input("THE BLACKENED SKULL ROLLS AROUND ON THE GROUND BEFORE STOPPING AT YOUR FEET.")
                input("DALTHUURS HEAD TURNS TO DUST AND THE REST OF HIS BODY FOLLOWS. ALL THAT IS LEFT IS HIS CLOAK OF BONES. ")
                input("MAX YELLS AGAIN IN ANGER, THEN KICKS THE CLOAK OF BONES")
                input("[%s] It’s ok Max. It's over."%(self.name))
                print("YOU PICK UP THE CLOAK. IT IS POWERLESS AND NOTHING MORE THAN A COLLECTION OF HUMAN BONES.")
                input("Max: Dammit! I should not have done that. He was giving us information.")
                input("[%s] No, he was stalling. Look: "%(self.name))
                input("YOU AND MAX RUN UP TO A WINDOW. THE ISLAND OF SHADOVAR IS IN THE DISTANCE. A RING OF ENERGY HANGS ABOVE THE EASTERN-MOST PART OF IT")
                input("THE ENERGY RING STARTS TO SWIRL DOWNWARD INTO THE GROUND.")
                input("ONCE ALL THE ENERGY IS GONE FROM THE SKY, A MASSIVE SHOCKWAVE PULSES FROM THE EPICENTER AND CRASHES INTO THE CASTLE.")
                input("YOU AND MAX ARE THROWN BACK BY THE BLAST. YOU SLOWLY AND GET UP AND LOOK AT EACH OTHER")
                input("Max: Shanzalar has awoken.")
                input("AS SHE SAYS THIS, THE CASTLE BEGINS TO CRUMBLE. THE DRAGON SKULLS TUMBLE TO THE GROUND BEHIND YOU")
                input("[Max] We have to get of here")
                input("YOU AND MAX RUN OUT OF THE COLLAPSING CASTLE")
                input("[%s] How do we get to Shadovar?"%(self.name))
                input("Max: Through a portal, just like you the one you took to get here.")
                input("[%s] Where is his portal?"%(self.name))
                input("Max: I have a hunch. I saw an island in between here and Shadovar. It’s completely surrounded by magik. Only a portal requires that much magik.")
                input("[%s] Let’s hope your right. Come on, let's go to Shadovar"%(self.name))
                


            else:
                input("DALTHUUR’S BODY LIES ON THE GROUND. HIS EXPOSED RIB CAGE MOVES UP AND DOWN SLOWLY; HE IS STILL ALIVE. ")
                input("Dalthuur: What…have you…done, brother? What happened to you? We were supposed to travel to Shadovar and awaken Shanzalar.")
                input("[%s] Like I said, I do not need you. Never did. "%(self.name))
                input("Dalthuur: You have betrayed your kind. Shanzalar will destroy you.")
                input("[%s] I doubt that. You were not much of a challenge"%(self.name))
                print("Dalthuur: I forget. You don’t remember him. You feared him more than anything. He is the most powerful being in the whole kingdom. ")
                input("...Stronger than me and certainly stronger than you.")
                input(" [%s]We shall see"%(self.name))
                input("[%s] Oh, before I kill you: you probably want to know what failed? Why I don’t remember anything? Max, come here."%(self.name))
                input("MAX SLOWLY WALKS TOWARDS YOU, STILL IN A TRANCE")
                input("Dalthuur: I don’t understand")
                input("[%s] Really? It appears your brain has rotted more than it looks. This is Max."%(self.name))

                input("Dalthuur: And..That’s supposed to mean something to me?")
                #######################3

                print("[%s] Certainly not. It’s her surname name, Mercer. I’m a little fuzzy on the history, but you should know Xeros Mercer"%(self.name))
                print(" Dalthuur: The coward Bandit Lord who had a legion of Morzala Bandits die by my hand? I didn't think he could have a family after people realized his cowardice.")
                input("[%s]...She is also a descendant of Alderis Tierren. You must surely remember than name.")

                input("	Dalthuur: Impossible.  ")
               
                input(" [%s] Afraid not. What did Alderis do? Destroy you and your brother? Sent Morceris into hiding for nearly a century?"%(self.name))
                print(" [%s] From what I worked out, her mother is his descendant and she knew about the portal... "%(self.name))
                print("...She goes in and damages it, but she gets captured and her husband is killed.. ")
                print("...She eventually is freed, but only at the price of her only daughter, Max..")
                input("...That’s how Morceris ended up with her as his Guard.")
                print("YOU LOOK AT MAX")
                print("[%s] Poor girl."%(self.name))
                input("MAX STIFFENS AND LETS OUT A STIFFLED GRUNT")
                input(" [%s] Hush, girl. There’s nothing you can do about that. I’d suggest you keep quiet if you want to remain alive."%(self.name))
                input("DALTHUUR STARTS TO LAUGH. BLACK LIQUID DRIPS TO THE FLOOR BELOW HIS MOUTH AND HE COOUGHS UP MORE.")
                print("Dalthuur: You may have killed me. But I stalled you. Shanzalar is awakened and there is nothing you can do to stop him. ")
                input("You will soon learn why you feared him so much.")
                input("[%s] How marvelous. You see, Dalthuur, I was waiting for you  to do just that.. "%(self.name))
                input("...I could never awaken Shanzalar without your cloak at full power.. ")
                input("...And killing you would release all that power, rendering it useless..")
                input("...I feared I would have to rip it off your alive body and that stress would damage it..")
                input("...rendering it useless anyway. But now, I have absolutely no fears of that happening. You already awakened him.")
                print("YOU STEP OVER DALTHUUR’S BODY AND PULL THE CLOAK OFF. LIGHTNING JUMPS FROM THE CLOAK AS YOU PEEL IT OFF HIS BODY. ")
                input("DALTHUUR LETS OUT A CRY OF PAIN AS THE CLOAK IS FINALLY RIPPED FREE")
                input("ONCE THE CLOAK IS COMPLETELY DETACHED, A SHOCKWAVE PUSHES YOU AND MAX TO THE GROUND. ")
                input("DALTHUUR REMAINS MOTIONLESS ON THE GROUND")
                print("YOU LOOK AT THE CLOAK AND SMILE. ")
                input("[%s] It would appear my fears, although reasonable, did not come to fruition."%(self.name))
                print("YOU PULL THE CLOAK OVER YOUR BODY. YOU FEEL A RUSH OF ENERGY. ")
                input("THE BONES INSIDE YOUR BODY QUIVER AND THE THRONE OF BONES STARTS TO SHAKE.")
                input("YOU AND MAX WALK UP TO A CASTLE WINDOW. THE ISLAND OF SHADOVAR IS IN THE DISTANCE")
                input("A RING OF ENERGY HANGS ABOVE THE EASTERN MOST PART OF IT. THE ENERGY RING STARTS TO SWIRL DOWNWARD INTO THE GROUND. ")
                input("ONCE ALL THE ENERGY IS GONE FROM THE SKY, A MASSIVE SHOCKWAVE PULSES FROM THE EPICENTER AND CRASHES INTO THE CASTLE.")
                input("YOU AND MAX ARE THROWN BACK FROM THE BLAST")
                input("YOU SLOWLY GET UP AND LOOK TOWARDS MAX, WHO IS STILL LYING ON THE GROUND")
                input("[%s] Come Max. It’s time we introduce ourselves to the most powerful being in Hjaron"%(self.name))
                input("YOU SNAP YOUR FINGERS AND SHE RELAXES")
                input("Max: What did you do to me?")
                input("[%s] I am sorry for all that. I needed Dalthuur to awaken Shanzalar. I couldn’t have you kill him before he had done so."%(self.name))
                input("Max: Mind control, really?")
                input("[%s] A necessary precaution"%(self.name))
                input("Max: You bastard. I trusted you.")
                input("[%s] You have three options: you follow my orders, I use mind control and make you follow my orders, or I kill you, again."%(self.name))
                input("THE CASTLE BEGINS TO CRUMBLE. THE DRAGON HEADS FALL TO THE GROUND BEHIND YOU ")
                input("Max: [she pauses for a few moments, noticing the collapsing ceiling, fists clenched] Fine, I’ll follow you.")
                input("[%s] I hoped you’d come to your senses. You’ll forgive me eventually. You forgave your mother, right?"%(self.name))
                input("Max: I don’t know. I didn’t think I had to forgive her for anything.")
                input("[%s] Come on.  Let’s get out of this ruin. "%(self.name))
                input("YOU AND MAX RUN OUT OF THE COLLAPSING CASTLE")
                input("[%s] You see that island? It's surrounded by powerful magik. Inside the island is the portal to Shadovar."%(self.name))
                input("[Max] How do you know that?")
                print("[%s] I saw the island when the ring of enrgy came down. Only a portal.."%(self.name))
                input("...needs to be surrounded by magik like that.")
                input("...Come on, Max. Let's go meet the most powerful being in all of Hjaron.")
            
            input("*-----{MORCENGARDE QUESTLINE COMPLETE}-----*")
            input("TRAVEL THROUGH THE PORTAL (Ꝋ) AND TRAVEL TO SHADOVAR")
            
            
        
   ######################################################## #Move East(d)     
    def moveRight(self, world):
        #print(self)
        self.x=self.x+1
        self.hp=self.hp
        #Player hits a token
        
        #################################################MERCHANTS################################3
        if world.isExit(self.x, self.y):
            xtCoord = self.x
            ytCoord = self.y
            self.x = self.xCoord
            self.y = self.yCoord
            playGame(game_world, self)
            self.x = xtCoord
            self.y = ytCoord
        if world.isExit2(self.x, self.y):
            xhCoord = self.x
            yhCoord = self.y
            self.x = self.xCoordH
            self.y = self.yCoordH
            playGame(game_worlda, self)
            self.x = xhCoord+1
            self.y = yhCoord
        
        if world.Merchant1(self.x, self.y): ###MERCHANT 1###HAS THE NEW WAY OF BUYING THINGS: DIFFERENT SUBSECTIONS FOR DIFFERENT ITEMS
            #HAVE TO INDENT ALMOST ALL THE LINES WHEN WE COMBINE THIS WITH MERCHANT 2
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("Merchant Inventory: Health Potions, Magik Potions, Arrows, Stamina Potions, Spell Books")#ADDED THIS, CHANGE FOR HIGHER MERCHANTS
                p=input("[Merchant] Would you like to sell or buy an item? ['sell', 'buy', 'no']")
                while p=='sell':
                    if self.snow<0:
                        self.snow=0
                    print("%s's Inventory: Snow Storm %d "%(self.name, self.snow-1))
                    p=input("[Merchant] Do you have more you wish to barter, Adventurer? ['sell', no]")
                    
                          
                
                s=input("Would you like to puchase an item? [yes, no]")#ADDED THIS 
                while self.gold>0 and s=='yes':##ADDED THIS, INDENTED EVERYTHING BELOW THIS
                    print("You have %s Gold, Adventurer"%(self.gold))
                    print("-----PRESS 7 TO EXIT-----")
                    f=input("PRESS: (1) HEALTH POTIONS  (2) MAGIK POTIONS (3)  ARROWS  (4) STAMINA POTIONS (5) SPELL BOOKS:  ")  
                    if f=='1':
                        i=(5*(self.maxhp-self.hp))
                        g=input("Health Potions: 1{Max Health, %d gold} 2{+10 hp, 50 gold}  3{+20 hp, 100 gold}  "%(i))
                        if g=='2':
                            c=50
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##                 
                                self.gold=self.gold-c
                                self.hp=self.hp+10
                                if self.hp>self.maxhp:
                                    self.hp=self.maxhp
                                print("YOU PURCHASED 10 HP FOR 50 GOLD")
                    
                        if g=='3':
                            c=100
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.hp=self.hp+20
                                if self.hp>self.maxhp:
                                    self.hp=self.maxhp
                                print("YOU PURCHASED 20 HP FOR 100 GOLD")
                        if g=='1':
                            c=i
                        
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.hp=self.hp+(c/5)
                                if self.hp>self.maxhp:
                                    self.hp=self.maxhp
                                print("YOUR HEALTH WAS FULLY RESTORED FOR %d GOLD"%(c))
                    
                        else:
                            pass
                                  
                    if f=='2':
                        t=(8*(self.maxmagik-self.magik))
                        y=input("Magik Potions: 1{Max Magik, %d gold} 2{+10 magik, 75 gold}  3{+20 magik, 150 gold}"%(t)) 
                        if y=='2':
                            c=75
                            if self.gold<c:
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:                    
                                self.gold=self.gold-c
                                self.magik=self.magik+10
                                if self.magik>self.maxmagik: #does not go over max health
                                    self.magik=self.maxmagik
                                print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                        if y=='3':
                            c=150
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.magik=self.magik+20
                                if self.magik>self.maxmagik:
                                    self.magik=self.maxmagik
                                print("YOU PURCHASED 20 HP FOR 100 GOLD")
                        if y=='1':
                            c=t
                        
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.magik=self.magik+(c/5)
                                if self.magik>self.maxmagik:
                                    self.magik=self.maxmagik
                                print("YOUR HEALTH WAS FULLY RESTORED FOR %d GOLD"%(c))
                    
                        else:
                            pass         
                               
                    if f=='3':
                    
                        t=(10*(self.maxarrows-self.arrows))
                        y=input("Arrows: 1{Full Quiver, %d gold} 2{+5 Arrows, 50 gold}  3{+10 Arrows, 100 gold}"%(t))
                        if y=='2':
                            c=50
                            if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:                
                                self.gold=self.gold-c
                                self.arrows=self.arrows+5
                                if self.arrows>self.maxarrows: #does not go over max health
                                    self.arrows=self.maxarrows
                                print("YOU PURCHASED 5 ARROWS FOR 50 GOLD")
                        if y=='3':
                            c=100
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.arrows=self.arrows+10
                                if self.arrows>self.maxarrows:
                                    self.arrows=self.maxarrows
                                print("YOU PURCHASED 10 ARROWS FOR 100 GOLD")
                        if y=='1':
                            c=t
                        
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.arrows=self.arrows+(c/10)
                                if self.arrows>self.maxarrows:
                                    self.arrows=self.maxarrows
                                print("YOUR QUIVER WAS FILLED FOR %d GOLD"%(c))
                    
                        else:
                            pass
                    
                
                    if f=='4':
                    
                        t=(5*(self.maxstam-self.stam))
                        y=input("Stamina Potions: 1{Max stamina, %d gold} 2{+10 stamina, 50 gold}  3{+20 stamina, 100 gold}"%(t))
                        if y=='2':
                            c=50
                            if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:                
                                self.gold=self.gold-c
                                self.stam=self.stam+10
                                if self.stam>self.maxstam: #does not go over max health
                                    self.stam=self.maxstam
                                print("YOU GAINED 10 STAMINA FOR 50 GOLD")
                        if y=='3':
                            c=100
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.stam=self.stam+10
                                if self.stam>self.maxstam:
                                    self.stam=self.maxstam
                                print("YOU GAINED 20 STAMINA FOR 100 GOLD")
                        if y=='1':
                            c=t
                        
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.stam=self.stam+(c/5)
                                if self.stam>self.maxstam:
                                    self.stam=self.maxstam
                                print("YOUR STAMINA WAS FULLY RESTORED FOR %d GOLD"%(c))
                    
                        else:
                            pass
                    if f=='5':
                        y=input("SPELL BOOKS: 1{Snow Storm 200 Gold} 2{Mystic Arrow 75 Gold}")
                        if y=='1':
                            c=200
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:                
                                self.gold=self.gold-c
                                self.snow=self.snow+1
                                
                                print("YOU ARE HANDED A WHITE AND SILVER BOOK. YOU OPEN IT AND ICE AND SNOW FLOWS FROM THE PAGES AND INTO YOUR CHEST")
                                print("SPELL ACQUIRED: <SNOW STORM> CREATE A SNOW STORM THAT ALWAYS AFFECTS THE ENEMY BUT DOES LITTLE DAMAGE")
                                #if self.snow==0:
                                    #self.snows='<LOCKED>'
                                if self.snow>0:
                                    self.snows='Snow Storm {-5mag}'
                        if y=='2':
                            c=75
                            if self.gold<c: 
                                print("I'm sorry adventurer, you do not have enough gold for that.")
                            if self.gold>c or self.gold==c:##
                            
                                self.gold=self.gold-c
                                self.mystic=self.mystic+1
                               
                                print("YOU ARE HANDED A BROWN AND GREEN BOOK WITH GLOWING BLUE ARROWS ON THE FRONT. YOU OPEN IT AND A BLUE ARROW FLYS INTO YOUR QUIVER")
                                print("SPELL ACQUIRED: <MYSTIC ARROWS> USE MAGIK TO SHOOT MYSTIC ARROWS FROM YOUR BOW.")
                                if self.mystic>0:
                                    self.mystics='Mystic Arrow {-1mag}'

                        
                    
                    print("You have %d/%d Gold, Adventurer."%(self.gold,self.maxgold))###ADDED THIS
                    s=input("[Merchant] Do wish to buy more, Adventurer? [yes, no]")###ADDED THIS
                    
                    if f=='7':
                    
                        print("Safe Travels, Adventurer!")
                    else:
                        pass #print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        if world.Merchant2(self.x, self.y): ###MERCHANT 2###HAS THE NEW WAY OF BUYING THINGS: PURCHASE AS MANY ITEMS AS YOU WANT
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                
                    
                print("Merchant Inventory: Health Potions, Magik Potions, Arrows, Stamina Potions")#ADDED THIS, CHANGE FOR HIGHER MERCHANTS
                s=input("Would you like to puchase an item? [yes, no]")#ADDED THIS 
                while self.gold>0 and s=='yes':##ADDED THIS, INDENTED EVERYTHING BELOW THIS
                    #s=input("[Merchant] Do my wears interest you, Adventurer? [yes, no]") 
                    print("-----PRESS 7 TO EXIT-----")
                    f=input("PRESS: (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION  {50 GOLD}:  ")
                #f=int(f)
                    c=5
                    if f=='1':
                        if self.gold<c: #MOVED THIS BACK ONE TAB
                            print("I'm sorry adventurer, you do not have enough gold for that.")
                        if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                            self.gold=self.gold-c
                            self.hp=self.hp+10
                            if self.hp>self.maxhp:
                                self.hp=self.maxhp
                            print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                    c=75
                    if f=='2':
                        if self.gold<c:#MOVED THIS BACK ONE TAB
                            print("I'm sorry adventurer, you do not have enough gold for that.")
                        if self.gold>c or self.gold==c:                    
                            self.gold=self.gold-c
                            self.magik=self.magik+10
                            if self.magik>self.maxmagik: #does not go over max health
                                self.magik=self.maxmagik
                            print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                    c=50
                    if f=='3':
                        if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                            print("I'm sorry adventurer, you do not have enough gold for that.")
                        if self.gold>c or self.gold==c:                
                            self.gold=self.gold-c
                            self.arrows=self.arrows+20
                            if self.arrows>self.maxarrows: #does not go over max health
                                self.arrows=self.maxarrows
                            print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                    c=50
                    if f=='4':
                        if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                            print("I'm sorry adventurer, you do not have enough gold for that.")
                        if self.gold>c or self.gold==c:                
                            self.gold=self.gold-c
                            self.stam=self.stam+10
                            if self.stam>self.maxstam: #does not go over max health
                                self.stam=self.maxstam
                            print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    print("You have %d/%d Gold, Adventurer."%(self.gold,self.maxgold))###ADDED THIS
                    s=input("[Merchant] Do wish to buy more, Adventurer? [yes, no]")###ADDED THIS
                    
                    if f=='7':
                        pass
                        print("Safe Travels, Adventurer!")
                
                    else:
                        print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        if world.Merchant3(self.x, self.y): ###MERCHANT 3
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION  {50 GOLD} (5) BUY 1 INFERNO SCROLL {250 GOLD}:  ")
                
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                   
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.inferno=self.inferno+1
                        if self.inferno>self.maxinferno: #does not go over max health
                            self.inferno=self.maxinferno
                        print("YOU PURCHASED 1 INFERNO SCROLL FOR 250 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        if world.Merchant4(self.x, self.y): ###MERCHANT 4
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                   (5) BUY 1 MAXIMUM HEALING  SCROLL {250 GOLD}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
            
                elif f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
            else:
                print("Till next time, Adventurer!")
                
        
        if world.Merchant6(self.x, self.y): ###MERCHANT 6
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD}  (4) BUY 1 STAMINA POTION {50 GOLD}                  (5) BUY 1 INFERNO SCROLL {250 GOLD}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.ultimhp=self.ultimhp+1
                        if self.ultimhp>self.maxultimhp: #does not go over max health
                            self.ultimhp=self.maxultimhp
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")

        if world.Merchant7(self.x, self.y): ###MERCHANT 7
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                               (5) BUY 1 INFERNO SCROLL {250 GOLD}  (6) BUY 1 SOUL {150}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 75 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.blizzard=self.blizzard+1
                        if self.blizzard>self.maxblizzard: #does not go over max health
                            self.blizzard=self.maxblizzard
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                        
                    
                c=400
                if f=='6':
                    print("Adventurer, this is some dark magic. Use it carefully.")
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.morzana=self.morzana+1
                        if self.morzana>self.maxmorzana: #does not go over max health
                            self.morzana=self.maxmorzana
                        print("YOU PURCHASED 1 SOUL FOR 150 GOLD")
                    
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")

        if world.Merchant8(self.x, self.y): ###MERCHANT 8
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION {50 GOLD}                                (5) BUY 1 INFERNO SCROLL {100 GOLD}:  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 50 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.blizzard=self.blizzard+1
                        if self.blizzard>self.maxblizzard: #does not go over max health
                            self.blizzard=self.maxblizzard
                        print("YOU PURCHASED 1 BLIZZARD SCROLL FOR 250 GOLD")
                    
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")

        if world.Merchant9(self.x, self.y): ###MERCHANT 5
            f=input("[Merchant] Hello Adventurer! Would you like to browse my wears? [yes, no]")
            if f=='yes':
                print("-----PRESS 7 TO EXIT-----")
                f=input("PRESS (1) BUY 1 HEALTH POTION {50 GOLD}  (2) BUY 1 MAGIK POTION {75 GOLD} (3) BUY 20 ARROWS {50 GOLD} (4) BUY 1 STAMINA POTION                              (5) BUY 1 THUNDERSTORM SCROLL {250 GOLD} (6) 10 UMBRA ARROWS {200 GOLD} :  ")
                #f=int(f)
                c=50
                if f=='1':
                    if self.gold<c: #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:###########3I THINK WE HAVE TO MOVE THESE AROUND TO MAKE SENSE                  
                        self.gold=self.gold-c
                        self.hp=self.hp+10
                        if self.hp>self.maxhp:
                            self.hp=self.maxhp
                        print("YOU PURCHASED A 10 HP POTION FOR 50 GOLD")
                    
                c=75
                if f=='2':
                    if self.gold<c:#MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                    
                        self.gold=self.gold-c
                        self.magik=self.magik+10
                        if self.magik>self.maxmagik: #does not go over max health
                            self.magik=self.maxmagik
                        print("YOU PURCHASED A 10 MAGIK POTION FOR 50 GOLD")
                    
                c=50
                if f=='3':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.arrows=self.arrows+20
                        if self.arrows>self.maxarrows: #does not go over max health
                            self.arrows=self.maxarrows
                        print("YOU PURCHASED 20 ARROWS FOR 50 GOLD")
                    
                c=50
                if f=='4':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.stam=self.stam+10
                        if self.stam>self.maxstam: #does not go over max health
                            self.stam=self.maxstam
                        print("YOU PURCHASED 10 STAMINA FOR 50 GOLD")
                    
                

                c=500
                if f=='5':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.thunder=self.thunder+1
                        if self.thunder>self.maxthunder: #does not go over max health
                            self.thunder=self.maxthunder
                        print("YOU PURCHASED 1 THUNDERSTORM SCROLL FOR 250 GOLD")
                    
                c=200
                if f=='6':
                    if self.gold<c: #DID NOT #MOVED THIS BACK ONE TAB
                        print("I'm sorry adventurer, you do not have enough gold for that.")
                    if self.gold>c or self.gold==c:                
                        self.gold=self.gold-c
                        self.umbra=self.umbra+10
                        if self.umbra>self.maxumbra: #does not go over max health
                            self.umbra=self.maxumbra
                        print("YOU PURCHASED 10 UMBRA ARROWS FOR 200 GOLD")
                    
                if f=='7':
                    pass
                    print("Safe Travels, Adventurer!")
                else:
                    print("I'm sorry, Adventurer. I do not have that item.")
                
            else:
                print("Till next time, Adventurer!")
                
        if world.isWall(self.x, self.y):
            print("ouch! You have been poisoned")
            self.hp=self.hp-1
            self.x=self.x-1
            
        if world.isWall2(self.x, self.y):
            self.x=self.x-1
            
        if world.isWall3(self.x, self.y):
            self.x=self.x-1
        if world.isCaveWall(self.x, self.y):
            self.x=self.x-1
       
        #Mountain
        if world.isMountian1(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x-1
        if world.isMountian2(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x-1
        if world.isMountian3(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x-1
        if world.isMountian4(self.x, self.y):
            print("You cannot go that way")
            self.x=self.x-1
        if world.isMountian5(self.x, self.y):
            print("You cannot go that way")
            self.x=self.x-1
        if world.isDarkElf(self.x, self.y):
            input("You are blind folded again and escorted by the Dark Elves back to where you were first captured")
            self.x=self.x-2
            self.y=self.y+2
        
        
         #Player goes Out of Bounds
        if world.isBoundary3(self.x, self.y):
            
            self.y=self.x-1
        if world.isBoundary1(self.x, self.y):
            
            self.x=self.x-1
        if world.isBoundary2(self.x, self.y):
            
            self.x=self.x-1
        #Player is underwater
        if world.isWater(self.x,self.y):
            print("You are Underwater")
            self.hp=self.hp
         #Player finds a health or magik potion or arrows

        if world.Smith(self.x, self.y):
            print("YOU HAVE ENTERED THE FORGE.")
            print(" ")
            print("{MAX BOW POINTS=%d} PRESS: (1) FIX BOW COMPLETELY  (10 GOLD PER POINT)   (2) FIX ENOUGH FOR 5 USES(50 GOLD)"%(self.maxbow))
            print(" ")
            f=input("{MAX SWORD POINTS= %d} PRESS: (3) FIX SWORD COMPLETELY  (10 GOLD PER POINT)   (4) FIX ENOUGH FOR 5 USES(50 GOLD)  (5) EXIT:  "%(self.maxsword))
            #f=int(f)
            b=self.maxbow-self.bow
            if f=='1':
                a=10*b
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.bow=self.bow+b
                    if self.bow>self.maxbow:
                        self.bow=self.maxbow
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='2':
                self.bow=self.bow+5
                self.gold=self.gold-50
            c=self.maxsword-self.sword  
            if f=='3':
                a=10*c
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.sword=self.sword+c
                    if self.sword>self.maxsword:
                        self.sword=self.maxsword
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='4':
                self.sword=self.sword+5
                self.gold=self.gold-50
            else:
                pass
        #POTIONS AND GOLD
        if world.hpotion(self.x, self.y): 
            print("+1 Health Potion")
            self.hpotion=self.hpotion+1
            if self.hpotion>self.maxhpotion:
                self.hpotion=self.maxhpotion
        if world.mpotion(self.x, self.y): 
            print("+1 Magik Potion")
            self.mpotion=self.mpotion+1
            if self.mpotion>self.maxmpotion:
                self.mpotion=self.maxmpotion
        if world.coins(self.x, self.y):
            self.gold=self.gold+1
            if self.gold>self.maxgold:
                self.gold=self.maxgold
                ##########################PORTAL TO AMODERA
        if world.PortalA(self.x, self.y):
            input("YOU HAVE ENTERED AMODERA")
            self.x=self.x-78
            self.y=self.y-23
        
         #PLayer finds MainQuest1   ########## MQ 1########################
        if world.MainQuest1(self.x, self.y):
            input("MISSION 1")
            print("You wake up in an unknown forest. The trees block out most of the sunlight, and they appear to secrete a dark, black ooze. ")
            print("You look around and see an old man standing in front of you. His face is withered and shrouded by a dark red cloak, but")
            input("something about him seems familiar.")
            print("[Old Man] Greetings Stranger. What brings you to these parts?:")
            s=input("[%s]-PRESS 1: I'm not sure how I got here. PRESS 2: I seem to have lost my whereabouts, and my name.: "%(self.name))
            #s=int(s)
            if s=='1':
                print("[Old Man] Well Stranger, I cant tell you how you got here, but you have found yourself in the land of Hjaron, ruled")
                print("by the Sorceror Morceris. This place may seem magical, but it is plagued with scum and evil creatures.")
            elif s=='2':
                print("[Old Man] Well Stranger, I cannot help you find your name, but you are in the land of Hjaron, ruled")
                print("by the Sorceror Morceris. This place may seem magical, but it is plagued with scum and evil creatures.")
            
            else:
                print("[Old Man] Don't talk much, do ya Stranger? That's alright. You're in the land of Hjaron, ruled by the Sorceror Morceris.")
                print("[Old Man] This place may seem magical, but it is plagued with scum and evil creatures.")
                
            input("[%s]  What sort of scum?"%(self.name))
            input("[Old Man] Well, there is a bandit camped a ways south of here. He has been causing mayhem and pillaging the village Korifstead.")
    
            input("[%s] I still do not know who I am, but I seem to remember I was a trained warrior. I beleieve I can rid the land of that scum."%(self.name))
            input(" TRAVEL TO THE SOUTHERN BANDIT CAMP (Ѧ) AND DEFEAT THE BANDIT. AFTER, HEAD TO MISSION 2 (Ω)")
            input("[END OF MISSION 1]")
            self.story=self.story
            
            #####################  #MQ 2#########################
        if world.MainQuest2(self.x, self.y) and self.story>0:
            input("MISSION 2")
            input("[Villager]Oh ,hello traveller,I have not seen you before. Who are you? Where did you come from?")
            print("[%s]"%(self.name), " I don't know my real name, but for now I'm calling myself, %s."%(self.name))
            input("[%s] I woke up in this forest. I ran across a bandit and defeated him, but I am injured and tired from battle"%(self.name))
            print("[Villager] Oh why thank you traveller that bandit had been terrorizing this village for months. Here, take this, you need it more than I.")
            input("YOU ARE HANDED AND YELLOW AND ORANGE BOOK WITH A GLOWING, RED HEART ON THE FRONT. AS YOU OPEN IT, YOU FEEL A RUSH OF WARMTH AND YOUR WOUNDS ARE HEALED.")
            input("<SPELL ACQUIRED> HEALING   USE MAGIK TO HEAL YOUR WOUNDS DURING BATTLE")
            self.heal=1
            if self.heal==0:
                self.heals='<LOCKED>'
            if self.heal==1:
                self.heals='Healing Spell {-3mag}'
            print("[Merchant] Thank you again, %s. That's all I have, but if you need more supplies, there are merchants scattered around this land."%(self.name))
            input("If you have the coin, they can help you. If you don't have the coin, you can find health potions scattered around this land.")
            input("I wish you luck on your travels, friend. I'd say be weary of bandits, but they don't seem to bother you.")

            input("MISSION: FIND A MERCHANT($ ₡ ₿ ₵ ₴ € ฿ Ŀ §) AND BUY A POTION{optional} AND/OR FIND A HEALTH(ᴥ) AND MAGIK(ϫ) POTION ")
            
            print("END OF MISSION HEAD TO MISSION 3(Ψ)")
            self.story=2
            ##########################MQ3###################
        if world.MainQuest3(self.x, self.y) and self.story>1:
            input("MISSION 3")
            input("ENCOUNTER FRANTIC, SCARED MINERS WHO HAVE BEEN ATTACKED BY A CAVE TROLL, PREVENTING THEM FROM MINING.")
            input("[Miner]Help!")
            input("[%s] What is the problem?"%(self.name))
            input("[Miner] A cave troll has attacked our mine. We can't work while that foul beast is in there. Please adventurer, will you help us?")
            input("[%s] You shall be rid of that beast at once."%(self.name))
            input("[Miner] Oh thank you, adventurer! Here take my gold as payment. It's not much, but it's all I got.")
            self.gold=self.gold+57
            if self.gold>self.maxgold:
                self.gold=self.maxgold
            print("[Miner] Be careful adventurer, that beast wears enchanted armor that makes it nearly impossible to kill. But if you do somehow")
            input("manage it, you can obtain the armor for yourself.")
            input("[Miner] If you do kill it, return here.")
            print("GO INTO THE CAVE 'Ō' AND KILL THE CAVE TROLL '¤'")
            self.story=3

            input("TRAVEL TO KORIFSTEAD(Ξ) AND START MISSION 4 AFTER KILLING THE CAVE TROLL.")
            #################MQ4
        if world.isCave2(self.x,self.y):
            print("AS YOU GO DEEPER, IT BECOMES IMPOSSIBLE TO SEE ANYTHING. YOU CAST A FIREBALL AND HOLD THE FLAME IN YOUR HAND")
            input("THE FIREBALL CASTS A WARM GLOW ON THE CAVE WALLS. AS YOU WALK FARTHER INWARD, YOU HEAR A LOW GROWL.")
        if world.isCave3(self.x,self.y):
            input("YOU LOOK TOWARDS THE SOURCE AND SEE A LARGE MOUND OF ROCKS. YOU A TAKE STEP CLOSER AND KICK A MINER'S HELMET.")
            input("THE HELMET CLATTERS AROUND UNTIL IT HITS THE MOUND OF ROCKS.")
            input("SUDDENLY, THE MOUND OF ROCKS STARTS TO MOVE. YOU SEE A LARGE ROCK HAND GRAB A TREE TRUNK AND PUSH ITSELF UP.")
            input("ONCE THE TROLL FULLY STANDS UP, IT LOOKS DOWN AT YOU AND OPENS ITS LARGE ROCK MOUTH AND ROARS.")
            input("IT RAISES THE TREE TRUNK AND YOU FEEL IT SMASH INTO YOU AND SENDS YOU CRASHING INTO THE CAVE WALLS.")
            input("YOU LOST 3 HEALTH")
            self.hp=self.hp-3
            self.story=4
        if world.MainQuest4a(self.x, self.y) and self.lydiaStory == 1:
        #Right
            input("[Lydia] He didn't have to. He was never imprisoned. He disappeared just after his brothers were defeated. He wasn't seen for a nearly half a millenia.")
            input("[Lydia] Then he returned. He impersonated a wealthy king from outside the kingdom of Hjaron. A land called Morzala...")
            input("...Before we realized who he really was, it was too late. He used his potions of obedience and spread his control over the entire land.Few managed to escape.")
            input("[%s] That must have 500 years ago. How are people still under his control? How do I know you aren't under his control."%(self.name))
            input("[Lydia] You don't. The potion trickles down through the generations. All I can tell you is that my bloodline is immune to it.")
            input("[%s] Have you tried to attack him? Surely they are others who aren't affected."%(self.name))
            input("[Lydia] My husband, Orin, and I and a dozen others made an assault on his castle and tried to understand how he has lived so long.")
            input("[Lydia] Most of them were killed by his Guard. A powerful monster that has been here as long as Morceris has.")
            input("... My husband and I and a few others managed to escape and scale the castle's tallest tower and find and destroy everything we could.") 
            input("[Lydia] My husband must have damaged something important because Morceris killed him the slowest. He had his beast kill the others, but...")
            input("LYDIA PAUSES, SHE LOOKS DOWN FOR A FEW MOMENTS AND CONTINUES TO WALK THROUGH HER HOUSE.")
            self.lydiaStory = 2
        if world.SerpentMission(self.x, self.y) and self.story>5:
            input("MISSION: A MYSTERIOUS CREATURE")
            print("AS YOU CONTINUE YOUR QUEST TO FIND MORCERIS, YOU COME ACROSS A LAKE. YOU PEER INTO THE DISTANCE AND SEE")
            input("A LARGE CREATURE BREACH THE WATER AND PLUNGE BACK UNDERNEATH.")
            input("INVESTIGATE THE LAKE AND THE MYTERIOUS CREATURE.")
            print("AS YOU APPROACH THE EDGE OF THE LAKE, YOU SEE A SMALL ROCK OUTCROP IN THE CENTER OF THE LAKE, EXACTLY WHERE YOU")
            print("NOTICED THE STRANGE CREATURE. SWIM OVER AND INVESTIGATE THE CREATURE (Ѯ)")
            self.story=7

        if world.isRuinRoom(self.x, self.y):
            input("YOU CRAWL THROUGH THE OPENING AND FIND YOURSELF IN A ROOM FILLED WITH A SOFT GREEN LIGHT. IN THE CENTER OF THE ROOM LIES A LARGE BLACK OBELISK.")

            input("YOU WALK TOWARDS THE OBELISK NOTICE CRACKS ALONG THE SURFACE. AS YOU PEER CLOSER YOU SEE GREEN LIGHT RADIATING OUT FROM THEM.")
            input("YOU PLACE YOUR HAND ON THE OBELISK AND THE VOICE RETURNS. IT GETS LOUDER AND LOUDER AND THE ROOM BEGINS TO SHAKE.")
            input("THE CRACKS ON THE OBELISK GROW UNTIL THE ENTIRE OBELISK CRUMBLES, REVEALING AN OCTAHEDRON. IT LEVITATES ABOVE THE GROUND, UNMOVING.")
            input("THE OCTAHEDRON BURSTS OPEN. YOU ARE SENT FLYING BACKWARDS BY THE POWER OF IT. YOU LOOK BACK AND SEE A GREEN TINTED GHOST EMERGE FROM IT.")
            input("THE GHOST HAS ITS BACK TURNED TO YOU AND REMAINS STILL, AS IF IT DOES NOT HEAR YOU.")
            input("YOU SLOWLY GET UP, TRYING NOT TO ALERT THE GHOST. AS SOON AS YOU MOVE, THE GHOST IMMEDIATELY TURNS AROUND, REVEALING ITS BLACK SKELETAL FORM")
            input("THE GHOST WEARS A GREEN MASK WITH FLAMES FLAMES COMING OUT THE BACK. RUNES SIMILAR TO THE ONES ON THE OCTAHEDRON ARE ETCHED AROUND THE EDGES OF IT.")
            input("THE GHOST SCREECHES AND ITS BODY BECOMES ENGULFED WITH GREEN FLAMES.")
            input("YOUR HANDS BECOME ENGULFED IN FLAMES AS YOU PREPARE TO FIGHT IT.")
            input("[STEP FORWARDS TO FIGHT THE GHOST]")
            self.story=9
        if world.isPedestal(self.x,self.y):
            self.x = self.x - 1
        if world.largeChest(self.x, self.y):
            input("+300 GOLD.")
            self.gold=self.gold+300
            if self.gold > self.maxgold:
                self.gold = self.maxgold
            input("+10 ARROWS")
            if self.arrows > self.maxarrows:
                self.arrows = self.maxarrows
            input("+1 HEALTH POITION")
            if self.hpotion > self.maxhpotion:
                self.hpotion = self.maxhpotion
            input("+1 MAGIK POTION")
            if self.mpotion > self.maxmpotion:
                self.mpotion = self.maxmpotion


        if world.MorcerisDoor(self.x,self.y) and self.story> 11:
            
            input("YOU ARRIVE AT THE DOOR TO THE CASTLE. THE DOORS ARE BLACK WITH DARK RED CRACKS THAT JUT ACROSS IT LIKE ROOTS FROM A TREE.")
            print("THE RED CRACKS PULSE; GROWING BRIGHTER AND THEN DIMMER. YOU CAN FEEL THE POWER RESONATING FROM IT.")
            print("YOU PLACE YOUR HAND ON THE DOOR AND IT OPENS IMMEDIATELY. YOU WALK IN AND UNSHEATH YOUR SWORD.")
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 1
            self.y = 5
            playGame(game_worlde1, self)
            self.x = xCoord
            self.y = yCoord
            
        if world.MorcerisCastle(self.x,self.y) and self.story> 11:
            print("MORCERIS SITS ON A THRONE MADE OUT OF HUMAN BONES. HE WEARS A DARK RED CLOAK WITH ARCHAIC SYMBOLS ETCHED INTO THE FABRIC.")
            input("HE HOLDS A CURVED, BLACK STAFF TOPPED WITH A FLAMING COBRA'S HEAD. HE OPENS HIS MOUTH AND SPEAKS WITH A LOW, RASPY VOICE.")
            input("[Morceris] I see you have found me, %s. It would appear that my Guard has failed me. Pity, I put a lot of work into the mind-control spell."%(self.name))
            input("[Morceris] Poor innocent girl, I was going to set her free if she was able to kill you; give her back to that rebel mother of hers.")
            input("[Morceris] But no matter, I can always find a new Guard. There are plenty of potential servants in this realm.")
            input("[Morceris] I assume you have come to kill me then? Rid the kingdom of me and restore peace to it?")
            input("[Player] Yes, I have. I am the Morzana and I'm destined to destroy you. I will bring peace to this land.")
            input("[Morceris] Very well. Step forward and seal your destiny.")
            input("PRESS 'w' TO ATTACK MORCERIS.")
            self.story=13

        if world.FinalDecision(self.x,self.y) and self.story>12:
            input("MORCERIS'S BODY LIES CRUMPLED ON THE GROUND. YOU REMOVE HIS HOOD WITH THE TIP OF YOUR SWORD TO SEE THE FACE OF YOUR ENEMY.")
            input("[Player] No, it cant be.")
            input("YOU REALIZE THE OLD MAN AND MORCERIS ARE THE SAME PERSON. IN ANGER, YOU RAISE YOUR SWORD TO STRIKE HIM DOWN.")
            input("[Morceris] WAIT!! Before you strike me down, you must know who you truly are. You are me.")
            input("[Morceris] When you arrived, I was visiting the place that brought me to this wretched world. I was expecting you.")
            input("[Morceris] As I was walking towards it, I saw you materialize on the ground before me.")
            input("[Morceris] Just like you, I was greeted by an old man. And now, you are confronted with the same decision that I had to make.")
            input("[Morceris] As you can see, I am old and sick. You must take my place and find Dalthuur. You must awaken Shanzalar and retake the kingdom.")
            input("[Morceris] This is your destiny. Take my staff and live the life you were meant for.")
            input("YOU CAN TAKE MORCERIS'S STAFF AND CONTINUE THE RULE OF MORCERIS.")###
            input("BUT THAT MEANS CONDEMNING THE ENTIRE KINGDOM TO LIVE UNDER A TYRRANICAL RULE. IN ORDER TO END THIS CYCLE OF TERROR, YOU MUST KILL MORCERIS.")###
            print(">MORALITY PRESS 1: Kill Morceris now and end his reign of terror, knowing that you might end up just like him later, OR")
            s=input("Do you--PRESS 2: Take his staff and unite with Dalthuur and Shanzalar to rule over the kingdom?: ")
            #s=int(s)
            if s=='1':#good ending
                self.moral=self.moral+1
                if self.moral==2:
                    self.morals='the Guardian'
                input("YOUR DECISION HAS INCREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                print("YOU THRUST YOUR BLADE THROUGH HIS CHEST. AS THE LIFE SEEPS AWAY FROM MORCERIS, YOU SEE HIM FADE INTO NOTHING.")
                print("ALL YOU CAN DO IS HOPE THAT YOU NEVER END UP LIKE HIM. YOU MUST DO EVERYTHING POSSIBLE TO NOT TURN INTO MORCERIS AND STOP THE CYCLE.") 
                print("YOU SEE HIS STAFF ON THE GROUND. IT NO LONGER HAS THE FIRE AND APPEARS POWERLESS. YOU TAKE THE STAFF FOR SAFE KEEPING.")##THIS IS SORT OF DUMB, BUT OHWELL
                input("YOU REMEMBER THE RUIN AND NOW UNDERSTAND WHAT COULD HAPPEN IF DALTHUUR AND SHANZALAR ARE AWAKENED.")
                input("YOU MUST TRAVEL TO MORCENGARDE AND DEFEAT DALTHUUR.")
                
                #self.hp=0##############DESCRIBE WHY THE PLAYER WOULD HAVE THE STAFF IF THEY DIDNT TAKE THE STAFF
                #########MAYBE, YOU TAKE THE STAFF, BUT ONLY IF YOU CHOOSE THE BAD ENDING DO YOU GET ITS POWER
                self.hp=self.maxhp                
                self.magik=self.maxmagik              
                self.arrows=self.maxarrows
                self.stam=self.maxstam
                self.morc=0
            else: #bad ending
                self.moral=self.moral-1
                if self.moral==-2:
                    self.morals='the Corrupt'
                input("YOUR DECISION HAS DECREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                print("YOU TAKE MORCERIS'S STAFF, AND YOU FEEL THE POWER OF IT FLOW THROUGH YOUR VEINS. YOU FEEL DIFFERENT.")
                print("THE ITEM HAS TURNED EVERY LAST BIT OF GOOD IN YOU INTO DARKNESS.")
                print("EVERYTHING BECOMES CLEAR TO YOU. THE CYCLE MUST CONTINUE IN ORDER TO MAKE YOU AND YOUR REIGN OF TERROR IMMORTAL.")
                input("YOUR PAST SELF MUST BE BROUGHT TO THE FUTURE AND CORRUPTED, JUST AS YOU WERE.")
                input("AS YOU TOUCH THE TOP PART OF THE STAFF, YOU SEE A VISION OF THE SAME STRANGE LAND YOU SAW IN THE RUIN.")
                input("THIS TIME IS DIFFERENT, IT SHOWS DALTHUUR IN HIS TOMB. YOU SEE HIS DARK PURPLE EYES OPEN AND THE TOMB EXPLODES.")
                input("YOU MUST FIND THE TOMB AND JOIN DALTHUUR.")
                
                
                self.hp=self.maxhp                
                self.magik=self.maxmagik              
                self.arrows=self.maxarrows
                self.stam=self.maxstam
                self.morc=self.maxmorc
            input("YOU START TO LEAVE THE CASTLE, BUT YOU HERE A LOUD CRACK COME FROM THE BACK OF THE ROOM.")
            input("--MOVE TOWARDS THE 'Ѻ' TO INVESTIGATE.")
       # if world.PortalM(self.x,self.y):
            

        ################portal to morcengarde
        if world.PortalM(self.x, self.y):#(29,2)
            input("YOU MOVE TOWARDS THE BACK OF THE CASTLE AND SEE LARGE CRACKS FORM A SPIDERWEB-LIKE PATTERN ON THE BACK WALL.")
            input("SUDDENLY, THE WHOLE WALL BREAKS REVEALING A PURPLE VORTEX. YOU TRY TO EVADE IT BUT ARE SUCKED INTO IT ALONG WITH MUCH OF THE CASTLE...")
            input("AND THEN EVERYTHING GOES BLACK.")
            input("*-----{AMODERA QUESTLINE COMPLETE}-----*")
            self.story=14
            input("YOU HAVE ENTERED MORCENGARDE")
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 58
            self.y = 4
            playGame(game_world, self)
            self.x = xCoord
            self.y = yCoord
            
            self.x=self.x+14
            self.y=self.y+2
            
        ###################MORCENGARDE
        if world.morcIntro(self.x, self.y):
            print("AFTER DEFEATING MORCERIS IN AMODERA, YOU TRAVEL THROUGH THE PORTAL TO MORCENGARDE. YOU ARRIVE IN A BARREN LAND VOID OF ANY VEGETATION.")
            input("LIKE AMODERA, THERE ARE POISON TREES COVERING MUCH OF THE LANDSCAPE. ")
            input("YOU LOOK AROUND AND TRY TO FIND A CLEARING OR A PATH OUT OF THE FOREST")
            input("AS YOU WANDER AROUND, YOU HEAR SOMETHING MOVING AROUND THE FOREST. ")
            input("YOU LOOK AROUND, BUT SEE NOTHING BUT POISON TREES. YOU CONTINUE LOOKING FOR AN EXIT AND EVENTUALLY FIND A CLEARING.")
            input("THERE IT IS AGAIN, THE RUSTLING. YOU LOOK AROUND AGAIN, BUT STILL ONLY SEE TREES.")
            input("YOU DRAW YOUR SWORD AND CREATE A FIREBALL IN YOUR HAND FOR LIGHT.")
            input("SUDDENLY, A TREE MOVES AS IF IT WERE ALIVE AND HUMANOID. THE CREATURE RAISES ITS HAND AND DOZENS OF POISON DARTS FLY AT YOU. ")
            input("YOU RAISE YOUR SHIELD JUST IN TIME AND THE DARTS SLAM INTO IT.")
            input("PRESS ENTER AND MOVE TO ATTACK IT(ϔ).")
            print("AFTER DEFEATING THE TREE CREATURE, CONTINUE TO STRǾMVAR(Ƿ)")
        #if world.isTreeDead(self.x, self.y):
            #print("YOU LOOK DOWN AT THE CREATURE AND WATCH IT SLOWLY DRY OUT AND TURN TO DUST. YOU CONTINUE ON YOUR QUEST. GO TO STROMVAR(Ƿ)")
            
        if world.StrǾmvar(self.x, self.y):
            print("MISSION 1: THE FROZEN VILLAGE OF STROMVAR ")
            input("AFTER TRAVELLING THROUGH THE TREES AND INTO THE CLEARING, YOU FIND AN AMBANDONED TOWN")
            input("THE TOWN IS IN DISREPAIR AND APPEARS TO HAVE BEEN ABANDONED FOR CENTURIES. A FROST AND SNOW COVERED SIGN READS 'VILLAGE OF STRǾMVAR'")
            input("YOU CONTINUE FARTHER INTO THE TOWN AND FIND SKELETONS AND FROZEN CORPSES." )
            input("STRANGELY ENOUGH, THEY APPEAR TO HAVE JUST BEEN FROZEN MERE MOMENTS AGO. IT COULD NOT HAVE BEEN THE CLIMATE OR THE WEATHER. ")
            input("THE AIR IS MILD AND THE ENTIRE LANDSCAPE IS ARID. SOMETHING ELSE MUST HAVE DONE THIS TO THEM.")
            input("YOU CONTINUE FARTHER INTO THE TOWN AND LOOK INTO DIFFERENT BUILDINGS.")
            input("YOU HOPE TO FIND SOME CLUE OF WHAT THIS PLACE USED TO BE OR WHAT HAPPENED, BUT ALL YOU FIND IS FROZEN BODIES. ")
            input("CONTINUE TO HORASTEAD (Ħ) AND START MISSION 2")
        if world.Horastead(self.x, self.y):
            print("MISSION 2: A FAMILIAR FACE")
            input("YOU CONTINUE THE NEXT TOWN. YOU FIND A FALLEN OVER SIGN THAT READS, “HORASTEAD”. ")
            input("THIS TOWN IS NOT NEARLY AS DESTROYED, BUT THE FROZEN BODIES ARE JUST AS NUMEROUS. ")
            input("YOU EXPLORE ONE OF THE LARGER HOUSES IN HOPES OF FINDING A FEW CLUES.")
            input("AS YOU SEARCH AROUND THE LOWER FLOOR, YOU HERE CREAKING COMING FROM THE FLOOR ABOVE.")
            input("PRESS ENTER TO INVESTIGATE")
            input("YOU SLOWLY, AND QUIETLY WALK UP THE STAIRS; CAREFUL TO AVOID THE MANY HOLES AND UPTURNED NAILS.")
            input("AFTER YOU REACH THE TOP, YOU SEE A FLASH OF BLACK COME FROM AROUND THE CORNER AND EVERYTHING GOES DARK.")
            input("PRESS ENTER TO CONTINUE")
            input("AS YOU REGAIN CONSCIOUSNESS, YOU REALIZE YOU ARE TRAPPED AND UNABLE TO WIGGLE FREE")
            input("YOU TURN YOUR HEAD AROUND AND SEE THE PARTIALLY DECOMPOSED FACE OF A DEAD PERSON. ")
            input("YOU GAG QUIETLY AND FEEL SOME PUKE RISE UP YOUR THROAT. AT THAT MOMENT, YOU SEE A DARK FIGURE COME TOWARDS YOU.")
            input("[Voice] Not a fan of my friend, huh? If you live here long enough, you’ll get to know him more...")
            input("...There wasn’t a single living soul to talk to, so I got by making conversation with the other housemates. They don’t talk much, though.")
            input("YOU STARE AT THE FIGURE BLANKLY. YOU TRY TO GET A LOOK AT ITS FACE, BUT YOUR EYES ARE STILL BLURRY.")
            input("[Voice] Relax. I’m kidding. Well, mostly kidding. Name’s Max.")
            input("AS YOUR VISION IMPROVES, YOU REALIZE WHO THE FIGURE IS.")
            input("[Max] We’ve met, you know. Not formally of course. You are quite the fighter. No one had ever defeated me before.")
            print("MAX STILL WEARS THE ENCHANTED BLACK GUARD ARMOR. HER RED HAIR IS WORN IN A PONYTAIL. ")
            print("AS YOU LOOK CLOSER AT HER FACE, YOU NOTICE HER SKIN IS A LITTLE GREYER THAN THE HUMANS YOU HAVE ENCOUNTERED.")
            input("YOU LOOK IN HER EYES AND NOTICE THEY HAVE THE SAME ORANGE COLOR AS THE REBEL.")
            s=input("MORALITY> {PRESS 1} (GOOD RESPONSE: ASSUMES YOU SPARED THE GUARD)    {PRESS 2} (EVIL RESPONSE: ASSUMES YOU KILLED THE GUARD): ")
            #s=int(s)
            if s=='1':
                input("[%s] How did you get here? I thought the only way was through the portal in Morceris’s castle?"%(self.name))
                input("[Max] Well, if you are the personal Guard of the most powerful alchemist in all the realms, you know how to get through the poison trees and take cross into new lands")
                input("[Max] Come to think of it, I was the first human to travel to a new realm in nearly a millenia. I should get a medal.")
                input("[%s] what happened here? What happened to these people?"%(self.name))
                input("The place was destroyed by an Ice dragon. Kinda spooky, huh? How life-like some of them are? Looks like they were frozen yesterday? ")
                input("Nope, frozen many centuries ago. They were probably the last living people until we showed up")
                #input("")

            else:
                input("[%s] I thought I killed you. I stabbed you in the Chest."%(self.name))
                input("[Max] That you did. Sort of. Through the years in his servitude, I learned how to brew various potions")
                input("One of which is the Elixir of Life. I’m an alchemy prodigy you could say. ")
                input("..I’m totally kidding. I couldn’t even make a proper ale. I stole it from Morceris’s collection.")
                input("..Come to think of it, that decision probably spared your life. So, you owe me two lives now. ")
                input("..After you stabbed me in the chest, the potion did its work and here I am, minus a few details about how in Oblivion I got here. ")
                input("[%s]: I needed to get passed you. You would have tried to kill me the moment I turned my back on you."% (self.name))
                input("[Max]: Would I have though? Surely you realize I was under a spell. A spell that, oddly enough, faded after you bested me. ")
                input("..Probably something to do with his whole plan with you. By the looks of you, it would appear he succeeded. But whatever, we both did what we had to do. ")
                input("..The place was destroyed by an Ice dragon, if you're curious. Kinda spooky, huh? How life-like some of them are? Looks like they were frozen yesterday?")
                input("..Nope, frozen many centuries ago. They were probably the last living people until we showed up")
            input("[%s]: So are you going to untie me? Or are you going to leave me here and wait for the ice dragon to come?" %(self.name))
            print("[Max]: I thought about that. I would have a pretty good chance of killing it as it was eating you. But then I figured since you defeated Morceris,")
            input("and me for that matter, you would be more helpful up and about.")
            input("[MAX UNTIES YOU]")
            w=input("MORALITY> PRESS 1 (GOOD ACTION: ASSUMES YOU DID NOT TAKE MORCERIS STAFF) PRESS 2 (EVIL ACTION: ASSUMES YOU BECAME MORCERIS)")
            #w=int(w)
            if w=='1':
                print("YOU RUB YOUR WRISTS WHERE THE ROPES ONCE WERE. YOU STAND UP AND WALK OVER TO ")
                print("[%s] Thanks."%(self.name))
            else:
                self.moral=self.moral-1
                if self.moral==-3:
                    self.morals='the Betrayer'
                input("YOUR DECISION HAS INCREASED YOUR MORALITY. YOU ARE NOW KNOWN AS %s %s."%(self.name,self.morals))
                print("YOU REALIZE SHE HAS A MIND OF HER OWN. SHE COULD RUIN YOUR PLAN TO UNITE WITH DALTHUUR AND AWAKEN SHANZALAR.")
                input("YOU USE ONE OF YOUR NEWFOUND ABILITIES: MANIPULATION.")
                input("USE IT TO GAIN HER TRUST AND USE HER TO GET TO DALTHUUR")
                print("KEEP HER ALIVE AND MAKE SURE SHE KEEPS HER SWORD. YOU WILL NEED HER TO DEFEAT DALTHUUR")
                
                print("[%s] Thanks."%(self.name))
                   
            input("[Max] What do you call yourself?")
            print("[%s]"%(self.name), "I arrived in Amodera with no memory. I call myself %s"%(self.name))
            print("[Max] Strange. You arriving with no memory, not your name.")
            input("...I thought Morceris wanted to send you to the future with a memory. Something must have gone wrong.")
            input("[%s] You knew his plan, then?"%(self.name))
            input("[Max] Aye, that I did. I don't know what he wanted with you, though. He never told me.")
            input("[%s] I am Morceris. Well, his past self anyway. I have no memory of my past life, though."%(self.name))
            print("MAX STIFFENS AND REACHES FOR HER SWORD")
            input("[Max] No memory, huh? Does that mean your not going to control my mind again, right? I swear I'll kill you if you do.")
            t=input("MORALITY> PRESS 1 (GOOD RESPONSE: ASSUMES YOU SPARED THE GUARD) PRESS 2 (EVIL RESPONSE: ASSUMES YOU KILLED THE GUARD)")
            t=int(t)
            if t=='1':
                
                input("[%s] None. That's just what Morceris said. I don't believe him. He could have been manipulating me just like he did you."%(self.name))
                input("[Max] Good. I'm still an eye on you. I will not hesitate to kill you.")
                input("[%s] Duly noted."%(self.name))
            else:
                print("[%s] I have no memory, but I know the truth. I am his past self. I defeated him and claimed his staff as my own."%(self.name))
                input("... I will fulfill my destiny. But don't worry, I have no idea how to mind control you even if I wanted to {LIE}. ")
                input("[Max] Fine. I will kill you before I'm forced under the control of Morceris.")
                input("GOOD. SHE HAS NO IDEA SHE IS ALREADY AT YOUR MERCY.")
            input("[Max] Now answer me this: What would an immortal sorceror want with his past self?")
            input("[%s] He's not immortal. His younger, past selves just keep getting sent farther into the future. They replace the him once he's too old."%(self.name))
            input("[Max] Strange. Before Dalthuur and Shanzalar were imprisoned, they ruled for centuries. Perhaps something happened to Morceris and he became mortal.")
            input("[%s] Or, Dalthuur and Shanzalar and Morceris have always been mortal. They just keep sending their young selves to the future."%(self.name))
            input("[Max] Perhaps. I wouldn't count on that, though.")
            input("[%s] You really killed all that opposed you?"%(self.name))
            
            
            input("[Max] Aye, every last one")
            input("[%s] But that was Morceris’s spell controlling you. So that wasn’t you."%(self.name))
            input("[Max] Yes and no. I had to kill them, but I was trained to fight by my mother. Whatever skills I had under the spell are the same skills as I have now. ")
            print("[%s] I met your mother. She’s in Korifstead. I didn’t know at the time, and I do not think she knew you were the Guard."%(self.name))
            input("[%s] She said I had to kill him to get to Morceris."%(self.name))
            input("[Max] Perhaps. I always thought she would figure it out. I was taken as a teenager by Morceris’s men and my body was never found. ")
            input("[%s] Has the guard always been here? Surely they would have figured out it was you when the Guard showed up."%(self.name))
            input("[Max] The Guard is a title and to gain the title you must kill the previous Guard. ")
            input("[%s] That way each incarnation of me has a personal Guard."%(self.name))
            input("[Max] Looks like you got stuck with me. Lucky you!")
            input("YOU AND MAX SEE A FLASH OF PURPLE FOLLOWED CLOSELY BY A RUSH OF WIND AND A DEAFENING ROAR.]")
            input("[%s] What in Oblivion...?"%(self.name))
            input("END OF MISSION 2")
            input("[PRESS ENTER TO WALK OUTSIDE AND START NEXT MISSION(Œ)]")

        if world.morcMission1(self.x, self.y):
            print("MISSION 3: THE BEGINNING OF THE END")
            input("YOU AND MAX RUN OUTSIDE AND SEE THE CLOUDS SHIFT FROM RED TO DARK PURPLE. BOLTS OF BLUE AND PURPLE LIGHTNING SCATTER AROUND CLOUDS")
            input("[Max] Looks like Morceris’s second plan has succeeded. Dalthuur has awoken and escaped his prison.")
            print("[%s] Before I arrived at Morceris’s castle, I entered an ancient ruin and defeated a Ghost of Morzana. When I defeated it, I was granted its mask"%(self.name))
            input("...I was told by a voice in an ancient ruin that Dalthuur is trying to resurrect Shanzalar. We can’t let that happen. ")
            input("[Max] The Mask of Morzana? You have it? Well, you are just full of surprises. If you truly are the Morzana, we might just have a chance.")
            input("[%s] Maybe, we still have to get to Dalthuur’s Castle."%(self.name))
            input("[Max] I’d wager that’s about a 5 days journey. Assuming we don’t get frozen by a frost dragon. ")
            input("[%s] What other creatures lurk in this land?"%(self.name))
            input("[Max] I don’t know. I haven’t travelled far in this land. Certainly nothing the great Morzana cant handle.")
            input("[%s] Well, I’m ready when you are."%(self.name))
            input("[END OF MISSION 3]")
            input("[PRESS ENTER AND TRAVEL TO SURTESTEAD(Д) TO START THE NEXT MISSION]")
            
        if world.Surtestead(self.x, self.y):
            print("MISSION 4: THE LAND OF THE DEAD IS NOT RESPONSIBLE FOR STOLEN GOODS")
            input("AFTER TRAVELLING FOR A DAY AND A HALF, YOU AND MAX COME ACROSS THE OLD VILLAGE OF SURTESTEAD")
            input("[Max] Lets camp here. Travelling during the daytime is dangerous enough. Travelling at night is much worse")
            input("[%s] Agreed. Lets see if the buildings have any supplies."%(self.name))
            input("[Max] Unless youre looking for icicles and frozen meatbags, you wont find much. But whatever.")
            input("YOU AND MAX WALK INTO A FROST COVERED BUILDING AND SEARCH FOR WHATEVER MIGHT BE USEFUL")
            input("AS YOU ENTER THE BUILDING, YOU FEEL THE WARMTH DRAIN FROM YOUR BODY. THE LITTLE BIT OF SUNLIGHT DRIPPING IN CASTS A PURPLE HUE ON THE GROUND")
            input("YOU CREATE A FIREBALL IN YOUR HAND AND LIFT IT UP TO BETTER SEE THE ROOM")
            input("[Max] ooo! Magik! Try not to set anything on fire. And my anything, I mean me. One fireball to the chest from you is enough for me.")
            input("AS YOU MOVE AROUND, YOU NOTICE A SMALL HANDLE ATTACHED TO THE FLOOR BOARDS")
            input("PRESS ENTER TO OPEN SECRET DOOR")
            input("[%s] It won’t budge. Must be locked from the inside"%(self.name))
            input("[Max] Oh no, the great Morzana’s weakness: A locked door. We better pray Dalthuur doesn’t summon the great Door of Lockedness,...")
            print("...or else we might as well give up now. Let me show you how it’s done.")
            input("MAX LIFTS HER BLACK GREAT SWORD FROM HER BACK AND SLIDES IT IN BETWEEN THE CRACKS")
            input("SLOWLY, THE BLADE BEGINS TO GLOW ORANGE, GETTING BRIGHTER AND WHITER BY THE SECOND. ")
            print("SHE SLOWLY MOVES THE BLADE AROUND THE DOOR IN A LARGE CIRCULAR FASHION")
            print("AS THE BLADE MOVES AROUND THE LATCHED DOOR, THE WOOD IGNITES AND SLOWLY BEGINS TO DISINTEGRATE")
            input("AFTER A FEW MOMENTS, THE WOOD CIRCLE CRUMBLES INTO A DARK ROOM")
            input("[%s] Well, that’s one way to do it."%(self.name))
            input("[Max] Come on, lets see whats inside")
            input("YOU BOTH JUMP IN THROUGH THE HOLE")
            
            print("YOU LIFT YOUR HANDS AND CAST ANOTHER FIREBALL. ")
            input("[Max] Woah! ")
            input("YOU SEE THE ENTIRE ROOM IS FILLED WITH GOLD COINS, BRONZE HELMETS, JEWELS, AND COUNTLESS OTHER VALUABLE ITEMS")
            input("[%s] This must have been one of the army’s treasures."%(self.name))
            input("[Max] I’m not so sure about that. Would your treasure include these?")
            input("MAX POINTS TO ONE OF THE CHESTPLATES. AT FIRST YOU DON’T SEE ANYTHING, BUT ON CLOSER INSPECTION, YOU SEE ANOTHER FROZEN CORPSE")
            input("YOU LOOK AROUND THE ROOM AND SEE HELMETS WITH SEVERED HEADS INSIDE THEM, GOLD RINGS STILL RESTING ON THEIR OWNERS HANDS")
            input("[Max] Something dragged these poor souls here. Judging by the assortment of treasure, it could only be one thing: Goblins")
            input("YOU HEAR RUSTLING FROM BEHIND THE STACK OF ARMOR AND YOU SEE A BLUR OF BLACK AND GREEN RUN PAST YOU AND OUT THE OPENING")
            input("[Max] By Oblivion that thing was fast. Shit! Strong, too! That sneaky bastard stole my sword!")
            input("[%s] Stole my gold, too!"%(self.name))
            self.gold=0
            #print("Gold: %d"%(self.gold))
            input("YOU AND MAX RUN OUT OF THE BUILDING, BUT THERE IS NO SIGN OF HIM")
            input("[Max] Dammit! We lost it. Those slimy goblins are fast. There’s no way we’ll catch it. Come on, lets go.")
            input("...I can just use your sword; my sword’s full of dark magic anyway ")
            input("[%s] wait. Look at that."%(self.name))
            input("YOU POINT AT THE GROUND")
            input("[Max] The sneaky goblin’s fast, but he aint so bright, huh? ")
            input("THE GOBLIN LEFT A TRAIL OF GOLD COINS (ₒ) ON THE GROUND. THE PATH LEADS STRAIGHT TO THE GOBLIN")
            input("[Max] Alright, Morzana, let’s go get that goblin.")
            input("END OF MISSION 4")
            input("PRESS ENTER AND TRACK THE GOBLIN (ҩ) TO ITS OTHER HIDEOUT")
        if world.iceLair(self.x, self.y):
            input("MISSION 5: COLD AS COLD CAN BE ")
            input("YOU AND MAX FOLLOWED MAZE OF POISON TREES, NAVIGATING IT THROUGH FEELING. THE COLDER THE TEMPERATURE WAS, THE CLOSER THE DRAGON WAS.")
            input("[Max]  By Morzana, it’s damn cold. Oh, oops, I mean, by you, it’s damn cold. ")
            input("[%s] We have to be close now. Have you ever seen an Ice Dragon? Besides, the flyover, I mean."%(self.name))
            input("[Max] Not directly, just the perhaps overexaggerated depictions of those who have survived the encounters. ")
            input("The survivors say it has black scales and light blue spines that run down the back. The head and jaws were the most popular topics of conversation")
            input("The teeth are like jagged icicles and the eyes are made of pure ice. ")
            input("They say that if you make eye contact, you heart freezes solid.")
            input("[%s] Is it worse than a normal fire dragon?"%(self.name))
            input("Much worse. The Ice Dragon can create a raging blizzard just by flapping its wings. And whatever you do, do not look in the eyes. ")
            input("It is said it will freeze your heart and your blood will turn to ice. ")
            input("[%s] Don’t look at it’s eyes, got it. "%(self.name))
            input("[Max] Pretty much. And avoid its claws,  and hope you can avoid its ice breath, and pray it doesn’t create a giant blizzard. Easy pe—")
            input("[%s] Shh! "%(self.name))
            input("AS YOU ROUND A CORNER, YOU SEE THE ICE DRAGON. THE TEMPERATURE IS UNBEARABLY COLD AND THE GROUND IS COVERED WITH ICE AND SNOW")
            input("DEFEAT THE ICE DRAGON(ʬ)")
            input("END OF MISSION 5")
        
        if world.iceLair2(self.x, self.y):
            input("MISSION 6: WHATEVER MAKES YOU SLEEP AT NIGHT")
            input("YOU AND MAX HAVE DEFEATED THE ICE DRAGON AND CONTINUE ON YOU QUEST TO FIND DALTHUUR")
            print("[Max] I’d say the rumors were correct for once")
            s=input("MORALITY> PRESS 1 (GOOD RESPONSE: ASSUMES YOU SPARED THE GUARD) PRESS 2 (EVIL RESPONSE: ASSUMES YOU KILLED THE GUARD)")
            #s=int(s)
            if s=='1':#good
                print("[%s] I for one never doubted them."%(self.name))
                
                input("[Max] Good for you. Neither did I. There was always a different tone in the room when people talked of the Ice Dragon.")
                input("[%s] I can imagine. But hey, were probably the first to ever kill an Ice Dragon, huh? That makes us the most powerful mortals in the kingdom."%(self.name))
                input("[Max] I don’t know if you qualify as mortal, mate. You could have been born thousands of years ago. ")
                input("[%s] I can still die, though. That means I’m not immortal"%(self.name))
                input("[Max] Sure. Whatever makes you sleep at night.")
                input("[%s] That doesn’t. That’s what keeps me awake at ni--"%(self.name))
            else:#evil
                input("[%s] Eh, it was easy enough with Morceris’s Staff. "%(self.name))
                input("[Max] Well, aren’t you an all-powerful bad-ass? Take that staff away and let’s see how powerful you are. ")
                input("[%s] I defeated the last one who held it previously, so I’d say I’m powerful enough."%(self.name))
                input("[Max] He was an old man and that was his plan, you dolt. It was practically a mercy kill.")
                input("[%s] Say what you will. With or without it, I’m powerful. "%(self.name))
                input("[Max] Sure. Whatever makes you sleep at night.")
            input("[Max] Look, there’s the necromancer’s castle. ")
            print("YOU LOOK THROUGH A GAP IN THE TREES AND SEE A LARGE, DARK CASTLE IN THE DISTANCE. ")
            input("THE CASTLE HAS THREE MASSIVE SPIRES THAT REACH FROM THE GROUND AND INTO THE PURPLE COLORED SKY. ")
            input("[%s] Now there’s just his guard in our way. What’s the difference between you and it?"%(self.name))
            input("[Max] Well, I was chosen by Morceris. Dalthuur created his guard.")
            input(".... It’s apparently a combination of the bones of all the men Dalthuur has killed. It is said to wield a large axe. ")
            input("[%s] Any chance you can reason with it? Guard to Guard?"%(self.name))
            input("[Max] Wouldn’t that be nice? Each Guard is loyal to their master, so unless Dalthuur wants to arrange a sit-down dinner with us, we’re out of luck. ")
            input("[%s] I think we’d be the meal in that case."%(self.name))
            input("[Max] Agreed, that would probably be the case.")
            input("[%s] How do we kill the Guard, then?  "%(self.name))
            print("[Max] I don’t know. Maybe we plan on not getting killed by it and then figure it out from there?")
            c=input("MORALITY> PRESS 1 (GOOD RESPONSE: ASSUMES YOU SPARED THE GUARD) PRESS 2 (EVIL RESPONSE: ASSUMES YOU KILLED THE GUARD)")
            #c=int(c)
            if c=='1':
                input("[%s] Sounds like a plan. Let’s go kill a Guard made of dozens of dead warriors. This should be fun."%(self.name))
                input("[Max] Now you’re starting to think like me. I was worried there for a moment.")
            else:
                input("[%s] Sounds like a plan. Let’s go kill another Guard."%(self.name))
                input("[Max] Hey, I’m right here you know.")
            
            input("END OF MISSION 6: FIND AND DEFEAT THE SKELETON GUARD(Ꝙ)")
        if world.sGate(self.x, self.y):
            if self.ring1==1 and self.ring2==1 and self.ring3==1:
                input("Gate opens")
            else:
                input("Gate cannot open without the three rings")
                self.x=self.x-1
                
                      
          
        
   ##############################################3 #Move West(a)   
    def moveLeft(self, world):
        self.x=self.x-1
        self.hp=self.hp
        #self.moral=self.moral-1
        #Player hits a wall "#"
        if world.isWall(self.x, self.y):
            print("ouch! You have been poisoned")
            self.hp=self.hp-1
            self.x=self.x+1
        if world.isWall2(self.x, self.y):
            self.x=self.x+1
        if world.isWall3(self.x, self.y):
            self.x=self.x+1
        if world.isCaveWall(self.x, self.y):
            self.x=self.x+1
        if world.Horastead(self.x, self.y):
            xCoord = self.x
            yCoord = self.y
            self.x = 1
            self.y = 1
            playGame(mini_world1, self)
            self.x = xCoord
            self.y = yCoord
            
        if world.isEntrance(self.x, self.y):
            xCoord = self.x
            yCoord = self.y
            self.x = self.xCoord
            self.y = self.yCoord #-1
            playGame(game_world, self)
            self.x = xCoord
            self.y = yCoord
        if world.isEntrance2(self.x, self.y):
            xhCoord = self.x
            yhCoord = self.y
            self.x = self.xCoordH
            self.y = self.yCoordH#-1
            playGame(game_worlda, self)
            self.x = xhCoord
            self.y = yhCoord+1
        #Mountain
        if world.isMountian1(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x+1
        if world.isMountian2(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x+1
        if world.isMountian3(self.x, self.y):
            print("That cliff is not climbable")
            self.x=self.x+1
        if world.isMountian4(self.x, self.y):
            print("You cannot go that way")
            self.x=self.x+1
        if world.isMountian5(self.x, self.y):
            print("You cannot go that way")
            self.x=self.x+1
        if world.isMtnCave(self.x, self.y):
            input("You enter the cave and travel through a secret tunnel")
            self.y=self.y-1
            self.x=self.x-5

        #Player goes Out of Bounds
        if world.isBoundary3(self.x, self.y):
            
            self.y=self.x+1
        if world.isBoundary1(self.x, self.y):
            self.x=self.x+1
        if world.isBoundary2(self.x, self.y):
            self.x=self.x+1
            
        #Player is underwater
        if world.isWater(self.x,self.y):
            print("You are Underwater")
            self.hp=self.hp
         #Player finds a health or magik potion or arrows
        if world.Smith(self.x, self.y):
            print("YOU HAVE ENTERED THE FORGE.")
            print(" ")
            print("{MAX BOW POINTS=%d} PRESS: (1) FIX BOW COMPLETELY  (10 GOLD PER POINT)   (2) FIX ENOUGH FOR 5 USES(50 GOLD)"%(self.maxbow))
            print(" ")
            f=input("{MAX SWORD POINTS= %d} PRESS: (3) FIX SWORD COMPLETELY  (10 GOLD PER POINT)   (4) FIX ENOUGH FOR 5 USES(50 GOLD)  (5) EXIT:  "%(self.maxsword))
            #f=int(f)
            b=self.maxbow-self.bow
            if f=='1':
                a=10*b
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.bow=self.bow+b
                    if self.bow>self.maxbow:
                        self.bow=self.maxbow
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='2':
                self.bow=self.bow+5
                self.gold=self.gold-50
            c=self.maxsword-self.sword  
            if f=='3':
                a=10*c
                if self.gold>a or self.gold==a:
                    
                    self.gold=self.gold-a
                    self.sword=self.sword+c
                    if self.sword>self.maxsword:
                        self.sword=self.maxsword
                else:
                    print("YOU DO NOT HAVE ENOUGH GOLD FOR THIS PURCHASE")
            if f=='4':
                self.sword=self.sword+5
                self.gold=self.gold-50
            
            else:
                pass
        #POTIONS AND GOLD
        if world.hpotion(self.x, self.y): 
            print("+1 Health Potion")
            self.hpotion=self.hpotion+1
            if self.hpotion>self.maxhpotion:
                self.hpotion=self.maxhpotion
        if world.mpotion(self.x, self.y): 
            print("+1 Magik Potion")
            self.mpotion=self.mpotion+1
            if self.mpotion>self.maxmpotion:
                self.mpotion=self.maxmpotion
        if world.coins(self.x, self.y):
            self.gold=self.gold+1
            if self.gold>self.maxgold:
                self.gold=self.maxgold
        if world.isDarkElf(self.x, self.y):
            #print
            input("Dark elves bring you to there secret hideout.")
            self.x=self.x+20

        ################MQ3#################
        if world.MainQuest3(self.x, self.y):
            if self.mine==1:
                input("YOU FIND THE MINERS. THE LEAD MINER LOOKS AT YOU WIDE-EYED. HE SLOWLY WALKS TOWARDS YOU.")
                input("[Miner] Oh my, you are actually alive. We thought you would not survive.")
                input("[%s] Well, here I am. Your Cave Troll is dead"%(self.name))
                input("[Miner] Oh thank you, Adventurer.")
                input("[Miner] I'm afraid to admit, but I lied to you. We didn't give you all we had. We thought you would die in there.")
                input("[Miner] Here take this. And, you are always welcome in this mine.")
                self.hp=self.maxhp
                self.gold=self.gold+75
                print("Gold: %d"%self.gold)
                if self.gold>self.maxgold:
                    self.gold=self.maxgold
                input("[%s] I appreciate your gesture of goodwill. Farewell."%(self.name))
                input("[Miner] Farewell, friend.")
            #print("ENTER GAME COMBAT")

                input("CONTINUE ON TO MISSION FOUR(Ξ)")
       
           ###################SERPENT MISSION##############3       
        if world.SerpentMission(self.x, self.y):
            input("MISSION: A MYSTERIOUS CREATURE")
            input("AS YOU CONTINUE YOUR QUEST TO FIND MORCERIS, YOU COME ACROSS A LAKE. YOU PEER INTO THE DISTANCE AND SEE A LARGE CREATURE")
            input("BREACH THE WATER AND PLUNGE BACK UNDERNEATH.")
            input("DO YOU: INVESTIGATE THE LAKE AND THE MYTERIOUS CREATURE PRESS 1, OR CONTINUE ON YOUR JOURNEY: ")

            print("AS YOU APPROACH THE EDGE OF THE LAKE, YOU SEE A SMALL ROCK OUTCROP IN THE CENTER OF THE LAKE, EXACTLY")
            print("WHERE YOU NOTICED THE STRANGE CREATURE. SWIM OVER AND INVESTIGATE THE CREATURE (Ѯ)")
        ######IF PLAYER CHOOSES 1, THEY WILL SWIM OVER TO THE SERPENT AND ONCE THEY HIT THE TOKEN, THEY WILL COMBAT THE SERPENT########
        if world.isPedestal(self.x,self.y):
            self.x = self.x + 1   
        if world.realGold(self.x, self.y):
            print("WHILE OPENING THE CHEST, A BLADE SWINGS OUT OF THE WALL AND SLICES AT YOUR CHEST.")
            print("YOU LOST 20 HEALTH")
            self.hp=self.hp-20
            input("+100 GOLD.")
            self.gold=self.gold+100
            if self.gold > self.maxgold:
                self.gold = self.maxgold
        if world.MorcerisDoor(self.x,self.y) and self.story> 11:
            xCoord = self.x
            yCoord = self.y
            self.xCoord = self.x
            self.yCoord = self.y
            self.x = 12
            self.y = 3
            playGame(game_worlde, self)
            self.x = xCoord
            self.y = yCoord

        if world.isGobCave(self.x, self.y):
            input("YOU AND MAX DEFEATED THE GOBLIN AND RETRIEVE YOUR ITEMS. ")
            input("YOU EXIT THE CAVE AND EMERGE INTO THE DARK PURPLE COLORED LANDSCAPE. ")
            input("[%s] Well, damn. I have no idea where we are. I don’t even know if were closer or farther."%(self.name))
            
            input("YOU LOOK AROUND FOR A FEW MOMENTS AND TRY TO GET YOUR BEARRINGS. ")
            input("[%s] Let’s try going-- "%(self.name))
            input("SUDDENLY, YOU HEAR A SCREECHING, ROAR FROM ABOVE YOU. ")
            input("YOU LOOK UP JUST IN TIME TO SEE A BLACK AND LIGHT BLUE DRAGON FLY OVER YOU")
            input("MEER MOMENTS LATER, THE TEMPERATURE AROUND YOU DROPS AND FROST FORMS ON THE GROUND AND THE POISON TREES")
            input("[Max] Whatever you were going to say, scratch that. We’re going to kill that dragon.")
            input("START OF MISSION 5: FIND THE ICE DRAGON (ʬ) ")
        if world.morcMission7(self.x, self.y):
            print("YOU AND MAX ARRIVE IN A CLEARING. UP AHEAD YOU CAN SEE THE CASTLE IN ITS FULL GLORY. ")
            print("THE THREE SPIRES ARE COVERED IN CURVED SPIKES AND IN THE CENTER THE IS A SPHERE OF PURPLE ENERGY...")
            input("SURROUNDED BY FIVE CURVED SPIKES THAT WRAP AROUND THE OUTSIDE OF IT. IN THE CENTER LIES A SKELETAL FIGURE IN A WHITE AND BLACK CLOAK.")
            input("THERE IS NO SIGN OF ANY SKELETON GUARD.")
            input("[%s] There he is, the necromancer himself. I guess his guard will not be joining us."%(self.name))
            input("[Max] Something doesn’t feel right")
            input("[%s] Maybe the guard was destroyed when Dalthuur was imprisoned?"%(self.name))
            input("[Max] Perhaps. But look, the bones of his fallen enemies are all over the place and there’s no frost, so they weren’t preserved.")
            input("YOU LOOK AROUND AND NOTICE RIB CAGES, SPINES, SKULLS AND TIBEAS SCATTERED AROUND")
            input("AS SHE SAYS THIS, YOU AND MAX SLOWLY WALK TOWARDS THE CASTLE, KEEPING AN EYE ON BOTH THE CASTLE AND THE BONES AROUND THEM.")
            input("AS YOU WALK PASSED EACH OF THE BONES, THEY START TO MOVE SILENTLY BEHIND YOU. ")
            input("[%s] What are you saying?"%(self.name))
            input("[Max]: These bones are the Skeleton Gua-")
            input("BEFORE SHE COULD FINISH HER SENTENCE, THE INDIVIDUAL BONES AROUND MAX MOVE AND FORM A LARGE SKELETAL HAND.")
            input("...THE HAND MOVES QUICKLY LIKE A SPIDER AND GRABS MAX. ")
            input("YOU QUICKLY TURN AROUND AND UNSHEATH YOUR SWORD.")
            input("YOU SEE A  15 FOOT TALL HIDEOUS CONGLOMERATION OF HUMAN SPINES, RIB CAGES, SKULLS, AND TIBEAS")
            input("THE BONES ARE STILL RECONNECTING AS YOU STARE AT IT WIDE-EYED")
            input("THE LEGS ARE ASSYMETRICAL: ONE HAS A SPINE AND RIB CAGES FOR THE THIGH AND ANKLE AND THE OTHER IS A CRUDE COMBINATION OF PELVISES, SKULLS, TIBEAS AND FIBEAS. ")
            input("THE LEGS CONNECT INTO THE TORSO BY LODGING THEMSELVES INTO A PELVIS MADE OF SKULLS.")
            input("THE TOP OF THE LEGS CONNECT TO AN OPEN MOUTH OF A SKULL")
            input("AS YOU MOVE YOUR EYES UPWARD, YOU SEE A RIBCAGE MADE OF HUMERI INSTEAD OF RIBS. ")
            input("THE STERNUM IS MADE OF A COLUMN OF SKULLS AND EACH OF THE HUMERI SLIDE INTO THE MOUTH OF ONE OF THE SKULLS")
            input("AS YOU LOOK UP AT THE HEAD, YOU SEE A HORRID AMALGAMATION OF NEARLY EVERY BONE IN THE BODY")
            input("SPINES AND RIBS MAKE UP THE JAW AND TEETH AND DOZENS OF SCAPULA MAKE UP THE REST OF THE SKULL.")
            input("[Max] Oy! ")
            input("YOU SEE MAX STUCK IN ONE OF THE SKELETON’S HANDS. HER SWORD IS PINNED IN BETWEEN THE BONE FINGERS AND HER BACK.")
            input("[Max] You just gonna stand there? Distract the Guard so I can wriggle free.")
            input("YOU CAST AN INFERNO SPELL AND CREATE A TORNADO OF FIRE. IT CRASHES INTO THE SKELETON SIDES OPPOSITE OF MAX. ")
            self.inferno=self.inferno-1

            input("YOU HEAR A LOUD SCRATCHY ROAR AND IT LETS MAX FREE. SHE DROPS TO THE GROUND.")
            input("[Max] Nice one. Not to micromanage, but next time, could you use that a little sooner?")
            input("[%s]: Your Welcome. "%(self.name))
            input("THE SKELETON STARTS TO LUMBER TOWARDS YOU. IT OPENS ITS PALM TO THE GROUND AND MORE HUMAN BONES BEGIN TO RISE FROM THE GROUND")
            input("WITHIN MOMENTS, THE BONES COME TOGETHER TO MADE A LARGE STAFF.")
            input("THE SKELETON REACHES INTO THE GROUND AND PULLS UP A RUSTED IRON BLADE AND ATTACHES IT TO THE STAFF.")
            input("IT REACHES INTO THE GROUND AGAIN AND PULLS UP A RUSTED, BLACK CHEST PLATE AND ATTACHES IT TO THE SKULL-LINED STERNUM.")
            input("...A BRIGHT PURPLE (Ӂ) CAN BE SEEN ON THE FRONT")
            print("[Max] Well, this just got even more fun. That chest-plate is enchanted. It cannot be killed until it is removed.")
            input("..I’ll worry about getting that chest piece off, you take over from there. ")         
            input("YOU DISTRACT THE SKELETON GUARD WHILE MAX RUNS UNDER AND STARTS CLIMBING ONE OF THE LEGS; USING THE RIB CAGES AS MAKESHIFT LADDERS")   
            print("MAX CLIMBED UP THE SKELETON'S BACK AND THRUST HER GLOWING RED SWORD INTO THE TOP OF THE CHESTPLATE.")
            print("THE CHESTPLATE EXPLODES AND LAUNCHES MAX OFF THE SKELETON GUARD'S BACK.")
            input("[Max] Alright, %s, you're up. I'll work on crippling its legs, you destroy the rest of him"%(self.name))
            print("MOVE TOWARDS THE SKELETON GUARD (Ꝙ) AND DEFEAT IT")


##############################################################################
        
        if world.isTown(self.x, self.y):
            xCoord = self.x
            yCoord = self.y
            self.x = 1
            self.y = 1
            playGame(mini_world1, self)
            self.x = xCoord
            self.y = yCoord
            
###########################################################################
    #Getter
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getSymbol(self):
        return self.symbol

    def isAlive(self):
        if self.hp>-100:   ##DECIDES WHETHER PLAYER IS ALIVE used to be 0
            if self.hp<1 and self.hp>-100:
                
                print("YOU DIED")
                self.lives=self.lives-1
                print("YOU HAVE %d LIVES LEFT"%(self.lives))
                if self.lives==0:
                    self.hp=-100
                    return
                s=input("DO YOU WISH TO CONTINUE? [yes,no]: ")
                if s=='yes':
                    print("YOU ARE REBORN")
                    self.hp=self.maxhp#add the others
                    self.magik=self.maxmagik
                    self.stam=self.maxstam
                    self.arrows=self.maxarrows
                    self.bow = self.maxbow
            
                elif s=='no':
                    q=input("ARE YOU SURE?[yes,no]: ")
                    if q=='yes':
                        self.hp=-100
                        return
                        
                        
                    if q=='no':
                        t=input("DO YOU WISH TO CONTINUE? [yes,no]: ")
                        if t=='yes':
                            print("YOU ARE REBORN")
                            self.hp=self.maxhp#add the others
                            self.magik=self.maxmagik
                            self.stam=self.maxstam
                            self.arrows=self.maxarrows
                            
                        if t=='no':
                            print("SINCE YOU'RE NOT GOING TO MAKE UP YOUR MIND, I'M JUST GOING TO END THE GAME. SORRY")
                            self.hp=-100
                            return
                        
                else:
                    print("%s, YOU MUST TYPE 'yes' OR 'no'."%(self.name))
                    s=input("SO, DO YOU WISH TO CONTINUE? [yes,no]: ")
                    if s=='yes':
                        print("YOU ARE REBORN")
                        self.hp=self.maxhp#add the others
                        self.magik=self.maxmagik
                        self.stam=self.maxstam
                        self.arrows=self.maxarrows
                        
                        
                    elif s=='no':
                        q=input("ARE YOU SURE?[yes,no]: ")
                        if q=='yes':
                            self.hp=-100
                            return
                        
                        
                        if q=='no':
                            t=input("DO YOU WISH TO CONTINUE OR NOT? MAKE UP YOUR MIND![yes,no]: ")
                            if t=='yes':
                                print("YOU ARE REBORN")
                                self.hp=self.maxhp#add the others
                                self.magik=self.maxmagik
                                self.stam=self.maxstam
                                self.arrows=self.maxarrows
                                
                            if t=='no':
                                print("SINCE YOU'RE NOT GOING TO MAKE UP YOUR MIND, I'M JUST GOING TO END THE GAME.")
                                self.hp=-100
                                return
                    else:
                        print("REALLY %s? WHAT ARE YOU DOING? YOU LITERALLY JUST NEED TO TYPE 'yes' or 'no'. IF YOU MESS THIS UP AGAIN, IT'S GAME OVER, MATE"%(self.name))
                        s=input("LET ME MAKE THIS REALLY EASY FOR YOU: JUST TYPE 'y' FOR YES AND 'n' FOR NO. DO YOU WISH TO CONTINUE? [y,n]: ")
                        if s=='y':
                            print("SEE? NOT THAT DIFFICULT. OK, YOU ARE REBORN, (KNOWING YOU, HOWEVER, YOU'LL BE DEAD AGAIN IN TWO SECONDS)")
                            self.hp=self.maxhp#add the others
                            self.magik=self.maxmagik
                            self.stam=self.maxstam
                            self.arrows=self.maxarrows
                            
                        elif s=='n':
                            q=input("ARE YOU SURE? {I BELIEVE YOU CAN TYPE FULL WORDS NOW} [yes,no]: ")
                            if q=='yes':
                                self.hp=-100
                                return
                        
                        
                            if q=='no':
                                t=input("DO YOU WISH TO CONTINUE? [yes,no]: ")
                                if t=='yes':
                                    print("YOU ARE REBORN")
                                    self.hp=self.maxhp#add the others
                                    self.magik=self.maxmagik
                                    self.stam=self.maxstam
                                    self.arrows=self.maxarrows
                                    
                                if t=='no':
                                    print("OH FOR MORZANA'S SAKE...SINCE YOU'RE NOT GOING TO MAKE UP YOUR MIND, I'M JUST GOING TO END THE GAME. HAPPY?")
                                    self.hp=-100
                                    return
                        else:
                            print("UGH. YOU ARE REALLY BAD AT FOLLOWING DIRECTIONS? I SURE HOPE I DIDNT HIRE YOU TO GUARD MY CASTLE.")
                            print("WELL, HERE YOU ARE, AS PROMISED. DON'T SAY I DIDN'T WARN YOU.")
                            self.hp=-100
                            return
                        
                    
                
            return True
        else:
            return False
    def hasMagik(self):
        if self.magik>0:   ##DECIDES WHETHER PLAYER HAS MAGIK
            if self.magik<0:
                self.magik=0
            return True
        else:
            
            return False
    def hasArrows(self):
        if self.arrows>0:   #DECIDES IF PLAYER HAS ARROWS
            if self.arrows<0:
                self.arrows=0
            return True
        else:
            return False
    def hasEnergy(self):
        if self.stam>0:   #DECIDES IF PLAYER HAS STAMINA
            if self.stam<0:
                self.stam=0
            return True
        else:
            return False
    def hasGold(self):
        if self.gold>0:   #DECIDES IF PLAYER HAS STAMINA
            if self.gold<0:
                self.gold=0
            return True
        else:
            return False
    
        
    def island(self):
        if self.x>1 and self.x<51 and self.y>1 and self.y<17:
            self.island='Amodera'
        if self.x>57  and self.x<100 and self.y>1 and self.y<22:
            self.island='Morcengarde'
        if self.x>4  and self.x<92 and self.y>19 and self.y<31:
            self.island='Shadovar'
        #else:
            #print("IN BETWEEN ISLANDS")
    #def moral(self):
        #if self.moral>0:
         #   morals= 'Hero'
        #if self.moral<0:
          #  morals='Anti-hero'
        #if self.moral==0:
           # morals= 'Neutral'
        
    #Display charcter status
    def display(self):
        print("Name: %s %s"%(self.name,self.morals),"    {LIVES: %d}"%(self.lives), "  {Gold: %d/%d Pieces}"%(self.gold, self.maxgold),  "     {Location: %d, %d}"%(self.x, self.y), " {Kingdom: %s}"%(self.island))
 
        print("STATS>"," {Health: %d/%d}"%(self.hp,self.maxhp), "   {Magik: %d/%d}"%(self.magik, self.maxmagik), "   {Stamina: %d/%d}"%(self.stam, self.maxstam))
        print("Items>",  " {Sword Status: %d/%d Uses}"%(self.sword,self.maxsword),"    {Bow Status: %d/%d Uses}"%(self.bow,self.maxbow),"  {Quiver: %d/%d Arrows}"%(self.arrows,self.maxarrows))

        #print("MISC>", "Gold: %d/%d Pieces"%(self.gold, self.maxgold), "    {Health Potions: %d/3 Potions}"%(self.hpotion), "   {Magik Potions: %d/3 Potions}"%(self.mpotion))

       # print("SCROLLS>"," {Inferno: %d/5 Scrolls}"%(self.inferno),"  {Tidal Wave: %d/5 Scrolls}"%(self.wave), "{Maximum Healing: %d/5 Scrolls}"%(self.ultimhp),
           #   "  {Blizzard: %d/5 Scrolls}"%(self.blizzard), "  {Thunderstorm: %d/5 Scrolls}"%(self.thunder))
        #print("ARTIFACTS OF POWER>"," {ShadowBow: %d/20 Umbra Arrows}"%(self.umbra),"  {Mask of Morzana: %d/5 Souls}"%(self.morzana), "  {Morceris's Staff: %d/10 Energy}"%(self.morc), "  {Dalthuur's Cloak: %d/6 Energy}"%(self.dalthuur))

        #print("                     {Shanzalar's Staff: %d/1 Energy}"%(self.shan))     

        #self.inv.display()  
        
        

###########################ALL CHARACTER CLASSES ARE IMPORTED HERE#############################
from CharactersWA import *
        
########################PLAYING THE GAME##########################################
# Problem: need to get input and loop
def playGame(world, player):
    while player.isAlive():

        player.heal=1
        if player.heal==0:
            player.heals='<LOCKED>'
            player.healss='<LOCKED>'
        if player.heal>0:
            player.heals='Healing Spell {-3mag}'
            player.healss='Healing Spell'
        player.snow=1
        if player.snow==0:
            player.snows='<LOCKED>'
            player.snowss='<LOCKED>'
        if player.snow>0:
            player.snows='Snow Storm {-5mag}'
            player.snowss='Snow Storm'
        player.lightning=1
        if player.lightning==0:
            player.lightnings='<LOCKED>'
            player.lightningss='<LOCKED>'
        if player.lightning>0:
            player.lightnings='Chain Lightning {-5mag}'
            player.lightningss='Chain Lightning'
        player.mystic=1
        if player.mystic==0:
            player.mystics='<LOCKED>'
            player.mysticss='<LOCKED>'
        if player.mystic>0:
            player.mystics='Mystic Arrow {-1mag}'
            player.mysticss='Mystic Arrow'
            
        #HEAVY SPELLS
        player.iBlast=1
        if player.iBlast==0:
            player.iBlasts='<LOCKED>'
            player.iBlastss='<LOCKED>'
        if player.iBlast>0:
            player.iBlasts='Ice Blast {-10mag}'
            player.iBlastss='Ice Blast'
        player.fBlast=1
        if player.fBlast==0:
            player.fBlasts='<LOCKED>'
            player.fBlastss='<LOCKED>'
        if player.fBlast>0:
            player.fBlasts='Fire Blast {-10mag}'
            player.fBlastss='Fire Blast'
        player.tBlast=1
        if player.tBlast==0:
            player.tBlasts='<LOCKED>'
            player.tBlastss='<LOCKED>'
        if player.tBlast>0:
            player.tBlasts='Thunderbolt {-10mag}'
            player.tBlastss='Thunderbolt'
            
        #ABILITIES
        player.fSword=1
        if player.fSword==0:
            player.fSwords='<LOCKED>'
            player.fSwordss='<LOCKED>'
        if player.fSword>0:
            player.fSwords='Flame Sword {-5mag, -5stam}'
            player.fSwordss='Flame Sword'
        player.tArrow=1
        if player.tArrow==0:
            player.tArrows='<LOCKED>'
            player.tArrowss='<LOCKED>'
        if player.tArrow>0:
            player.tArrows='Triple Arrows {-3arrows}'
            player.tArrowss='Triple Arrows'

        
        if player.Morc==0:
            player.Morcs='<LOCKED>'
            player.Morcss='<LOCKED>'##do this for all scrolls and special weapons
        if player.Morc>0:
            player.Morcs="Morceris's Staff"
            player.Morcss=" {Morceris's Staff: %d/10 Energy}"%(player.morc) ##do this for all scrolls and special weapons
            
        
        if player.Dalthuur==0:
            player.Dalthuurs='<LOCKED>'
            player.Dalthuurss='<LOCKED>'##do this for all scrolls and special weapons
        if player.Dalthuur>0:
            player.Dalthuurs="Dalthuur's Cloak"
            player.Dalthuurss=" {Dalthuur's Cloak: %d/6 Energy}"%(player.dalthuur) ##do this for all scrolls and special weapons
            
      
        if player.Shan==0:
            player.Shans='<LOCKED>'
            player.Shanss='<LOCKED>'##do this for all scrolls and special weapons
        if player.Shan>0:
            player.Shans="Shanzalar's Staff"
            player.Shanss=" {Shanzalar's Staff: %d/1 Energy}"%(player.shan) ##do this for all scrolls and special weapons
            
        
        if player.Umbra==0:
            player.Umbras='<LOCKED>'
            player.Umbrass='<LOCKED>'##do this for all scrolls and special weapons
        if player.Umbra>0:
            player.Umbras="Shadowbow {-1 Umbra Arrow}"
            player.Umbrass=" {Shadowbow: %d/20 Umbra Arrows}"%(player.umbra) ##do this for all scrolls and special weapons

        
        if player.Morz==0:
            player.Morzs='<LOCKED>'
            player.Morzss='<LOCKED>'##do this for all scrolls and special weapons
        if player.Morz>0:
            player.Morzs="Mask of Morzana {-5souls}"
            player.Morzss=" {Mask of Morzana: %d/5 Souls}"%(player.morzana) ##do this for all scrolls and special weapons
        
        
       
        if player.Inferno==0:
            player.Infernos='<LOCKED>'
            player.Infernoss='<LOCKED>'##do this for all scrolls and special weapons
        if player.Inferno>0:
            player.Infernos='Inferno Scroll{-1 Scroll}'
            player.Infernoss=" {Inferno: %d/5 Scrolls}"%(player.inferno) ##do this for all scrolls and special weapons
       
        if player.Wave==0:
            player.Waves='<LOCKED>'
            player.Wavess='<LOCKED>'
        if player.Wave>0:
            player.Waves='Tidal Wave Scroll{-1 Scroll}'
            player.Wavess=" {Tidal Wave: %d/5 Scrolls}"%(player.wave) ##do this for all scrolls and special weapons
        
        if player.Ultimhp==0:
            player.Ultimhps='<LOCKED>'
            player.Ultimhpss='<LOCKED>'
        if player.Ultimhp>0:
            player.Ultimhps='Maximum Healing Scroll {-1 Scroll}'
            player.Ultimhpss=" {Maximum Healing: %d/5 Scrolls}"%(player.ultimhp) ##do this for all scrolls and special weapons
       
        if player.Blizzard==0:
            player.Blizzards='<LOCKED>'
            player.Blizzardss='<LOCKED>'
        if player.Blizzard>0:
            player.Blizzards='Blizzard Scroll {-1 Scroll}'
            player.Blizzardss=" {Blizzard: %d/5 Scrolls}"%(player.blizzard)
       
        if player.Thunder==0:
            player.Thunders='<LOCKED>'
            player.Thunderss='<LOCKED>'
        if player.Thunder>0:
            player.Thunders='Thunder Storm {-1 Scroll}'
            player.Thunderss=" {Thunderstorm: %d/5 Scrolls}"%(player.thunder)
        
        #display map
        world.display(player)
        # display status
        player.display()
        if player.x>1 and player.x<51 and player.y>1 and player.y<17:
            player.island='Amodera'
        if player.x>57  and player.x<100 and player.y>1 and player.y<22:
            player.island='Morcengarde'
        if player.x>4  and player.x<92 and player.y>19 and player.y<31:
            player.island='Shadovar'
       # else:
           # print("IN Town")
        
        # ask for a move
        move= input("Direction of Travel (w,s,d,a):  ")
        #make a move: MOVES PLAYER 1 OR 2 SPACES
        #UP,W,WW,WWW
        if move=="?":# no longer need the Legend, or at least in a large extent
            print("<INFORMATION>")
            s=input("PRESS: (1)COMBAT (2)MAP, MISSIONS, DECISIONS, AND OTHER SYMBOLS (3)MERCHANTS($,§) AND FORGES(Ӿ) (4)PICK-UPS  (5)ENEMIES (6)UPGRADES/UNLOCKABLES: ")
            if s=='1':
                print("==COMBAT==")
                print("-Press: [w]-normal weapons (1=bow(7,4,3,0 dmg), 2=sword(4,0 dmg), 3=knife (2,0 dmg)")
                print("-Press: [s]-spells (1=fireball(5,0 dmg), 2=snowstorm(3,3 dmg), 3=chain lightning(6,4,2 dmg), 4=healing(+5 hp), 5=mystic arrow(2,0dmg)")
                print("-Press: [d]-scrolls (1=inferno(10,0 dmg), 2=Tidal wave(7,3 dmg), 3=max healing(maxhp), 4=blizzard(8,0 dmg), 5=thunderstorm(8,0 dmg)")
                print("-Press: [a]-super weapons (1=shadowbow(5,0 dmg), 2=mask of morzana(20,20 dmg), 3=morceris staff(+5hp, 15 dmg), 4=dalthuur(6,16 dmg), 5=shanzalar(1000 dmg)")
                print("-Press: [e]-heavy attacks (1=Fire Blast(5,5 dmg), 2=Ice Blast(7,4,2 dmg), 3=Thunderbolt(10,0 dmg), 4=Flame Sword(8,4 dmg), 5=tripleshot bow(9,6,3,0 dmg)")
                print("-Press: [q]-potions (1=health potion(+10 hp,+10 stamina) 2=magik potion(+10 magik)")
            if s=='2':
                print("==MAP, MISSIONS, DECISIONS, INTROS==")
                print("-Map: You are in the Kingdom of Hjaron. Amodera is the top left island, Morcengarde is the top right island, and Shadovar is the bottom Island.")
                print("-Missions(IN ORDER): Amodera(1 Ω Ψ Ξ Φ Σ ₪), Morcengarde(π Ƿ Ħ Œ Д * ẘ Ǿ Ѫ ₻), Shadovar( Ұ Ҵ Ꚅ Ꜻ ѿ ₾ ꝙ Ꝝ Ʊ Ԭ)")
                print("-Decisons: The player will have to make choices as they continue through the game. These are noted by: ȣ,Ꙉ,₻")
                print("-Intros: Some enemies will have dialogue or descriptions of it. These are noted by:!,◊")
                
            if s=='3':
                print("==MERCHANTS, GOLD, CHESTS, AND FORGES==")
                print("-Merchants: sell potions that give the player health immediately and maybe scrolls that will be added to inventory")
                print("-Merchants: ($) normal merchants-have 4 types of potions and 3 different variations and can have a scroll")
                print("-Merchants: (§) special merchants-have 4 types of potions and 3 different variations and will have at least 1 scroll")
                
                print("-Forges: (Ӿ) Repair swords and bows for a price. Can repair the entire weapon or repair it to add more uses. Can also improve your weaponfor a price")
            if s=='4':
                print("==PICK-UPS==")
                print("-Player can pick up health and magik potions that will be added to inventory (max 2 health, 2 magik potions")
                print("-Health (ᴥ), magik (ϫ)")
                print("-Player can pick up gold coins and access chests.")
                print("-Gold Coins: (ₒ) Coins can be picked up and added to inventory")
                print("Chests: (ﬦ,ш): Give player gold. Watch out: some sneaky goblins have added traps to them.")
            if s=='5':
                print("==ENEMIES==")
                print("-Amodera Enemies: Bandits (ѧ), Cavetroll(¤), Dragon(ṽ), Serpent(Ѯ), Ancient Ghost(₼), Guard(Ꚛ), Morceris(Ꙛ)")
                print("")
                print("-Morcengarde Enemies: Tree Creature(ϔ), Goblin(ҩ), Ice Dragon(ʬ), Skeleton Guard(Ꝙ), Dalthuur(Ӂ)")
                print("")
                print("-Shadovar Enemies: Hoarfrost Wolf(Ɏ), Skaraith(ƺ), The Korvorath(Ꙃ), Thunder Dragon(Ϟ), Fire Saverek(ᵮ), Frost Saverek(҉), Thunder Saverek(ϗ), Shanzalar(₰)")
             
            if s=='6':
                print("==UPGRADES AND LOCKED ATTACKS==")
                print("-Player can unlock new attacks by completing missions, defeating enemies, and buying spell books from merchants")
                print("SPELLS: ")
                print("-Player can upgrade their spells by using experience points (XP) gained by completing missions and defeating enemies")
                print("-Press 'x' to open upgrades.")
            else:
                pass
            input("") 
        if move=="i":
            print("<INVENTORY>")
            print(player.Morz)
            print(" ")
                
            print("MISC>", "Gold: %d/%d Pieces"%(player.gold, player.maxgold), "    {Health Potions: %d/3 Potions}"%(player.hpotion), "   {Magik Potions: %d/3 Potions}"%(player.mpotion))
            print(" ")
            #print("SPELL BOOKS: %s   %s   %s   %s   %s   %s")
            print("SCROLLS>"," %s"%(player.Infernoss), " %s"%(player.Wavess), " %s"%(player.Ultimhpss),
              " %s"%(player.Blizzardss), " %s"%(player.Thunderss))
            print(" ")
            print("ARTIFACTS OF POWER>"," %s"%(player.Morcss),"  %s"%(player.Morzss), "  %s"%(player.Dalthuurss), "  %s"%(player.Umbrass), " %s"%(player.Shanss))
            
            #print()
            
            player.inv.display()
            input("")
        if move=='p':
            print("<PROFILE>")
            print("NAME: %s"%(player.name))
            print("PLAYER TOKEN: %s"%(player.symbol))
            print("MORALITY: %s"%(player.morals))
            
            n=input("PRESS 'n' TO CHANGE NAME, PRESS 's' TO CHANGE PLAYER TOKEN")
            if n=='n':
                s=input("UPDATE YOUR NAME: ")
                player.name=s
            
            if n=='s':
                x=input("CHOOSE A NEW PLAYER TOKEN {PRESS 1(ԗ) 2(Ӻ) 3(Ϫ) 4(₸) 5(Ꙙ)}")
                if x=='1':
                    player.symbol='ԗ'
                if x=='2':
                    player.symbol='Ӻ'
                if x=='3':
                    player.symbol='Ϫ'
                if x=='4':
                    player.symbol='₸'
                if x=='5':
                    player.symbol='Ꙙ'
            
                
                
                
                                      
        if move == 'l':
            print("          =={LEGEND}==         ")
            print("Ꙙ=Player             Ѯ=Serpent")
            print("1=Mission One        0=Serpent Egg")
            print("Ω=Mission Two       ꙲=Ancient Ruins")
            print("Ψ=Mission Three      Ꚛ=The Guard ")
            print("Ξ=Mission Four       ȣ=Guard Decision")
            print("Φ=Mission Five       Ꙛ=Morceris")
            print("Σ=Mission Six,       Ꙉ=Morceris Decision")
            print("₪=Morceris's Castle  Ѻ=Portal to Morcengarde")
            print("!=Bandit Gate        Ꝋ=Portal to Shadovar")
            print("ѧ=Bandit Camp        Ꝍ=Portal to Amodera")
            print("Ō=Cave               ₼=Ancient Ghost")
            print("¤=Cave Troll          ◊=Morzacron")
            print("Ơ=Dragon Cave        Ӿ=Forges  ")
            print("ṽ=Dragon               ")
            print("[$ ₡ ₿ ₵ ₴ € ฿ Ŀ §]=Merchants")
            print("(π Ƿ Ħ Œ Д * ẘ Ǿ Ѫ ₻)=MORCENGARDE MISSIONS(1-10) ")
            print("ϔ=Tree Creature       ʬ=Ice Dragon      ")
            print("ҩ=Goblin              Ꝙ=Skeleton Guard ")
            print("Ӂ=Dalthuur                    ")
            print("(              )=SHADOVAR MISSIONS (1- )   ")
            print("Ɏ=Hoarfrost Wolf       Ɣ=Dark Elf")
            print("Ҩ= Goblin King         Ϟ=Electro Dragon ")
            print("ᵮ,҉,ϗ= Saverek Mages   ₰=Shanzalar  ")
            print("#=Poison Trees         .=Water   ")
            input("ₒ=Gold Coins          [ш,ﬦ]=Chests")
            
            
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                      
                    

        if move=='t':
            w=input("<TUTORIAL>")
                
            input("Welcome Adventurer! Before you embark on your quest, here is a tutorial PRESS ENTER TO CONTINUE: ")
    #r=int(r)
    
            print("This is your character token: %s. You can move around the map by pressing: w-move north,s- move south, d-move east, and a-move west."%(player.symbol))
        
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
    

                #w=input(":")
            
        if move=='x':
            w='yay'
            while w is not 'x':
                
                print("<SKILLS UPGRADE>")
                print("XP POINTS: %d POINTS"%(player.perks))
            #print("Fireball: Level %d"%(player.fireBallLvl))
                w=input("Upgrade>Spells['s']  Heavy Spells ['a']  Heavy Weapons['w']   Exit['x']: ")#repeat this for all 5 normal spells and 5 heavy attacks
                if w=='w':
                    x=input("Upgrade  (1) %s  (2) %s: "%(player.fSwordss, player.tArrowss))
                    if x=='1':
                        if player.fSword>0: #copy this to other weapons and spells
                            if player.fSwordLvl==1:
                                    c=4
                            if player.fSwordLvl==2:
                                    c=7
                            if player.fSwordLvl==3:
                                print("FIRE SWORD AT MAX LEVEL!")
                            if player.fSwordLvl<3:
                                p=input("Upgrade Fire Sword to Level %d (%d xp)? [yes,no]"%(player.fSwordLvl+1, c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.fSwordLvl+1>2:
                                            player.perks=player.perks-c
                                            player.fSwordLvl=player.fSwordLvl+1
                                            print("Fire Sword Upgraded to Max Level")#make this happen at lvl 3
                                            player.fSwordLvl=3
                                        if player.fSwordLvl+1<3:
                                            player.perks=player.perks-c
                                            player.fSwordLvl=player.fSwordLvl+1
                                            print("Fire Sword Upgraded to Level %d"%(player.fSwordLvl))
                                if p=='no':
                                    pass
                                    
                            
                        else:
                            print("SKILL NOT ACQUIRED!")
                    if x=='2':
                        if player.tArrow>0:
                            if player.tArrowLvl==1:
                                    c=4
                            if player.tArrowLvl==2:
                                    c=7
                            if player.tArrowLvl==3:
                                print("TRIPLE ARROWS AT MAX LEVEL!")
                            if player.tArrowLvl<3:
                                p=input("Upgrade Triple Arrow to Level %d (%d xp)? [yes,no]"%(player.tArrowLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.tArrowLvl+1>2:
                                            player.perks=player.perks-c
                                            player.tArrowLvl=player.tArrowLvl+1
                                            print("Triple Arrow Upgraded to Max Level")#make this happen at lvl 3
                                            player.tArrowLvl=3
                                        if player.tArrowLvl+1<3:
                                            player.perks=player.perks-c
                                            player.tArrowLvl=player.tArrowLvl+1
                                            print("Triple Arrow Upgraded to Level %d"%(player.tArrowLvl))
                                if p=='no':
                                    pass
                            
                                        
                        else:
                            print("SKILL NOT ACQUIRED!")
                    
                
                if w=='s':
                    x=input("Upgrade  (1)Fireball  (2)%s  (3) %s  (4) %s  (5) %s: "%(player.snowss, player.lightningss, player.healss, player.mysticss))
                    if x=='1':
                        if player.fire>0:
                            if player.fireBallLvl==1:
                                    c=3
                            if player.fireBallLvl==2:
                                    c=5
                            if player.fireBallLvl==3:
                                print("FIREBALL AT MAX LEVEL!")
                            if player.fireBallLvl<3:
                                p=input("Upgrade Fireball to Level %d (%d xp)? [yes,no]"%(player.fireBallLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.fireBallLvl+1>2:
                                            player.perks=player.perks-c
                                            player.fireBallLvl=player.fireBallLvl+1
                                            print("Fireball Upgraded to Max Level")#make this happen at lvl 3
                                            player.fireBallLvl=3
                                        if player.fireBallLvl+1<3:
                                            player.perks=player.perks-c
                                            player.fireBallLvl=player.fireBallLvl+1
                                            print("Fireball Upgraded to Level %d"%(player.fireBallLvl))
                                if p=='no':
                                    pass
                    if x=='2':
                        if player.snow>0:
                            if player.snowStormLvl==1:
                                    c=2
                            if player.snowStormLvl==2:
                                    c=4
                            if player.snowStormLvl==3:
                                print("FIREBALL AT MAX LEVEL!")
                            if player.snowStormLvl<3:
                                p=input("Upgrade Snow Storm to Level %d (%d xp)? [yes,no]"%(player.snowStormLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.snowStormLvl+1>2:
                                            player.perks=player.perks-c
                                            player.snowStormLvl=player.snowStormLvl+1
                                            print("Fireball Upgraded to Max Level")#make this happen at lvl 3
                                            player.snowStormLvl=3
                                        if player.snowStormLvl+1<3:
                                            player.perks=player.perks-c
                                            player.snowStormLvl=player.snowStormLvl+1
                                            print("Fireball Upgraded to Level %d"%(player.snowStormLvl))
                                if p=='no':
                                    pass
                        else:
                            print("SPELL NOT DISCOVERED!")
                    if x=='3':
                        if player.lightning>0:
                            if player.cLightLvl==1:
                                    c=3
                            if player.cLightLvl==2:
                                    c=5
                            if player.cLightLvl==3:
                                print("CHAIN LIGHTNING AT MAX LEVEL!")
                            if player.cLightLvl<3:
                            
                                p=input("Upgrade Chain Lightning to Level %d (3 xp)? [yes,no]"%(player.cLightLvl+1))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.cLightLvl+1>2:
                                            player.perks=player.perks-c
                                            player.cLightLvl=player.cLightLvl+1
                                            print("Chain Lightning Upgraded to Max Level")#make this happen at lvl 3
                                            player.cLightLvl=3
                                        if player.cLightLvl+1<3:
                                            player.perks=player.perks-c
                                            player.cLightLvl=player.cLightLvl+1
                                            print("Chain lightning Upgraded to Level %d"%(player.cLightLvl))
                                if p=='no':
                                    pass
                                
                        else:
                            print("SPELL NOT DISCOVERED!")
                        
                    if x=='4':
                        if player.heal>0:
                            if player.healLvl==1:
                                    c=3
                            if player.healLvl==2:
                                    c=4
                            if player.healLvl==3:
                                print("HEALING AT MAX LEVEL!")
                            if player.healLvl<3:
                                p=input("Upgrade Healing to Level %d (3 xp)? [yes,no]"%(player.healLvl+1))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.healLvl+1>2:
                                            player.perks=player.perks-c
                                            player.healLvl=player.healLvl+1
                                            print("Healing Upgraded to Max Level")#make this happen at lvl 3
                                            player.healLvl=3
                                        if player.healLvl+1<3:
                                            player.perks=player.perks-c
                                            player.healLvl=player.healLvl+1
                                            print("Healing Upgraded to Level %d"%(player.healLvl))
                                if p=='no':
                                    pass
                                
                        else:
                            print("SPELL NOT DISCOVERED!")
                    if x=='5':
                        if player.mystic>0:
                            if player.mArrowsLvl==1:
                                    c=2
                            if player.mArrowsLvl==2:
                                    c=3
                            if player.mArrowsLvl==3:
                                print("MYSTIC ARROWS AT MAX LEVEL!")
                            if player.mArrowsLvl<3:
                                p=input("Upgrade Mystic Arrows to Level %d (%d xp)? [yes,no]"%(player.mArrowsLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.mArrowsLvl+1>2:
                                            player.perks=player.perks-c
                                            player.mArrowsLvl=player.mArrowsLvl+1
                                            print("Mystic Arrows Upgraded to Max Level")#make this happen at lvl 3
                                            player.mArrowsLvl=3
                                        if player.mArrowsLvl+1<3:
                                            player.perks=player.perks-c
                                            player.mArrowsLvl=player.mArrowsLvl+1
                                            print("Mystic Arrows Upgraded to Level %d"%(player.mArrowsLvl))
                                if p=='no':
                                    pass
                                
                        else:
                            print("SPELL NOT DISCOVERED!")
            
                if w=='a': ###KEEP WORKING ON THIS, ADDING THIS TO PLAYER ATTACKS
                    x=input("Upgrade  (1)%s  (2)%s  (3) %s: "%(player.fBlastss, player.iBlastss, player.tBlastss))
                    if x=='1':
                        if player.fBlast>0:
                            if player.fBlastLvl==1:
                                    c=4
                            if player.fBlastLvl==2:
                                    c=7
                            if player.fBlastLvl==3:
                                print("FIRE BLAST AT MAX LEVEL!")
                            if player.fBlastLvl<3:
                                p=input("Upgrade Fire Blast to Level %d (%d xp)? [yes,no]"%(player.fBlastLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.fBlastLvl+1>2:
                                            player.perks=player.perks-c
                                            player.fBlastLvl=player.fBlastLvl+1
                                            print("Fire Blast Upgraded to Max Level")#make this happen at lvl 3
                                            player.fBlastLvl=3
                                        if player.fBlastLvl+1<3:
                                            player.perks=player.perks-c
                                            player.fBlastLvl=player.fBlastLvl+1
                                            print("Fire Blast Upgraded to Level %d"%(player.fBlastLvl))
                                if p=='no':
                                    pass
                        else:
                            print("SPELL NOT DISCOVERED!")
                                
                        
                    if x=='2':
                        if player.iBlast>0:
                            if player.iBlastLvl==1:
                                    c=4
                            if player.iBlastLvl==2:
                                    c=7
                            if player.iBlastLvl==3:
                                print("ICE BLAST AT MAX LEVEL!")
                            if player.iBlastLvl<3:
                                p=input("Upgrade Ice Blast to Level %d (%d xp)? [yes,no]"%(player.iBlastLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.iBlastLvl+1>2:
                                            player.perks=player.perks-c
                                            player.iBlastLvl=player.iBlastLvl+1
                                            print("Ice Blast Upgraded to Max Level")#make this happen at lvl 3
                                            player.iBlastLvl=3
                                        if player.iBlastLvl+1<3:
                                            player.perks=player.perks-c
                                            player.iBlastLvl=player.iBlastLvl+1
                                            print("Ice Blast Upgraded to Level %d"%(player.iBlastLvl))
                                if p=='no':
                                    pass
                        else:
                            print("SPELL NOT DISCOVERED!")
                                    
                        
                    if x=='3':
                        if player.tBlast>0:
                            if player.tBlastLvl==1:
                                    c=5
                            if player.tBlastLvl==2:
                                    c=8
                            if player.tBlastLvl==3:
                                print("THUNDERBOLT AT MAX LEVEL!")
                            if player.tBlastLvl<3:
                                p=input("Upgrade Thunderbolt to Level %d (%d xp)? [yes,no]"%(player.tBlastLvl+1,c))
                                if p=='yes':
                                    if player.perks<c:
                                        print("NOT ENOUGH XP TO UPGRADE!!")
                                    if player.perks>c or player.perks==c:
                                        if player.tBlastLvl+1>2:
                                            player.perks=player.perks-c
                                            player.tBlastLvl=player.tBlastLvl+1
                                            print("Thunderbolt Upgraded to Max Level")#make this happen at lvl 3
                                            player.tBlastLvl=3
                                        if player.tBlastLvl+1<3:
                                            player.perks=player.perks-c
                                            player.tBlastLvl=player.tBlastLvl+1
                                            print("Thunderbolt Upgraded to Level %d"%(player.tBlastLvl))
                                if p=='no':
                                    pass
                        else:
                            print("SPELL NOT DISCOVERED!")
                                  
                  
        if move== "w":
            player.moveUp(world)
            
            
        if move== "ww":
            player.moveUp(world)
            player.moveUp(world)
            
        if move== "www":
            player.moveUp(world)
            player.moveUp(world)
            player.moveUp(world)
            player.stam=player.stam-1
        #DOWN, S,SS,SSS
            
        if move== "s":
            player.moveDown(world)
        if move== "ss":
            player.moveDown(world)
            player.moveDown(world)
        if move== "sss":
            player.moveDown(world)
            player.moveDown(world)
            player.moveDown(world)
            player.stam=player.stam-1
        #RIGHT, D,DD,DDD   
        if move== "d":
            player.moveRight(world)
        if move== "dd":
            player.moveRight(world)
            player.moveRight(world)
        if move== "ddd":
            player.moveRight(world)
            player.moveRight(world)
            player.moveRight(world)
            player.stam=player.stam-1
        #LEFT, A,AA,AAA   
        if move== "a":
            player.moveLeft(world)
        if move== "aa":
            player.moveLeft(world)
            player.moveLeft(world)
        if move== "aaa":
            player.moveLeft(world)
            player.moveLeft(world)
            player.moveLeft(world)
            player.stam=player.stam-1

        w=world.playerCollidesEnemy() #enemy
        if w is None:
            pass
        if w is not None:
            #print("Fight!")
            fightToDeath(player,w)
        #print(world)   
           
             
    print("GAME OVER")
 
    
##########################################
    #COMBAT#
##########################################

myInv=[]
def fight(e1,e2):#add guard as e3, or if this gets weird, just say she attacks with the player in print statements  before and after
    
    attack1=e1.getAttack()   
    attack2=e2.getAttack()
    #attack3=e3.getAttack()
    e1.applyAttack(attack2)
    e2.applyAttack(attack1)
    #e3.applyAttack(attack2)
    
def fightToDeath(e1,e2):
    x=0
    '''repeat fight exchange until one entity is dead''' 
    print("%s ENCOUNTERED! FIGHT TO THE DEATH!!"%e2.name)
    print("%s HEALTH: %d"%(e2.name,e2.hp))
    #x=0
    
    while e1.isAlive() and e2.isAlive(): #figure out how to penalize people by making them lose lives if they collect an item again
        #x=0
        fight(e1,e2)
        print("**%s HEALTH: %d**"%(e2.name,e2.hp))
        x=1
        #x=x+1
        #e1.lives=e1.lives-x
    #postcondition- someone is dead
    
    if e1.isAlive() and x==1: #if
        
        
        print("%s VANQUISHED!"%(e2.name))  #fix this so that the mission is complete after enemy is vanquished.
        print("SOUL ABSORBED!")
        e1.receiveItem(e2.getLoot()) #this should store the getLoot item string from enemy    ###cahnged this, fixied some repeated text problems
        #e1.inv.display()
        e1.gold=e1.gold+e2.gold
        e1.perks=e1.perks+e2.perks
        print("%d XP GAINED!"%(e2.perks))
        if e1.gold>e1.maxgold:
            e1.gold=e1.maxgold
        #if e1.inferno>e1.maxinferno:
           # e1.inferno=e1.maxinferno
        if e1.morzana<e1.maxmorzana:
            e1.morzana=e1.morzana+1
        else:
            e1.morzana=e1.maxmorzana
        
        
        
        #if alive, mission is complete, place player on main map
        
    if e2.isAlive():
        print("")
        
        #if dead, restart mission(have to beat enemy to proceed) or have an honor system and place them back on the map to try again.


# CREATING THE GAME (initial game world)

e1= Player(44,8) #(4,4) to start (44,4) morceris  (58,4)-morcengarde portal  (78,20)-Shadovar portal (83,25)-Amodera portal #was 16,14 was 74,5
game_world = Map()

game_world.setPlayer(e1) #(47,22)
#minimaps:
#Amodera
game_worlda = miniMap1()# town Korvastead
game_worlda1 = miniMap1a()# rebel house
game_worldb = miniMap2()#ancient ruins

game_worldc = miniMap3()#cave troll
game_worldd = miniMap4() #dragon cave
game_worlde = miniMap5() # Morceris Bridge
game_worlde1 = miniMap5a() # Morceris Castle

'''
game_worldd = miniMap4()
game_worlde = miniMap5()#ancient ruins
game_worldf = miniMap6()# rebel house
game_worldg = miniMap7()# town Korvastead
game_worldh = miniMap8()#ancient ruins
game_worldi = miniMap9()# rebel house
game_worldj = miniMap10()# town Korvastead
game_worldk = miniMap12()#ancient ruins
game_worldl = miniMap13()# rebel house
game_worldm = miniMap14()# town Korvastead
game_worldn = miniMap15()#ancient ruins
game_worldo = miniMap16()# rebel house
game_worldq = miniMap15()#ancient ruins
game_worldr = miniMap16()# rebel house

'''
game_worlda.setPlayer(e1)#Town
game_worlda1.setPlayer(e1)# rebel house
game_worldb.setPlayer(e1)#Ancient Ruin
game_worldc.setPlayer(e1) # troll cave
game_worldd.setPlayer(e1) # Dargon Cave
game_worlde.setPlayer(e1) # Morceris Bridge
game_worlde1.setPlayer(e1)# Morceris caslte


'''
game_worldd.setPlayer(e1)#
game_worlde.setPlayer(e1)#
game_worldf.setPlayer(e1)#
#Morcengarde
game_worldg.setPlayer(e1)#
game_worldh.setPlayer(e1)#
game_worldi.setPlayer(e1)#

game_worldj.setPlayer(e1)#
game_worldk.setPlayer(e1)#
game_worldl.setPlayer(e1)#
#Shanzalar
game_worldm.setPlayer(e1)#
game_worldn.setPlayer(e1)#
game_worldo.setPlayer(e1)#

game_worldp.setPlayer(e1)#
game_worldq.setPlayer(e1)#
game_worldr.setPlayer(e1)#
'''
#{Enemies}




#enemies in minimap1

A=ancientGhost(5,2)
game_worldb.addEnemies(A)




 
#PLAYER


#FRIENDS

#MERCHANTS (REALLY COMPLICATED VERSION)
#Ms=Merchant(69,9)
#game_world.addMerchants(Ms)

#Mss=Merchant(68,9)
#game_world.addMerchants(Mss)
##AMODERA
d=Dragon(10,14)
game_world.addEnemies(d)
#dd=Dragon(39,14)
#game_world.addEnemies(dd)
b=Bandit(6,9)
game_world.addEnemies(b)
bb=Bandit2(23,4)
game_world.addEnemies(bb)
#bbb=Bandit(12,9)
#game_world.addEnemies(bbb)

c=CaveTroll(10,5)
game_worldc.addEnemies(c)
#cc=CaveTroll(29,8)
#game_world.addEnemies(cc)
s=Serpent(30,8)
game_world.addEnemies(s)
#A=ancientGhost(29,4)
#game_world.addEnemies(A)
g=Guard(41,9)
game_world.addEnemies(g)
M=Morceris(44,4)
game_world.addEnemies(M)

##MORCENGARDE

t=treeCreature(60,5)
game_world.addEnemies(t)
go=goblin(78,7)
game_world.addEnemies(go)
#goo=goblin(89,6)
#game_world.addEnemies(goo)
i=IceDragon(63,10)
game_world.addEnemies(i)
ig=invisibleGoblin(65,17)
game_world.addEnemies(ig)
sk=SkeletonGuard(79,15)
game_world.addEnemies(sk)
D=Dalthuur(77, 17)
game_world.addEnemies(D)


##SHADOVAR
de=DarkElf(22,26)
game_world.addEnemies(de)
dee=DarkElf2(20,24)
game_world.addEnemies(dee)
deee=DarkElf2(21,23)
game_world.addEnemies(deee)

hw=HoarFrostWolves(10, 21)
game_world.addEnemies(hw)
gk=goblinKing(35,19)
game_world.addEnemies(gk)
k=korvorath(55,14)
game_world.addEnemies(k)
e=ElectroDragon(48,23)
game_world.addEnemies(e)

fm=fireMage(50, 24)
game_world.addEnemies(fm)
frm=frostMage(51,24)
game_world.addEnemies(frm)
tm=thunderMage(52,24)
game_world.addEnemies(tm)

S=Shanzalar(74,26)
game_world.addEnemies(S)
#Ss=Shanzalar2(14,14)
#game_world.addEnemies(Ss)

##PLAY GAME
playGame(game_world, e1)


           


#THINGS TO DO NOW
#GLITCHES:
###add extra stamina to healing spell :)
###make sure stam cant go below 0 :)

#GAME CONCEPTS
#seasons-can add this into descriptions, sort of meaningless in code
#cities and towns: make a whole new map for each-this will be tricky
##create maps for cities, towns, villages, houses, caves, ruins, castles  (this will be difficult

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
#####delete all potions and such and just have merchants#####

#smithing-this would require things being added to and manipulated in the inventory
#enchanting-this would require things being added to and manipulated in the inventory

#night and day-can add this into descriptions, sort of meaningless in code

#COMBAT
#getting new items to give new attaks :)
#making different bandit camps etc. :)    ###but can do more
###allows for differnt fighting experience :)indeed ###but can do more

#add a life system :)
#####keep track of deaths and subtract 1 every time the player dies
###penalize the payer for trying to loot twice by getting rid of one of their lives.

#END OF GAME:#

###GOOD ENDING: PRINT("ALL IS WELL, YOU SAVED THE KINGDOM %S")(SELF.NAME)). THE KINGDOM IS NOT SAFE, HOWEVER. YOU MUST USE YOUR POWERS AS MORZANA TO..."
#..PROTETT THE KINGDOM FROM OTHER DANGERS. MORCERIS, DALTHUUR AND SHANZALAR WERE NOT THE ONLY THREATS

##BAD ENDING: YOU BECOME MORTHUURZAR THE DESTROYER OF WORLDS. YOU ARE NOW THE MOST POWERFU  BEING.
#USING YOUR POWER AS THE MORZANA AND THE POWER OF MORHTUURZAR (THE LIGHT AND THE DARK) YOU DAWN THE FOUR ANCIENT ARTIFACTS:
#THE STAFF OF MORCERIS, THE CLOAK OF DALTHUUR, THE DESTRUCTION GAUNTLETS OF SHANZALAR, AND THE MASK OF MORZANA
#YOU FIRST DAWN THE CLOAK. yOU POINT YOUR TOWARDS THE GROUND AND SUMMON AN UNDEAD DRAGON
#YOU THEN DAWN THE GAUNTLETS. YOU RAISE YOUR HANDS TOWARDS THE HEAVENS AND THUNDERBOLTS STRIKE THE DRY GROUND AND CREATE AN INFERNO
#YOU THEN TAKE THE STAFF. YOU POINT THE STAFF TOWARDS MAX AND DRAIN HER LIFE (NOT BIG ON KILLING MAX-MAYBE EBSLAVE HER OR TURN HER EVIL? AND THEN SEND OUT POISON
#FINALLY, YOU TAKE THE MASK OF MORZANA AND PLACE IT ON YOUR FACE. GREEN FLAMES BLAST OUT THE TOP OF THE MASK AND TENDRILS OF FLAMES LEAP FROM YOUR FINGERTIPS
####...AND WRAP AROUND YOUR BODY.
#YOU LIFT THE STAFF TOWARDS THE SKY AND SLAM IT INTO THE GROUND. A WAVE OF PURE, INFINITE ENRGY BURSTS OUT FROM YOU.
#...THE CASTLE IS VAPORIZED INSTANTLY AND THE WAVE CONTINUES ACROSS THE ENTIRE LAND. WITHIN SECONDS, ALL THREE LANDS ARE DESTROYED, LEAVING NO SURVIVORS.
#GAME OVER
#######MAKE A MAP THAT IS COMPLETELY DESTROYED.


#make the blacksmith actually make some weapons and armor for a price.
#create way to add something to the inventory and subtract a certain amount of gold
#maybe just self.inv.store(smith1)????? might be a neat feature



#################################MINIMAPS###################################
#mini0 = mission 2 town
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







