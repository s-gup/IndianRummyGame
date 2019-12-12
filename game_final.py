import pygame
import random
import copy

import time

''' objects '''
# python classes and functions

class card():
    def __init__(self,name_of_image,suit,rank,position=[0,0],value=0,prev_pos=[0,0]):
        self.name_of_image=name_of_image
        self.suit=suit
        self.rank=rank


        self.position=position
        self.value=value
        self.prev_pos=prev_pos



    def get_position(self):
    	return self.position  #tupple of (x,y)



class Computer():
    def __init__(self,score,computercards):
    	self.score=score
    	self.computercards=computercards

    #function to updatecsore


    #picks the show card if
    def pickcard():
    	return

    def show_hidecomputercards(self):
        x=display_width*0.1
        for i in range(len(self.computercards)):

            #draws the image to the screen coordinates (x,y)
            gameDisplay.blit(card1,(x,display_height*0.03))
            x=x+35

    def show_computercards(self):
        x3=display_width*0.1
        y3=display_height*0.03
        for i in computer_grouplist1:
            for j in i:
                j.position[0]=x3
                j.position[1]=y3



                x3=x3+35
            x3=x3+55
        for i in computer_notgrouplist1:
            i.position[0]=x3
            i.position[1]=y3

            x3=x3+35


        l=[]
        for i in range(len(self.computercards)):
            l.append([self.computercards[i].position[0],self.computercards[i].position[1]])
        l.sort() #sort card in increasing order of x coordinate
        for j in l:
            for i in range(len(self.computercards)):
                if j==[self.computercards[i].position[0],self.computercards[i].position[1]]:


                    #draws the image to the screen coordinates (x,y)
                    gameDisplay.blit(self.computercards[i].name_of_image,(self.computercards[i].position[0],self.computercards[i].position[1]))







    #to form groups of sets and runs of computer cards
    def group_computercards(self):

        global computer_pickcardpositionX
        global computer_pickcardpositionY
        global computer_grouplist1
        global computer_notgrouplist1 # cards which does not form any group







        '''' Forming groups of sets and runs of computercards'''
        Clubscardlist=[]
        Heartscardlist=[]
        Spadescardlist=[]
        Diamondscardlist=[]
        computer_runlist=[]
        computer_setlist=[]
        computer_grouplist=[]
        computer_notgrouplist=[] # cards which does not form any group

        computer_grouplist1=computer_grouplist

        for i in self.computercards:
            computer_notgrouplist.append(i)


        for i in self.computercards:

            if i.suit=="Clubs":
                Clubscardlist.append(i)

            if i.suit=="Spades":
                Spadescardlist.append(i)
            if i.suit=="Hearts":
                Heartscardlist.append(i)
            if i.suit=="Diamonds":
                Diamondscardlist.append(i)


        ''' making runs of computer cards'''
        for i in Clubscardlist:
            m=0
            for k in computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Clubscardlist:
                    m=0
                    if j.value==i.value-1:
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)
                    if j.value==i.value+1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    computer_grouplist.append(l)


        for i in Spadescardlist:
            m=0
            for k in computer_grouplist:

                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Spadescardlist:
                    m=0
                    if j.value==i.value-1:
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                    if j.value==i.value+1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    computer_grouplist.append(l)


        for i in Heartscardlist:
            m=0
            for k in computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Heartscardlist:
                    if j.value==i.value-1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                    if j.value==i.value+1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    computer_grouplist.append(l)




        for i in Diamondscardlist:
            m=0
            for k in computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Diamondscardlist:
                    if j.value==i.value-1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                    if j.value==i.value+1:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break

                        if m==0:
                            l.append(j)

                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    computer_grouplist.append(l)










        ''' making sets of computer cards'''
        for i in Clubscardlist:
            m=0
            for k in computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:

                l=[]
                for j in Spadescardlist:
                    if i.rank==j.rank:
                        m=0

                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break
                        if m==0:

                            l.append(j)
                for j in Heartscardlist:
                    if i.rank==j.rank:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break
                        if m==0:

                            l.append(j)


                for j in Diamondscardlist:
                    if len(l)<2:


                        if i.rank==j.rank:
                            m=0
                            for k in computer_grouplist:
                                if j in k:
                                    m=1
                                    break
                            if m==0:

                                l.append(j)

                if len(l)>=2:
                    l.append(i)
                    computer_setlist.append(l)
                    computer_grouplist.append(l)

        # because it can be that we have a set without club
        for i in Spadescardlist:
            m=0
            for k in computer_grouplist:
                if i in k:
                    m=1
                    break

            if m==0:
                l=[]
                for j in Clubscardlist:
                    if i.rank==j.rank:
                        m=0

                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break
                        if m==0:

                            l.append(j)


                for j in Heartscardlist:
                    if i.rank==j.rank:
                        m=0
                        for k in computer_grouplist:
                            if j in k:
                                m=1
                                break
                        if m==0:

                            l.append(j)


                for j in Diamondscardlist:
                    if len(l)<2:

                        if i.rank==j.rank:
                            m=0
                            for k in computer_grouplist:
                                if j in k:
                                    m=1
                                    break
                            if m==0:

                                l.append(j)

                if len(l)>=2:
                    l.append(i)
                    computer_setlist.append(l)
                    computer_grouplist.append(l)
        for i in computer_grouplist:
            for j in i:
                computer_notgrouplist.remove(j)








        ''' computer pick card'''

        global showcard
        Clubscardlist=[]
        Heartscardlist=[]
        Spadescardlist=[]
        Diamondscardlist=[]

        ungroup_computer_grouplist=[]


        if showcard.suit=="Clubs":
            Clubscardlist.append(showcard)

        elif showcard.suit=="Hearts":
            Heartscardlist.append(showcard)

        elif showcard.suit=="Spades":
            Spadescardlist.append(showcard)

        elif showcard.suit=="Diamonds":
            Diamondscardlist.append(showcard)



        for i in computer_notgrouplist:

            if i.suit=="Clubs":
                Clubscardlist.append(i)

            if i.suit=="Spades":
                Spadescardlist.append(i)
            if i.suit=="Hearts":
                Heartscardlist.append(i)
            if i.suit=="Diamonds":
                Diamondscardlist.append(i)

        ''' making runs of computer cards from ungrouped cards and showcard'''
        for i in Clubscardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Clubscardlist:
                    if j.value==i.value-1:
                        l.append(j)
                    if j.value==i.value+1:
                        l.append(j)
                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    ungroup_computer_grouplist.append(l)


        for i in Spadescardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Spadescardlist:
                    if j.value==i.value-1:
                        l.append(j)
                    if j.value==i.value+1:
                        l.append(j)
                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    ungroup_computer_grouplist.append(l)


        for i in Heartscardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Heartscardlist:
                    if j.value==i.value-1:
                        l.append(j)
                    if j.value==i.value+1:
                        l.append(j)
                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    ungroup_computer_grouplist.append(l)




        for i in Diamondscardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:
                l=[]
                for j in Diamondscardlist:
                    if j.value==i.value-1:
                        l.append(j)
                    if j.value==i.value+1:
                        l.append(j)
                if len(l)==2:
                    l.append(i)
                    computer_runlist.append(l)
                    ungroup_computer_grouplist.append(l)











        ''' making sets of ungrouped computer cards and show card'''
        for i in Clubscardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break
            if m==0:

                l=[]
                for j in Spadescardlist:
                    if i.rank==j.rank:

                        l.append(j)
                for j in Heartscardlist:
                    if i.rank==j.rank:

                        l.append(j)
                for j in Diamondscardlist:


                    if i.rank==j.rank:
                        l.append(j)
                if len(l)>=2:
                    l.append(i)
                    computer_setlist.append(l)
                    ungroup_computer_grouplist.append(l)

        # because it can be that we have a set without club
        for i in Spadescardlist:
            m=0
            for k in ungroup_computer_grouplist:
                if i in k:
                    m=1
                    break

            if m==0:
                l=[]
                for j in Clubscardlist:
                    if i.rank==j.rank:

                        l.append(j)
                for j in Heartscardlist:
                    if i.rank==j.rank:

                        l.append(j)
                for j in Diamondscardlist:

                    if i.rank==j.rank:
                        l.append(j)
                if len(l)>=2:
                    l.append(i)
                    computer_setlist.append(l)
                    ungroup_computer_grouplist.append(l)

        if len(ungroup_computer_grouplist)>=1:
            #pick show card
            self.computercards.append(showcard)
            for i in ungroup_computer_grouplist:
                computer_grouplist.append(i)

        else:
            #pick card from hide bundle
            hidebundle=updated_hidebundle()


            l=len(hidebundle)
            a=random.randrange(l)
            hidebundle[a].position=[computer_pickcardpositionX,computer_pickcardpositionY]

            self.computercards.append(hidebundle[a])










            for i in ungroup_computer_grouplist:
                computer_grouplist.append(i)










        if len(computer_runlist)==0:
            self.score=0
        else:
            self.score=len(computer_grouplist)

        pygame.display.update()
        clock.tick(60)







        ''' Computer throws card'''
        computer_ungroupcards_list=[]  #stores cards which are not grouped
        computer_notgrouplist1=computer_ungroupcards_list

        for i in self.computercards:
            computer_ungroupcards_list.append(i)
        for i in computer_grouplist:
            for j in i:
                computer_ungroupcards_list.remove(j)

        l=len(computer_ungroupcards_list)

        a=random.randrange(l)
        computer_pickcardpositionX=computer_ungroupcards_list[a].position[0]
        computer_pickcardpositionY=computer_ungroupcards_list[a].position[1]

        showcard=computer_ungroupcards_list[a]

        #computer throws card

        self.computercards.remove(computer_ungroupcards_list[a])
        computer_ungroupcards_list.remove(computer_ungroupcards_list[a])




    def get_computerscore(self):
        return self.score





































