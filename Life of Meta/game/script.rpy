# Declare characters used by this game.
#sylvie
define s = Character(_("Sylvie"), image="sylvie", color="#c8ffc8")
image side sylvie = "sylvie blue normal.png"
#TODO plaatje vertaler
define ve = Character(_("Vertaler"), color="#c8ffc8")

#metarobbin
define m = Character(_("MetaRobbin"), color="#c8c8ff")
define kid = Character(_("[kidname]"), color="#c8c8ff")

#metamindy en metamama
define v = Character(_("MetaMindy"), image="mindy", color="#a23af9")
define ma = Character(_("MetaMama"), image="mindy", color="DA0CD1")
image side mindy =  im.Scale("mindy.png", 400, 700)
image side mindy happy = im.Scale("mindy blush.png", 400, 700)
image side mindy annoyed = im.Scale("mindy annoyed.png", 400, 700)
image side mindy angry = im.Scale("mindy angry.png", 400, 700)
image side mindy blush = im.Scale("mindy blush.png", 400, 700)
image side mindy blush1 = im.Scale("mindy blush1.png", 400, 700)
image side mindy cry = im.Scale("mindy cry.png", 400, 700)
image side mindy sad = im.Scale("mindy sad.png", 400, 700)
image side mindy tired = im.Scale("mindy tired.png", 400, 700)
image side mindy upset = im.Scale("mindy upset.png", 400, 700)


#metapapa
define pa = Character(_("MetaPapa"), image="metapapa", color="FF5733")
image side metapapa = im.Scale("s1-normal.png", 400, 700)
image side metapapa angry = im.Scale("s1-angry.png", 400, 700)
image side metapapa derp = im.Scale("s1-derp.png", 400, 700)
image side metapapa disgust = im.Scale("s1-disgust.png", 400, 700)
image side metapapa happy = im.Scale("s1-grin.png", 400, 700)
image side metapapa grin = im.Scale("s1-grin2.png", 400, 700)
image side metapapa question = im.Scale("s1-maybe-not.png", 400, 700)
image side metapapa n2 = im.Scale("s1-normal2.png", 400, 700)
image side metapapa surprise = im.Scale("s1-surprise.png", 400, 700)
image side metapapa blush = im.Scale("s1-surprise-blush.png", 400, 700)
image side metapapa angry1 = im.Scale("s1-tsundere.png", 400, 700)



#receptionist en Sylvie
define receptionist = Character(_("receptionist"), image="sylvie1", color="#c8ffc8")
image side sylvie1 = im.Scale("sylvie green normal.png", 400, 700)
define a = Character(_("Ambtenaar"), image="sylvie", color="#c8ffc8")
image side sylvie = "sylvie blue normal.png"

#narrator
define n = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="images/n_bg.png", what_color="#ddd")
# define text = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="images/n_bg.png", what_color="#ddd")

#images
image hospital = im.Scale("ziekenhuis.jpg", 1920,1080)
image stadhuis = im.Scale("Stadhuis.jpg", 1920,1080)
image ditlablogo = im.Scale("46.png", 1920,500)
image ma = im.Scale("mindy.png", 400, 700)
image pa = im.Scale("s1-normal.png", 400, 700)
image balie = im.Scale("balie.png", 1920,1080)

#random score die overal gebruikt kan worden
default rng = 1
default rng1 = 1
#werkscore voor hoe goed je werk doet
default score = 15
#score om te bepalen of je een booster hebt of niet
default booster = False
#score om te bepalen welk event je hebt afgerond zodat je doorgaat in het leven
default lasteventnr = 1
default toekomstevent = 1
#score om de toekomst in te gaan
default toestemming = False
#score die bepaald of je maandmederker bent geweest
default maandmedewerker = False
#score van de drukte op de afdeling waar je op werkt...
default drukte = 1
#score om te kijken waar in toekomstcasus de speler is
default toekomstcas = 1
#werk variabele voor enkel werk casussen of niet
default werk = False
#variabelen voor de toekomstcasussen
default rus = False
default hol = False
default apel = False
#variabelen voor teammeeting:
default teltimer = 1000
default zoektimer = 1000
#variabelen voor werkoud
default teveelinfo = False
default laat = False
default tijd = 1
default tijdperdag = 5

default dag = 0
#variabelen voor de score
default open = 0
default afgerond = 0
default kosten = 0
default resuse = 0
default budget = 15
default vert = 0
default informatie = 0
default foutediplomas = False
default aantekening = 0
default evil = 0

