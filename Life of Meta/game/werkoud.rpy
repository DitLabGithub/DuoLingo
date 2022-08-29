
label randomcasus:

    #$ rng = renpy.random.randint (1,5)
    # uitgezet voor een doorloop van casussen ipv random bepaling van een casus
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

    else:
        jump eventpicker

    return

label casus1:

    # inholland casus

    "Hm.."
    $ rng += 1
    show dip2
    with fade

    "Dit diploma ziet er goed uit, maar is uitgegeven door een afgekeurde school, wat wil je doen?"

    menu:

        "Wil je deze persoon uitnodigen?"

        "Ja":

            jump badending

        "Nee":

            jump goedbezig
    return


label casus2:

    # gewoon diploma
    $ rng += 1
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
    $ rng += 1
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
    $ rng += 1
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
    $ rng += 1
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

                    if werk:
                        jump toekomstbaan

                    else:
                        jump goedbezig

                "Keur de sollicitatie af":

                    if werk:
                        jump toekomstbaan
                    else:
                        jump goedbezig

        "Weg ermee!":

            if werk:
                s "dat is niet goed MetaRobbin... maar voor deze keer..."
                jump toekomstbaan
            else:
                jump badending

    return





