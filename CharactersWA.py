#######CHARACTERS###############
import random




#Entity
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


#player

#FRIENDS:
##MERCHANTS

#Enemies
######AMODERA############
class Dragon(Entity):
    def __init__(self,x,y): #mob enemy: appears many times
        super().__init__(x,y)
        self.hp=25
        self.x=x
        self.y=y
        self.symbol='ṽ'
        self.name='FIRE DRAGON'
        self.perks=3
        self.gold=200
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Scroll of the Inferno" #This will go into special spells
    def getAttack(self):
        '''to give damage to another entity'''
       # print("**FIRE DRAGON'S HEALTH: %d"%(self.hp))          
        m=random.randint(1,6)
        p=random.randint(1,2)
        if m==1:
            x=5
            print("Fire Dragon cuts you with claw")
        elif m==4:
            x=0
            print("Fire Dragon's claw misses you")
        
        elif m==2:
            x=4
            print("Fire Dragon engulfs you with Fire Breath")
            if p==2:
                print("[Special Attack!] Fire Dragon flaps his wings and fans the flames, creating a raging inferno")
                x=x+5
        elif m==5:
            x=0
            print("Fire Dragon's Fire Breath misses you")
            
        elif m==3:
            x=5
            print("Fire Dragon bites you")
        elif m==6:
            x=0
            print("Fire Dragon's bite misses")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

##############BANDIT TYPES#######
#SWORD AND BOW       
class Bandit(Entity):
    def __init__(self,x,y): #mob creature: will appear a few times
        super().__init__(x,y)
        self.hp=10
        self.x=x
        self.y=y
        self.symbol='ѧ'
        self.name='BANDIT ARCHER'
        self.perks=1
        self.gold=100
    
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Bandit's Quiver" #allows for different items to be obtained by different monsters

    def getAttack(self):
        '''to give damage to another entity'''     
        #print("**BANDIT ARCHER'S HEALTH: %d"%(self.hp))   
        m=random.randint(1,6)#random input to ATTACK
        
       
        if m==1:
            x=4
            print("Bandit stabs you with a Sword.")
        elif m==4:
            x=0
            print("Bandit's sword misses you.")
        
        elif m==2:
            x=4
            print("Bandits Shoots a Flaming Arrow and hits you")
        elif m==5:
            x=0
            print("Bandit's arrow misses you")
        elif m==3:
            x=5
            print("Bandit cuts through your flesh with an Axe")
        elif m==6:
            x=0
            print("Bandit's Axe gets lodged in a tree")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

#BATTLEAXE
class Bandit2(Entity):
    def __init__(self,x,y): #mob creature: will appear a few times
        super().__init__(x,y)
        self.hp=10
        self.x=x
        self.y=y
        self.symbol='ѧ'
        self.name='BANDIT CHIEF'
        self.perks=1
        self.gold=100
    
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Steel Armor Set" #This will go into special weapons

    def getAttack(self):
        '''to give damage to another entity'''     
        #print("**BANDIT CHIEF'S HEALTH: %d"%(self.hp))    
        m=random.randint(1,6)#random input to ATTACK
        
       
        if m==1:
            x=5
            print("Bandit swings Battle axe at your head.")
        elif m==4:
            x=0
            print("You duck just before the blade cuts off your head.")
        
        elif m==2:
            x=3
            print("Bandit bashes you in the head with the blunt side of the axe")
        elif m==5:
            x=0
            print("You back step to avoid the axe")
        elif m==3:
            x=3
            print("Bandit punches you with his steel gauntlets")
        elif m==6:
            x=0
            print("You side step and avoid the punch")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt
        


#####CAVETROLLS

class CaveTroll(Entity):   ########make sure to copy other enemies like this     
    def __init__(self,x,y): #mob creature: will appear a few times
        super().__init__(x,y)
        self.hp=14
        self.x=x
        self.y=y
        self.symbol='¤'
        self.name='CAVE TROLL'
        self.perks=2
        self.gold=150
        
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Armor of the Destroyer" #allows for different items to be obtained by different monsters


    def getAttack(self):
        '''to give damage to another entity'''    
        #print("**CAVETROLL'S HEALTH: %d"%(self.hp))   

        m=random.randint(1,6)#random input to ATTACK
        
        if m==1:
            x=5
            print("Cave Troll throws boulder")
        elif m==4:
            x=0
            print("You dodge the Cave Troll's boulder")
        
        elif m==2:
            x=7
            print("Cave Troll clubs you with a log")
        elif m==5:
            x=0
            print("You dodge the Cave Troll's log swing")
        elif m==3:
            x=8
            print("Cave Troll charges and knocks you down")
        elif m==6:
            x=0
            print("You dodge Cave Troll's charge")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt    
     
class CaveTroll2(Entity):   ########make sure to copy other enemies like this     
    def __init__(self,x,y): #mob creature: will appear a few times
        super().__init__(x,y)
        self.hp=14
        self.x=x
        self.y=y
        self.symbol='¤'
        self.name='CAVE TROLL'
        self.perks=2
        self.gold=100
        
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Cavetroll's Club" #This will go into special weapons, maybe


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**CAVETROLL'S HEALTH: %d"%(self.hp))      
            

        m=random.randint(1,6)#random input to ATTACK
        
        if m==1:
            x=3
            print("Cave Troll kicks you with his stone foot")
        elif m==4:
            x=0
            print("You dive roll out of the cavetroll's foot")
        
        elif m==2:
            x=3
            print("Cave Troll clubs you with a log")
        elif m==5:
            x=0
            print("You dodge the Cave Troll's log swing")
        elif m==3:
            x=2
            print("Cave Troll charges and knocks you down")
        elif m==6:
            x=0
            print("You dodge Cave Troll's charge")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt    
     


