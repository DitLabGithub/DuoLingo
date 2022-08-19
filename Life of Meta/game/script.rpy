# Declare characters used by this game.
#sylvie
define s = Character(_("Sylvie"), image="sylvie", color="#c8ffc8")
image side sylvie = "sylvie blue normal.png"

#metarobbin
define m = Character(_("MetaRobbin"), color="#c8c8ff")

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
#werk variabele voor enkel werk casussen of niet
default werk = False
#variabelen voor de toekomstcasussen
default rus = False
default hol = False
default apel = False


label start:

    menu:
        "ga naar spel":

            jump born

        "alleen de werkcasussen":
            $ werk = True

            jump werk

        "start het metaleven van Robbin":

            jump born

      #  "test events":

      #      jump randomtoekomstcasus
    return

label born:

    show pa at left
    show ma at right
    show hospital
    play music "audio/hospital.mp3"
    n "dit zijn metapapa en metamama."

    pa happy"dat is het liefste kind dat ik ooit heb gezien "
    ma happy "hmm ja, hoe zullen we hem noemen? "
    pa "zullen we hem vernoemen naar je grootvader? "
    ma "ik vind robbertinus wel een beetje een ouderwetse naam, misschien robbert? "
    pa "wat denk je van robbin?"
    ma "ja, dat is een leuke naam!"
    pa n2 "wat hebben we allemaal nodig voor die aangifte?"
    ma annoyed "even checken... oh wat een ingewikkelde website is dit..."
    ma "oh vandaag nog niet... want Robbin is vandaag geboren, morgen is het zaterdag, dan kan het ook niet"
    ma angry "zondag niet... maandag is het toch pasen? en dinsdag bevrijdingsdag? "
    ma "ehm... het staat er niet bij... "
    pa angry1 "wat is dat voor onzin... zijn ze dinsdag dicht dan? "
    ma "weet ik niet... maar het moet wel op tijd anders krijgen we een boete... "
    pa "kan ik het dan niet online doen?"
    ma annoyed "nee, niet hier... in sommige gemeentes wel... "
    pa blush "okay woensdag dus... Wat moet ik meenemen?"
    ma "ehm hier... je id bewijs, naamkeuze? van te voren... nee dus..  "
    ma "en verklaring van geboorte.. maar die is ook niet verplicht "
    pa disgust "wat onduidelijk allemaal... dus alleen mijn id bewijs"
    ma -annoyed "ja denk ik... "
    stop music
    scene
    show stadhuis

    n "Die woensdag gaat MetaPapa gaat op pad naar het gemeentehuis"
    n "Metapapa meld zich bij de balie en zegt dat hij zn baby wil aangeven"

    play music "audio/crowd-talking-2.mp3"
    receptionist "heeft u een afspraak?"
    pa surprise"nee, kan dat?"
    n "de receptionist drukt op een aantal knoppen en er komt een kaartje uit, met nummer 89"
    receptionist "de wachttijd vandaag is wat langer dan normaal wegens paspoorten die ongeldig zijn"
    pa - surprise "oh, dan wacht ik toch eventjes"

    n "pa gaat zitten en kijkt om zich heen... op zoek naar de nummer melder"
    show nr13 at truecenter
    pa "nummer 13... oh dat is wel iets langer dan eventjes"
    scene black
    show stadhuis
    $ n ("Metapapa kijkt op zijn horloge... 9.14", interact=False)
    $ renpy.pause (4.0, hard=True)
    $ n ("10.14", interact=False)
    $ renpy.pause (4.0, hard=True)
    $ n ("11.14", interact=False)
    $ renpy.pause (4.0, hard=True)
    $ n ("Mededeling: het is nu 12 uur pause, dus de wachttijd wordt iets langer", interact=False)
    $ renpy.pause (4.0, hard=True)
    n "12.45"
    show nr87 at truecenter
    pa "oh bijna aan de beurt..."
    $ renpy.pause(2.0, hard=True)
    show nr88 at truecenter
    $ renpy.pause(2.0, hard=True)
    show nr89 at truecenter
    pa angry1 "eindelijk..."
    scene
    show balie
    stop music
    "metapapa loopt naar de balie"
    a "hallo, wat kan ik voor je doen?"
    pa happy "ik wil mijn zoon aangeven, die is vorige week geboren"
    a "gefeliciteerd! heeft u een verklaring van geboorte bij u?"
    pa "ehm nee, er stond op de website dat dat niet hoefde..."
    a "hmm oh... ja dat is wel wat lastiger dan... "
    a "momentje... ik print even het formulier uit"
    a "wilt u dit formulier invullen met blokletters?"
    pa grin "papier? ehm... natuurlijk"
    a "heeft u ondertussen u ID bewijs meegenomen"
    n "metapapa geeft zijn paspoort aan de ambtenaar"
    a "dank je wel"
    n "na een tijdje heeft metapapa alle antwoorden ingevuld en geeft het formulier terug"
    a "dank u wel... "
    n "de ambtenaar begint met invullen"
    a "Robbin is dat correct? en vorige week vrijdag geboren?"
    pa "ja met 2 b's "
    a "hij is geboren met 2 b's?"
    pa angry "nee, de naam is met 2 b's"
    a "ja ik zie het... en metamama is de moeder?"
    pa - angry "jazeker"
    a "dan heb ik nu alles in het systeem staan, momentje nog dat krijgt u de geboorteakte"
    n "metapapa krijgt een papier waarop groot staat geboorteakte en alle gegevens"
    a "wilt u het allemaal nog even controleren?"
    pa "oh de naam van Robbin staat fout... "
    a "oh ik zie het, 2 b's toch? momentje dan print ik een nieuwe geboorteakte uit"
    n "de nieuwe geboorteakte lijkt allemaal in orde en MetaRobbin is eindelijk ingeschreven en daarmee begint het digitale leven!"
    scene black

    play music "audio/woo_scary.ogg"

    show text "{b}Life of Meta{/b}" at truecenter with dissolve

    $ renpy.pause(2.0)
    show metarobbinmedium at top
    $ renpy.pause(4.0)
    scene black
    show ditlablogo at truecenter

    "{b}Een spel ontwikkeld door het Dit-Lab. Een samenwerking tussen de Hanzehogeschool en DUO{/b}"
    $ renpy.pause(2.0)
    jump school

    return

