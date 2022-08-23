label oudwerknewstyle:
#     show desk
#     default werkdag = 0
#     default area = "club"
#     default dossier1 = True
#     default school1info = False
#     default school1gebeld = True
#     default aanvrager1info = True
#     default aanvrager1bel = False
#     default vertaling1 = 1
#     n "tijd om op te staan. Koffie en ontbijt en je favoriete krant terwijl op de achtergrond het nieuws aanstaat"
#     jump club

# label club:
#     "clubblubblublbul"
#     show screen movement
#     $ renpy.pause (hard=True)
#     # n "welkom op je [werkdag]e werk"
#
# label lecture:
#     "lecturehall"
#     show screen movement
#     $ renpy.pause (hard=True)
#
# label meadow:
#     "this is meadow"
#     show screen movement
#     $ renpy.pause (hard=True)
#
# label archief:
#                  if school1info:
#                    "Deze school is opgericht in 1954 en heeft geen einddatum, dus is nog steeds geldig"
          #                          "this is archief"
    #if dossier1:
                  #textbutton "dossier 1"
#                  if school1gebeld:
#                     "De school zegt dat het diploma is uitgegeven door de school"
#                  if school1gebeld:
#                      "De gegevens van de aanvrager komt overeen met het diploma"
                  #showif aanvrager1bel message  "De aanvrager reageert gewoon aan de telefoon en heeft al je vragen beantwoord"
#
#                  "De vertaling is opgevraagd" if vertaling1 == 1
#
#                  "De vertaling ziet er goed uit" if vertaling1 == 2
#                  show screen movement
    #$ renpy.pause (hard=True)
#    screen item_selection:






##screen movement:
    #style_prefix "choice"           #What does this do?
    #modal True                        # This means the player can interact only with this screen, right?
    #vbox:
        #if area == "club":
            #add "bg club.png"   #TODO ander
            #imagebutton auto "metamama.png" xpos 609 ypos 592 focus_mask True action [SetVariable("area", "lecture"),Jump("lecture")]
        #elif area == "lecture":
            #add "bg lecturehall.png"
            #imagebutton auto "metapapa.png" xpos 609 ypos 592 focus_mask True action [SetVariable("area", "club"),Jump("club")]
            #imagebutton auto "metamama.png" xpos 20 ypos 20 focus_mask True action [SetVariable("area", "meadow"),Jump("meadow")]
        #elif area == "meadow":
            #add "bg meadow.png"
            #imagebutton auto "metapapa.png" xpos 609 ypos 592 focus_mask True action [SetVariable("area", "club"),Jump("club")]
        #else:
            #pass

#screen movement:
#    style_prefix "choice"
#    modal True
#    vbox:
#        if area == "club":
#            add "bg club.jpg" ##This will show your background for the room you are in.
#            textbutton "lecture": ##You can change this to be your image button code! This is just for testing purposes.
#                action [SetVariable("area", "lecture"),Jump("lecture")] ##I'll explain the Jump later on.
            #imagebutton auto "plaatje.png" xpos 609 ypos 592 focus_mask True action [SetVariable("area", "lecture"),Jump("lecture")]
#            textbutton "meadow":
#                action [SetVariable("area", "meadow"),Jump("meadow")]
#            textbutton "archief":
#                action [SetVariable("area", "archief"),Jump("archief")]
#        elif area == "lecture":
#            add "bg lecturehall.jpg"
#            textbutton "meadow":
#                action [SetVariable("area", "meadow"),Jump("meadow")]
#        elif area == "meadow":
#            add "bg meadow.jpg"
#            textbutton "club":
#                action [SetVariable("area", "club"), Jump("club")]
#            textbutton "lecture":
#                action [SetVariable("area", "lecture"),Jump("lecture")] ##blah blah blah etc.
#        elif area == "archief":
#            add "archief.png"
#            if dossier1:
#                textbutton ""
#        else:
#            pass

init python:
    class Place(object):
        def __init__(self, x, y, name, IsActive):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive

    Places = []

    while t < 50:
        Places.append(place(0,0,"", False)
        t += 1

    Places[0] = Place(1000,600, "archief", True)
    Places[1] = Place(200,600, "koffieapparaat", True)
    Places[2] = Place(600,200, "inkomende mail", True)
    Places[3] = Place(200,200, "telefoon", True)

screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1000
        background "desk.png"
        for q in Places:
            if q.IsActive:
                button:
                    xpos q.x
                    ypos q.y
                    text q.name
                    action Return(q.name)