default casus1 = Casus()
default casus2 = Casus()
default casus3 = Casus()
default casus4 = Casus()
default casus5 = Casus()
default casus6 = Casus()

label start:

    jump born
return


label Alleenwerk:
#TODO weer opnieuw inbouwen na nieuwe werkwijze
        # "alleen de werkcasussen":
            $ werk = True

            jump werk


label test:
    jump toekomstevent5

return



label toekomstbaan:
#andere baan...

    scene black
    with dissolve

    n "Je hebt het verder uitgedacht en denkt dat het werk een stuk simpeler kan worden door een blockchain"
    n "Zodra je op het werk bent plan je een overleg in met Sylvie"
    m "Hoi Sylvie, ik heb een idee. Wil je dat met mij bespreken?"
    s "Natuurlijk MetaRobbin, zeg het maar!"
    m "Je weet dat we iedere keer die diplomas checken, terwijl veel van dat check werk makkelijker kan."
    m "Als we die diplomas opvragen, via een wallet, die de personen hebben gekregen van de school."
    m "Dan hoeven we een heleboel diplomas niet meer te controleren, alleen de moeilijke gevallen waarbij iemand de boel probeert te flessen"
    s "Ik snapte niet helemaal hoe dat ging... maar denk je dat dit kan werken?"
    m "Ja, ik kreeg het idee van de consentual-app"
    m "Ehm... "
    #TODO andere metarobbin plaatje
    n "MetaRobbin kleurt gelijk rood..."
    s "Oh ja, die ken ik wel... Dat is toch waar je toestemming geeft?"
    m "Ja die! Nou precies zo eigenlijk, maar in plaats van toestemming, geef je je diploma tijdelijk aan ons."
    s "Oh dat is slim... Wil je dat verder uitwerken? Dan hoef je de komende tijd geen diploma's te checken. "

    n "Na een paar weken heb je het idee wat verder uitgewerkt."
    n "Als mensen nu digitaal hun diploma opsturen via een wallet, dan we checken gelijk of de school door ons geregistreerd is betrouwbare school."
    n "Het enige wat we dan moeten doen is een keuze maken tussen een register bijwerken of de lastige gevallen handmatig afhandelen"

    m "Zullen we een voorbeeld doen, Sylvie?"
    s "Ja, graag!"
    m "Weet je nog dat gekochte diploma? waarbij ik werd bedreigd?"
    s "Ja, natuurlijk... wat een ellende was dat..."
    m "Kijk, we vragen niet meer om een copy van het diploma, maar alle diplomas van een persoon staan in z'n wallet"
    s "Net zoiets als die consentual app?"
    m "Precies zo.Op het moment dat iemand een diploma krijgt, dan kun je dat diploma in je wallet laden en kun je hem versturen."
    m "wij krijgen dan die copy van het diploma bij ons binnen en zien gelijk of het diploma geldig is."
    m "we moeten hiervoor wel een registratie bijhouden van betrouwbare scholen."
    m "Maar iedere keer als er een diploma binnenkomt van een school die niet in de lijst staat moeten we daarover een beslissing nemen"
    s "dus als er een onbekende school binnenkomt, moeten we onderzoeken of het een echte school is?"
    m "Precies dat!"
    s "Oh als dat alles is, gaat dat ons een een hoop werk schelen"
    s "Goed gedaan MetaRobbin!"
    s "Het lijkt mij een goed idee als jij die afdeling gaat aansturen! Lijkt je dat wat?"
    m "Oh echt? Dat is fantastisch!"

    n "De volgende dag ga je gelijk aan de slag, langzamerhand moet het register gevuld worden, maar gelukkig heb je een lijst met betrouwbare scholen"
    n "Deze diplomas gaan vanaf nu automatisch door"

    $ lasteventnr +=1
    jump randomtoekomstcasus
    return

# nieuwe werk is TIR aanpassen of handmatig checken
# x rusland casus (boycot rusland, oplossen in TIR, je mist een belangrijke rus die in nederland zou kunnen werken, oplossen hand, DUO komt in tijdnood)
# x appenpokken in apeldoorn en we willen niemand uit apeldoorn accepteren (handmatig is enige oplossing)
# x in holland casus, (heel inholland of 60 diplomas die ongeldig zijn of combi)
# latenz ien verschil tussen oude casussen...





# bewaren van resultaten vna oude casus icm de nieuwe zien
# flowchart
# diploma via email
# diploma legaliseren vragen naar casussen

label credits:
    "sounds from soundjay.com and pixabay.com"