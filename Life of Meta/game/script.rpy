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

label start:

    menu:
        "ga naar werk spel":

            jump werk

        "begin metas leven":

            jump born

        "naar de toekomst van meta":

            jump toekomst

        "test events":

            jump covidevent
    return

label born:

    #geboorte van meta robin voorstellen van mama en papa meta...
    #aangifte van meta robin bij de gemeente
    #inschrijven meta bij een school
    #àanmelden voor stex met beperking
    #aanmelden stufi

    "dit zijn metapapa en metamama."

    "metamama staat op het punt om te bevallen en hiermee begint jouw leven."

    "je vernoemen je naar je overgrootvader en vanaf nu heet je MetaRobin"

    "natuurlijk moet je eerst aangemeld worden bij de gemeente om je registraties op orde te maken... "

    return


label afgestudeerd:

    jump werk

label toekomst:

    # moet nog verder uitgewerkt worden...
   scene gameover
   with fade
   return



label werk:

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

    return


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

label eventpicker:
# de eventpicker voor activiteiten na meta's werkdag

    if toestemming == False:
        $ rng = renpy.random.randint (1,3)

        if rng < 3:

            jump randomcasus

        if rng == 3:


            if lasteventnr == 1:

                jump covidevent

            if lasteventnr == 2:

                jump loverevent

            if lasteventnr == 3:

                jump deavond

            if lasteventnr == 4:

                jump deechteavond



    else:

        if lasteventnr == 5:
            jump toekomstbaan

        # 6 metarobin neemt een hond
        # 7 metarobin gaat samenwonen, huurtoeslag etc...
        # 8 metarobin gaat huis kopen (hypotheek, verhuizen etc…)
        # 9 metarobin gaat trouwen
        # 10 metarobin krijgt kinderen
        # 11 metarobin moet kinderen ophalen van kinderopvang
        # 12 metarobin moet de begrafenis van metapapa regelen
        # 13 metarobin gaat scheiden
        # 14 metarobin kan kinderen niet meer ophalen


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

    return

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
    return


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

        jump eventpicker

        return

    if score >= 10:
        if maandmedewerker == False:
            s "Gefeliciteerd, MetaRobbin!"

            s "Je bent de werknemer van de maand!"

            scene duogroot
            with fade

            s "Hulde!"

            show win
            with fade

            s "Je hebt zulk goed werk gedaan hier MetaRobbin... "
            s "Je verdient een promotie!"
            s "We gaan ook het systeem van diplomas een beetje veranderen"
            s "Hoe dat werkt leggen we je later wel uit, eerst een feestje!!"
            $ maandmedewerker = True
            jump toekomstbaan

        else:
            jump eventpicker

    return

label badending:

    scene black
    with dissolve

    s "Dat is niet goed MetaRobbin."

    $ score -= 1

    if score > 3:

        s "Voor deze keer zie ik het door de vingers..."

        jump eventpicker

    if score < 4:

        s "Sorry MetaRobin, maar ik denk dat je te dom bent voor dit werk..."

        s "Daar is de deur."

        scene gameover
        with fade

    return

label toekomstbaan:

    scene black
    with dissolve

    #andere baan...
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
    m "Ja die! Nou precies zo eigenlijk, maar in plaats van toestemming, geef je je diploma tijdelijk."
    s "Oh dat is slim... Wat mij betreft mag je daarmee bezig! Dan hoef je de komende tijd geen diploma's te checken. "
    #nieuwe casus bouwen op de nieuwe manier!

    jump eventpicker
    return

