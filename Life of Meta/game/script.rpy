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

    "Na een paar weken heb je het idee wat verder uitgewerkt."
    "Als mensen nu digitaal hun diploma opsturen via een wallet, dan we checken gelijk of de school door ons geregistreerd is betrouwbare school."
    "Het enige wat we dan moeten doen is een keuze maken tussen een register bijwerken of de lastige gevallen handmatig afhandelen"

    M "Zullen we een voorbeeld doen, Sylvie?"
    S "Ja, graag!"
    M "Weet je nog dat gekochte diploma? waarbij ik werd bedreigd?"
    S "Ja, natuurlijk... wat een ellende was dat..."
    M "Kijk, we vragen niet meer om een copy van het diploma, maar alle diplomas van een persoon staan in z'n wallet"
    S "Net zoiets als die consentual app?"
    M "Precies zo.Op het moment dat iemand een diploma krijgt, dan kun je dat diploma in je wallet laden en kun je hem versturen."
    M "wij krijgen dan die copy van het diploma bij ons binnen en zien gelijk of het diploma geldig is."
    M "we moeten hiervoor wel een registratie bijhouden van betrouwbare scholen."
    M "Maar iedere keer als er een diploma binnenkomt van een school die niet in de lijst staat moeten we daarover een beslissing nemen"
    S "dus als er een onbekende school binnenkomt, moeten we onderzoeken of het een echte school is?"
    M "Precies dat!"
    S "Oh als dat alles is, gaat dat ons een een hoop werk schelen"
    S "Goed gedaan MetaRobbin!"
    S "Het lijkt mij een goed idee als jij die afdeling gaat runnen! Lijkt je dat wat?"
    M "Oh echt? Dat is fantastisch!"

    "De volgende dag ga je gelijk aan de slag, langzamerhand moet het register gevuld worden, maar gelukkig heb je een lijst met betrouwbare scholen"
    "Deze diplomas gaan vanaf nu automatisch door"



#nieuwe casus bouwen op de nieuwe manier!


    jump eventpicker
    return

# nieuwe werk is TIR aanpassen of handmatig checken
# rusland casus (boycot rusland, oplossen in TIR, je mist een belangrijke rus die in nederland zou kunnen werken, oplossen hand, DUO komt in tijdnood)
# appenpokken in apeldoorn en we willen niemand uit apeldoorn accepteren (handmatig is enige oplossing)
# in holland casus, (heel inholland of 60 diplomas die ongeldig zijn of combi)
# latenz ien verschil tussen oude casussen...

label randomtoekomstcasus:

    $ rng = renpy.random.randint (1,5)

    if rng == 1:

        jump toekomstcasus1

    if rng == 2:

        jump toekomstcasus2

    if rng == 3:

        jump toekomstcasus3

    if rng == 4:

        jump toekomstcasus4

    if rng == 5:

        jump toekomstcasus5

    return

label toekomstcasus1:
# rusland casus
    "Je hoort in de ochtend op het nieuws dat alles uit Rusland geboycot moet worden. Je denkt nog, dat heeft met mij niet zoveel te maken"
    "Halverwege de ochtend krijg je een opdracht vanuit het ministerie. Wil je erover zorgen dat iedere rus tegen gehouden wordt, zodat ze niet per ongeluk worden aangenomen?"
    "Je hebt nu een paar keuzes..."
    "Wat wil je doen?"

    menu:
