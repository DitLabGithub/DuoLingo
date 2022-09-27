#TODO beperkte tijd voor een open casus...
#TODO casus rusland (omkoping evil +1)
#TODO jump naar toekomst werk./... dat moet niet dag wordt niet correct afgelsoten
#TODO casussen uitwerken over hoe het in de toekomst zou gaan
#TODO plaatjes van nieuwe werkwijze opschuiven zodat sylvie er niet voor staat

label werk:
# intro naar werk. alleen eerste keer
    stop music
    scene duogroot
    with fade

    "Je eerste werkdag bij DUO start vandaag"

    "In de verte zie je het DUO gebouw naderen"

    scene duoingang
    with fade

    "Na een rondleiding en lunch is het tijd om je manager te ontmoeten"
    "Je wordt begroet door je manager, Sylvie"
    s "Hoi en welkom bij duo!"

    s "Vandaag is je eerste dag hier en ik leid je rond."

    s "De bedoeling is dat je diploma's controleert. je hebt uiteindelijk 2 keuzes, je kunt een aanvraag afwijzen of toewijzen"

    s "Dat doe je door te kijken of de school een bekend is en actief was ten tijde van het diploma"
    s "Daarnaast kun je de school bellen."
    s "Voor wat betreft de aanvrager kun je bellen of extra informatie opvragen."
    s "Je kunt altijd terugzoeken wat er over een casus is vastgelegd in het archief."
    s "Als het diploma in een andere taal is, is het verstandig om even een vertaling op te vragen. Dat duurt wel eventjes"
    s "En als je een beslissing wilt nemen, meldt dat even bij mij."
    s "Denk er wel over na dat iedere activiteit tijd kost. "
    s "je kunt meerdere casussen tegelijk doen natuurlijk"
    s "succes MetaRobbin!"

    jump kantoor
    return

label oudwerknewstyle:
    default Location = "kantoor"
    scene ontbijttafel
    show screen score_screen()
    if laat:
        n "Geen tijd voor ontbijt, je moet gaan..."
        n "veel te laat kom je aan op werk en je ziet Sylvie al staan"
        scene baas
        with dissolve
        if dag % 3 == 0:
            s "Wat een slechte timing om te laat te komen MetaRobbin... het is tijd voor je functioneringsgesprek"

            $ tijd = 1
            $ dag += 1
            $ laat = False
            jump functioneringsgesprek

        else:
            s "Dat is niet goed MetaRobbin."
            s "Voor deze keer zie ik het door de vingers..."
            s "Ik verwacht beter van je. Nu snel aan het werk"
            $ tijd = 1
            $ dag += 1
            $ laat = False
            jump kantoor

    else:
        $ rng = renpy.random.randint (1,5)
        if dag > 3 and rng == 1:  #TODO goede verdeling maken
             if toekomstcas == 1:
                jump toekomstcasus1
             if toekomstcas == 2:
                jump toekomstcasus2
             if toekomstcas == 3:
                jump toekomstcasus3
#
#                 if drukte > 4:
#
#                     jump toekomstcasus4

        else:
            n "tijd om op te staan. Koffie en ontbijt en je favoriete krant terwijl op de achtergrond het nieuws aanstaat"
            $ tijd = 0
            $ dag += 1
            n "na het ontbijt ga je naar kantoor"

            if dag > 0 and dag % 3 == 0:
                #functioneringsgesprek
                s "Hallo MetaRobbin, het is tijd voor je periodieke functioneringsgesprek"
                jump functioneringsgesprek
            elif dag > 0:
                # teamoverleg

                $ rng = renpy.random.randint (1,10)
                $ rng1 = renpy.random.randint (1,2)
                if rng == 5:
                    scene teammeeting
                    s "welkom allemaal op de teammeeting"

                    if rng1 == 1 and teltimer >= 200:
                        #afdeling zoeken dicht voor x dagen
                        s "we hebben te horen gekregen dat de informatiediensten afdeling het werk niet meer aan kan"
                        s "het gevolg is dat vanaf morgen ze even geen nieuwe opdrachten meer oppakken"
                        s "houdt er rekening mee met je werk"
                        s "Rondvraag..."
                        s "Niemand? okay, dan maar weer aan het werk!"
                        $ Places[7].IsActive = False
                        $ zoektimer = dag + 3

                        jump kantoor
                    elif rng1 == 2 and teltimer >= 200:
                        #telefoon is dicht voor x dagen
                        s "we hebben te horen gekregen dat de telefoonlijnen in onderhoud gaan"
                        s "het gevolg is dat vanaf morgen je niet kunt bellen voor een paar dagen"
                        s "houdt er rekening mee met je werk"
                        s "Rondvraag..."
                        s "Niemand? okay, dan maar weer aan het werk!"
                        $ Places[3].IsActive = False
                        $ teltimer = dag + 3
                        jump kantoor
                    else:
                        n "na een half uur..."
                        s "vandaag hebben we niets meer te bespreken"
                        jump kantoor
                else:
                    jump kantoor
            else:
                # teveel gebruik van rss door speler
                jump kantoor


