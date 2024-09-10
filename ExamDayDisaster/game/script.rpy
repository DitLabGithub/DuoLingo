# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define E = Character(_("Emma"), image="emma")
image side emma =  im.Scale("emmasmile.png", 400, 700)
image side emma happy = im.Scale("mindysmile.png", 400, 700)
image side emma scared = im.Scale("emmascared.png", 400, 700)
image side emma angry = im.Scale("emmanagry.png", 400, 700)


define N = Character (None)

define A = Character(_("Anna"), image="anna")
image side anna = im.Scale("annacolor1.png", 400, 700)

define T = Character(_("Teacher"), image="teacher")
image side teacher = im.Scale("colorteacher.png", 400, 700)

define C = Character(_("Coffeegirl"), image="coffeegirl")
image side coffeegirl = im.Scale("coffeegirl.png", 400, 700)

define B = Character(_("Bus driver"), image="busdriver")
image side coffeegirl = im.Scale("colordriver.png", 400, 700)


define S = Character(_("Shady"), image="shady")
image side shady = im.Scale("shadyguycolor.png", 400, 700)

define W = Character(_("Worker"), image="worker")
image side worker = im.Scale("slominoworker.png", 400, 700)

define card_reader = Character("Card Reader")

define un = Character(_("???"), image="anna")

#narrator
# define n = Character(None, what_style="centered_text", window_style="centered_window")
# define text = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="images/n_bg.png", what_color="#ddd")

image bedroom = im.Scale("colorrroom2.png", 1920,1080)
# image ditlablogo = im.Scale("46.png", 1920,500)
image outside = im.Scale("BusColorBG.png", 1920,1080)
image bus = im.Scale("buscolorinside.png", 1920,1080)
image outside2 = im.Scale("BusStopShady.png", 1920,1080)
image gotoschool = im.Scale("LeagueJump.png", 1920,1080)
image slomino = im.Scale("colorslomino.png", 1920,1080)
image classroom = im.Scale("classcolor.jpg", 1920,1080)
image coffeecorner = im.Scale("CoffeeColor.png", 1920,1080)
image outside = im.Scale("BusColorBG.png", 1920,1080)
image news1 = im.Scale("bla.png", 1920,1080)
image news2 = im.Scale("day2.png", 1920,1080)
image clock = im.Scale("angryclock.png", 1920,1080)
image hallway = im.Scale("hallway.png", 1920,1080)
image papervote = im.Scale("PosterPaper.jpg", 1920,1080)


default notvoted = True
default vote_points = 0
default voteforCoffee = True
default bus_scammed = False
default scammedphone = False
default quiz = False


# The game starts here.

label start:
    scene bedroom
    show clock
    N "Alarm *BEEP BEEP* WAKE UP, YOU'RE LATE AGAIN"
    E "Oh my god, I got it. Shush!"
    hide clock
    E "Last day before the exam, I better not be late."
    menu bedroomday1:
        "Play Fallout4":
            ## to sign in with ssi
            show gotoschool
            E "You know what, maybe school doesn't sound too bad"
            hide gotoschool
            jump bedroomday1

        "Read Newspaper":
            show news1
            E "What's the paper saying today then?"
            hide news1
            jump bedroomday1

        "Go outside":
            jump Busstop ##(bus with booze shop, slominos etc)
return

label Busstop:
    scene outside
    E "Ah, just in time"
    scene bus
    menu insbus:
        "Read Sign":
            E "I guess they finally replaced the OV Chipcard system"
            E "Makes sense since SSI took over, guess it's less of a hassle now"
            E "I kinda like it to be honest, it feels my data belongs to me now"
            ## back to inside bus
            jump insbus

        "Scan bus card":
            card_reader "*BEEP BEEP*"
            un "Oh my god, hiii girly"
            E "Anna! Also running late?"
            A "Well yea we are on the same bus aren't we"
            menu:
                "Uhhh…"
                "i guess ur right":
                    A "haha"
                    E "Ah, it's our stop"
                    jump school_hall
                "fuck off":
                    A "Ask stupid questions get stupid answers"
                    E "Haha"
                    E "Ah, it's our stop"
                    jump school_hall
