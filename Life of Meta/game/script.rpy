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
default toekomstevent = 1
#score om de toekomst in te gaan
default toestemming = False
#score die bepaald of je maandmederker bent geweest
default maandmedewerker = False
#score van de drukte op de afdeling waar je op werkt...
default drukte = 1
#score om te kijken waar in toekomstcasus de speler is
default toekomstcas = 1


default rus = False
default hol = False
default apel = False


label start:

    menu:
        "ga naar werk spel":

            jump werk

        "begin metas leven (nog mee bezig)":

            jump born

        "naar de toekomst van meta":

            $ toestemming = True
            jump toekomstbaan

        "test events":

            jump randomtoekomstcasus
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

    "De volgende dag ga je gelijk aan de slag, langzamerhand moet het register gevuld worden, maar gelukkig heb je een lijst met betrouwbare scholen"
    "Deze diplomas gaan vanaf nu automatisch door"



#nieuwe casus bouwen op de nieuwe manier!

    $ lasteventnr +=1
    jump toekomsteventpicker
    return

# nieuwe werk is TIR aanpassen of handmatig checken
# x rusland casus (boycot rusland, oplossen in TIR, je mist een belangrijke rus die in nederland zou kunnen werken, oplossen hand, DUO komt in tijdnood)
# x appenpokken in apeldoorn en we willen niemand uit apeldoorn accepteren (handmatig is enige oplossing)
# x in holland casus, (heel inholland of 60 diplomas die ongeldig zijn of combi)
# latenz ien verschil tussen oude casussen...

label randomtoekomstcasus:

    # $ rng = renpy.random.randint (1,3)


    if toekomstcas == 1:

        jump toekomstcasus1

    if toekomstcas == 2:

        jump toekomstcasus2

    if toekomstcas == 3:

        jump toekomstcasus3

    if drukte > 4:

        jump toekomstcasus4

    else:
        jump toekomsteventpicker

    return

label toekomstcasus1:
# rusland casus

    $ toekomstcas += 1
    "Je hoort in de ochtend op het nieuws dat alles uit Rusland geboycot moet worden. Je denkt nog, dat heeft met mij niet zoveel te maken"
    "Halverwege de ochtend krijg je een opdracht vanuit het ministerie. Wil je erover zorgen dat iedere rus tegen gehouden wordt, zodat ze niet per ongeluk worden aangenomen?"
    "Je hebt nu een paar keuzes..."
    "Wat wil je doen?"

    menu:
        "Alle scholen uit Rusland uitsluiten in het register":
            "vanaf nu worden alle scholen uit Rusland uitgesloten en de diplomas afgekeurd."
            "Dit is een goede keuze. Het bespaard je enorm veel handmatig werk..."
            "Maar 2 jaar later hoor je dat in Belgie er een briljante Estse is aangenomen die ook bij ons had gesolliciteerd"
            "Wij hebben haar afgewezen omdat ze van een russische school kwam"

            "maar laten we verder gaan!"

            jump toekomsteventpicker

        "Handmatig alle Russen uitsluiten":
            "Vanaf nu komen alle Russen langs bij de handmatige beoordeling"
            "Dit zorgt er in ieder geval voor dat je niet alle mensen van een Russische school zomaar uitsluit"
            "Maar door de hoeveelheid extra werk krijgt je afdeling het ineens enorm druk"

            $ drukte +=3
            $ rus = True
            "laten we verder gaan"

            jump toekomsteventpicker

    return