label functioneringsgesprek:
    scene baas
    if budget < kosten and teveelinfo:
        s "ik heb 2 dingen met je te bespreken"
        s "De AIVD vraagt zich af waarom je extra informatie hebt opgevraagd over Cor van Hout"
        s "Deze informatie heb jij niet nodig voor het bepalen van de geldigheid van een diploma..."
        s "dit levert je een aantekening op in je dossier"
        s "daarnaast lopen de kosten behoorlijk uit de hand."
        s "je moet echt snellere beslissingen nemen door minder resources te gebruiken. probeer wat slimmere keuzes te maken"
        s "gelukkig heb ik nog een beetje budget kunnen krijgen, maar gebruik het niet allemaal gelijk"
        $ budget += 5
        $ teveelinfo == False
        $ aantekening += 1
        jump kantoor
    elif budget < kosten:
        s "we moeten echt bezuinigen..."
        s "de kosten rijzen de pan uit"
        s "gelukkig heb ik een beetje extra budget kunnen krijgen... maar die is niet eindeloos"
        $ budget += 5
        jump kantoor
    elif teveelinfo:
        s "Ik werd gebeld door de AIVD over een informatieverzoek"
        s "waarom heb je extra informatie opgevraagd?"
        s "dit is duidelijk niet nodig voor het bepalen van de geldigheid van een diploma..."
        s "dit kan echt niet MetaRobbin.."
        s "ik moet hiervan een aantekening maken in je dossier"
        $ teveelinfo == False
        jump kantoor
    elif afgerond < 2 and dag > 10:
        s "MetaRobbin... ik zie te weinig progressie in je werk... "
        s "ik zie geen andere optie dan je te ontslaan... "
        s "het spijt me "

    else:
        s "het gaat goed zo MetaRobbin! ik geen geen opmerkingen over je werk"
        jump kantoor

label koffieapparaat:
    scene koffieapparaat
    n "je loopt naar het [Location]"
    $ tijd += 1
    menu:
        "welke koffie wil je?"
        "neem een gewone koffie":
            n "je pakt een gewone koffie..., je neemt een slok en het smaakt naar slootwater... misschien de volgende keer wat anders?"
            return

        "neem een dubbele espresso":
            if espresso < 2:
                n "je pakt een dubbele espresso. zoveel caffiene. het lijkt erop of je vandaag meer kunt dan anders!"
                #TODO max 1 keer per  dag tijd aftrek. misschien na 2 een nahcte niet slapen?
                $ espresso += 1
                $ tijd = max(0, tijd-2)
                return
            else:
                n "je pakt een dubbele espresso... maar dit is duidelijk teveel..."
                n "de rest van de dag ben je enorm hyper en van werken komt er niet veel meer terecht"
                scene civ
                n "als je naar huis gaat komt er ook niets van slapen terecht"
                n "je blijft de hele nacht om Civilazation VI te spelen"
                n "na het derde spel ga je naar bed"
                $ laat = True
                $ espresso = 0
                jump oudwerknewstyle


        "neem een latte machiatto met lactosevrije amandelmelk en glutenvrije vanille creme":
            n "Sorry robbin. Maar eh. dit lijkt mij echt niet de bedoeling!"
            $ score = 0
            jump gameover

        "neem een warme chocolademelk":
            n "je neemt een warme chocolademelk. heerlijk..."
            return


label toilet:
    scene toilet
    menu:
        "[Location]"
        "kggrrrrgg" if evil > 5:
            n "het gaat niet meer zo goed, of wel MetaRobbin"
            n "je pakt je messen op en wacht tot de volgende persoon op het toilet komt"
            scene toiletblood
            n "zodra de persoon binnenkomt, leef je je uit!"
            n "je voelt je voor het eerst vrij"
            n "wat een heerlijk gevoel..."
            menu:
                "wat wil je doen?"
                "op zoek naar Berend Botje":
                    jump Berend
                "blijf op kantoor":
                    jump kantoor
            return

        "Doe een plasje en ga terug naar kantoor":
            return

        "klaag over het toilet":
            scene baas
            m "die toilet is echt niet te harden..."
            s "welke gebruik je dan?"
            n "je wijst de toilet aan"
            s "oh... deze zou op slot moeten zijn... er zijn hier vroeger rare dingen gebeurd..."
            s "wij gebruiken altijd die andere wc... die is iets beter"
            $ Places[8].IsActive = True