label school:
    #inschrijven meta bij een school
        #àanmelden voor stex met beperking
        #aanmelden stufi
    scene black
    play sound "audio/exp.mp3"
    image exp = im.Scale("exp.jpg", 1920,1080)
    show exp
    $ renpy.pause(4.0)
    jump werk
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
        if werk:
            return
        else:
            jump toekomsteventpicker

    return

label toekomstcasus1:
# rusland casus

    $ toekomstcas += 1
    image rus = im.Scale("nf rusland.png", 1920,1080)
    show rus
    play sound "audio/newsflash.mp3"
    n "Je hoort in de ochtend op het nieuws dat alles uit Rusland geboycot moet worden. Je denkt nog, dat heeft met mij niet zoveel te maken"
    n "Halverwege de ochtend krijg je een opdracht vanuit het ministerie. Wil je erover zorgen dat iedere rus tegen gehouden wordt, zodat ze niet per ongeluk worden aangenomen?"
    n "Je hebt nu een paar keuzes..."
    n "Wat wil je doen?"

    menu:
        "Alle scholen uit Rusland uitsluiten in het register":
            "vanaf nu worden alle scholen uit Rusland uitgesloten en de diplomas afgekeurd."
            "Dit is een goede keuze. Het bespaard je enorm veel handmatig werk..."
            "Maar 2 jaar later hoor je dat in Belgie er een briljante Estse is aangenomen die ook bij ons had gesolliciteerd"
            "Wij hebben haar afgewezen omdat ze van een russische school kwam"

            "maar laten we verder gaan!"

            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker

        "Handmatig alle Russen uitsluiten":
            "Vanaf nu komen alle Russen langs bij de handmatige beoordeling"
            "Dit zorgt er in ieder geval voor dat je niet alle mensen van een Russische school zomaar uitsluit"
            "Maar door de hoeveelheid extra werk krijgt je afdeling het ineens enorm druk"

            $ drukte +=3
            $ rus = True
            "laten we verder gaan"

            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker


    return

