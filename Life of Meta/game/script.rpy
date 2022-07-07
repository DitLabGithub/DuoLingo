﻿# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("MetaRobin"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False
default rng = 4
default score = 5

label start:

    # Start by playing some music.
    # play music "illurock.opus"

    scene duogroot
    with fade
    "Welkom bij Life of Meta!"

    show metarobbinmedium at left
    with dissolve

    "Je eerste werkdag bij DUO start vandaag"

    "In de verte zie je het DUO gebouw naderen"

    scene duoingang
    with fade

    "Na een rondleiding en lunch is het tijd om je manager te ontmoeten"

    scene duomanagergroot
    with fade

    "Je wordt begroet door je manager, Sylvie"

    jump intro


label intro:

    "Je bent aangenomen bij Duo op de personeelszaken en je wordt rondgeleid door Sylvie"

    s "Hoi en welkom bij duo!"

    s "Vandaag is je eerste dag hier en ik leid je rond."

    s "De bedoeling is dat je diploma's controleert. je hebt 2 keuzes, of het diploma is vals, of hij is geldig."

    s "Dat doe je door te kijken waar het diploma vandaan komt, of de school een echte school is en of de uitgifte datum van het diploma binnen de geldigheid van de school ligt."

    s "Als een diploma goed is, nodigen we die persoon uit voor een gesprek."

    scene desk
    with fade

    s "Laten we beginnen met deze."

    s "Dit diploma heeft een datum dat in de geldigheid van de school ligt en de school zelf is ook geldig"

    show dip1
    with fade

    menu:

        s "Wat denk je van dit diploma?"

        "ziet er goed uit.":

#             show sylvie green smile

            m "Deze lijkt me geldig... misschien moeten we deze persoon uitnodigen"

            s "Correct!"

            s "Laten we kijken of je het alleen kunt!"

            s "Je krijgt nu het gewone werk te zien. probeer het goed te doen, want iedere fout heeft een consquentie"

            jump randomcasus

        "ik denk niet dat deze geldig is.":

            s "Sorry metarobin... dat is niet goed... ik denk niet dat dit gaat werken..."

            s "Daar is de deur"

            scene gameover
            with fade

    return


label randomcasus:

    $ rng = renpy.random.randint (1,5)

    if rng == 1:

        jump casus1

    if rng == 2:

        jump casus2

    if rng == 3:

        jump casus3

    if rng == 4:

        jump casus4

    if rng == 5:

        jump casus5

label casus1:

    # inholland casus

    "Hm.."

    show dip2
    with fade

    "Dit diploma ziet er goed uit, maar is uitgegeven door een afgekeurde school, wat wil je doen?"

    menu:

        "Wil je deze persoon uitnodigen?"

        "Ja":

            jump badending

        "Nee":

            jump goedbezig

label casus2:

    # gewoon diploma

    scene black
    with dissolve

    "Volgend diploma"

    show dip4
    with fade

    "Dit diploma ziet er goed uit "

    menu:

        "Wat denk je ervan?"

        "Uitnodigen":

            jump goedbezig

        "Weg ermee!":

            jump badending

    return

label casus3:

    # chinees diploma

    scene black
    with dissolve

    "Dat is raar.."

    show dip5
    with fade

    "Je ziet het diploma en begrijpt er niets van."

    menu:

        "Wat denk je ervan?"

        "vraag om een vertaling van het diploma":

            # vertaling van het chinese diploma

            "Je ziet het diploma en het is vertaald, maar totaal niet te gebruiken."

            menu:

                "Wat denk je ervan?"

                "Uitnodigen!":

                    jump badending

                "Weg ermee!":

                    jump goedbezig

        "Weg ermee!":

            jump badending

    return

label casus4:

    # gekocht diploma

    scene black
    with dissolve

    "Dat is opvallend..."

    show dip6
    with fade

    "Dit diploma ziet er goed uit, maar er is iets raars mee "

    menu:

        "Wat denk je ervan?"

        "Check het diploma met de school":

            "Het diploma is nooit uitgegeven door deze school en je besluit de persoon op te bellen"

            "De persoon begint te stotteren en na een tijdje wordt de toon dreigend"

            menu:

                "De persoon dreigt met geweld als je hem niet accepteert, wat doe je?"

                "Hang snel op en roep Sylvie!":

                    jump goedbezig

                "Accepteer het diploma":

                    jump badending

        "Weg ermee!":

            jump badending

        "Uitnodigen":

            jump badending

    return

label casus5:

    # diploma van een onbekende school

    scene black
    with dissolve

    "Wat is dit.."

    show dip7
    with fade

    "Dit diploma ziet er goed uit, maar je kent de school niet."

    menu:

        "Wat denk je ervan?"

        "Zoek uit welke school het diploma heeft uitgegeven":

            "Je zoekt op internet naar de school en kan niets vinden"

            menu:

                "Wat wil je doen?"

                "Bel de persoon op":

                    "Je belt de persoon op en krijgt niemand te pakken... je besluit om deze sollicitatie af te keuren"

                    jump goedbezig

                "Keur de sollicitatie af":

                    jump goedbezig

        "Weg ermee!":

            jump badending

    return



label goedbezig:

    scene black
    with dissolve
    show duomanagergroot

    s "Hulde!! dat was het goede antwoord."

    $ score += 1

    if score < 10:

        "Probeer de volgende!"

        jump randomcasus

        return

    if score >= 10:

        s "Gefeliciteerd, MetaRobin!"

        s "Je bent de werknemer van de maand!"

        scene duogroot
        with fade

        s "Hulde!"

        s "Tijd voor een feestje!"

        show win
        with fade

    return

label badending:

    scene black
    with dissolve

    s "Dat is niet goed MetaRobbin."

    $ score -= 1

    if score > 3:

        s "Voor deze keer zie ik het door de vingers..."

        jump randomcasus

    if score < 4:

        s "Sorry MetaRobin, maar ik denk dat je te dom bent voor dit werk..."

        s "Daar is de deur."

        scene gameover
        with fade

    return