label toilet1:
    scene toilet1
    menu:
        "[Location]"
        "kggrrrrgg" if evil > 3:
            jump toilet

        "Doe een plasje en ga terug naar kantoor":
            n "dit toilet is veel te relaxed..."
            n "je pakt rustig je telefoon erbij en begint te gamen"
            n "na een tijdje... is het genoeg"
            $ tijd += 1
            return


label baas:
    #TODO zaak sluiten na besluit
    scene baas
    menu:
        "wil je een besluit nemen over een casus?"
        "casus 1" if casus1.cas:
            menu:
                "wat wil je besluiten over casus 1"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus1.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer, als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus1.res_used += 1
                    $ casus1.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus1.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus1.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus1.res_used += 1
                    $ casus1.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus1.nogniet = False
                    return
        "casus 2" if casus2.cas:
            menu:
                "wat wil je besluiten over casus 2"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus2.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus2.res_used += 1
                    $ casus2.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus2.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus2.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus2.res_used += 1
                    $ casus2.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus2.nogniet = False
                    return
        "casus 3" if casus3.cas:
            menu:
                "wat wil je besluiten over casus 3"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus3.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus3.res_used += 1
                    $ casus3.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus3.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus3.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus3.res_used += 1
                    $ casus3.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus3.nogniet = False
                    return
        "casus 4" if casus4.cas:
            menu:
                "wat wil je besluiten over casus 4"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus4.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus4.res_used += 1
                    $ casus4.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus4.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus4.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus4.res_used += 1
                    $ casus4.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus4.nogniet = False
                    return
        "casus 5" if casus5.cas:
            menu:
                "wat wil je besluiten over casus 5"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus5.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus5.res_used += 1
                    $ casus5.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus5.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus5.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus5.res_used += 1
                    $ casus5.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus5.nogniet = False
                    return
        "casus 6" if casus6.cas:
            menu:
                "wat wil je besluiten over casus 5"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ casus6.besluit = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus6.res_used += 1
                    $ casus6.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus6.nogniet = False
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ casus6.besluit = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ casus6.res_used += 1
                    $ casus6.cas = False
                    $ afgerond += 1
                    $ open -= 1
                    $ casus6.nogniet = False
                    return

        "aangeven dat je teveel werk hebt":
            m "Hallo baas, ik kom nauwelijks aan mijn werk toe, ik moet echt werk laten vallen"
            s "goed dat je dat aangeeft MetaRobbin! wat wil je laten vallen?"
            jump minderwerk
        "terug naar kantoor":
            return

label archief:
    scene archief
    menu:
        "Je bent in het [Location]. Welke zaak wil je inzien?"
        "casus 1" if casus1.cas:
            n "[casus1.aanv_bel]\n[casus1.aanv_data]\n[casus1.school_bel]\n[casus1.school_data]\n[casus1.vertaling]\n\n[casus1.besluit]"
            jump archief
        "casus 2" if casus2.cas:
            n "[casus2.aanv_bel]\n[casus2.aanv_data]\n[casus2.school_bel]\n[casus2.school_data]\n[casus2.vertaling]\n\n[casus2.besluit]"
            jump archief
        "casus 3" if casus3.cas:
            n "[casus3.aanv_bel]\n[casus3.aanv_data]\n[casus3.school_bel]\n[casus3.school_data]\n[casus3.vertaling]\n\n[casus3.besluit]"
            jump archief
        "casus 4" if casus4.cas:
            n "[casus4.aanv_bel]\n[casus4.aanv_data]\n[casus4.school_bel]\n[casus4.school_data]\n[casus4.vertaling]\n\n[casus4.besluit]"
            jump archief
        "casus 5" if casus5.cas:
            n "[casus5.aanv_bel]\n[casus5.aanv_data]\n[casus5.school_bel]\n[casus5.school_data]\n[casus5.vertaling]\n\n[casus5.besluit]"
            jump archief
        "casus 6" if casus6.cas:
            n "[casus6.aanv_bel]\n[casus6.aanv_data]\n[casus6.school_bel]\n[casus6.school_data]\n[casus6.vertaling]\n\n[casus6.besluit]"
            jump archief

        "terug naar kantoor":
            return


