import random as rd

class Risk:
    
    def __init__(self):
        self.world = {}
        self.round = 1
        self.listAlias = '''
        Alias -  Region\n
        NA  - North America\n
        CA  - Central America\n
        SA  - South America\n
        NP  - North Pole\n
        WE  - Western Europe\n
        EE  - Eastern Europe\n
        NAF - North Africa\n
        SAF - South Africa\n
        A   - Asia\n
        O   - Oceania\n
        '''
        self.Napoleon = '''                 `osso+/:-.                                                                    
                      :ddmdhhhhhys/-`            `.                                                 
                       :ddmdddddhhhhyso+/-.`    `.:-`                                               
                       +hyshdddddddddhhhyyys+-` `:+-//            `.....`                           
                       ```.yyhyyhhhhhhhhhhhhyyso-.--/soo-      `..:+shosso/.                        
                           +yyyyyyyyyyyyyyhyyyyyys+:/ysyy+`  ./-smNNmyhddyso+.                      
                           oyyyyyyyyyyysoosssoo+/++osyhNmNmo:o+hMMNMMyhMMMNdy+/-`                   
                           syyoohys/--:::::+yooooshshoshNNNd++dMNdyshdMMNmhhs+//.                   
                           .ydsosss:..`` ``:sossoos/hyo+smh/omMMms/osymNd:``                        
                            -yhdhyosyo+///:-:++ohhyoddddyssyNmNNy-/-:ymddsoooo++/-.`                
                             .so/smNdso+/..-:+ooyhdy/:/ohhdhhmNNNsyoooyhhhhyyhyyyyys+.              
                              ./ymmdmhyys`..----/y+.`.-/oydhshmNNmss+oyyhhhhyyhhyhhhys/             
                              :+//oyyyhhho::::/ss-``.-:/oddddNNdyhhyyssyyhdhhhyyyyhhhhy-            
                          `-:+//+` .syyyyyyoys+:-..-:+yyddddNdmhhyysso+osyhhhyyyyyyhhhdo`           
                         +/-`  y`   -yyys+.`````.-//oyhmmmmmdhhhyysso++oosssssyyyyhhhhhhy-`         
                        `s     :o``..os/.     ``.-:osydmmmdmhhhyyssoo++++oosssyhhhhhhdhddhs`        
                         /:-`   -s..:.```` ````.-:/+oyhhmmmmmhyyssooooooosssssyyhhdddddddy-         
                           `/:`` `s`````..``..-/+yyhhhmmmyyddhyssssssssyhdmmddhdddhddddh+`          
                             :/-:--``    `./osyhddhhmNmd/:.:oooyhssyhddddmddmmmddhhhyys-            
                           `.``://:::/:---:+++ssshhmNNNm+::.``.sNmNNNMMMMMMdyhmdhyyyo:`             
                          ``.---...`.://+oo+/+ydmNNNNNNNmhhy/:+NMMMMMMMNdmmmdhhdyo:`                
                           .-::..`.-://+ooyyhdmNNNNNNNmNmdhy--:hdmNNmmmdhdhhdddhs                   
                              ```.-:--:+ydddmmmNNNNNmmmdddsoo/-:-+ssohhhhddhhhhh.                   
                                   `-/+ssyhdmhydmmmd+/ooo:-/::--:///yNNmhhhyyhhy`                   
                         .:.---:.-:/+oyysoyhhdmmmdys+++:d:---.``:ohhmMMdyyhyyys-                    
                         ```      ``./ossyhdddho:.+oosoom::ooo+ohmNNMMMdyyyso:`                     
                                   ```.-/syyo:..../yhdyohsyhydmNMMMMMNo//::.`                       
                   `-:/-`        `....-:+o/...:/oshdmms/hddmmNMMMMMMNy-  `so.                       
           `...  .oyhdmy```    `````.:ooo.`-/shmmNmNNNhhmNNMMMMMMMNmmmyyyyhs-                       
        .+sshmmy/ohmmmdd:.``   ```-:-/oso-./+ohmNNmhyhhhdNMMMMMMNmmmNmmdhhys+/:-.``                 
       :hddmNMNmdy/--.-::`    `.-:oyoshy++/:--:ohdyddmNMMMMMMMNmdyyhhhyyyhhhhhhhhss+:.`             
     .odNNds+odmdyo:.`````...-/:/ohhddds.:oo/::/ohhyNNMMMNNMMNhooyy/.````-:/+syyhhhhhds/.           
   .ohdmy-   .ydyyss+o//+osysshsoydNNNh- ./sssooshmhdNNNNMMNh++yms`      `../+oyhdmmmdhhyo-         
  `/oos-    .-//y-.:+yhyydmNNmNNNNNmmNo``-.--+yhyhmNh+mNNNds/sdmd:``      ``-//sydmNNmdhhss/`       
 `-oos`     -:/yy`   `-/shmmNNNNNNmmmdo-/---.-:hdhdmd/odyys+ddddd+.``      `.:/syhNMMNmdhhso+       
 .ydo.      `.:s/-        `.-/o+/ydddds+y++/:. `sdddmhs+//-odmdddo.``     ``-/+ydmNMMMNmhhdys+-`    
  ./o-       `-odd.               -oydhohssyo.``-mmmNMms/--+ymmdh/````   ``.:osdmNMMMMNNdydNmddho.  
.:odm/       /ssm+                  `/syyhhhs-:/+hdNNNMmhoyyhddho.```````.-/oydNNMMMMNmmhsdMyNNmmd+ 
`soh/         /s/                      `/oyysoshddmmNmmNNdddddh:  `````.-:+ydmdmNNMMNmdhyyNm`+NNNNm:
 :s-           `                          `:+shhhhymmmMhdddddh-``.```..:+oshhddmNMMMNmmhhNN- +mMNNms
                                              `.:+oyNNNyhhddd+--:```.-:+osymNNMMMMMNNmddNd-.yNNMNNdo
                                                  -mhdhd+-----//+..-:+yhhdmNMMMMMMNmmmNMdshNMNNNNmh`
                                                  +o:``ys`    .`.-:/oydmNMMMMNNNNNNmNMMNNNMMMNNmdd+ 
                                                      ./+/``` .`.+o+oosyyysyddmNNNNNNNNNNNNNNmmmdo  
                                                    ``.--.....`--++:+sysyyysssshhhdmNNmmmNNNmdys:   
                                                    ..---.......---..-//+++sysshhdddmmNNNmdhy+:`    
                                                     `.--:.````....--:/+////+osyyhhydmmNdo:.``      
                                                     `-..-/::::/++++osssydhhddmmmmdmNNNMNy:.        
                                                      :////://///+oyyyyyyhdmmmdhhdhdNMMMMMMms       
                                                     `+++++//oyhddmmhdmmmNNMNd-` `.-yNMMMMMNs       
                                                      .syyyyhhdddddys/:dNNMMMMm+`  `sNMMMNy-        
                                                       `:/+oshhhhy+:` .hNMMMMMMN+ .yNNNmy-          
                                                         ``.-::--` `:ymNMMMNmdy/-odmNms-            
                                                                 .ohNNNNNds/. .oddmmo.              
                                                               `-ymNNds/.   `+hyhds-                
                                                        ``-``.-/hmh+-`` ``.`:syys-                  
                                                   ./...::+ooohy/.  .o-`-yysyyy/`                   
                                                  -so+/oy+ydhy:    .++yhyh+-/:.                     
                                                 `//yhdhs`` `      `.::///`                         '''                           
    
    
    def createWorld(self,listobj):
        '''creates the map on which the game will be played'''
        for i in listobj:
            self.world[i.alias] = i
            
    def checkWorld(self):
        '''checks if there are regions without troops and updates its controlled status'''
        for i in self.world:
            if self.world[i].troopsRegion == 0:
                self.world[i].controlled_by = None
                
    def checkTotalDomination(self, play1, play2):
        players_who_control = []
        for i in self.world:
            if self.world[i].controlled_by != None:
                players_who_control.append(self.world[i].controlled_by)
        if play1.name in players_who_control and play2.name not in players_who_control:
            return True
        elif play1.name not in players_who_control and play2.name in players_who_control:
            return True
        else:
            return False
                
                

    
    def checkrounds(self):
        '''checks the number of rounds played and adds 1 to the count if rounds are less than 10'''
        if self.round == 10:
            print('THE GAME HAS ENDED')
            # aqui pendent de fer count de controlled
            pass
        else:
            print(f'\n \n Round {self.round} finished.\n Starting round {self.round + 1} \n')
            self.round += 1
    
    def checkWinner(self, play1, play2):
        '''checks which player has more controled countries'''
        play1_control = 0
        play2_control = 0
        for i in self.world:
            if self.world[i].isControlled() == play1.name:
                play1_control += 1
            elif self.world[i].isControlled() == play2.name:
                play2_control += 1
            else:
                pass
        if play1_control > play2_control:
            print(f'{play1.name} wins!\n')
            print(self.Napoleon)
        elif play1_control < play2_control:
            print(f'{play2.name} wins!\n')
            print(self.Napoleon)
        else:
            print("it's a draw! World Domination must wait..." )  