class Player():
    def __init__(self,score,playercards):
    	self.score=score
    	self.playercards=playercards



    def showcards(self):
        l=[]
        for i in range(len(self.playercards)):
            l.append([self.playercards[i].position[0],self.playercards[i].position[1]])
        l.sort() #sort card in increasing order of x coordinate
        for j in l:
            for i in range(len(self.playercards)):
                if j==[self.playercards[i].position[0],self.playercards[i].position[1]]:


                    #draws the image to the screen coordinates (x,y)
                    gameDisplay.blit(self.playercards[i].name_of_image,(self.playercards[i].position[0],self.playercards[i].position[1]))


    def get_playerscore(self):
        return self.score












def group_button(text,font):

    # create a text suface object,
    # on which text is drawn on it.

    textSurface=font.render(text,True,white,blue)

    # .get_rect() create a rectangular object for the
    # text surface object
    return textSurface,textSurface.get_rect()

textrectpos=[]   #to get position of group button
#group_button_centre=((display_width/2)+250,(display_height/2)+50)
def text_button(text,font):

    # create a text suface object,
    # on which text is drawn on it.

    textSurface=font.render(text,True,blue)

    # .get_rect() create a rectangular object for the
    # text surface object
    return textSurface,textSurface.get_rect()

def text_button_message(text):

    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    largeText = pygame.font.Font('freesansbold.ttf',30)

    TextSurf, TextRect = text_button(text, largeText)
    textrectpos.append(TextRect[0])
    textrectpos.append(TextRect[1])
    TextRect.center = (text_button_centre[0],text_button_centre[1])
    gameDisplay.blit(TextSurf, TextRect)