return


label school_hall:
    scene hallway
    E "What room are we in again?"
    A "332 I believe"
    menu hall:
        "Room 331":
            A "Wrong room girlypops"
            E "Oh, my god I'm totally buggin'"
            jump hall
        "Read exams message":
            E "I thought the exams were tomorrow??"
            A "Hanze moment"
            jump hall
        "Clock":
            E "Not us literally being on time"
            A "We ate"
            jump hall
        "Room 332":
            N "You scan your phone with the SSI scanner"
            jump classroom
return


label classroom:
    scene classroom
    menu:
        "exam tomorrow":
            T "Ah hello girls, just in time"
            T "As you know, there's an exam tomorrow. \n It's at 11, don't be late."
            T "To prepare, i'll ask a few sample questions"
            jump Quiz1

        "vote":
            if quiz:
                E "have you voted yet?"
                A "nope"
                jump classroom
            else:
                E "I'm so tired of the people outside of school harrassing me to vote for them"
                jump classroom

        "tree":
            N "plant"
            jump classroom

        "to cafetaria" if quiz:
            jump cafetaria
return

label Quiz1:
    T "Your Self Sovereign Identity is a digital version of your wallet."
    T "After sharing your data with a verifier, what happens?"
    $ quiz = True
    menu:
        T "Using SSI, after sharing data, the data gets…"
        "stored by them":
            T "incorrect, the data gets retracted."
            T "Companies are no longer free to collect and store your data as they please."
            jump Quiz2
        "retracted":
            T "Correct, data gets retracted"
            T "Companies are no longer free to collect and store your data as they please."
            jump Quiz2
return

label Quiz2:
    T "Last question, how has SSI made the internet safer?"
    menu:
        "It's harder to impersonate people":
            T "That's right,SSI makes impersonation harder and thus reduced the cyber-crime rate."
            T "It also lets you choose what data to you want to share, which you couldn't really do pre-SSI"
            jump endquiz

        "You are in control of your own data":
            T "That's right, SSI lets you choose what data you want to share, \n which you couldn't really do pre-SSI."
            T "SSI also makes impersonation harder and thus reduced the cyber-crime rate."
return


label endquiz:
    T "I was also asked to inform you that the student elections are coming to an end this week. I advise you to vote."
    T "That's it, you're free to go."
    E "Omg, why did she only pick me to answer her questions \n I swear she hates me"
    A "You got scammed I can't even lie, \n let's get a latte to cheer u up"
    jump cafetaria
return

label cafetaria:
    scene coffeecorner
    if notvoted:
        A "Oeh we should probably vote, we might get free stuff"
        jump cafmenu
    else:
        jump cafmenu

label cafmenu:
    menu:
        "get coffee":
            jump coffee
        "vote" if notvoted:
            jump vote
        "leave":
            jump busback
return


label vote:
    N "Read the sign"
    N "Vote me for free coffee \n And another one Vote to improve the Hanze Experience"
    menu:
        "how do you want to vote?"
        "use SSI":
            $ vote_ssi = "Y"
            "SSI allows you to choose what information you want to share"
            menu studentnumber:
                "Hanze Student Elections requests: student number *required "
                "share":
                    $ vote_points +=1
                    N "SSI allows you to choose what information you want to share"
                    jump age
                "don't share":
                    N "Information that is *required must be shared in order to vote"
                    jump studentnumber

            menu age:
                "Hanze Student Elections requests: age."
                "share":
                    jump gender
                "don't share":
                    $ vote_points +=1
                    jump gender

            menu gender:
                "Hanze Student Elections requests: gender."
                "share":
                    jump vote_person
                "don't share":
                    $ vote_points +=1
                    jump vote_person
        "use paper":
            show papervote
            menu:
                E "My BSN??? MY IBAN??? For the student Elections??"
                "Fill out":
                    menu:
                        "x for Coffee woman":
                            $ voteforCoffee = True
                            E "My god, the paper voting just absolutely scammed em into sharing some bizarre data"
                            hide papervote
                            A "Really? I voted with my SSI, I only had to share my student ID and the rest was optional"
                            $ notvoted = False
                            jump cafetaria
                        "x for Girly POP":
                            $ voteforCoffee = False
                            E "My god, the paper voting just absolutely scammed em into sharing some bizarre data"
                            hide papervote
                            A "Really? I voted with my SSI, I only had to share my student ID and the rest was optional"
                            $ notvoted = False
                            jump cafetaria
                "quit":
                    hide papervote
                    jump cafmenu