class Regions:
    
    def __init__(self, country, alias, coordinate):
        self.name = country
        self.alias = alias
        self.controlled_by = None
        self.troopsRegion = 0
        self.coordinate = coordinate
        
    def isControlled(self):
        '''returns the controler^s name'''
        return self.controlled_by
    
    def howManyTroops(self):
        '''returns how many troops are in the country'''
        return self.troopsRegion
    
    def adjacent(reg1, reg2):
        '''checks if two regions are adjacent'''
        if (reg1.coordinate == reg2.coordinate + 1) or (reg1.coordinate == reg2.coordinate - 1):
            return True
        else:
            return False
        
    def getAlias(ali,listobj):
        '''returns a Region object that checks with the alias passed'''
        for i in listobj:
            if ali == i:
                return listobj[ali]        

        print('Non existant alias')
        return False
    
    def checkWorld(game):
        '''prints the status and number of troops of each region in the worldmap'''
        for i in game:
            print(f'the country {game[i].name} is controlled by {game[i].controlled_by}')
            print(f'with a total of {game[i].troopsRegion} troops \n\n')
               
    def checkWorld_2(game):
        world = game
        NP = world['NP'].isControlled()
        NPt = world['NP'].troopsRegion
        NPn = world['NP'].name
        WE = world['WE'].isControlled()
        WEt = world['WE'].troopsRegion
        WEn = world['WE'].name
        EE = world['EE'].isControlled()
        EEt = world['EE'].troopsRegion
        EEn = world['EE'].name
        NA = world['NA'].isControlled()
        NAt = world['NA'].troopsRegion
        NAn = world['NA'].name
        CA = world['CA'].isControlled()
        CAt = world['CA'].troopsRegion
        CAn = world['CA'].name
        SA = world['SA'].isControlled()
        SAt = world['SA'].troopsRegion
        SAn = world['SA'].name
        NAF = world['NAF'].isControlled()
        NAFt = world['NAF'].troopsRegion
        NAFn = world['NAF'].name
        SAF = world['SAF'].isControlled()
        SAFt = world['SAF'].troopsRegion
        SAFn = world['SAF'].name
        A = world['A'].isControlled()
        At = world['A'].troopsRegion
        An = world['A'].name
        O = world['O'].isControlled()
        Ot = world['O'].troopsRegion
        On = world['O'].name
        world_map = f'''
////////////////////////////::{NPn}    ////////////////////////////////////////////////
/////////////////////::---/:-.      {NPt}//////////////::-..````----:::::://///////////////////////
//:-.`   ```````....```.. `:/-  {NP}.-://///-`` ``....``                     `````.--///////////////
/-```.`           `-::.`..://-.-:///:://:/-` `-                             ```.` `-:///////////////
::::://-           .:.    -///////////:-`::``.`                {EEn}.-:/-`-/////////////////
///////.{NAn}           /////`-..//{WEn} {WEt}                 {EE} {EEt}                   `-/:://///////////////
//////-   {NA}    //////-.`/////////////{WE}.                        `::.://////////////
//////    {NAt}      -:////////////////////-``---:-:--``         {An}             .-.:-`://////////////////
//////-`     ``` -://////////////////:`     `.-..--    `      {A}           -::-:///////////////////
///////..   ::::.://///////////////:.              .   `.````  {At}            `-///////////////////////
///////:{CAn}-//////- //////// {NAFn}    `            ://-.   .:.   `--::://////////////////////
/////////::{CAt}  //:::://///////////-      {NAF}    :////:` -///:`` .//:-://///////////////////
////////{CA}//:-:.` ``.:://////////:-`   ` {NAFt}       ``://////:./////---:/::///////////////////////
////////////////-       `-://////////:-::          `://////////////-`-/-``:://://////////////////
////////////////   {SAn}///////////- {SAFn}       /////////////-`:.`-`-/:...-://////////////
////////////////.    {SA}    `://///////////-  {SAF}  `///////////////////::-:/://:::...://///////////
/////////////////-` {SAt}    ://////////////.  `::.{SAFt}/////////////////////:-.``:.-///////////////
///////////////////-        `///////////////-      .:: -//////////////////:-.` {O}   -//////////////
///////////////////:      .::////////////////`    `:/:-///////////////////. {On}     :////
///////////////////:     `://////////////////:  `.:///////////////////////.  `.{Ot}   .//////////////
////////////////////    .:////////////////////:://////////////////////////::////-``.:////:-:////////
////////////////////-  -//////////////////////////////////////////////////////////////:---://///////
/////////////////////` ://////////////////////////////////////////////////////////////::////////////
//////////////////////--:///////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////// '''
        world_map_named = world_map.replace('/',' ')
        print(world_map_named)

