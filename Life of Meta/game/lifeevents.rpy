label eventpicker:
# de eventpicker voor activiteiten na meta's werkdag

    if toestemming == False:
        $ rng1 = renpy.random.randint (1,4)

        if rng1 < 3 or werk:
            # na alle casussen toestemming op true?
           return

        else:


            if lasteventnr == 1:

                # eerste event voor na werk. uitgaan met de covid pass.
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
                                $ laat = True
                                jump badending

                            "je besluit niet te gaan en een nieuwe booster aan te vragen":

                                "je mist helaas een goed feestje, maar bent gelukkig op tijd op werk"
                                "en je afspraak voor een booster is gemaakt"

                                $ booster = True
                                jump oudwerknewstyle

                                return


                            "je besluit gewoon te gaan en maar zien hoe het loopt":

                                "je gaat de stad in en komt wat vrienden tegen"
                                "jullie besluiten naar de kroeg te gaan"
                                "als jullie bij de kroeg komen zie je dat er een corona controle is..."

                                menu:

                                    "je besluit toch maar naar huis te gaan":

                                        "je mist helaas een goed feestje, maar bent gelukkig op tijd op werk"

                                        jump oudwerknewstyle
                                        return

                                    "je gaat naar een andere kroeg, zonder corona controle":

                                        "je zit in je eentje in de kroeg, want al je vrienden zijn de andere kroeg gegaan"
                                        "na een tijdje verveel je je en besluit je maar naar huis te gaan"
                                        "op tijd naar bed. in ieder geval ben je op tijd op je werk"

                                        jump oudwerknewstyle

                                    "je besluit een telefoon van je vriend te gebruiken":

                                        "na wat gedoe kom je toch binnen"
                                        "laat het feest maar beginnen!!"
                                        "na een paar uur wil je nog een biertje halen, maar je krijgt een onverwachte controle"

                                        menu:

                                            "je besluit maar snel naar huis te gaan":

                                                "redelijk aangeschoten kom je thuis aan"
                                                "de volgende ochtend wordt je waker met een behoorlijke kater"
                                                "maar gelukkig wel op tijd op het werk"

                                                jump oudwerknewstyle

                                            "je vraagt je vriend om een biertje te gaan halen":

                                                "je hebt een fantastisch feestje tot laat in de nacht"
                                                "helaas... kom je veel te laat op je werk"
                                                $ laat = True
                                                jump badending

                                            "je gaat gewoon bestellen":

                                                "je loopt naar de bar en besteld een rondje bier"
                                                "de barman vraagt naar je coronapas"
                                                "je kijkt hem aan en zegt dat je die niet hebt"
                                                "de barman roept de uitsmijter waarop een kleine vechtpartij begint"
                                                "de volgende ochtend wordt je wakker in een politiecel"
                                                scene gameover
                                                $ score = 0
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
                        $ laat = True
                        jump badending
                    return

            if lasteventnr == 2:

                call loverevent

            if lasteventnr == 3:

                call deavond

            if lasteventnr == 4:

                call deechteavond
    else:

        if lasteventnr == 5 or werk:
            jump toekomstbaan

        else:
            jump toekomsteventpicker

return

label toekomsteventpicker:

    if toekomstevent == 1:
        jump toekomstevent1

    if toekomstevent == 2:
        jump toekomstevent2

    if toekomstevent == 3:
        jump toekomstevent3

    if toekomstevent == 4:
            jump toekomstevent4

    if toekomstevent == 5:
            jump toekomstevent5

    if toekomstevent == 6:
            jump toekomstevent6

    if toekomstevent == 7:
            jump toekomstevent7

    if toekomstevent == 8:
            jump toekomstevent8

    if toekomstevent == 9:
            jump toekomstevent9

    if toekomstevent == 10:
            jump toekomstevent10

    if toekomstevent == 11:
            jump toekomstevent11

    else:
        return
        #jump randomtoekomstcasus




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
                $ laat = True
                $ lasteventnr += 1

                jump badending

            "je blijft zitten waar je zit en drinkt nog wat verder":

                "je besteld nog een biertje en gaat daarna over op vodka"
                "het wordt een lange avond en wordt wakker naar de kroeg"
                "helaas, ga je vandaag je werk niet halen..."
                $ laat = True
                jump badending

            "je besluit maar naar huis te gaan...":

                "je loopt naar de bar en betaalt je rekening"
                "daarna snel naar huis en komt redelijk vroeg thuis"
                "de volgende ochtend ben je een beetje brak, maar nog op tijd op het werk"

                #jump randomcasus
                return

        return

label deavond:

    "Als je terug komt uit je werk besluit je haar te bellen"
    "wat wil je doen?"

    menu:

        "praat nog wat langer door aan de telefoon":

            "je praat nog wat langer door aan de telefoon"
            "na een tijdje zegt ze dat ze nu toch echt moet gaan... "
            "dus jullie zeggen elkaar gedag en beloven weer te bellen"
            #jump randomcasus
            return


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

            #jump randomcasus
            return

        "sluit af en ga naar bed":

            "jammer... zo wordt het nooit wat natuurlijk..."

            scene gameover

    return