def player_score_message(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)

    TextSurf, TextRect = text_button(text, largeText)
    textrectpos.append(TextRect[0])
    textrectpos.append(TextRect[1])
    TextRect.center = (player_score_message_centre[0],player_score_message_centre[1])
    gameDisplay.blit(TextSurf, TextRect)

def computer_score_message(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)

    TextSurf, TextRect = text_button(text, largeText)
    textrectpos.append(TextRect[0])
    textrectpos.append(TextRect[1])
    TextRect.center = (computer_score_message_centre[0],computer_score_message_centre[1])
    gameDisplay.blit(TextSurf, TextRect)







def group_button_message(text):

    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    largeText = pygame.font.Font('freesansbold.ttf',30)

    TextSurf, TextRect = group_button(text, largeText)
    textrectpos.append(TextRect[0])
    textrectpos.append(TextRect[1])
    TextRect.center = (text_button_centre[0],text_button_centre[1])
    gameDisplay.blit(TextSurf, TextRect)


def throwcard_button_message(text):

    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    largeText = pygame.font.Font('freesansbold.ttf',30)

    TextSurf, TextRect = group_button(text, largeText)
    textrectpos.append(TextRect[0])
    textrectpos.append(TextRect[1])
    TextRect.center = (throwcard_button_centre[0],throwcard_button_centre[1])
    gameDisplay.blit(TextSurf, TextRect)