label toekomstcasus2:
#inhollandcasus

        image fraude = im.Scale("nf fraude.png", 1920,1080)
        show fraude
        play sound "audio/newsflash.mp3"
        #TODO newsflash hoge school is niet betrouwbaar meer... zeker 100 diplomas ongeldig
        $ toekomstcas += 1
        n "je krijgt een bericht dat een school niet meer betrouwbaar is. Eerste onderzoeken wijzen uit dat zeker 100 diplomas ongeldig zijn.  wat wil je doen?"

        menu:
            "wat wil je doen?"
            "sluit de school gelijk uit via het register":
                "je sluit alle diplomas van deze school uit. het gaat om circa een half miljoen diplomas terwijl er maar 100 ongeldig zijn"
                "misschien is dit niet de beste keuze... , maar je kunt het herstellen"

                menu:
                    "je sluit tijdelijk alle leerlingen van deze school uit.":
                        "Hierdoor mis je een aantal sollicitanten... maar je krijgt ook geen ongeldige diplomas binnen"
                        "alle sollicitanten van de school kun je later opnieuw oproepen voor een sollicitatie"

                        if werk:
                            jump randomtoekomstcasus
                        else:
                            jump toekomsteventpicker

                    "je besluit om alle leerlingen van deze school handmatig tegen te houden":
                        "Je team controleert alle gevallen met de hand, maar je weet nog niet welke diploma's onterecht zijn uitgegeven"
                        "dit levert veel extra handwerk op, misschien had je beter alle leerlingen van deze school tijdelijk uitgesloten"

                        $ drukte +=2
                        $ hol = True
                        if werk:
                            jump randomtoekomstcasus
                        else:
                            jump toekomsteventpicker

            "wacht op het onderzoek dat persoonlijke diploma's uitsluit en sluit die handmatig uit":
                "Tijdens het onderzoek sijpelen er langzaam een aantal diplomas door die onterecht zijn uitgegeven."
                "Helaas kun je dit achteraf niet meer herstellen..."

                if werk:
                    jump randomtoekomstcasus
                else:
                    jump toekomsteventpicker

        return

label toekomstcasus3:
    #TODO appenpokken in apeldoorn
    image apen = im.Scale("nf apen.png", 1920,1080)
    show apen
    play sound "audio/newsflash.mp3"

    #newsflash over een appenpokken uitbraak in apeldoorn...lasteventnr
    $ toekomstcas += 1
    "Je krijgt opdracht van de directie om niemand meer uit te nodigen uit apeldoorn"
    "Wat wil je doen?"
    menu:

        "Haal alle scholen uit apeldoorn uit het register":

            "dit lijkt me niet goed MetaRobbin"
            "het gaat om 500.000 diplomas waarvan er maar een paar ongeldig zijn..."
            "maar je bespaard je afdeling een hoop handmatig werk"
            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker


        "Controleer handmatig per persoon of ze uit Apeldoorn komen":
            $ drukte +=1
            $ apel = True
            "dit levert wat handmatig werk op, maar gelukkig krijg je wel de kans om alle sollicitaties te controleren"
            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker

    return

label toekomstcasus4:
#te druk op de afdeling
    image drukte = im.Scale("nf drukte.png", 1920,1080)
    show drukte
    play sound "audio/newsflash.mp3"
    menu:

        "De druk op je afdeling wordt veel te hoog... Je moet echt dingen automatisch doen"
        "beoordeel de russiche scholen automatisch" if rus:
            "Je laat je afdeling nu 20.000 extra gevallen per maand minder doen"
            "dat zal de druk op de afdeling zeker verlagen!"
            $ drukte -=3
            $ rus = False
            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker

        "doe apeldoorn automatisch" if apel:
            "je laat ongeveer 5 sollicitaties per maand geautomatiseerd doen"
            "dit levert helaas niets op qua drukte van de afdeling"
            $ apel = False
            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker

        "stop met de handmatige afhandeling van de afgekeurde school" if hol:
            "De afdeling gaat vanaf nu alle diplomas van de afgekeurde shool geautomatiseerd afkeuren"
            "dit bespaard je een hoop werk... maar je mist enorm veel solliciaties"
            $ drukte -=2
            $ hol = False
            if werk:
                jump randomtoekomstcasus
            else:
                jump toekomsteventpicker

        "meer informatie over de verschillen":
            "aantal sollicitaties met een russiche nationaliteit zijn 20.000 per maand, en van Russische scholen 25.000"
            "vanuit Apeldoorn zijn er 5 sollicitaties per maand en 600 die van een school in Apeldoorn een diploma hebben gekregen"
            "De afgekeurde school heeft 500.000 diplomas uitgegeven en naar, verwachting, zijn er ca. 100 die ongeldig moeten worden"
            jump toekomstcasus4

    return



# bewaren van resultaten vna oude casus icm de nieuwe zien
# flowchart
# diploma via email
# diploma legaliseren vragen naar casussen

label credits:
    "sounds from soundjay.com and pixabay.com"