label deechteavond:
#keuze om tot de vrijpartij te komen... of niet...

    "Het is zo ver! Eindelijk een avondje uit"
    "Je besluit je netjes aan te kleden"

    "Waar wil je afspreken?"
    menu:
        "In een restaurant":

            v "Weet jij nog een leuk restaurant?"
            m "Ja hoor, hier om de hoek zit een leukv eettentje"
            v "Leuk!"
            "Jullie gaan naar binnen en raken aan de praat"
            "Na een heerlijk diner gaan jullie naar buiten"
            v "Ga je mee naar mijn huis?"
            m "Ehm... Ja... Leuk.."
            "Ze kust je langzaam op je lippen en daarna lopen jullie naar haar huis"
            jump consentual

        "In de kroeg":

            "Jullie spreken af in de kroeg waar jullie elkaar hebben ontmoet"
            "Als je aankomt zit ze er al"
            "Je geeft haar een knuffel"
            m "Wil je wat drinken?"
            v "Doe maar een biertje"
            "Je loopt naar de bar en haalt 2 biertjes op en gaat naast haar zitten"
            "Al snel raken jullie in gesprek en hebben een leuke avond"
            "Na een tijdje beginnen jullie te zoenen en vraagt ze"
            v "Ga je mee naar mijn huis?"

            menu:
                "ja, graag":
                    jump consentual

                "nee, laten we nog even blijven":
                    "Jullie halen nog een biertje... en nog een... en nog een"
                    "Aan het einde van de avond gaan jullie allebei naar je eigen huis"
                    "Helaas metarobbin! Je had een kans... volgende keer beter"

                    #jump randomcasus
                    return

        "In de bioscoop":
            "Je ontmoet haar bij de bioscoop"
            "Maar welke film wil je zien"
            menu:

                "The Room":
                    "Na 3 minuten film rennen jullie de bioscoopzaal uit"
                    "Dit is geen goed idee voor een avondje uit met haar"
                    "Volgende keer beter!"
                    #jump randomcasus
                    return

                "The Titanic":
                    "Hoewel de film haar erg aanspreekt, val jij langzaam in slaap"
                    "Als je wakker wordt is ze verdwenen..."
                    "Volgende keer beter!"
                    #jump randomcasus
                    return

                "The Postman met Kevin Costner!":
                    "Je zit te genieten van de fantastische film met schitterende beelden"
                    "Helaas valt ze langzaam in slaap"
                    "Als ze wakker wordt zegt ze"
                    v "Ik denk dat ik maar ga..."
                    "Volgende keer beter!"
                    #jump randomcasus
                    return

                "cocktail":
                    "Voor je naar de bioscoopzaal gaat kopen jullie een drankje"
                    v "Wil je ook een biertje?"
                    m "Graag, zal ik ze halen"
                    v "Dat is lief"
                    m "Wil je ook wat eten erbij?"
                    v "Nee hoor, dankje"
                    "Jullie lopen naar de bioscoopzaal en gaan ergens achterin zitten"
                    "De film begint en jullie gaan steeds dichter bij elkaar zitten"
                    "Na een tijdje beginnen jullie langzaam aan te zoenen"
                    v "Zullen we naar mijn huis gaan?"
                    menu:
                        "Ja, graag":

                            jump consentual

                        "Neuh, laten we de film afkijken":

                            "Jullie kijken de film af, maar de sfeer is weg"
                            "Jammer MetaRobbin... Volgende keer beter"

                            #jump randomcasus
                            return


return

label consentual:
# blockchain voor consentual sex

    "Jullie komen bij haar huis aan"
    "Na wat gezoen vraagt ze"
    v "Je gebruikt het toch wel?"
    "Je kijkt verward..."
    m "Ehm wat?"
    v "Je weet wel! de consentual-app!"
    m "De wat?"
    v "Gewoon even downloaden, in checken, akkoord geven voor de vrijpartij met toestemming en we kunnen"
    "Je download snel de app, logt in."
    "Je ziet gelijk al de vraag staan"
    "Er is iemand de een vrijpartij met je wil, wil jij ook?"

    menu:
        "Geef geen toestemming":
            "Zucht... moeten we echt alles uitspellen... dit een een belangrijk onderdeel van het spel"
            "Af en toe moet je gewoon even meespelen anders heeft die arme MetaRobbin geen leven..."
            "Je besluit toestemming te geven"
            jump toestemming

        "geef toestemming":

            jump toestemming

return

label toestemming:
    $ lasteventnr += 1
    "Eindelijk is het zover, je beland in bed met deze prachtige vrouw"
    "Het begin van een mooie relatie"
    "Die toestemmingsapp zet je op een idee"
    "Dat met die diploma's kan ook makkelijker"
    "Misschien op dezelfde manier..."
    "Je besluit het eventjes te laten bezinken en later met Sylvie te bespreken"
    $ toestemming = True
    #jump randomcasus
    return