class Troops:
    
    def __init__(self,power,owner, location=None):
        self.power = power
        self.owner = owner
        self.location = location
    
    def unit():
        pass
    
    


class Player:
    
    def __init__(self,name):
        self.name = name
        self.currentSel = 0 # This is Troops
        self.currentTar = 0 # This is Regions
        
    def select(self, world):
        '''checks if a country is a valid source for an attack'''
   
        while True:
            selection = input('select a country(by alias) where your troops are stationed')
            if selection.upper() == 'EXIT':
                print('\n Bye! See you at the next War.. \n')
                quit()
                break
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if regSelected.isControlled() != self.name:
                    print('you do not control the selected country')
                elif regSelected.howManyTroops() == 0:
                    print('you do not have troops on the selected country')
                else:
                    self.currentSel = Troops(regSelected.howManyTroops(),regSelected.isControlled(),regSelected)
                    print(f'you selected {self.currentSel.power} troops on {regSelected.name}')
                    break
    
    def target(self, world):
        '''checks if a country is a valid target for an attack'''
        while True:
            selection = input('select a country(by alias) to attack.\n Write "selection" to go back to region selection')
            if selection.upper() == 'EXIT':
                print('\n Bye! See you at the next War.. \n')
                quit()
                break
            if selection == 'selection':
                return False
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if Regions.adjacent(self.currentSel.location, regSelected) == False:
                    print('country out of reach (not adjacent)')
                elif regSelected.isControlled() == self.name:
                    print('you already control this country!')
                else:
                    self.currentTar = regSelected
                    print(f'your next attack will target {self.currentTar.name}')
                    break
    
    def attack(self,world):
        '''resolves the attack with random rolls of dice. Updates the control of countries if needed'''
        if self.currentSel.power != 0:
            base_attack = self.currentSel.power
            base_defense = self.currentTar.troopsRegion

            input('you try to attack! (press Enter to continue)')
            input('you roll a dice! (press Enter to continue)')
            current_roll = rd.randint(1,6)
            input(f'you rolled a {current_roll} (press Enter to continue)')
            final_attack = current_roll + base_attack
            print(f'Your total attack is {base_attack + current_roll} \n')

            input("now it's time for the opponent to defend..(press Enter to continue)")
            input("opponent rolls a dice.. (press Enter to continue)")
            current_roll = rd.randint(1,6)
            input(f' opponent rolled a {current_roll} (press Enter to continue)')
            final_defense = base_defense + current_roll
            print(f'opponent total defense is {base_defense + current_roll} \n')

            if final_defense >= final_attack:
                print('the opponent resists the attack..')
                print('you lose 1 troop on the combat..')
                world[self.currentSel.location.alias].troopsRegion -= 1
            else:
                print(f'you win! you conquered {self.currentTar.name}')
                world[self.currentTar.alias].controlled_by = self.name
                world[self.currentTar.alias].troopsRegion = 1
        else:
            print('all your troops on this country died or fled..')
            
    def recruit(self, world):
        '''recruits 1 troop in one of the player controled regions'''
        while True:
            selection = input('select a country (by alias) to gather troops from')
            if selection.upper() == 'EXIT':
                print('\n Bye! See you at the next War.. \n')
                quit()
                break
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if regSelected.isControlled() == self.name:
                    #regSelected.troopsRegion += 1
                    world[regSelected.alias].troopsRegion +=1
                    print(f'{self.name} recruited 1 troop on {regSelected.name}\n ')
                    break
                else:
                    print('you cannot recruit on regions you dont control')
                
            
            
            
    def resetPlay(self):
        '''sets to 0 both select and target'''
        self.currentTar = 0
        self.currentSel = 0

