# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("MetaRobbin"), color="#c8c8ff")
define v = Character(_("MetaMindy"), color="#a23af9")

#random score die overal gebruikt kan worden
default rng = 4
#werkscore voor hoe goed je werk doet
default score = 5
#score om te bepalen of je een booster hebt of niet
default booster = False
#score om te bepalen welk event je hebt afgerond zodat je doorgaat in het leven
default lasteventnr = 1
#score om de toekomst in te gaan
default toestemming = False
#score die bepaald of je maandmederker bent geweest
default maandmedewerker = False

label start:

    menu:
        "ga naar werk spel":

            jump werk

        "begin metas leven (nog mee bezig)":

            jump born

        "naar de toekomst van meta (nog mee bezig)":

            jump toekomstbaan

        "test events":

            jump covidevent
    return

label born:

    #geboorte van meta robin voorstellen van ma en pa meta...
    #aangifte van meta robin bij de gemeente
    #inschrijven meta bij een school
    #àanmelden voor stex met beperking
    #aanmelden stufi

    "dit zijn metapapa en metamama."

    "metamama staat op het punt om te bevallen en hiermee begint jouw leven."

    "je vernoemen je naar je overgrootvader en vanaf nu heet je MetaRobin"

    "natuurlijk moet je eerst aangemeld worden bij de gemeente om je registraties op orde te maken... "

    return

label toekomstbaan:
#andere baan...

    scene black
    with dissolve

    "Je hebt het verder uitgedacht en denkt dat het werk een stuk simpeler kan worden door een blockchain"
    "Zodra je op het werk bent plan je een overleg in met Sylvie"
    m "Hoi Sylvie, ik heb een idee. Wil je dat met mij bespreken?"
    s "Natuurlijk MetaRobbin, zeg het maar!"
    m "Je weet dat we iedere keer die diplomas checken, terwijl veel van dat check werk makkelijker kan."
    m "Als we die diplomas opvragen, via een wallet, die de personen hebben gekregen van de school."
    m "Dan hoeven we een heleboel diplomas niet meer te controleren, alleen de moeilijke gevallen waarbij iemand de boel probeert te flessen"
    s "Ik snapte niet helemaal hoe dat ging... maar denk je dat dit kan werken?"
    m "Ja, ik kreeg het idee van de consentual-app"
    m "Ehm... "
    "MetaRobbin kleurt gelijk rood..."
    s "Oh ja, die ken ik wel... Dat is toch waar je toestemming geeft?"
    m "Ja die! Nou precies zo eigenlijk, maar in plaats van toestemming, geef je je diploma tijdelijk aan ons."
    s "Oh dat is slim... Wil je dat verder uitwerken? Dan hoef je de komende tijd geen diploma's te checken. "
    #nieuwe casus bouwen op de nieuwe manier!

    "Na een paar weken heb je het idee wat verder uitgewerkt."
    "Als mensen nu digitaal hun diploma opsturen en we checken gelijk of de school door ons geregistreerd dan scheelt dat ons al veel werk"
    "Als er dan ook nog gecontroleerd kan worden of dat diploma echt door die school is uitgegeven dan zijn we bijna klaar"



    jump eventpicker
    return