def print_showcard(showcard):
    gameDisplay.blit(showcard.name_of_image,(display_width*0.5,display_height*0.27))


#displaying hide bundle
def print_hidebundle():
    hidecardpositionX=display_width*0.3
    hidecardpositionY=display_height*0.27
    gameDisplay.blit(card1,(hidecardpositionX,hidecardpositionY))

# function to update hide bundle
def updated_hidebundle():
    global listcards
    global showcard


    hidecards=[]
    for i in listcards:
        if (i not in player1.playercards) and (i not in computer1.computercards) and i!=showcard:
            hidecards.append(i)
    return hidecards




# function for computer to pick hide card
def computerpickhidecard():
    a=random.randrange(len(updated_hidebundle))
    computer1.computercards.append(updated_hidebundle[a])




















































''' setup '''
#put once run code here


#initialize the pygame
pygame.init()


display_width=800
display_height=600

black=(0,0,0)
blue=(0,0,128)
white=(255,255,255)

#create the screen or main display of our game
gameDisplay=pygame.display.set_mode((display_width,display_height))

#title of game window
pygame.display.set_caption('Desi Rummy')




#this is game clock, to track time within game ,used for frames per second(FPS)
clock=pygame.time.Clock()


x=display_width*0.1   # first player card x position
y=display_height*0.5  #playercards y position

x1=x  #for selected cards
y1=display_height*0.75 #for selected cards
group_button_centre=((display_width/2)+265,(display_height/2)+50)

throwcard_button_centre=((display_width/2)+300,(display_height/2)+50)

finish_button_centre=(display_width*0.87,40)

final_win_message_centre=(display_width*0.5,display_height*0.4)

player_score_message_centre=(display_width*0.2,display_height*0.45)
computer_score_message_centre=(display_width*0.2,display_height*0.3)


generalmessage_positionX=display_width*0.8
generalmessage_positionY=display_height*0.4

generalmessagecentre=(generalmessage_positionX,generalmessage_positionY)






#making list of objects of all the 52 cards
listcards=[]
ranks=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suits=['Clubs','Spades','Hearts','Diamonds']
for i in ranks:
    for j in suits:
        obj=card(i[0]+j[0],j,i)
        obj.prev_pos=[0,0]
        obj.pos=[0,0]
        if obj.rank=='Ace':
            obj.value=1
        elif obj.rank=='Jack':
            obj.value=11
        elif obj.rank=='Queen':
            obj.value=12
        elif obj.rank=='King':
            obj.value=13
        else:
            obj.value=int(obj.rank)
        listcards.append(obj)


#distributing 13 cards randomly to each player
playercards1=[]
computercards1=[]

#player cards
k=0
while k<13:

    a=random.randrange(0,52)
    if listcards[a] not in playercards1 :
        listcards[a].position=[x,y]  #initializing the position of player cards

        listcards[a].prev_pos=[0,0]
        playercards1.append(listcards[a])
        x=x+35
        k=k+1
pickcardpositionX=x  #for player
pickcardpositionY=y

#computer cards
x2=display_width*0.1
y2=display_height*0.03
k=0
while k<13:
    x=random.randrange(0,52)
    if listcards[x] not in playercards1 and listcards[x] not in computercards1:
        listcards[x].position=[x2,y2]


        computercards1.append(listcards[x])
        x2=x2+35

        k=k+1