label toekomstevent1:
    $ toekomstevent +=1
    "na lang zwoegen slaagt MetaMindy eindelijk voor haar diploma"
    m "tijd voor een feestje MetaMindy!"
    v "ja, maar eerst mijn diploma ophalen!"
    v "ik heb de wallet al gedownload... nu nog het diploma"
    "casus van wallet uit diplomaregister"
    jump randomtoekomstcasus

label toekomstevent2:
    $ toekomstevent +=1

    # "het is datenight vanavond, dus je maakt je op voor een date met MetaMindy"
    #TODO "samenwonen..."

    jump randomtoekomstcasus

label toekomstevent3:
    $ toekomstevent +=1
    "samen een huis komen, hypotheek en al die meuk..."
    jump randomtoekomstcasus

label toekomstevent4:
    $ toekomstevent +=1
    "trouwen"
    jump randomtoekomstcasus

label toekomstevent5:
    $ toekomstevent +=1
    #TODO tijdelijk event geboorte plaatjes maken
    n "metamindy komt naar je toe en zegt"
    v happy "ik moet je wat vertellen"
    m "wat?"
    n "ze laat je iets zien"
    show zwanger
    m "echt??"
    v "ja..."
    m "wat fantastisch!"
    n "aangezien we geen maanden gaan wachten, springen we wat voorwaarts in de tijd"
    show hospital
    play sound "audio/hospital.mp3"
    m "dat is het liefste kind dat ik ooit heb gezien "
    v happy "hmm ja, hoe zullen we hem noemen? "
    m "wat denk je van ehm..."

    $ kidname = renpy.input("welke naam wil je het kind geven?", length=32)
    if not kidname:
        $ kidname = "kiddo"
    v "[kidname]... ja dat is een leuke naam!"
    m "ugh... weet je nog wat pa vertelde over mijn aanmelding?"
    v annoyed "ja... dat weet ik nog... laten we hopen dat het tegenwoordig wat makkelijker gaat... die lange wachttijden"
    m "ja ik geloof dat het via mijn wallet kan tegenwoordig..."
    v happy "oh dat zou fantastisch zijn"
    m "even kijken... "
    n "je kijkt op de website van de gemeente en ziet de digitale aanmelding staan"
    menu:
            "wil je je kind digitaal aanmelden?"
            "ja":
                #TODO plaatjes met werking in de toekomst maken
                v "hoe werkt dat eigenlijk die digitale aanmelding?"
                stop sound
                "digiale aanmelding"
                jump randomtoekomstcasus
            "nee":
                n "ah je wilt dezelfde werkwijze hanteren als je vader..."
                n "verstandig..."
                play music "audio/crowd-talking-2.mp3"
                receptionist "heeft u een afspraak?"
                m "nee, kan dat?"
                n "de receptionist drukt op een aantal knoppen en er komt een kaartje uit, met nummer 89"
                receptionist "de wachttijd vandaag is wat langer dan normaal wegens paspoorten die ongeldig zijn"
                m "oh, dan wacht ik toch eventjes"

                n "je gaat zitten en kijkt om zich heen... op zoek naar de nummer melder"
                show nr13 at truecenter
                m "nummer 13... oh dat is wel iets langer dan eventjes"
                scene black
                show stadhuis
                $ n ("MetaRobbin kijkt op zijn horloge... 9.14", interact=False)
                $ renpy.pause (4.0, hard=True)
                $ n ("10.14", interact=False)
                $ renpy.pause (4.0, hard=True)
                $ n ("11.14", interact=False)
                $ renpy.pause (4.0, hard=True)
                $ n ("Mededeling: het is nu 12 uur pause, dus de wachttijd wordt iets langer", interact=False)
                $ renpy.pause (4.0, hard=True)
                n "12.45"
                show nr87 at truecenter
                m "oh bijna aan de beurt..."
                $ renpy.pause(2.0, hard=True)
                show nr88 at truecenter
                $ renpy.pause(2.0, hard=True)
                show nr89 at truecenter
                m "eindelijk..."
                scene
                show balie
                n "ben je er al flauw van?"
                n "laten we maar aannemen dat de aanmelding goed is gegaan... "
                jump randomtoekomstcasus
    jump randomtoekomstcasus

label toekomstevent6:
    $ toekomstevent +=1
    "kinderopvangcasus"
    jump randomtoekomstcasus

label toekomstevent7:
    $ toekomstevent +=1
    "kinderopvangcasus"
    jump randomtoekomstcasus

label toekomstevent8:
    $ toekomstevent +=1
    "begrafenis van metapapa"
    jump randomtoekomstcasus

label toekomstevent9:
    $ toekomstevent +=1
    "scheiden"
    jump randomtoekomstcasus

label toekomstevent10:
    $ toekomstevent +=1
    "robbin mag kids niet halen van kinderopvang"
    jump randomtoekomstcasus

label toekomstevent11:
    $ toekomstevent +=1
    "endgame, robbin gaat naar museum met ponskaarten en ziet waar we vandaan komen"
    jump randomtoekomstcasus