return


menu vote_person:
    "Confirm vote for:"
    "Coffee woman":
        $ voteforCoffee = True
        $ notvoted = False
        A "My god, the paper voting just absolutely scammed me into sharing all of my data..."
        E "Really? I voted with my SSI, I only had to share my student ID and the rest was optional"
        jump cafetaria
    "Girly POP":
        $ voteforCoffee = False
        $ notvoted = False
        A "My god, the paper voting just absolutely scammed me into sharing all of my data..."
        E "Really? I voted with my SSI, I only had to share my student ID and the rest was optional"
        jump cafetaria
return

label coffee:
    if voteforCoffee:
        C "What will it be?"
        A "Two lattes pls"
        C "Good choice \n Question, have you voted for the students elections?"
        A "Yes girl we gave u our votes"
        C "No way! Coffee is on me (;"
        A "..."
        A "Crazy how that works"
        jump busback
    else:
        C "What will it be?"
        A "Two lattes pls"
        C "Good choice \n Question, have you voted for the students elections?"
        A "Yup, not on u tho"
        C "That's Crazy"
        C "That will be 5,40 then"
        N "Anna swipes her phone past the scanner *beep beep*"
        jump busback
return

label busback:
scene bus
N "you swipe your phone bast the scanner *beep beep*"
A "have u ever thought about what would happen if someone just stole your phone lol"
E "Oh my god, I would die"
A "I mean I guess its fine cus they can't actually do anything with your data \n since they don't know your SSI log in, but still"
E "Not having ur phone on u means u r not carrying your ID with you either though"
E "not even mentioning the other services SSI replaced"
A "True I guess but you also had that problem in the past if you lost your wallet"
E "Ah it's my stop, see u tomorrow"
A "See ya"
scene bedroom
E "time to sleep I guess"
N "**next day**"
menu bedroomday2:

    "Play Fallout4":
        show gotoschool
        E "You know what, maybe school doesn't sound too bad"
        hide gotoschool
        jump bedroomday2
    "Read Newspaper":
         show news2
         E "What's the paper saying today then?"
         hide news2
         jump bedroomday2
    "Go outside":
        jump BUSSTOPday2
return


label BUSSTOPday2:
    scene outside2
    E "ah in time for the bus-"
    N "you trip"
    E "You're joking... "
    N "you hurry in the bus"
    scene bus
    E "Aight let's hope I can check in"
    E "..."
    E "Shit"
    menu:
        E "Uhm miss bus driver"
        "free trip?":
            B "Hell no, get out of my bus."
            $ bus_scammed = True
            jump outside
        "help pls":
            B "... Sorry I don't think i'm able to help you here"
            $ bus_scammed = False
            jump outside
return

label outside:
    scene outside2
    menu ssi_broken:
        "bike":
            E "oeh an unlocked bike? Don't mind if i do..."
            menu:
                "steal it":
                    jump endgame
                "leave it":
                    jump ssi_broken
        "shady person":
            S "Phone broken? i can help u lol"
            E "Really?"
            S "Yep.. u can use mine untill u get it fixed"
            E "Omg ur the goat, how much will it cost me?"
            S "Nothing dw about it lol"
            menu:
                E "it costs nothing?"
                "shady af":
                    S "Ok. Do you want it or not?"
                    menu:
                       E "this person is defo gonna steal all of my data"
                       "hell naw":
                             jump ssi_broken
                       "yurrr":
                             jump shadyscam

                "ur so kind":
                    jump shadyscam



        "Slomino's":
                scene slomino
                E "Free?? I have an idea"
                E "I guess there's no human interaction in the store anymore?"
                menu:
                    E "What to do..."
                    "scream":
                        W "Um wtf can i help you?"
                        E "Can i please get a pizza delivered to school?"
                        W "Sure"
                        E "Can i join you on the delivery? Crisis... \n Phone broke, can't enter bus, exam..."
                        W "Say less... \n Girls support girls... \n Hop on!"
                        jump endgame


                    "leave":
                        jump ssi_broken

        "bus stop":
            if bus_scammed:
                E "dont think waiting on a new bus is a good strat since that bus driver just absolutely scammed me"
                jump ssi_broken
            else:
                E "dont think waiting on a new bus is a good strat since that bus driver just absolutely scammed me"
                ##TODO other tekst maybe... busdriver didnt scam
                jump ssi_broken