computer_pickcardpositionX=x2
computer_pickcardpositionY=y2

#creating initial show card
k=0
while k==0:
    x=random.randrange(0,52)
    if listcards[x] not in computercards1 and listcards[x] not in playercards1:
        showcard=listcards[x]
        k=k+1

#creatting initial hide bundle

hidecards=[]
for i in listcards:
    if (i not in playercards1) and (i not in computercards1) and i!=showcard:
        hidecards.append(i)






#creating player object (player1)
player1=Player(0,playercards1)   #have to change initial score

#creating computer object(computer1)
computer1=Computer(0,computercards1)






computer_grouplist1=[] # have list of groups of computer cards
computer_notgrouplist1=[] #computer cards which are not grouped







#loading images of the 52 cards
for i in range(52):
	listcards[i].name_of_image=pygame.image.load(listcards[i].name_of_image+".png")

#loading image of hide bundle
card1=pygame.image.load("card2.png")



no_selectedcards=0
selectcards=[]  #temporary to store selected cards for each grouping

present_groupedcards=[]#store lists of all the groups of cards
group_card_select=0
grouped_selectcards=[]
emptyposition_groupcards=[]

player_run_list=[]
player_set_list=[]




# positions of hide bundle and show card
hidecardpositionX=display_width*0.3
hidecardpositionY=display_height*0.27
showcardX=display_width*0.5
showcardY=display_height*0.27










#Game Loop
running=True





''' main loop '''