class Serpent(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=4
        self.x=x
        self.y=y
        self.symbol='Ѯ'
        self.name='SERPENT'
        self.perks=3
        self.gold=250
    
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Scroll of the Tide" #will be added to the special spells
                                        #will create a large tidal wave

    def getAttack(self):
        '''to give damage to another entity'''
        #print("**SERPENT'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACL
        p=random.randint(1,4)
        c=random.randint(1,2)
        if m==1:
            x=7
            print("Serpent spews acid")
        elif m==4:
            x=0
            print("You dodge the acid stream")
        
        elif m==2:
            x=6
            print("Serpent pulls you underwater")
            if c==2:
                print("[Special Attack!] Serpent wraps around the you and crushes your body")
                x=x+5
        elif m==5:
            x=0
            print("Serpent misses you and instead pulls fallen tree underwater")
        elif m==3:
            x=8
            print("Serpent attacks you with Venomous Bite")
        elif m==6:
            x=0
            print("You dodge the  bite")
            if p==4:
                print("As you dodge the bite, you raise your sword to slice at the Serpent's vulnerable neck [CRITICAL HIT: SERPENT LOSES 10 HEALTH]")
                self.hp=self.hp-10
                
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt


class ancientGhost(Entity):     
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=5
        self.maxhp=5
        self.x=x
        self.y=y
        self.symbol='₼'
        self.name='CORRUPTED GHOST'
        self.perks=4
        self.gold=250
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Mask of Morzana" #Dont know what this will do. probably go into special spells


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**CORRUPTED GHOST'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        c=random.randint(1,2)
        if m==1:
            x=5
            print("The Ghost uses Fires of the Morzana. You are engulfed by a torrent of green flames. The flames wrap you like vines")
            if c==2:
                print("[Special Attack!] As the Fires of the Morzana wrap around. The Ghost begins to absorb your health")
                x=x+5
                self.hp=self.hp+5
            
        elif m==4:
            x=0
            print("The Ghost uses Fires of the Morzana. You barely dodge the torrent of green flames")
        
        elif m==2:
            x=7
            print("The Ghost absorbs your life force with its ancient magik")
            self.hp=self.hp+5
            if self.hp>self.maxhp:
                self.hp=self.maxhp
            
        elif m==5:
            x=0
            print("The Ghost attempts to absorb your life force, but you manage to evade it")
        elif m==3:
            x=8
            print("The Ghost possesses you and causes you to harm yourself")
        elif m==6:
            x=0
            print("The Ghost attempts to possess you, but you are able to escape its control.")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt       


class Guard(Entity):     
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=10
        self.perks=3
        self.x=x
        self.y=y
        self.symbol='Ꚛ'
        self.name='THE GUARD'
        self.perks=3
        self.gold=250
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Helm of the Corrupted" #allows for different items to be obtained by different monsters


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**GUARD'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        c=random.randint(1,2)
        if m==1:
            x=8
            print("The Guard sweeps his sword at your legs and knocks you down")
        elif m==4:
            x=0
            print("You step backwards and avoid the Guard's sword")
        
        elif m==2:
            if c==2:
                print("[Special Attack!] The Guard's sword glows to red. The dark red flames erupt from the sword. The Guard stabss you in the chest. The flames burn your organs")
                x=10+3
                
            else:         
                print("The Guard thrusts his sword at your chest. The sword penetrates your chest")
                x=8
            
            
        elif m==5:
            x=0
            print("The Guard thrusts his sword and misses")
        elif m==3:
            x=7
            print("You lock swords with the Guard, but he kicks you in the chest")
        elif m==6:
            x=0
            print("You lock swords with the Guard, but free yourself and step backwards")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt       


class Morceris (Entity):      #####change attacks to better fit his character
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=10
        self.maxhp=10
        self.x=x
        self.y=y
        self.symbol='Ꙛ'
        self.name='MORCERIS'
        self.perks=5
        self.gold=300
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "The Staff of Morceris" #allows for the player to increase their magik and stamina (grants the user the ability to make powerful potions
                                            #will go into special weapons


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**MORCERIS'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        #m=int(m)
        p=random.randint(1,6)
        c=random.randint(1,2)
        if m==1:
            x=10
            #print("Morceris creates a lightning storm and bolts of lightning rain down upon you")
            print("Morceris creates a poison cloud that engulfs you and causes your skin to disintegrate")
        elif m==4:
            x=5
            #print("Morceris creates a lightning storm, but you were able to dodge the lightning bolts")
            print("You are able to escape Morceris's poison cloud, but you are still slightly injured")
        elif m==2:
            x=9
            #print("Morceris creates a whirlwind and hurls you at a wall")
            print("Morcercis uses his staff to create a 10 foot tall flaming cobra. The cobra bites you and spits fire on you.")
            if c==2:
                print("[Special Attack!] The cobra explodes. Fire and molten lave engulf you")
                x=x+5
                
        elif m==5:
            x=7
            #print("Morceris creates a whirlwind and hurls you at a wall, but you land on your feet unharmed")
            print("Morceris uses his staff to create a 10 foot tall flaming cobra. You kill it with ease, but it explodes and burns you")
        elif m==3:
            x=6
            #print("Morceris unleashes a Blizzard and causes a tornado of ice spikes to slam into you")
            print("Morceris lifts his hand and you feel him absorb your life force.")
            self.hp=self.hp+5
            if self.hp>self.maxhp:
                self.hp=self.maxhp
            
        elif m==6:
            x=0
            #print("Morceris unleashes a Blizzard of ice spikes, but you raise your shield and block them")
            print("Morceris lifts his hand to absorb your life force, but you evade it.")
            if p==4:
                self.hp=self.hp-5
                print("Morceris lifts his hand to absorb your life force, but you evade it and shoot an arrow at his head [CRITICAL HIT MORCERIS LOSES 5 HP.")
            
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt




#####MORCENGARDE#####
class treeCreature(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=50
        self.maxhp=50
        self.x=x
        self.y=y
        self.symbol='ϔ'
        self.name='TREE CREATURE'
        self.perks=2
        self.gold=200
    
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Heart of the Forest" #allows for different items to be obtained by different monsters

    def getAttack(self):
        '''to give damage to another entity'''     
       # print("**TREE CREATURE'S HEALTH: %d"%(self.hp))    
        m=random.randint(1,6)#random input to ATTACK
        p=random.randint(1,7)
       
        if m==1:
            x=4
            print("Tree creature sucks the life out of you")
            self.hp=self.hp+5
            if self.hp>self.maxhp:
                self.hp=self.maxhp
        elif m==4:
            x=0
            print("The tree creature is unable to drain your energy ")
            
    
        elif m==2:
            x=9
            print("Tree creature shoots poison darts at you")
        elif m==5:
            x=0
            print("You dodge the poison darts")
            
        elif m==3:
            x=12
            print("The tree creature's sharp claws slash your back")
        elif m==6:
            x=0
            print("You duck just before the tree creature slashes.")
            if p==5:
                print("---As you duck under the tree creature, you thrust your sword into its chest [CRITICAL HIT: %s LOSES 7 HEALTH]" %(self.name))
                self.hp=self.hp-7
                x=0
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt


class goblin(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=40
        self.x=x
        self.y=y
        self.symbol='ҩ'
        self.name='GOBLIN'
        self.perks=1
        self.gold=100
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Goblin's Bag of Gold" #allows for more gold to be carried

    def getAttack(self):
        '''to give damage to another entity'''     
        #print("**GOBLIN'S HEALTH: %d"%(self.hp))   
        m=random.randint(1,6)#random input to ATTACK
        p=random.randint(1,7)
       
        if m==1:
            x=7
            print("Goblin stabs you with a poisoned dagger")
            self.hp=self.hp
        elif m==4:
            x=0
            print("You dodge the Goblin's dagger")
            
    
        elif m==2:
            x=10
            print("Goblin jumps on you and bites you with its sharp teeth")
        elif m==5:
            x=0
            print("You catch the Goblin just before he jumps on you. You throw him in all the ground")
            
        elif m==3:
            x=8
            #print("The Goblin steals your gold")#if we can get other things to work, then goblin can steal gold
            print("The Goblin scratches you with its claws")
        elif m==6:
            x=0
            #print("You avoid the Goblin's sneaky fingers and keep your gold.")
            print("You dodge Goblin slashes.")
            
            #if p==5:
                #print("---As you duck under the tree creature, you thrust your sword into its chest [CRITICAL HIT: ENEMY LOSES 7 HEALTH].")
                #self.hp=self.hp-7
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt


class IceDragon(Entity):
    def __init__(self,x,y): #mob enemy: will appear many times
        super().__init__(x,y)
        self.hp=40
        self.x=x
        self.y=y
        self.symbol='ʬ'
        self.name='ICE DRAGON'
        self.perks=4
        self.gold=300
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Scroll of the Blizzard"   #, "Shield of the Glacier"#allows for player to create ice storms
                                        #Added to special spells
    def getAttack(self):
        '''to give damage to another entity'''
       # print("**ICE DRAGON'S HEALTH: %d"%(self.hp))           
        m=random.randint(1,6)
        p=random.randint(1,4)
        t=random.randint(1,10)
        
        if t==6:
            x=99
            print("[Special Attack!] The Ice Dragon stares at you. A strange feeling comes over you and you feel your eyes start to look towards the Ice Dragon's.")
            print("You try to resist it, but you stare directly into the beast's eyes. You feel your blood start to freeze and moments later, your heart freezes solid.")
        else:
            if m==1:
                x=8 #was 5
                print("The Ice Dragon beats its wings and creates a raging blizzard. You are unable to escape it ")
            elif m==4:
                x=8 #was 5
                print("The Ice Dragon beats its wings and creates a raging blizzard. You are unable to escape it")
        
            elif m==2:
                x=10 #was 10
                print("The Ice Dragon opens its mouth deluges you with a torrent of ice spikes")
            elif m==5:
                x=0
                print("You avoid The Ice Dragon's torrent of ice spikes by ducking behind a boulder")
            elif m==3:
                x=11 #was 7
                print("The Ice Dragon picks you up with its mouth and throws you into the air")
            elif m==6:
                x=0
                print("You were able to dodge the Ice Dragon's bite")
                if p==3:
                    print("As you dodge the bite, you raise your sword to slice at the Ice Dragon's vulnerable neck [CRITICAL HIT: ICE DRAGON LOSES 10 HEALTH]")
                    self.hp=self.hp-10
                    x=0
        
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt
class invisibleGoblin(Entity):   #Large 10 ft tall humanoid skeleton. carries a large dragon bone and steel axe.    
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=40
        self.x=x
        self.y=y
        self.symbol='.'
        self.name='TRICKSTER GOBLIN'
        self.perks=2
        self.gold=0
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Goblin Feces" #allows for increased health (allows for increased resistance against swords


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**TRICKSTER GOBLIN'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
       
        if m==1:
            x=7
            print("You feel a knife cut your leg. You look around and see nothing. All you hear is high pitched snickering")
        elif m==4:
            x=0
            print("You look down to the ground and see footsteps moving towards you. You step away from them")
        
        elif m==2:
            x=8
            print("You feel multiple poison darts hit your chest. You can't see the source, and all you hear is high pitched snickering ")
        elif m==5:
            x=0
            print("You look down to the ground and see footsteps moving towards you. You raise your shield and feel multiple darts become lodged into it")
        elif m==3:
            x=7
            print("You see footsteps approaching you quickly. Suddenly they stop and moments later, you feel a small climbing on your back. It bites and scatches you.")
        elif m==6:
            x=0
            print("You step away from the approaching steps. You try to swing your sword but hit nothing. ")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt



    
class SkeletonGuard(Entity):   #Large 10 ft tall humanoid skeleton. carries a large dragon bone and steel axe.   
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=90
        self.x=x
        self.y=y
        self.symbol='Ꝙ'
        self.name='THE SKELETON GUARD'
        self.perks=4
        self.gold=300
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Chestplate of the Revenant" #allows for increased health (allows for increased resistance against swords


    def getAttack(self):
        '''to give damage to another entity'''
        
        #print("**SKELETON GUARD'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        c=random.randint(1,2)
        
       
        if m==1:
            x=12
            print("The Skeleton Guard raises his axe and slams it down right on top of you")
           
            
        elif m==4:
            x=0
            print("You dive roll underneath the Skeleton Guards legs and avoid its axe")
        
        elif m==2:
            x=13
            print("The Skeleton Guard grabs your neck and lifts you into the air. It crushes your windpipe and then throws you on the ground.")
            if c==2:
                print("[Special Attack!] As you struggle to regain your breath, the Skeleton Guard slams his axe on top of you")
                x=x+5
        elif m==5:
            x=0
            print("The Skeleton Guard is slow and you dodge its large, bony hand")
        elif m==3:
            x=10
            print("The Skeleton Guard kicks you with its large bony foot.")
        elif m==6:
            x=0
            print("You dive roll away from the Skeleton Guard's kick")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt


class Dalthuur (Entity):      #####change attacks to better fit his character
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=100
        self.x=x
        self.y=y
        self.symbol='Ӂ'
        self.name='DALTHUUR'
        self.perks=5
        self.gold=350
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "The Cloak of Dalthuur" #allows for increased magik and hp (allows the player to summon an army of undead
                                            #might change this to staff and add it to special weapons


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**DALTHUUR'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        #m=int(m)
        p=random.randint(1,6)
        
        if m==1:
            x=13
            print("Dalthuur raises his hand and conjures a dozen skeletons.")
            print("The skeletons overwhlem you with their numbers and you cannot defend against their attacks")
            print("After a few moments, the army disintegrates into dust. Even magic cannot bring back the dead for long.")
            
            #print(Morceris creates a poison cloud that engulfs you and causes your skin to disintegrate)
        elif m==4:
            x=7
            print("Dalthuur raises his hand and conjures a dozen skeletons.")
            print("You destroy the skeletons, but they were still able to hurt you.")
            
            #print("You are able to escape Morceris's poison cloud, but you are still slightly injured
        elif m==2:
            x=15
            print("Dalthuur raises his hand and conjures an undead cavetroll. In its undead form, the beast is even more terrifying.")
            print("The undead cavetroll breaks off an old bone from a dragon's skeleton and slams it into your chest.")
            print("After a few moments, the cavetroll crumbles into a heap of flesh and bone. Even magic cannot bring back the dead for long.")
            #print("morcercis uses his staff to create a 10 foot tall flaming cobra. The cobra bites you and spits fire on you. "
        elif m==5:
            x=7
            print("Dalthuur raises his hand and conjures an undead cavetroll. In its undead form, the beast is even more terrifying.")
            print("You see the cavetroll break off an old bone from a dragon's skeleton and prepares to smash you with it. You dodge the makeshift club.")
            print("You raise your sword to strike, but the cavetroll crumbles into a heap of flesh and bone. Even magic cannot bring back the dead for long.")
            #print("Morceris uses his staff to create a 10 foot tall flaming cobra. You kill it with ease, but it explodes and burns you
        elif m==3:
            x=10+5+3+2
            print("Dalthuur raises his hands and creates a large dark twister. From behind it, you see a large skeletal dragon  emerge from it.")
            print("In its undead form, it cant breath fire, but it can still bite and claw at you")
            print("Luckliy for you, the Dragon slowly turns to dust. Even magic cannot bring back the dead for long.")
            #print("Morceris lifts his hand and you feel him absorb your life force.")
            #self.hp=self.hp+2
        elif m==6:
            x=5+4
            print("Dalthuur raises his hands and creates a large dark twister. From behind it, you see a large skeletal dragon emerge from it.")
            print("In its undead form, it cant breath fire, but its claws are still sharp. The dragon cuts and slams its tail into your chest.")
            print("You use a fireball and the dragon's wings disintegrate. You then use your sword to slice off the head and vanquish the beast.")
            #print("Morceris lifts his hand to absorb your life force, but you evade it.")
                #if p==4:
                    #self.hp=self.hp-5
                    #print("Morceris lifts his hand to absorb your life force, but you evade it and shoot an arrow at his head [CRITICAL HIT MORCERIS LOSES 5 HP.")
            
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt






#####SHADOVAR######

class DarkElf(Entity):             #mob enemy: many tokens 
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=30
        self.x=x
        self.y=y
        self.symbol='ƺ'
        self.name='SKARAITH'
        self.perks=3
        self.gold=200
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Shadowbow of the Umbra" #will be put into special weapons


    def getAttack(self):
        '''to give damage to another entity'''        
        #print("**SKARAITH'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
       
        if m==1:
            x=4+3+3
            print("The Skaraith shoots a flurry of flaming arrows from his shadowbow")
        elif m==4:
            x=0
            print("You dodge the Skaraith's flaming arrows")
        
        elif m==2:
            x=7
            print("The Skaraith shoots lightning bolts at your chest.")
        elif m==5:
            x=3
            print("You dodge the Skaraith's lightning bolt, but you are still injured by the chain effects")
        elif m==3:
            x=5+3
            print("The Skaraith uses his twin deathblades and slices at both your chest and stomach.")
        elif m==6:
            x=0
            print("You step backwards and dodge the Skaraith's blades.")
        
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt       
class DarkElf2(Entity):             #mob enemy: many tokens 
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=20
        self.x=x
        self.y=y
        self.symbol='ƺ'
        self.name='SKARAITH'
        self.perks=3
        self.gold=200
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Umbra Arrows" #will be put into special weapons


    def getAttack(self):
        '''to give damage to another entity'''    
        #print("**CORRUPTED ELF'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
       
        if m==1:
            x=4+3+3
            print("The Skaraith shoots a flurry of flaming arrows from his shadowbow")
        elif m==4:
            x=0
            print("You dodge the Skaraith's flaming arrows")
        
        elif m==2:
            x=7
            print("The Skaraith shoots lightning bolts at your chest.")
        elif m==5:
            x=1
            print("You dodge the Skaraith's lightning bolt, but you are still injured by the chain effects")
        elif m==3:
            x=5+3
            print("The Skaraith uses his twin deathblades and slices at both your chest and stomach. The blades absorb 4 points of your health")
            self.hp=self.hp+4
        elif m==6:
            x=0
            print("You step backwards and dodge the Skaraith's blades.")
        
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt       


class HoarFrostWolves(Entity):               #'''###'''#might add to dark elf as an attack
    def __init__(self,x,y):  ##mob enemy: many tokens
        super().__init__(x,y)
        self.hp=20
        self.x=x
        self.y=y
        self.symbol='Ɏ'
        self.name='HOARFROST WOLF'
        self.perks=2
        self.gold=100
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Pelt of the Hoarfrost" #allows for more hp (increased frost resistance)


    def getAttack(self):
        '''to give damage to another entity'''
        #print("**HOARFROST WOLF'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
       
        if m==1:
            x=5
            print("The Hoarfrost Wolf jumps in the air and tackles you to the ground. It claws at your chest")
        elif m==4:
            x=0
            print("You sidestep and slice at the wolf's stomach")
            print("[Hoarfrost Wolf loses 2 health]")
            self.hp=self.hp-2
        
        elif m==2:
            x=7
            print("The Hoarfrost Wolf bites at your sword arm.")
        elif m==5:
            x=0
            print("You dodge the wolf's bite.")
        elif m==3:
            x=4+2+2+2
            print("The Hoarfrost Wolf howls and a blizzard comes in. The temperature drops and you can no longer see the wolf.")
            print("You hear several other wolves barking at you and then they start biting your extremeties and clawing at your chest.")
        elif m==6:
            x=0
            print("The Hoarfrost Wolf begins to howl and a blizzard starts to form. Before the ski becomes a white-out, you lunge stab the wolf through the mouth.")
            print("[Hoarfrost Wolf loses 5 health]")
            self.hp=self.hp-5
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

class goblinKing(Entity): ##maybe remove this and replace it with Sarvo Mercer, Bandit Lord of Morzala: Came here by sea after he saw Dalthuur escape
    def __init__(self,x,y): ##Knows the Rebel. Wants to createa better name for Morzala. For the passed millenia, citizens of Morzala have been known as
        super().__init__(x,y)## cowards. Ever since they abandonned the attack on Dalthuur. Sarvo was the Rebel's husband's twin brother. Both brothers
        self.hp=9               ##were from Morzala. Sarvo, in hopes of creating a better name for Morzala, tries to help. He got word from Lydia shortly after 
        self.x=x             ###Morceris impersonated the lord because he knew that Amodera knew of Morzala. He knew if he offered help and gold, they would believe him
        self.y=y                  ##it had been 500 years and so Amodera would have expected this. Mercer is a disgraced name. The wealthy king was of a different family
        self.symbol='Ҩ'
        self.name='GOBLIN KING'
        self.perks=4
        self.gold=1000
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Goblin King's Hoard of Gold" #allows for even more gold storage

    def getAttack(self):
        '''to give damage to another entity'''     
        #print("**GOBLIN KING'S HEALTH: %d"%(self.hp))   
        m=random.randint(1,6)#random input to ATTACK
        p=random.randint(1,7)
       
        if m==1:
            x=3
            print("Goblin stabs you with a poisoned dagger")
            self.hp=self.hp
        elif m==4:
            x=0
            print("You dodge the Goblin's dagger")
            
    
        elif m==2:
            x=2
            print("Goblin jumps on you and bites you with its sharp teeth")
        elif m==5:
            x=0
            print("You catch the Goblin just before he jumps on you. You throw him in all the ground")
            
        elif m==3:
            x=3
            #print("The Goblin steals your gold")#if we can get other things to work, then goblin can steal gold
            print("The Goblin scratches you with its claws")
        elif m==6:
            x=0
            #print("You avoid the Goblin's sneaky fingers and keep your gold.")
            print("You dodge Goblin slashes.")
            
            #if p==5:
                #print("---As you duck under the tree creature, you thrust your sword into its chest [CRITICAL HIT: ENEMY LOSES 7 HEALTH].")
                #self.hp=self.hp-7
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

class korvorath (Entity):      ###SECOND SEA CREATURE
    def __init__(self,x,y):
        super().__init__(x,y)#₰
        self.hp=300
        self.x=x
        self.y=y
        self.symbol='Ꙃ'
        self.name='THE KORVORATH'
        self.perks=5
        self.gold=350
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "The Staff of Shanzalar" #grants the player a very powerful attack
                                            #will go into special weapons-only weapon to create storms or something

    def getAttack(self):
        '''to give damage to another entity'''
        a=random.randint(1,2)
        m=random.randint(1,6)#random input to ATTACK
        #m=int(m)
        p=random.randint(1,6)
        c=random.randint(1,4)
        if a==1: #does trigger Rage of the Sea
            print("The Korvorath becomes enraged and it performs more dangerous attacks")
            
            if m==1:
                x=8
                print("The Korvorath uses telekinesis and lifts you into the air. As you float in the air helpless, it wraps its tentacles around you and crushes you.")
                if c==2:
                    print("[Special Attack!] As you struggle to escape, the Korvorath creates a massive whirlpool and throws you into the swirling water.")
                    x=x+8
                else:
                    pass
            
            elif m==4:
                x=10
                print("The Korvorath uses telekinesis and lifts you into the air. You struggle to move, but you are able to let loose a thunderbolt at the sea monster.")
                print("The Korvorath is stunned and you drop into the ocean.")
                print("THE KORVORATH LOSES 10 HEALTH")
                self.hp=self.hp-10         
            elif m==2:
                x=20
                print("The Korvorath uses its mind to unravel the chains on its arms. The chains that once trapped it are now hurling at you. ")
                print("The Korvorath uses telekinesis to wrap the chains around you. The spikes dig into you skin and the sharper ends pierce your lungs.")
            
            elif m==5:
                x=0
                print("You see the Korvorath's chains unravel and hurl towards you. You jump out of the way. ")
            
            elif m==3:
                k=random.randint(1,20)
                if k==19:
                    
                    x=99
                    print("The Korvorath opens its mouth and you see red vapor flow from its mouth towards you. It surrounds you and the vapor flows into your mouth")
                    print("You feel your life force leave you, and you see the red vapor return to the Korvorath, revitalizing it completely.")           
                    self.hp=self.maxhp
                else:
                    print("The Korvorath opens its mouth and you see red vapor flow from its mouth towards you. It surrounds you and the vapor flows into your mouth")
                    print("As the red vapor enters your body, you feel as if your being electrocuted from the inside.")
                    x=10
            elif m==6:
                x=0
                print("The Korvorath opens its mouth and you see red vapor flow from its mouth towards you. You use raise your hands and cast Fire Blast. ")
                print("The fire burns the red cloud and the Korvorath.")
                self.hp=self.hp-10
                print("THE KORVORATH LOSES 10 HP.")
        if a==2: #Does not trigger Rage of the Sea: Everything does not do double damage
            print("")
            if m==1:
                x=13
                print("The Korvorath grabs you with its scaly, spiked hands. Its sharp claws dig into back and chest.")
                if c==2:
                    print("[Special Attack!] It raises its hand and throws you into its mouth and eats you.")
                    x=20
                else:
                    pass
           
            elif m==4:
                x=2
                print("The Korvorath attempts to grab you, but you dodge the hand and prepare to retaliate")
            #
            elif m==2:
                x=15
                print("The Korvorath dives underwater. You look around the water but can't see it. Suddenly, the water erupts and the wave throws you into the air")
                print("As you are falling towards the water, you stop moving and realize the Korvorath is using telekinesis.")
                print("You turn around just in time to see a cavern of teeth engulf you.")
            elif m==5:
                x=0
                print("The Korvorath dives underwater. You look around the water but can't see it. Suddenly, the water erupts and the wave throws you into the air")
                print("As you are falling, you move around to face the Korvorath. As the Korvorath opens its mouth, you use Ice Blast and send ice spikes into its mouth.")
                self.hp=self.hp-10
                print("THE KORVORATH LOSES 10 HP.")
            elif m==3:
                x=4
                print("The Korvorath raises its tentacles and they shoot out and wrap around you.")
                print("Half the tentacles are used to crush your chest while the rest rip your limbs off.")
            
                
            elif m==6:
                x=0
                print("The Korvorath raises its tentacles and they shoot out and wrap around you. Fortunately, you have a free sword hand and slice at the tentacles.")
            #print("Morceris lifts his hand to absorb your life force, but you evade it.")
                #if p==4:
                    #self.hp=self.hp-5
                    #print("Morceris lifts his hand to absorb your life force, but you evade it and shoot an arrow at his head [CRITICAL HIT MORCERIS LOSES 5 HP.")
            
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

    



class ElectroDragon(Entity):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=120
        self.x=x
        self.y=y
        self.symbol='Ϟ'
        self.name='ELECTRODRAGON'
        self.perks=5
        self.gold=300
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Scroll of the Thunderstorm" #allows for more magik and hp. (allows the player to summon lightning storms
                                        #will go into special spells
    def getAttack(self):
        '''to give damage to another entity'''
        #print("**ELECTRODRAGON'S HEALTH: %d"%(self.hp))           
        m=random.randint(1,6)
        c=random.randint(1,2)
        if m==1:
            x=13
            print("Electrodragon raises its wings and creates a Thunder storm. The lightning strikes all around you.")
        elif m==4:
            x=4
            print("Electrodragon raises its wings and creates a Thunder storm. You dodge most of the bolts, but a few still hit you.")
            if c==2:
                print("[Special Attack!] As you are struggling to dodge the lightning bolts, the Electro Dragon opens its mouth and releases a torrent of electricity")
                x=x+8
        
        elif m==2:
            x=11
            print("The Electrodragon opens its mouth releases a torrent of electricity. The torrent hits you right in the chest")
        elif m==5:
            x=0
            print("The Electrodragon's lightning breath misses you")
        elif m==3:
            x=9
            print("The Electrodragon slashes at you with its lightning claws")
        elif m==6:
            x=0
            print("You dodge the Electrodragon's claws")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

class fireMage(Entity): ##FIRE MAGE
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=5 #120
        self.x=x
        self.y=y
        self.symbol='ᵮ'
        self.name='FIRE SAVEREK'
        self.perks=4
        self.gold=250
        self.ring1=1
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Ring of the Firestorm" #allows for more magik and hp. (allows the player to summon lightning storms
                                        #
    def getAttack(self):
        '''to give damage to another entity'''
        #print("**FIRE SAVEREK'S HEALTH: %d"%(self.hp))           
        m=random.randint(1,6)
        if m==1:
            x=13
            print("The Fire Saverek shoots fire from his hands. The flames engulf you")
        elif m==4:
            x=4
            print("You fire erupt out of the Fire Saverek's hands. You dodge flames in")
        
        elif m==2:
            x=11
            print("The Fire Saverek summons a sword made of fire. He slices at your chest and cuts and burns you")
        elif m==5:
            x=0
            print("The Fire Saverek summons a sword made of fire. He slices at your chest, but you dodge the flaming sword")
        elif m==3:
            x=9
            print("The Fire Saverek raises his hands and the ground opens up beneath your feet. Molten lava erupts from hole and engulfs you.")
        elif m==6:
            x=0
            print("You see the Fire Saverek raise his hands you feel the ground cave in, but you jump out of the way before molten lava erupts out of it.")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

class frostMage(Entity): ### FROST MAGE
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=5 #120
        self.x=x
        self.y=y
        self.symbol='҉'
        self.name='FROST SAVEREK'
        self.perks=4
        self.gold=250
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Ring of the Snowstorm" #allows for more magik and hp. (allows the player to summon lightning storms
                                        #will go into special spells
    def getAttack(self):
        '''to give damage to another entity'''
        #print("**FROST SAVEREK'S HEALTH: %d"%(self.hp))           
        m=random.randint(1,6)
        if m==1:
            x=13
            print("The Frost Saverek raises his arms in the air and slams his fists into the ground. Ice spikes erupt from the ground and crash into you.")
        elif m==4:
            x=4
            print("The Frost Saverek raises his arms in the air and slams his fists into the ground. Ice spikes erupt from the ground, but you doge them")
        
        elif m==2:
            x=11
            print("You feel a large gust of wind rush passed you. You see the Frost Saverek levitating in the air; surrounded buy snow and ice.")
            print("He reaches his arm out and you see thousands of ice shards rush at you and surround you, piercing your skin")
        elif m==5:
            x=0
            print("You feel a large gust of wind rush passed you. You see the Frost Saverek levitating in the air; surrounded buy snow and ice.")
            print("He reaches his arm out and you see thousands of ice shards rush at you. You cast a fireball just before they engulf you.")
        elif m==3:
            x=9
            print("The Frost Saverek hands and arms become engulfed in ice spikes. The ice spikes make their way towards his hands and combine to form twin ice blades.")
            print("The Frost Saverek rushes at you and stabs you in the gut. You feel the cold blades cut through your organs.")
        elif m==6:
            x=0
            print("The Frost Saverek hands and arms become engulfed in ice spikes. The ice spikes make their way towards his hands and combine to form twin ice blades.")
            print("He rushes at you, but you use your shield and sword to break the ice blades")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt

class thunderMage(Entity): ###THUNDER MAGE
    def __init__(self,x,y):
        super().__init__(x,y)
        self.hp=5 #120
        self.x=x
        self.y=y
        self.symbol='ϗ'
        self.name='THUNDER SAVEREK'
        self.perks=4
        self.gold=250
        #e=Dragon
        
   
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "Ring of the Maelstrom" #allows for more magik and hp. (allows the player to summon lightning storms
                                        #will go into special spells
    def getAttack(self):
        '''to give damage to another entity'''
       # print("**THUNDER SAVEREK'S HEALTH: %d"%(self.hp))           
        m=random.randint(1,6)
        if m==1:
            x=13
            print("Thunder Saverek releases the heavens. Giant ice shards rain down upon you followed by a single destructive bolt of lightning")
        elif m==4:
            x=4
            print("You dodge the ice shards, but the bolt of lightning hits you.")
        
        elif m==2:
            x=11
            print("The Thunder Saverek cups his hands together. Small lightning bolts fly everywhich way. He thrusts is hands forward and releases a vortex of lightning.")
            print("The vortex slams into you engulfs you in lightning. You then are thrown into the air by a blast of thunder")
        elif m==5:
            x=4
            print("The Thunder Saverek's vortex of lightning misses you. The force of the thunder following it throw you into the air and you crash into the ground.")
        elif m==3:
            x=9
            print("The Thunder Saverek summons a  Battle Axe made of lightning. The axe slams into your chest and you are forced into the air.")
            print("As you fly through the air, you still feel the electricity running through your veins. When you hit the ground, there is an explosion of lightning")
        elif m==6:
            x=3
            print("You dodge the lightning Battle Axe, but then Thunder Saverek slams the axe into the ground. You see a flash of energy travel through the ground and into your body")
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt




class Shanzalar (Entity):      #####replace all mentions of morceris with shanzalarif c==2:
               # print("[Special Attack!] As you are struggling to dodge the lightning bolts, the Electro Dragon opens its mouth and releases a torrent of electricity")
                #x=x+5
    def __init__(self,x,y):
        super().__init__(x,y)#₰
        self.hp=400
        self.x=x
        self.y=y
        self.symbol='₰'
        self.name='SHANZALAR'
        self.perks=5
        self.gold=400
    
    def getLoot(self): ##goes into the body of whichever enemy we are fighitng
        return "The Staff of Shanzalar" #grants the player a very powerful attack
                                            #will go into special weapons-only weapon to create storms or something

    def getAttack(self):
        '''to give damage to another entity'''
        #print("**SHANZALAR'S HEALTH: %d"%(self.hp))
        m=random.randint(1,6)#random input to ATTACK
        #m=int(m)
        p=random.randint(1,6)
        #c=random.randint(1,2)
        if m==1:
            x=1000
            print("Shanzalar creates a lightning storm and bolts of lightning rain down upon you")
            #print(Morceris creates a poison cloud that engulfs you and causes your skin to disintegrate)
        elif m==4:
            x=6
            print("Shanzalar creates a lightning storm and bolts of lightning crash down upon the ground. You dodge most of them, but some hit you")
            #print("You are able to escape Morceris's poison cloud, but you are still slightly injured
        elif m==2:
            x=1000
            print("Shanzalar creates a whirlwind and hurls you at a wall")
            #print("morcercis uses his staff to create a 10 foot tall flaming cobra. The cobra bites you and spits fire on you. "
        elif m==5:
            x=1000
            print("Shanzalar creates a whirlwind and hurls you at a wall, but you land on your feet unharmed")
            #print("Morceris uses his staff to create a 10 foot tall flaming cobra. You kill it with ease, but it explodes and burns you
        elif m==3:
            x=12
            print("Shanzalar unleashes a Blizzard and causes a tornado of ice spikes to slam into you")
            #print("Morceris lifts his hand and you feel him absorb your life force.")
            #self.hp=self.hp+2
        elif m==6:
            x=0
            print("Shanzalar unleashes a Blizzard of ice spikes, but you raise your shield and block them")
            #print("Morceris lifts his hand to absorb your life force, but you evade it.")
                #if p==4:
                    #self.hp=self.hp-5
                    #print("Morceris lifts his hand to absorb your life force, but you evade it and shoot an arrow at his head [CRITICAL HIT MORCERIS LOSES 5 HP.")
            
        print("YOU LOST: %s Health"%(x))
        return x #how much damage is dealt



#SPECIAL
    #WEAPON (5-6)
    #STAFFS, BATTLEAXE, 
    #SPELLS (6-7) :}

#ADD MORE CRITICAL HITS TO LARGER ENEMIES LIKE DRAGONS, GUARDS, MAGES, SERPENTS, SORCERERS.