label kantoor:
    #backbone van freeroam. kantoormap
    if tijdperdag < 1:
        jump timereset
    if dag == teltimer:
        $ Places[3].IsActive = True
    if dag == zoektimer:
        $ Places[7].IsActive = True
    scene black
    while dag < 15:
        while tijd < tijdperdag:
            $ resuse = casus1.res_used + casus2.res_used + casus3.res_used + casus4.res_used + casus5.res_used + casus6.res_used
            $ kosten = informatie + (vert * 5)
            $ Location = renpy.call_screen("MapScreen", _layer="screens")
            if Location == "archief":
                call archief
            if Location == "toilet":
                call toilet
            if Location == "koffieapparaat":
                call koffieapparaat
            if Location == "mail":
                call mail
            if Location == "telefoon":
                call telefoon
            if Location == "baas":
                call baas
            if Location == "informatiepunt":
                call informatiepunt
            if Location == "toilet1":
                call toilet1
            #TODO vrijemiddag

        call eventpicker
    jump oudwerknewstyle

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
#TODO rusland casus, 2 russische casussen in bouwen (revocation?)
#TODO gevolgen rusland inbouwen (minder werk...)

    $ toekomstcas += 1
    image rus = im.Scale("nf rusland.png", 1920,1080)
    show rus
    play sound "audio/newsflash.mp3"
    n "Je hoort in de ochtend op het nieuws dat alles uit Rusland geboycot moet worden. Je denkt nog, dat heeft met mij niet zoveel te maken"
    stop sound
    n "maar als je op het werk komt: "
    scene teammeeting
    s "welkom allemaal op deze ingelaste teammeeting"
    s "zoals jullie misschien hebben gehoord, moeten we alle aanvragen vanuit rusland blokeren op dit moment."
    s "Ik wil dat jullie halve dagen hieraan besteden totdat het klaar is"
    "betekent dit alle diplomas van scholen uit rusland? of alle russen?"
    s "dat is een goede vraag MetaRobbin!"
    s "als we alle diplomas blokkeren hebben we de kans dat we mensen onterecht uitsluiten"
    s "als we alle diplomas handmatig gaan controlen betekent dat een force extra werkdruk"
    menu:
        s "wat stel je voor?"
        "alle diploma's van scholen uit rusland blokeren":
            $ tijdperdag -= 1
            s "laten we dat maar doen dan. Vanaf nu besteden jullie allemaal 1 tijd per dag aan rusland"
            $ rus = True
            jump kantoor
        "alle russen blokeren":
            $ tijdperdag -= 2
            s "laten we dat maar doen dan. Vanaf nu besteden jullie allemaal 2 tijd per dag aan rusland"
            $ rus = True
            $ rusblock = True
            jump kantoor
    return

label toekomstcasus2:
#inhollandcasus

        image fraude = im.Scale("nf fraude.png", 1920,1080)
        show fraude
        play sound "audio/newsflash.mp3"
        #TODO newsflash hoge school is niet betrouwbaar meer... zeker 100 diplomas ongeldig
        $ toekomstcas += 1
        n "Hogeschool heeft onterecht diplomas uitgegeven. Eerste onderzoeken wijzen uit dat zeker 100 diplomas ongeldig zijn."
        n "Gevolgen onbekend en DUO is nog niet bereikbaar"
        m "dat zal wel weer een teamoverleg worden..."
        stop sound
        scene teammeeting
        s "welkom allemaal op deze ingelaste teammeeting"
        s "zoals jullie misschien hebben gehoord, is er een school die onterecht diplomas heeft uitgekeerdkeren op dit moment."
        s "voor nu houden we alle aanvragen van deze school tegen. maar we moeten ook kijken naar de oude aanvragen"
        s "iemand een idee hoe we dit het beste op kunnen lossen?"
        menu:
            "alle aanvragen opnieuw bekijken":
                s "dat kan. betekent wel een enorme bak extra werk..."
                menu:
                    "weet je het zeker?"
                    "Ja":
                        $ tijdperdag -= 1
                        $ hol = True
                        jump kantoor
                    "Nee, we kunnen beter wachten op de ongeldige diploma's":
                        $ foutediplomas = True
                        jump kantoor

            "voorlopig niets en wachten op de ongeldige diplomas":
                s "ja dat klinkt goed... alleen wat als iemand dat ongeldige diploma gebruikt?"
                s "dat gaat ons problemen opleveren..."
                menu:
                    "weet je het zeker?"
                    "Ja":
                        $ foutediplomas = True
                        jump kantoor
                    "Nee, we kunnen beter alles checken":
                        $ tijdperdag -= 1
                        jump kantoor
        return