while running:
    for event in pygame.event.get():



        #just for checking


        #for event happening in the game foreg. arrow click,etc ,if an event happen of
        #pressing the cross button on top right of game button(called QUIT in pygame),
        #running is made false, so that the loop will run until cross button is pressed
        if event.type==pygame.QUIT:

            running=False


        gameDisplay.fill((0,255,0)) #paint the game with color, cover any existing stuff
        computer1.show_hidecomputercards()
        print_showcard(showcard)
        print_hidebundle()
        player1.showcards()

















        pygame.display.update()
















        '''player pick card'''
        # waits until player picks a card
        k=0


        while k==0:
            text_button_centre=generalmessagecentre

            gameDisplay.fill((0,255,0))
            computer1.show_hidecomputercards()
            print_showcard(showcard)
            print_hidebundle()
            player1.showcards()
            text_button_message("Pick a card")

            player_score=player1.get_playerscore()
            player_score_message1="Score : "+str(player_score)
            player_score_message(player_score_message1)



            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

                    k=1


                if event.type==pygame.MOUSEBUTTONDOWN:
                    for i in player1.playercards:



                        if i.position[0]<pygame.mouse.get_pos()[0]<i.position[0]+35 and i.position[1]<pygame.mouse.get_pos()[1]<i.position[1]+135:

                            if i.position[1]==y-30: # on second press of mouse on a card
                                i.position[1]=y
                                no_selectedcards=no_selectedcards-1
                                selectcards.remove(i)


                            elif i.position[1]==y:

                                i.position[1]=i.position[1]-30 # on first press of mouse on a card
                                no_selectedcards=no_selectedcards+1
                                selectcards.append(i)

                            # when mouse click on grouped player cards to select cards


                            if i.position[1]==y1-30:
                                i.position[1]=y1
                                group_card_select=group_card_select-1
                                grouped_selectcards.remove(i)





                            elif i.position[1]==y1: # on first press of mouse on a grouped card
                                i.position[1]=y1-30
                                grouped_selectcards.append(i)
                                group_card_select=group_card_select+1 #if any group card is selected










                    #if hide card is picked up
                    if hidecardpositionX<pygame.mouse.get_pos()[0]<hidecardpositionX+85 and hidecardpositionY<pygame.mouse.get_pos()[1]<hidecardpositionY+135:
                        hidebundle=updated_hidebundle()
                        l=len(hidebundle)
                        a=random.randrange(l)
                        hidebundle[a].position=[pickcardpositionX,pickcardpositionY]




                        player1.playercards.append(hidebundle[a])


                        k=1
                    # if show card is picked up
                    elif showcardX<pygame.mouse.get_pos()[0]<showcardX+85 and showcardY<pygame.mouse.get_pos()[1]<showcardY+135:
                        showcard.position=[pickcardpositionX,pickcardpositionY]

                        player1.playercards.append(showcard)





                        k=2





                if group_card_select>=1:
                    text_button_centre=group_button_centre
                    group_button_message('UnGroup')
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if group_button_centre[0]-65<pygame.mouse.get_pos()[0]<group_button_centre[0]+65 and group_button_centre[1]-15<pygame.mouse.get_pos()[1]<group_button_centre[1]+15:
                            new_present_groupedcards=[]
                            for j in present_groupedcards:
                                l=0
                                for i in grouped_selectcards:



                                    if i in j:


                                        l=1
                                if l==0:
                                    if j not in new_present_groupedcards:
                                        new_present_groupedcards.append(j)
                                else:

                                    #to check if it was a run or a set and remove accordingly
                                    #from player_run_list or player_set_list

                                    #to check if it form a set or run

                                    if j in player_run_list:
                                        player_run_list.remove(j)
                                    if j in player_set_list:
                                        player_set_list.remove(j)







                                    for m in j:


                                        m.position[0]=m.prev_pos[0]
                                        m.position[1]=m.prev_pos[1]






                            present_groupedcards=new_present_groupedcards
                            group_card_select=0
                            grouped_selectcards=[]










                if no_selectedcards>=3:

                    #to check if it form a set or run
                    set=1
                    t=1
                    run=0
                    p=0

                    for i in range(len(selectcards)-1):
                        if selectcards[i].rank!=selectcards[i+1].rank:
                            set=0
                        if selectcards[i].suit!=selectcards[i+1].suit:
                            t=0
                    if t==1 and len(selectcards)==3:
                        for i in selectcards:
                            p=0
                            for j in selectcards:
                                if j.value==i.value-1:
                                    p=p+1
                                if j.value==i.value+1:
                                    p=p+1

                            if p==2:
                                run=1


                    if run==1 or set==1:









                        text_button_centre=group_button_centre

                        group_button_message('Group')
                        if event.type==pygame.MOUSEBUTTONDOWN:


                            if group_button_centre[0]-45<pygame.mouse.get_pos()[0]<group_button_centre[0]+45 and group_button_centre[1]-15<pygame.mouse.get_pos()[1]<group_button_centre[1]+15:


                                present_groupedcards.append(selectcards)
                                if set==1:
                                    player_set_list.append(selectcards)
                                if run==1:
                                    player_run_list.append(selectcards)



                                for i in selectcards:
                                    #stores the previous position of cards before they are
                                    #grouped to send them to the same place if they are ungrouped


                                    i.prev_pos[0]=i.position[0]


                                    i.prev_pos[1]=y

                                    i.position[1]=y1









                                no_selectedcards=0
                                selectcards=[]

                x4=0.1*display_width
                y1=0.75*display_height


                for i in present_groupedcards:
                    for j in i:
                        j.position[0]=x4


                        x4=x4+35
                    x4=x4+55

                if len(player_run_list)==0:
                    player1.score=0
                else:

                    player1.score=len(present_groupedcards)


                text_button_centre=finish_button_centre
                group_button_message('End game')
                if event.type==pygame.MOUSEBUTTONDOWN:


                    if finish_button_centre[0]-73<pygame.mouse.get_pos()[0]<finish_button_centre[0]+73 and finish_button_centre[1]-15<pygame.mouse.get_pos()[1]<finish_button_centre[1]+15:
                        f=0
                        while f==0:
                            player_score=player1.get_playerscore()
                            computer_score=computer1.get_computerscore()

                            gameDisplay.fill((0,255,0)) #paint the game with color, cover any existing stuff

                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()

                                    f=1


                            player1.showcards()
                            computer1.show_computercards()

                            text_button_centre=final_win_message_centre

                            player_score_message1=" Player Score : "+str(player_score)
                            computer_score_message1=" Computer Score : "+str(computer_score)

                            player_score_message(player_score_message1)
                            computer_score_message(computer_score_message1)




                            if player_score>computer_score:

                                text_button_message("Player Wins")

                            elif player_score<computer_score:

                                text_button_message("Computer Wins")
                            else:

                                text_button_message("Draw match")

                            pygame.display.update()
                            clock.tick(60)




                pygame.display.update()
                clock.tick(60)









        '''PLAYER THROWS CARD'''
        l=0

        while l==0:
            text_button_centre=generalmessagecentre

            gameDisplay.fill((0,255,0))
            computer1.show_hidecomputercards()
            if k==1:
                print_showcard(showcard)
            print_hidebundle()
            player1.showcards()
            text_button_message("Throw a card")

            player_score=player1.get_playerscore()
            player_score_message1="Score : "+str(player_score)
            player_score_message(player_score_message1)



            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()

                    l=1


                if event.type==pygame.MOUSEBUTTONDOWN:
                    for i in player1.playercards:



                        if i.position[0]<pygame.mouse.get_pos()[0]<i.position[0]+35 and i.position[1]<pygame.mouse.get_pos()[1]<i.position[1]+135:

                            if i.position[1]==y-30: # on second press of mouse on a card
                                i.position[1]=y
                                no_selectedcards=no_selectedcards-1
                                selectcards.remove(i)

                            elif i.position[1]==y:

                                i.position[1]=i.position[1]-30 # on first press of mouse on a card
                                no_selectedcards=no_selectedcards+1
                                selectcards.append(i)


                            if i.position[1]==y1-30: # on second press of mouse on a grouped card
                                i.position[1]=y1
                                group_card_select=group_card_select-1
                                grouped_selectcards.remove(i)





                            elif i.position[1]==y1: # on first press of mouse on a grouped card
                                i.position[1]=y1-30
                                grouped_selectcards.append(i)
                                group_card_select=group_card_select+1 #if any group card is selected








                if group_card_select>=1:
                    text_button_centre=group_button_centre
                    group_button_message('UnGroup')
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        if group_button_centre[0]-65<pygame.mouse.get_pos()[0]<group_button_centre[0]+65 and group_button_centre[1]-15<pygame.mouse.get_pos()[1]<group_button_centre[1]+15:
                            new_present_groupedcards=[]
                            for j in present_groupedcards:
                                z=0




                                for i in grouped_selectcards:


                                    if i in j:


                                        z=1
                                if z==0:
                                    if j not in new_present_groupedcards:
                                        new_present_groupedcards.append(j)
                                else:


                                    #to check if it was a run or a set and remove accordingly
                                    #from player_run_list or player_set_list

                                    #to check if it form a set or run


                                    if j in player_run_list:

                                        player_run_list.remove(j)
                                    if j in player_set_list:
                                        player_set_list.remove(j)





                                    for m in j:


                                        m.position[0]=m.prev_pos[0]
                                        m.position[1]=m.prev_pos[1]





                            present_groupedcards=new_present_groupedcards
                            group_card_select=0
                            grouped_selectcards=[]












                if no_selectedcards==3:


                    #to check if it form a set or run
                    set=1
                    t=1
                    run=0
                    p=0

                    for i in range(len(selectcards)-1):
                        if selectcards[i].rank!=selectcards[i+1].rank:
                            set=0
                        if selectcards[i].suit!=selectcards[i+1].suit:
                            t=0
                    if t==1 and len(selectcards)==3:

                        for i in selectcards:
                            p=0
                            for j in selectcards:
                                if j.value==i.value-1:
                                    p=p+1
                                if j.value==i.value+1:
                                    p=p+1
                            if p==2:
                                run=1







                    if run==1 or set==1:


                        text_button_centre=group_button_centre
                        group_button_message('Group')
                        if event.type==pygame.MOUSEBUTTONDOWN:


                            if group_button_centre[0]-45<pygame.mouse.get_pos()[0]<group_button_centre[0]+45 and group_button_centre[1]-15<pygame.mouse.get_pos()[1]<group_button_centre[1]+15:
                                present_groupedcards.append(selectcards)
                                if set==1:
                                    player_set_list.append(selectcards)
                                if run==1:
                                    player_run_list.append(selectcards)


                                for i in selectcards:
                                    i.prev_pos[0]=i.position[0]



                                    i.prev_pos[1]=y


                                    i.position[1]=y1





                                no_selectedcards=0
                                selectcards=[]






                elif no_selectedcards==1:
                    throwcard_button_message('Throw Card')
                    if event.type==pygame.MOUSEBUTTONDOWN:


                        if throwcard_button_centre[0]-90<pygame.mouse.get_pos()[0]<throwcard_button_centre[0]+90 and throwcard_button_centre[1]-15<pygame.mouse.get_pos()[1]<throwcard_button_centre[1]+15:

                            for i in selectcards:
                                pickcardpositionX=i.position[0] #the next card which will be picked up will come to this position as there is no card here
                                pickcardpositionY=i.position[1]+30 #+35 because earlier the card was up
                                showcard=i
                                player1.playercards.remove(i)
                                l=1

                            no_selectedcards=0
                            selectcards=[]



                x4=0.1*display_width
                y1=0.75*display_height


                for i in present_groupedcards:
                    for j in i:
                        j.position[0]=x4


                        x4=x4+35
                    x4=x4+55

                if len(player_run_list)==0:
                    player1.score=0
                else:

                    player1.score=len(present_groupedcards)




                text_button_centre=finish_button_centre
                group_button_message('End game')
                if event.type==pygame.MOUSEBUTTONDOWN:


                    if finish_button_centre[0]-73<pygame.mouse.get_pos()[0]<finish_button_centre[0]+73 and finish_button_centre[1]-15<pygame.mouse.get_pos()[1]<finish_button_centre[1]+15:
                        f=0
                        while f==0:
                            player_score=player1.get_playerscore()
                            computer_score=computer1.get_computerscore()

                            gameDisplay.fill((0,255,0)) #paint the game with color, cover any existing stuff

                            for event in pygame.event.get():
                                if event.type==pygame.QUIT:
                                    pygame.quit()
                                    quit()

                                    f=1


                            player1.showcards()
                            computer1.show_computercards()

                            text_button_centre=final_win_message_centre

                            player_score_message1=" Player Score : "+str(player_score)
                            computer_score_message1=" Computer Score : "+str(computer_score)

                            player_score_message(player_score_message1)
                            computer_score_message(computer_score_message1)




                            if player_score>computer_score:

                                text_button_message("Player Wins")

                            elif player_score<computer_score:

                                text_button_message("Computer Wins")
                            else:

                                text_button_message("Draw match")

                            pygame.display.update()
                            clock.tick(60)








                pygame.display.update()
                clock.tick(60)





        '''Computer picks up and throws card'''
        gameDisplay.fill((0,255,0)) #paint the game with color, cover any existing stuff
        computer1.show_hidecomputercards()
        print_showcard(showcard)
        print_hidebundle()
        player1.showcards()
        computer1.group_computercards()

        pygame.display.update()
        clock.tick(60)

        player_score=player1.get_playerscore()
        computer_score=computer1.get_computerscore()

        if computer_score==4:
            f=0
            while f==0:
                player_score=player1.get_playerscore()
                computer_score=computer1.get_computerscore()

                gameDisplay.fill((0,255,0)) #paint the game with color, cover any existing stuff

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()

                        f=1


                player1.showcards()
                computer1.show_computercards()

                text_button_centre=final_win_message_centre

                player_score_message1=" Player Score : "+str(player_score)
                computer_score_message1=" Computer Score : "+str(computer_score)

                player_score_message(player_score_message1)
                computer_score_message(computer_score_message1)




                if player_score>computer_score:

                    text_button_message("Player Wins")

                elif player_score<computer_score:

                    text_button_message("Computer Wins")
                else:

                    text_button_message("Draw match")

                pygame.display.update()
                clock.tick(60)








































        pygame.display.update() #will update the specific areas of screen
        #whereas display.flip() updates the whole surface

        clock.tick(60) #tells how many frames per second we are running





pygame.quit() #to end pygame instance
quit()