class IAPlayer(Player):
    
    def __init__(self,name):
        super(IAPlayer,self).__init__(name)
        self.currentSel = 0 # This is Troops
        self.currentTar = 0 # This is Regions
        
        
    def select(self, world):
        '''checks if a country is a valid source for an attack'''
        while True:
            selection = rd.choice(['NA','CA','SA','NAF','SAF','NP','WE','EE','A','O'])
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if regSelected.isControlled() != self.name:
                    print('Thinking...\n')
                elif regSelected.howManyTroops() == 0:
                    print('Thinking...\n')
                else:
                    self.currentSel = Troops(regSelected.howManyTroops(),regSelected.isControlled(),regSelected)
                    print(f'you selected {self.currentSel.power} troops on {regSelected.name}')    
                    break    
    
    def target(self, world):
        '''checks if a country is a valid target for an attack'''
        tries = 0
        while True:
            selection = rd.choice(['NA','CA','SA','NAF','SAF','NP','WE','EE','A','O'])
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if tries == 10:
                    selection = 'selection'
                    return False
                elif Regions.adjacent(self.currentSel.location, regSelected) == False:
                    tries += 1
                    print('Thinking...\n')
                elif regSelected.isControlled() == self.name:
                    tries += 1
                    print('Thinking...\n')
                else:
                    self.currentTar = regSelected
                    print(f'your next attack will target {self.currentTar.name}')
                    break
                
    
    def attack(self,world):
        '''resolves the attack with random rolls of dice. Updates the control of countries if needed'''
        if self.currentSel.power != 0:
            base_attack = self.currentSel.power
            base_defense = self.currentTar.troopsRegion

            input('you try to attack! (press Enter to continue)')
            input( 'you roll a dice! (press Enter to continue)')
            current_roll = rd.randint(1,6)
            input(f'you rolled a {current_roll} (press Enter to continue)')
            final_attack = current_roll + base_attack
            print(f'Your total attack is {base_attack + current_roll} \n')

            input("now it's time for the opponent to defend..(press Enter to continue)")
            input("opponent rolls a dice.. (press Enter to continue)")
            current_roll = rd.randint(1,6)
            input(f' opponent rolled a {current_roll} (press Enter to continue)')
            final_defense = base_defense + current_roll
            print(f'opponent total defense is {base_defense + current_roll} \n')

            if final_defense >= final_attack:
                print('the opponent resists the attack..')
                print('you lose 1 troop on the combat..')
                world[self.currentSel.location.alias].troopsRegion -= 1
            else:
                print(f'you win! you conquered {self.currentTar.name}')
                world[self.currentTar.alias].controlled_by = self.name
                world[self.currentTar.alias].troopsRegion = 1
        else:
            print('all your troops on this country died or fled..')
            
    def recruit(self, world):
        '''recruits 1 troop in one of the player controled regions'''
        while True:
            selection = rd.choice(['NA','CA','SA','NAF','SAF','NP','WE','EE','A','O'])
            if Regions.getAlias(selection,world) != False:
                regSelected = Regions.getAlias(selection,world)
                if regSelected.isControlled() == self.name:
                    world[regSelected.alias].troopsRegion +=2
                    print(f'{self.name} recruited 2 troops on {regSelected.name}\n ')
                    break
                else:
                    print('Thinking...\n')
        
                
                       
            
    def resetPlay(self):
        '''sets to 0 both select and target'''
        self.currentTar = 0
        self.currentSel = 0