label toekomstcasus3:
#TODO casus vernieuwen
    show stentor_krant
    play sound "audio/ontbijt.mp3"
    $ toekomstcas += 1
    n "'s Ochtends, tijdens het ontbijt, lees je de krant"
    m "Lockdown in apeldoorn... apenpokken..."
    m "zal wel niets met ons te maken hebben... "
    stop sound
    scene teammeeting
    s "welkom allemaal op deze ingelaste teammeeting"
    s "zoals jullie misschien hebben gehoord, is er een apenpokken uitbraak in Apeldoorn."
    s "nou kregen wij het verzoek om zo snel mogelijk te impact te bepalen van dit virus"
    s "MetaRobbin, wil jij snel uitzoeken of dit impact heeft en wat voor impact?"
    $ apel = True
    $ tijdperdag -= 1
    jump kantoor
    return

label timereset:
#te druk op de afdeling
    image drukte = im.Scale("nf drukte.png", 1920,1080)
    show drukte
    play sound "audio/newsflash.mp3"
    n "nog voor je bent begonnen met de dag voelt het al alsof de dag voorbij is..."
    n "de drukte wordt te groot met al die zaken die je moet afhandelen"
    scene baas
    s "wat wil je doen, MetaRobbin?"
    s "volgens mij heb je teveel op je bordje liggen..."
    jump minderwerk

label minderwerk:
    menu:
        "Je moet echt dingen los laten... Maar welke?"
        "laat het russische werk voorlopig maar liggen" if rus:
            s "okay, dan doen we dat. ik hoop dat het een beetje scheelt"
            $ rus = False
            $ rusnot = True
            if rusblock:
                $ tijdperdag += 2
                jump kantoor
            else:
                $ tijdperdag += 1
                jump kantoor

        "doe de appenpokken maar even niet" if apel:
            s "sorry, MetaRobbin... dat kan niet... ik moet echt een antwoord hebben op deze vraag"
            s "of heb je inmiddels een antwoord?"
            menu:
                "Wat zijn de gevolgen voor appenpokken?"
                "Er zijn geen gevolgen":
                    $ apel = False
                    $ tijdperdag += 1
                    jump kantoor
                "we moeten alle diplomas uit apeldoorn stoppen op dit moment":
                    $ apel = False
                    $ apelnot = True
                    $ tijdperdag += 1
                    jump kantoor
                "ik weet het nog niet":
                    jump minderwerk

        "stop met de handmatige afhandeling van de afgekeurde school" if hol:
            s "okay, dan doen we dat. ik hoop dat het een beetje scheelt"
            $ tijdperdag -= 1
            $ hol = False
            $ foutediplomas = True
            $ holnot = True
            jump kantoor


    return

######################################################################################################################
# kantoor scherm

screen MapScreen():
    frame:
        #xalign 0.0
        #yalign 0.0
        #xsize 1920
        #ysize 1080
        background "kantoor.png"
        frame:
            background Solid("#C0C0C0")
            vbox:
                    text "{color=#000000}Tijd: [dag]:[tijd] ([tijdperdag]){/color}"
                    text "{color=#000000}{b}Zaken{/b}"
                    text "{color=#000000}open: [open]"
                    text "{color=#000000}afgerond: [afgerond]"
                    text "{color=#000000}{b}Resources{/b} "
                    text "{color=#000000}budget: [budget]"
                    text "{color=#000000}kosten: [kosten]"
                    text "{color=#000000}gebruikt: [resuse]"
        for q in Places:
            if q.IsActive:
                imagebutton:
                    xpos q.x
                    ypos q.y
                    #text q.name
                    hover q.avatar
                    idle q.avatar
                    action Return(q.name)

screen score_screen():
    frame:
        background Solid("#C0C0C0")
        vbox:
                text "{color=#000000}Tijd: [dag]:[tijd]/[tijdperdag]{/color}"
                text "{color=#000000}{b}Zaken{/b}"
                text "{color=#000000}open: [open]"
                text "{color=#000000}afgerond: [afgerond]"
                text "{color=#000000}{b}Resources{/b} "
                text "{color=#000000}budget: [budget]"
                text "{color=#000000}kosten: [kosten]"
                text "{color=#000000}gebruikt: [resuse]"