label toekomstcasus2:
#inhollandcasus

    #newsflash hoge school is niet betrouwbaar meer... zeker 100 diplomas ongeldig
        $ toekomstcas += 1
        "je krijgt een bericht dat een school niet meer betrouwbaar is, wat wil je doen?"

        menu:
            "sluit de school gelijk uit via het register":
                "je sluit alle diplomas van deze school uit. het gaat om circa een half miljoen diplomas terwijl er maar 100 ongeldig zijn"
                "misschien is dit niet de beste keuze... , maar je kunt het herstellen"

                menu:
                    "je sluit tijdelijk alle leerlingen van deze school uit.":
                        "Hierdoor mis je een aantal sollicitanten... maar je krijgt ook geen ongeldige diplomas binnen"
                        "alle sollicitanten van de school kun je later opnieuw oproepen voor een sollicitatie"

                        jump toekomsteventpicker

                    "je besluit om alle leerlingen van deze school handmatig tegen te houden":
                        "Je team controleert alle gevallen met de hand, maar je weet nog niet welke diploma's onterecht zijn uitgegeven"
                        "dit levert veel extra handwerk op, misschien had je beter alle leerlingen van deze school tijdelijk uitgesloten"

                        $ drukte +=2
                        $ hol = True

                        jump toekomsteventpicker

            "wacht op het onderzoek dat persoonlijke diploma's uitsluit en sluit die handmatig uit":
                "Tijdens het onderzoek sijpelen er langzaam een aantal diplomas door die onterecht zijn uitgegeven."
                "Helaas kun je dit achteraf niet meer herstellen..."

                jump toekomsteventpicker

        return

label toekomstcasus3:
#appenpokken in apeldoorn

    #newsflash over een appenpokken uitbraak in apeldoorn...lasteventnr
    $ toekomstcas += 1
    "Je krijgt opdracht van de directie om niemand meer uit te nodigen uit apeldoorn"
    "Wat wil je doen?"
    menu:

        "Haal alle scholen uit apeldoorn uit het register":

            "dit lijkt me niet goed MetaRobbin"
            "het gaat om 500.000 diplomas waarvan er maar een paar ongeldig zijn..."
            "maar je bespaard je afdeling een hoop handmatig werk"
            jump toekomsteventpicker


        "Controleer handmatig per persoon of ze uit Apeldoorn komen":
            $ drukte +=1
            $ apel = True
            "dit levert wat handmatig werk op, maar gelukkig krijg je wel de kans om alle sollicitaties te controleren"
            jump toekomsteventpicker

    return

label toekomstcasus4:
#te druk op de afdeling



    menu:

        "De druk op je afdeling wordt veel te hoog... Je moet echt dingen automatisch doen"
        "beoordeel de russiche scholen automatisch" if rus:
            "Je laat je afdeling nu 20.000 extra gevallen per maand minder doen"
            "dat zal de druk op de afdeling zeker verlagen!"
            $ drukte -=3
            $ rus = False
            jump toekomsteventpicker

        "doe apeldoorn automatisch" if apel:
            "je laat ongeveer 5 sollicitaties per maand geautomatiseerd doen"
            "dit levert helaas niets op qua drukte van de afdeling"
            $ apel = False
            jump toekomsteventpicker

        "stop met de handmatige afhandeling van de afgekeurde school" if hol:
            "De afdeling gaat vanaf nu alle diplomas van de afgekeurde shool geautomatiseerd afkeuren"
            "dit bespaard je een hoop werk... maar je mist enorm veel solliciaties"
            $ drukte -=2
            $ hol = False
            jump toekomsteventpicker

        "meer informatie over de verschillen":
            "aantal sollicitaties met een russiche nationaliteit zijn 20.000 per maand, en van Russische scholen 25.000"
            "vanuit Apeldoorn zijn er 5 sollicitaties per maand en 600 die van een school in Apeldoorn een diploma hebben gekregen"
            "De afgekeurde school heeft 500.000 diplomas uitgegeven en naar, verwachting, zijn er ca. 100 die ongeldig moeten worden"
            jump toekomstcasus4

    return

#oud casus niet meer random
# bewaren van resultaten vna oude casus icm de nieuwe zien
# flowchart
# diploma via email
# diploma legaliseren vragen naar casussen
# scheiding maken tussen casus en live events