label covidevent:
# eerste event voor na werk. uitgaan met de covid pass
# eventnr 1

    show win

    if booster == False:

        "tijd voor een avondje uit..."
        "beetje relaxen maar is je covid pass in orde?"
        "je pakt je telefoon en checkt je wallet"
        "je kijkt en ziet geen QR code... je vaccinatie is verlopen..."

        "wat ga je doen?"

        menu:

            "laat je testen en gaat":

                "je hebt een fantastisch feestje tot laat in de nacht"
                "helaas... kom je veel te laat op je werk"

                jump badending

            "je besluit niet te gaan en een nieuwe booster aan te vragen":

                "je mist helaas een goed feestje, maar bent gelukkig op tijd op werk"
                "en je afspraak voor een booster is gemaakt"

                $ booster = True

                jump randomcasus

            "je besluit gewoon te gaan en maar zien hoe het loopt":

                "je gaat de stad in en komt wat vrienden tegen"
                "jullie besluiten naar de kroeg te gaan"
                "als jullie bij de kroeg komen zie je dat er een corona controle is..."

                menu:

                    "je besluit toch maar naar huis te gaan":

                        "je mist helaas een goed feestje, maar bent gelukkig op tijd op werk"

                        jump randomcasus


                    "je gaat naar een andere kroeg, zonder corona controle":

                        "je zit in je eentje in de kroeg, want al je vrienden zijn de andere kroeg gegaan"
                        "na een tijdje verveel je je en besluit je maar naar huis te gaan"
                        "op tijd naar bed. in ieder geval ben je op tijd op je werk"

                        jump randomcasus


                    "je besluit een telefoon van je vriend te gebruiken":

                        "na wat gedoe kom je toch binnen"
                        "laat het feest maar beginnen!!"
                        "na een paar uur wil je nog een biertje halen, maar je krijgt een onverwachte controle"

                        menu:

                            "je besluit maar snel naar huis te gaan":

                                "redelijk aangeschoten kom je thuis aan"
                                "de volgende ochtend wordt je waker met een behoorlijke kater"
                                "maar gelukkig wel op tijd op het werk"

                                jump randomcasus

                            "je vraagt je vriend om een biertje te gaan halen":

                                "je hebt een fantastisch feestje tot laat in de nacht"
                                "helaas... kom je veel te laat op je werk"

                                jump badending

                            "je gaat gewoon bestellen":

                                "je loopt naar de bar en besteld een rondje bier"
                                "de barman vraagt naar je coronapas"
                                "je kijkt hem aan en zegt dat je die niet hebt"
                                "de barman roept de uitsmijter waarop een kleine vechtpartij begint"
                                "de volgende ochtend wordt je wakker in een politiecel"
                                scene gameover
                                $ score -= 20
                                "je komt niet door de poortjes op je werk..."
                                "wat je niet wist is dat je VOG is ingetrokken..."
                                s "sorry, maar je bent ontslagen! Als je niet op het werk kunt komen, hebben we niets aan je"
                                s "bovendien heb je geen VOG meer, dus kunnen we je niet aan de slag laten gaan met deze privicy gevoelige gegevens"

                                with fade

    if booster:

        "tijd voor een avondje uit..."
        "beetje relaxen maar is je covid pass in orde?"
        "je pakt je telefoon en checkt je wallet"
        "je kijkt en ziet een QR code. Mooi! niets houd je tegen om te gaan feesten!"

        "helaas kom je veel te laat op je werk..."
        $ lasteventnr += 1

        jump badending
    return

label loverevent:
#tweede event voor meta robbin

        "tijd voor een avondje uit..."
        "beetje relaxen maar is je covid pass in orde?"
        "je pakt je telefoon en checkt je wallet"
        "je kijkt en ziet een QR code. Mooi! niets houd je tegen om te gaan feesten!"
        "na een tijdje kom een een mooi persoon tegen"
        "wat doe je?"

        menu:

            "je spreek haar aan?":

                "je loopt op haar af en begint te praten"
                "het wordt een hele leuk avond en je komt veel te laat thuis, maar wel met een telefoonnummer"
                "helaas kom je wel te laat op je werk..."

                $ lasteventnr += 1

                jump badending

            "je blijft zitten waar je zit en drinkt nog wat verder":

                "je besteld nog een biertje en gaat daarna over op vodka"
                "het wordt een lange avond en wordt wakker naar de kroeg"
                "helaas, ga je vandaag je werk niet halen..."

                jump badending

            "je besluit maar naar huis te gaan...":

                "je loopt naar de bar en betaalt je rekening"
                "daarna snel naar huis en komt redelijk vroeg thuis"
                "de volgende ochtend ben je een beetje brak, maar nog op tijd op het werk"

                jump randomcasus

        return

label deavond:

    "Als je terug komt uit je werk besluit je haar te bellen"
    "wat wil je doen?"

    menu:

        "praat nog wat langer door aan de telefoon":

            "je praat nog wat langer door aan de telefoon"
            "na een tijdje zegt ze dat ze nu toch echt moet gaan... "
            "dus jullie zeggen elkaar gedag en beloven weer te bellen"
            jump raondomcasus


        "vraag haar uit":

            m "zeg... ehm... zou je... ehm... "
            v "wat zeg je MetaRobbin? de verbinding valt wel?"
            "je zegt nog wat... maar je hoort dat de verbinding wordt verbroken..."
            "je besluit maar naar bed te gaan en je op te maken voor een volgende werkdag"

            "als je wakker wordt voel je je wat sip... dit was de kans om haar mee uit te vragen"
            "terwijl je naar je werk loopt krijg je een berichtje"
            v "Hey MetaRobbin, sorry van ons gesprek gister... ik wilde je eigenlijk wat vragen"
            m "ik jou ook eigenlijk, ik bel je gelijk"

            "je belt haar op en ze neem gelijk op"
            v "Hoi MetaRobbin, wil je wel met me uit?"
            m "wa... hmm? ehm... ja!"
            v "oh gelukkig, wat wilde jij vragen?"
            m "hetzelfde"
            "jullie spreken af om snel weer te bellen voor een avondje uit"

            $ lasteventnr += 1

        "sluit af en ga naar bed":

            "jammer... zo wordt het nooit wat natuurlijk..."

            scene gameover

    return