return

label shadyscam:
                    S "Lol enjoy"
                    E "Aight I'll just log into my SSI account from this phone then and wait for the bus..."
                    scene bus
                    card_reader "*BEEP BEEP*"
                    E "Slay"
                    A "No shot we meet again what a coincidence"
                    E "Omg Anna I was so stressed cus I broke my phone and couldn't get on the first bus because of it"
                    A "Huh?? How did u manage to get into this one then?"
                    E "Some random dude let me borrow his phone for FREE lol"
                    A "For free?? GG that man defo knows ur SSI login now u are FUCKED"
                    E "U might be right bout that actually"
                    A "Noob"
                    E "Well at least I won't miss the exam i guess ha ha ha"
                    A "Right..."
                    $ scammedphone = True
                    jump endgame
return

label endgame:
    scene classroom
    if scammedphone:
         E "Alright, let me just scan my SSI"
         N "You made it to the exam, but you probably \n got your data stolen... \n Please be more careful!! \n Are you interested in SSI? \n Do you want to know more? \n Talk with the DIT-Lab"
         return

    else:
        menu:
            "cry":
                A "What's wrong girly? i just got here... \n Please don't tell me no one showered... \n I will cry too if the exam hall smells of a gamer"
                E "My phone broke... It was such a struggle to get here, \n can I please check in on your phone"
                A "Of course, I got u girlypops"
                E "U are a SAVIOR! TY!"
                N "You made it to the exam, good job! \n Hopefully you have an idea now of \n what SSI is (or could become) \n Are you interested in SSI? \n Do you want to know more? \n Talk with the DIT-Lab"
                return

            "bonk door":
                T "What's happening here?"
                E "My phone broke"
                E "I apologize for the scene but do you maybe have a device I can use to log into my SSI with?"
                T "Ah yes, come in. You can log in on my computer!"
                N "You made it to the exam, good job! \n Hopefully you have an idea now of \n what SSI is (or could become) \n Are you interested in SSI? \n Do you want to know more? \n Talk with the DIT-Lab"

return


##clicking on the screen misschien https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=27959
##verise uit vorige game
##init python:
##    config.developer = True
##    config.console = True
##    class Place(object):
##        def __init__(self, x, y, name, IsActive):
##            self.x = x
##            self.y = y
##            self.name = name
##            self.IsActive = IsActive
##        @property
##        def avatar(self):
##            icon = self.name.lower() + "_icon.png"
##            return(icon)

##    Places = []
##    t = 0

##    while t < 50:
##        Places.append(Place(0,0,"", False))
##        t += 1

##    Places[0] = Place(680,500, "archief", True)
##    Places[1] = Place(350,200, "koffieapparaat", True)
##    Places[2] = Place(900,225, "mail", True)
 ##   Places[3] = Place(1650,550, "telefoon", True)
##    Places[4] = Place(1900,800, "toilet", True)
##    Places[5] = Place(3000,1200, "kantoor", False)
##    Places[6] = Place(1650,75, "baas", True)
##    Places[7] = Place(25,375, "informatiepunt", True)
##    Places[8] = Place(1700,700, "toilet1", False)


#ToDo hints sparkle
#ToDo mouseover
#ToDo Inventory system (clickable icon in corner and open wallet)
#ToDo Inv_sys (introduction)
#ToDo Inv_sys (combining items)
#ToDo Inv_sys (dragging item to place on screen)
#ToDo background with clickable items on screen (all scenes)
#ToDo dialogue