def main():

    Title = '''
                                                                                                                                          
                                                                                                                                            
                                       ...                                                     `--`                `..                      
         `:::::::::::.                 ://                                   -:::::::::-.`     ://.                -//`                     
         .//:--------.                 ://                                   ://-------://-     ``                 -//`                     
         .//:            `.-:::--`     ://    `---.    `.-::::-.`            ://`       ://.   .--`    `--:::-.`   -//`   `---.             
         .//:```````    .::-...-//-    ://  `-//-`    .:/:-..-:/:-           ://`       ://.   -//`   -//-...-:`   -//` `-:/:.              
         .///:::::::-    ` `````://`   ://`-:/:`     .//.      -//.          ://.````..-//:    -//`   ://.``       -//..:/:.                
         .//:.......`   .-::::::://`   ://:///-`     ://:::::::://-          :///:::////-.     -//`   `-::/::-.`   -//:///:`                
         .//:          -//.`````://`   ://:..//:`    -//..........`          ://.```.://-      -//`      ``.-//:   -//:-.:/:.               
         .//:          ://.````.///`   ://`  `://.   `:/:.`````--`           ://`    `-//:`    -//`  `:-.````:/:   -//.  `://-              
         .::-          `-::::::--::`   :::     -::-    .::::::::-`           :::`      .:::.   -::`  `-:::::::-`   -::`    -::-`            
          ```             ````   ``    ```      ```       `````              ```        ````   ```      `````      ```      ````            
                                                                                                                                            
                                                                                                                                            
                                                                                                                                      
    '''
    
    print(Title)
    
    
    world_map = '''
////////////////////////////::----....-:////////////////////////////////////////////////////////////
/////////////////////::---/:-.    0  .//////////////////::-..````----:::::://///////////////////////
//:-.`   ```````....```.. `:/-  ``.-.-://///-`` ``....``                     `````.--///////////////
/-```.`           `-::.`..://-.-:///:://:/-` `-                             ```.` `-:///////////////
::::://-           .:.    -///////////:-`::``.`             2                .-:/-`-/////////////////
///////.      0         `-..///////////::.`  1                                  `-/:://///////////////
//////-             `.--:::///////////-.``.-..`                              `::.://////////////////
//////             -://///////////////-``---:-:--``                 3      .-.:-`://////////////////
//////-`     ``` -://////////////////:`     `.-..--    `                    -::-:///////////////////
///////..   ::::.://///////////////:.              .   `.````              `-///////////////////////
///////::. `---::-::///////////////-       2        `.    `://-.   .:.   `--::://////////////////////
/////////::--`-1//:::://///////////-                `.``-:////:` -///:`` .//:-://///////////////////
//////////////:-:.` ``.:://////////:-`   `            ``://////:./////---:/::///////////////////////
////////////////-       `-://////////:-::::.          `://////////////-`-/-``:://://////////////////
////////////////            `..://///////////-         -/////////////////-`:.`-`-/:...-://////////////
////////////////.            `://///////////-  3     `///////////////////::-:/://:::...://///////////
/////////////////-`    -2    ://////////////.       `::./////////////////////:-.``:.-///////////////
///////////////////-        `///////////////-      .:: -//////////////////:-.`       -//////////////
///////////////////:      .::////////////////`    `:/:-///////////////////.       4   ://///////////
///////////////////:     `://////////////////:  `.:///////////////////////.  `.`     .//////////////
////////////////////    .:////////////////////:://////////////////////////::////-``.:////:-:////////
////////////////////-  -//////////////////////////////////////////////////////////////:---://///////
/////////////////////` ://////////////////////////////////////////////////////////////::////////////
//////////////////////--:///////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////// '''
    # print a map for reference
    world_map_perfected = world_map.replace('/',' ')
    print(world_map_perfected)
    print('''FakeRisk rules\n\n'''
'''@Conquer the maximum of territories at the end of the 10 turns\n
@Recruit new troops and send them to occupied territories to fight\n
@Fortify your positions or you will get conquered instead!\n
@1)First select a country that you occupy with troops\n
@2)Then pick an adjacent country to attack\nou
@3)The attack will happen automatically! Your power is equal to the number
of troops + a random 1d6 dice roll\n
@If you win you conquer the country and a you gain 1 troop that will defend it!\n
@If you lose, 1 of your troops dies in combat..\n
@At the end of 10 rounds, the player who controls more countries is the winner
''')
    
    # Start the Game
    newGame = Risk()
    
    # Create the regions that conform the world
    NorthAfrica = Regions('NorthAfrica','NAF',2)
    CentralAmerica = Regions('CentralAmerica','CA', -1)
    NorthAmerica = Regions('NorthAmerica','NA',0)
    NorthPole = Regions('NorthPole','NP',0)
    SouthAmerica = Regions('SouthAmerica','SA',-2)
    WesternEurope = Regions('WesternEurope','WE',1)
    EasternEurope = Regions('EasternEurope','EE',2)
    Asia = Regions('Asia', 'A',3)
    SouthAfrica = Regions('SouthAfrica','SAF',3)
    Oceania = Regions('Oceania','O',4)
    
    # Create the game world
    newGame.createWorld([NorthAmerica,CentralAmerica,NorthAfrica,NorthPole,SouthAmerica,WesternEurope
                        ,EasternEurope,Asia,SouthAfrica,Oceania])
    
    # Start the two players
    
    while True:
        mode = input('you want to play Solo or Multiplayer?(write "solo" or "multi")')
        if mode == "multi":
            player1 = Player(input('Player 1, Choose your name'))
            player2 = Player(input('Player 2, Choose your name'))
            if player2.name == player1.name:
                player2.name = player2.name + '2'
            break
        elif mode == "solo":
            player1 = Player(input('Player 1, Choose your name'))
            player2 = IAPlayer('Napoleon')
            if player2.name == player1.name:
                player2.name = player2.name + '2'
            break
        else:
            print('Invalid choice \n')
            
    input('setting up world map..(press enter to continue) \n' )
    # Assign control and troops to each Player
    newGame.world['WE'].controlled_by = player1.name
    newGame.world['WE'].troopsRegion = 2
    newGame.world['CA'].controlled_by = player1.name
    newGame.world['CA'].troopsRegion = 2
    newGame.world['O'].controlled_by = player2.name
    newGame.world['O'].troopsRegion = 2
    newGame.world['EE'].controlled_by = player2.name
    newGame.world['EE'].troopsRegion = 3
    
    # Game CORE
    while True:
        print(f'CURRENT ROUND IS {newGame.round} \n')
        print('CURRENT STATUS OF THE WORLD: \n')
        Regions.checkWorld_2(newGame.world)
        input('press Enter to continue \n')
        print(newGame.listAlias)
        print('player 2 always recruits first!\n')
        input('press Enter to continue \n')
        player2.recruit(newGame.world)
        print('time for player 1 to recruit\n')
        input('press Enter to continue \n')
        player1.recruit(newGame.world)
        print('PLAYER 1 TURN: \n')
        input('press Enter to continue \n')
        while True:
            player1.select(newGame.world)
            if player1.target(newGame.world) != False:
                break   
        player1.attack(newGame.world)
        player1.resetPlay()
        print('\n\n\n')
        if input('Player 2: Press Enter to start your round') == 'Napoleon':
            newGame.round = 9
        else:
            pass
        print('CURRENT STATUS OF THE WORLD: \n')
        Regions.checkWorld_2(newGame.world)
        input('press Enter to continue \n')
        print('PLAYER 2 TURN: \n')
        input('press Enter to continue \n')
        while True:
            print(newGame.listAlias)
            player2.select(newGame.world)
            if player2.target(newGame.world) != False:
                break 
        player2.attack(newGame.world)
        player2.resetPlay()
        if newGame.round == 10:
            break
        if newGame.checkTotalDomination(player1,player2):
            break
        newGame.checkWorld()

        newGame.checkrounds()
        print('\n\n\n')
        input('Player 1: Press enter to start new round\n')
        
    Regions.checkWorld_2(newGame.world)
    newGame.checkWinner(player1,player2)

if __name__ == '__main__':
    main() 