label deechteavond:
#keuze om tot de vrijpartij te komen... of niet...

    "het is zo ver! eindelijk een avondje uit"
    "je besluit je netjes aan te kleden"

    "waar wil je afspreken?"
    menu:
        "in een restaurant":

            v "weet jij nog een leuk restaurant?"
            m "ja hoor, hier om de hoek zit een leukv eettentje"
            v "leuk!"
            "jullie gaan naar binnen en raken aan de praat"
            "na een heerlijk diner gaan jullie naar buiten"
            v "ga je mee naar mijn huis?"
            m "ehm... ja... leuk.."
            "ze kust je langzaam op je lippen en daarna lopen jullie naar haar huis"
            jump consentual

        "in de kroeg":

            "jullie spreken af in de kroeg waar jullie elkaar hebben ontmoet"
            "als je aankomt zit ze er al"
            "je geeft haar een knuffel"
            m "wil je wat drinken?"
            v "doe maar een biertje"
            "je loopt naar de bar en haalt 2 biertjes op en gaat naast haar zitten"
            "al snel raken jullie in gesprek en hebben een leuke avond"
            "na een tijdje beginnen jullie te zoenen en vraagt ze"
            v "ga je mee naar mijn huis?"

            menu:
                "ja, graag":
                    jump consentual

                "nee, laten we nog even blijven":
                    "jullie halen nog een biertje... en nog een... en nog een"
                    "aan het einde van de avond gaan jullie allebei naar je eigen huis"
                    "helaas metarobbin! je had de kans... volgende keer beter"

                    jump randomcasus

        "in de bioscoop":
            "je ontmoet haar bij de bioscoop"
            "maar welke film wil je zien"
            menu:

                "The room":
                    "na 3 minuten film rennen jullie de bioscoopzaal uit"
                    "dit is geen goed idee voor een avondje uit met haar"
                    "volgende keer beter!"
                    jump randomcasus

                "the titanic":
                    "hoewel de film haar erg aanspreekt, val jij langzaam in slaap"
                    "als je wakker wordt is ze verdwenen..."
                    "volgende keer beter!"
                    jump randomcasus

                "the postman met kevin costner!":
                    "je zit te genieten van de fantastische film met schitterende beelden"
                    "helaas valt ze langzaam in slaap"
                    "als ze wakker wordt zegt ze"
                    v "ik denk dat ik maar ga..."
                    "volgende keer beter!"
                    jump randomcasus

                "cocktail":
                    "voor je naar de bioscoopzaal gaat kopen jullie een drankje"
                    v "wil je ook een biertje?"
                    m "graag, zal ik ze halen"
                    v "dat is lief"
                    m "wil je ook wat eten erbij?"
                    v "nee hoor, dankje"
                    "jullie lopen naar de bioscoopzaal en gaan ergens achterin zitten"
                    "de film begint en jullie gaan steeds dichter bij elkaar zitten"
                    "na een tijdje beginnen jullie langzaam aan te zoenen"
                    v "zullen we naar mijn huis gaan?"
                    menu:
                        "ja, graag":

                            jump consentual

                        "neuh, laten we de film afkijken":

                            "jullie kijken de film af, maar de sfeer is weg"
                            "jammer MetaRobbin... Volgende keer beter"

                            jump randomcasus


return

label consentual:
# blockchain ding voor consentual sex

    "jullie komen bij haar huis aan"
    "na wat gezoen vraagt ze"
    v "je gebruikt het toch wel?"
    "je kijkt verward..."
    m "ehm wat?"
    v "je weet wel! de consentual app!"
    m "de wat?"
    v "gewoon even downloaden, in checken, akkoord geven voor de vrijpartij met toestemming en we kunnen"
    "je download snel de app, logt in."
    "je ziet gelijk al de vraag staan"
    "er is iemand de een vrijpartij met je wil, wil jij ook?"

    menu:
        "geef geen toestemming":
            "zucht... moeten we echt alles uitspellen... dit een een belangrijk onderdeel van het spel"
            "af en toe moet je gewoon even meespelen anders heeft die arme MetaRobbin geen leven..."
            "je besluit toestemming te geven"
            jump toestemming

        "geef toestemming":

            jump toestemming

return

label toestemming:
    $ lasteventnr += 1
    "Eindelijk is het zover, je beland in bed met deze prachtige vrouw"
    "Het begin van een mooie relatie"
    "Maar die toestemmingsapp zet je op een idee"
    "Dat met die diploma's kan ook makkelijker"
    "Misschien op dezelfde manier..."
    "Je besluit het eventjes te laten bezinken en later met Sylvie te bespreken"
    $ toestemming = True
    jump randomcasus
