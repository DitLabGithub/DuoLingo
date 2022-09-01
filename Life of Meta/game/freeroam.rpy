#TODO teammeeting als resources te hoog worden, misschien een manier blokken? of geen info meer opvragenvoor 2 dagen wegens drukt?
#TODO goedbezig label vervangen...
#TODO liveevents plaatjes fixen
#TODO plaatjes werk fixen
#TODO ikomende opdrachten goed afsluiten
#TODO nieuwe casussen in het oude stoppen
#TODO functioneringsgesprek
#TODO botje over school... school bestaat niet...

label werk:
# intro naar werk. alleen eerste keer
    stop music
    scene duogroot
    with fade

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

    "Je bent aangenomen bij Duo op de personeelszaken en je wordt rondgeleid door Sylvie"

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

    scene ontbijttafel
    show screen score_screen()
    if laat:
        n "Geen tijd voor ontbijt, je moet gaan..."
        n "veel te laat kom je aan op werk en je ziet Sylvie al staan"
        scene baas
        with dissolve
        s "Dat is niet goed MetaRobbin."
        s "Voor deze keer zie ik het door de vingers..."
        s "Ik verwacht beter van je. Nu snel aan het werk"
        $ tijd = 1
        $ dag += 1
        $ laat = False
        jump kantoor

    else:
        default Location = "kantoor"
        n "tijd om op te staan. Koffie en ontbijt en je favoriete krant terwijl op de achtergrond het nieuws aanstaat"
        $ tijd = 0
        $ dag += 1
        n "na het ontbijt ga je naar kantoor"

        #if dag == 3 or dag == 6 or dag == 9 or dag == 12:
        if dag > 0 and dag % 3 == 0:
            #functioneringsgesprek
            scene baas
            s "Hallo MetaRobbin, het is tijd voor je periodieke functioneringsgesprek"
            if budget < kosten and teveelinfo:
                s "ik heb 2 dingen met je te bespreken"
                s "De AIVD vraagt zich af waarom je extra informatie hebt opgevraagd over Cor van Hout"
                s "Deze informatie heb jij niet nodig voor het bepalen van de geldigheid van een diploma..."
                s "sorry MetaRobbin, maar dit levert een aantekening op in je dossier"
                s "daarnaast lopen de kosten behoorlijk uit de hand."
                s "je moet echt snellere beslissingen nemen door minder resources te gebruiken. probeer wat slimmere keuzes te maken"
                s "gelukkig heb ik nog een beetje budget kunnen krijgen, maar gebruik het niet allemaal gelijk"
                $ budget += 5
                $ teveelinfo == False
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

        else:
            #$ rng = 5
            #$ rng1 = 1
            if dag == teltimer:
                $ Places[3].IsActive = True
            if dag == zoektimer:
                $ Places[7].IsActive = True

            $ rng = renpy.random.randint (1,10)
            $ rng1 = renpy.random.randint (1,2)
            if rng == 5:
                scene teammeeting
                s "welkom allemaal op de teammeeting"

                if rng1 == 1 and teltimer >= 200:
                     #afdeling zoeken voor x dagen
                    s "we hebben te horen gekregen dat de informatiediensten afdeling het werk niet meer aan kan"
                    s "het gevolg is dat vanaf morgen ze even geen nieuwe opdrachten meer oppakken"
                    s "houdt er rekening mee met je werk"
                    s "Rondvraag..."
                    s "Niemand? okay, dan maar weer aan het werk!"
                    #$ Places[7] = Place(25,375, "informatiepunt", False)
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
                    #$ Places[3] = Place(1650,550, "telefoon", False)
                    $ Places[3].IsActive = False
                    $ teltimer = dag + 3
                    jump kantoor
                s "vandaag hebben we niets meer te bespreken"
                jump kantoor
            else:
                # teveel gebruik van rss door speler
                jump kantoor

label badending:
    jump oudwerknewstyle

label goedbezig:
    return


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
            n "je pakt een dubbele espresso. zoveel caffiene. het lijkt erop of je vandaag meer kunt dan anders!"
            #TODO max 1 keer per  dag tijd aftrek. misschien na 2 een nahcte niet slapen?
            $ tijd += -1
            return

        "neem een latte machiatto met lactosevrije amandelmelk en glutenvrije vanille creme":
            n "Sorry robbin. Maar eh. dit lijkt mij echt niet de bedoeling!"
            $ score = 0
            jump oudwerknewstyle

        "neem een warme chocolademelk":
            n "je neemt een warme chocolademelk. heerlijk..."
            return


label toilet:
    scene toilet
    menu:
        "[Location]"
        "kggrrrrgg":
            return

        "Doe een plasje en ga terug naar kantoor":
            return

label mail:
    scene mail
    menu:
        "je gaat zitten achter je bureau en logt in je computer..."
        "inkomende opdrachten":
            menu:
                "welke zaak wil je openen?"
                "zaak 1" if casus1.cas == False:
                    show dip1
                    n "je krijgt een diploma in handen van aanvrager B. Botje. Hij is van een Nederlandsche school Danzig"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus1.cas = True
                    $ tijd += 1
                    hide dip1
                    $ open += 1
                    return
                "zaak 2" if casus2.cas == False:
                    show dip2
                    n "je krijgt een diploma in handen van aanvrager Yang Xinhai. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus2.cas = True
                    $ tijd += 1
                    hide dip2
                    $ open += 1
                    return
                "zaak 3" if casus3.cas == False:
                    show dip3
                    n "je krijgt een diploma in handen van aanvrager Marco B.. Hij is van Rood, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus3.cas = True
                    $ tijd += 1
                    hide dip3
                    $ open += 1
                    return
                "zaak 4" if casus4.cas == False:
                    show dip4
                    n "je krijgt een diploma in handen van aanvrager Lin Shanshan. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus4.cas = True
                    $ tijd += 1
                    hide dip4
                    $ open += 1
                    return
                "zaak 5" if casus5.cas == False:
                    show dip5
                    n "je krijgt een diploma in handen van aanvrager Cor van Hout. Het diploma komt van het Flipper college, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus5.cas = True
                    $ tijd += 1
                    $ open += 1
                    hide dip5
                    return
                "zaak 6" if casus6.cas == False:
                    show dip6
                    n "je krijgt een diploma in handen van aanvrager Willem van Eijk. Hij is van de Driespan en in het Nederlands"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus6.cas = True
                    $ tijd += 1
                    $ open += 1
                    hide dip6
                    return

        "vertaling aanvragen":
            menu:
                "welk diploma wil je laten vertalen?"
                "zaak 1" if casus1.cas:
                    show dip1
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ casus1.vertaling = "De vertaling is aangevraagd"
                    hide dip1
                    $ tijd += 1
                    $ casus1.vertklaar = dag + 1
                    $ casus1.res_used += 1
                    $ vert += 1
                    return
                "zaak 2" if casus2.cas:
                    show dip2
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    hide dip2
                    $ casus2.vertaling = "De vertaling is aangevraagd"
                    $ tijd += 1
                    $ casus2.vertklaar = dag + 1
                    $ casus2.res_used += 1
                    $ vert += 1
                    return
                "zaak 3" if casus3.cas:
                    show dip3
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ casus3.cas = True
                    hide dip3
                    $ casus3.vertaling = "De vertaling is aangevraagd"
                    $ tijd += 1
                    $ casus3.vertklaar = dag + 1
                    $ casus3.res_used += 1
                    $ vert += 1
                    return
                "zaak 4" if casus4.cas:
                    show dip4
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ casus4.cas = True
                    $ casus4.vertaling = "De vertaling is aangevraagd"
                    hide dip4
                    $ casus4.vertklaar = dag + 1
                    $ casus4.res_used += 1
                    $ vert += 1
                    return
                "zaak 5" if casus5.cas:
                    show dip5
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ casus5.cas = True
                    $ casus5.vertaling = "De vertaling is aangevraagd"
                    hide dip5
                    $ casus5.vertklaar = dag + 1
                    $ casus5.res_used += 1
                    $ vert += 1
                    return
                "zaak 6" if casus6.cas:
                    show dip6
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ casus6.cas = True
                    $ casus6.vertaling = "De vertaling is aangevraagd"
                    hide dip6
                    $ casus6.vertklaar = dag + 1
                    $ casus6.res_used += 1
                    $ vert += 1
                    return

        "spam":
            n "moet nog worden uitgewerkt"
            #TODO spam uitwerken
            return

        "vertalingen inzien":
            menu:
                "zaak 1" if dag == casus1.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ casus1.vertklaar = 1200
                    $ casus1.vertaling = "Dit diploma is in het Nederlands"
                    return

                "zaak 2" if dag == casus2.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "Het was niet makkelijk, maar dit diploma is vertaald vanuit het Chinees. De school heet Zhengheng Middle School en het lijkt erop dat hij voor slager heeft geleerd "
                    $ tijd += 1
                    $ casus2.vertklaar = 1200
                    $ casus2.vertaling = "Dit diploma is vertaald naar het Nederlands, afkomstig van de Zhengheng Middle School. Richting: Slager "
                    $ casus2.vert is True
                    return

                "zaak 3" if dag == casus3.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ casus3.vertklaar = 1200
                    $ casus3.vertaling = "Dit diploma is in het Nederlands"
                    return

                "zaak 4" if dag == casus4.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "Dit diploma komt van Sun Yat Sen University en de richting is tekenen of kunst"
                    $ tijd += 1
                    $ casus4.vertklaar = 1200
                    $ casus4.vertaling = "Dit diploma is vertaald naar het Nederlands, afkokmstig van Sun Yat-Sen University, en ze heeft tekenen of kunst afgerond"
                    $ casus4.vert is True
                    return

                "zaak 5" if dag == casus5.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ casus5.vertklaar = 1200
                    $ casus5.vertaling = "Dit diploma is in het Nederlands"
                    return

                "zaak 6" if dag == casus6.vertklaar:
                    n "je opent de mail van de vertaler"
                    ve "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ casus6.vertklaar = 1200
                    $ casus6.vertaling = "Dit diploma is in het Nederlands"
                    return

                "terug naar kantoor":
                    return


label telefoon:
    scene telefoon
    menu:
        "je bent bij de [Location]. Je kunt hier aanvragers en scholen bellen."
        "Aanvrager opbellen":
            menu:
                "Welke aanvrager wil je bellen?"
                "B. Botje van de eerste zaak" if casus1.cas and casus1.aanv_belb == False:
                    play sound "audio/bellen.mp3"
                    n "je belt B. Botje"
                    stop sound
                    "met Berend!"
                    m "Hallo, je spreekt met MetaRobbin van DUO, ik heb een paar vragen over je aanvraag, komt dat uit"
                    "natuurlijk! zeg het maar"
                    $ tijd += 1
                    $ casus1.res_used += 1
                    menu:
                        "Wat wil je vragen?"
                        "vraag naar school" if casus1.schoolinfo:
                            m "ik kan de school niet vinden in onze database. dat betekend dat ik dit diploma niet kan verwerken"
                            "school niet vinden? wat raar... ik heb er toch jaren op gezeten..."
                            m "we hebben ook niemand anders kunnen vinden die ooit op deze school heeft gezeten"
                            "haha.. ehm.. ja... MetaRobbin toch?"
                            m "hmm ja."
                            "ik weet waar je woont... "
                            m "wat probeer je te zeggen"
                            "niets, maar ik ga ervan uit dat het diploma verwerkt wordt!"
                            n "Je hangt snel op en roept Sylvie"
                            s "wat is er aan de hand?"
                            m "Deze persoon heeft een vals diploma ingestuurd van een niet bestaande school en nu probeert hij mij te dwingen om het te verwerken."
                            s "OH? dat is niet best..."
                            s "ik bel security. Dan kan deze persoon worden opgepakt. gelukkig slaan we alle gespreken op"
                            s "zullen we deze zaak dan maar afwijzen? "
                            m "Lijkt me een goed idee, dank je, Baas"
                            $ casus1.besluit = "je hebt deze zaak afgewezen"
                            s "geen probleem, MetaRobbin! goed werk!"
                            $ casus1.aanv_bel = "je hebt gebeld en bent bedreigd door de aanvrager"
                            $ casus1.aanv_belb = True
                            return
                        "vraag naar de school" if casus1.schoolinfo == False:
                            m "Welke school heb je gezeten?"
                            "op een school in Zuidlaren, vernoemd naar een Boot van een zeevaarder, Danzig. niet te verwaren met de plaats of de band natuurlijk..."
                            m "ah ik snap het"
                            "maar dat staat toch op het diploma?"
                            m "ja klopt... de school kwam me alleen niet bekend voor, maar dat ligt aan mij denk ik"
                            $ casus1.aanv_bel = "De aanvrager is gebeld en zegt dat hij van de school Danzig komt"
                            m "bedankt voor de info, ik ga ermee aan de slag"
                            "geen probleem, succes!"
                            $ casus1.aanv_belb = True
                            return
                        "je hebt niets te vragen":
                            m "ehm nee laat maar, ik moet eerst wat anders onderzoeken"
                            "geen probleem"
                            return

                "Yang Xinhai van de tweede zaak" if casus2.cas and casus2.aanv_belb == False:
                    play sound "audio/bellen.mp3"
                    n "je laat de telefoon over gaan en hoort een stem aan de andere kant van de lijn"
                    stop sound
                    "Nǐ hǎo"
                    n "je legt uit wat je wilt"
                    "Wǒ bù míngbái"
                    n "de persoon verstaat geen Nederlands en lijkt alleen Chinees te spreken"
                    n "teleurgesteld hang je weer op"
                    $ casus2.aanv_bel = "Yang Xinhai spreekt geen Nederlands"
                    $ casus2.aanv_belb == True
                    $ tijd += 1
                    $ casus2.res_used += 1
                    return

                "Marco B. van de derde zaak" if casus3.cas and casus3.aanv_belb == False:
                    play sound "audio/bellen.mp3"
                    n "de telefoon gaat over en er neemt iemand op"
                    stop sound
                    "ben jij dit weer Leontien! ik heb toch al gezegd dat ik je nooit meer hoef te zien..."
                    m "Hallo Marco, je spreekt met metarobbin van DUO"
                    "ehm... oh. ja, wat wil je?"
                    m "u heeft een aanvraag gedaan voor het goedkeuren van een diploma?"
                    "eh dat zou kunnen, ja. hoezo?"
                    m "ik zou graag een paar vragen willen stellen over het diploma"
                    "kan dat een andere keer. ik heb het enorm druk"
                    m "maar natuurlijk, ik bel bin..."
                    n "tuut tuut tuut en opgehangen... het heeft niet veel zin om weer te bellen"
                    $ casus3.aanv_bel = "Marco B. heeft geen tijd voor uitleg"
                    $ casus3.aanv_belb = True
                    $ tijd += 1
                    $ casus3.res_used += 1
                    return

                "Lin Shanshan van de vierde zaak" if casus4.cas and casus4.aanv_belb == False:
                     play sound "audio/bellen.mp3"
                     n "je laat de telefoon over gaan en hoort een stem aan de andere kant van de lijn"
                     stop sound
                     "Nǐ hǎo"
                     n "je legt uit wat je wilt"
                     "Wǒ bù míngbái"
                     n "de persoon verstaat geen Nederlands en lijkt alleen Chinees te spreken"
                     n "teleurgesteld hang je weer op"
                     $ casus4.aanv_bel = "Lin Shanshan spreekt geen Nederlands"
                     $ casus4.aanv_belb = True
                     $ tijd += 1
                     $ casus4.res_used += 1
                     return

                "Cor van Hout van de vijfde zaak" if casus5.cas and casus5.aanv_belb == False:
                    play sound "audio/bellen.mp3"
                    n "je belt en de telefoon gaan over"
                    stop sound
                    "hallo?"
                    m "Hallo Cor? je spreekt met metarobbin van DUO"
                    "ja dit is Cor, wat kan ik voor je doen?"
                    $ tijd += 1
                    $ casus5.res_used += 1
                    menu:
                        "Wat wil je vragen?"
                        "vraag naar de school" if school5info:
                            m "ik zie dat je heb gestudeerd aan Flipper college?"
                            "ja dat klopt"
                            m "in 1981?"
                            "ja dat zou kunnen"
                            m "toen bestond die school nog niet"
                            "niet? oh ehm"
                            m "ik denk..."
                            n "tuut tuut tuut"
                            $ casus5.aanv_bel = "Je hebt Cor gesproken, maar hij hangt steeds op"
                            $ casus5.aanv_belb = True
                            return
                        "vraag naar de school" if school5info is False:
                            m "ik zie dat je heb gestudeerd aan Flipper college?"
                            "ja dat klopt"
                            m "in 1981?"
                            "ja dat zou kunnen"
                            m "ah okay, dan weet ik genoeg, bedankt!"
                            "geen probleem, doeg!"
                            n "tuut tuut tuut"
                            $ casus5.aanv_bel = "Je hebt Cor gesproken, en hij bevestigd dat hij op die school heeft gezeten"
                            $ casus5.aanv_belb = True
                            return
                        "je hebt niets te vragen":
                            m "nou eigenlijk niets"
                            "oh, geen probleem, doeg!"
                            n "tuut tuut tuut"
                            $ casus5.aanv_bel = "Je hebt Cor gesproken, en hij heeft niets gezegd"
                            $ casus5.aanv_belb = True
                            return

                "Bel Willem van Eijk van zaak 6" if casus6.cas and casus6.aanv_belb == False:
                    play sound "audio/bellen.mp3"
                    n "je belt en de telefoon gaan over"
                    stop sound
                    "hallo?"
                    m "Spreek ik met Willem? je spreekt met metarobbin van DUO"
                    "ja dit is Willem, ik ben nogal druk... wat wil je?"
                    $ tijd += 1
                    m "je hebt een aanvraag gedaan voor een diploma goedkeuring"
                    "ja is daar een probleem mee? het was al zwaar genoeg om dat ding te halen..."
                    m "nee voorlopig ziet het er goed uit"
                    "okay dan, ik ga weer verder"
                    n "tuut, tuut, tuut"
                    $ casus6.aanv_bel = "Je hebt Willem gesproken, maar het was weinig zinvol"
                    $ casus6.aanv_belb = True
                    $ casus6.res_used += 1
                    return


        "Scholen opbellen":
            menu:
                "Welke school wil je bellen?"
                "Danzig van zaak 1" if casus1.cas:
                    n "Je zoekt het nummer op van de school maar kan het niet vinden..."
                    $ tijd += 1
                    $ casus1.res_used += 1
                    $ casus1.school_bel = "De school heeft geen telefoonnummer"
                    return


                "Zhengheng Middle School van zaak 2" if casus2.cas and casus2.vert:
                    $ tijd += 1
                    $ casus2.res_used += 1
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    "Nǐ hǎo zhè shì Zhengheng Middle School"
                    n "helaas... alleen Chinees..."
                    n "gelukkig heb je de naam van de school gehoord, je weet alleen niet of de school dit diploma heeft uitgegeven"
                    $ casus2.school_bel = "De school bestaat, maar je kunt niet achterhalen of dit diploma is uitgegeven"
                    return


                "Rood van zaak 3" if casus3.cas:
                    $ tijd += 1
                    $ casus3.res_used += 1
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    "Rood"
                    m "Hallo, je spreekt met MetaRobbin van DUO"
                    "Hallo Robbin, wat kan ik voor je doen?"
                    m "heb je informatie over Marco B. en een diploma dat hij bij jullie heeft gehaald?"
                    "oh dat weet ik nog goed... ik snap niet dat hij ooit geslaagd is..."
                    "hij was meer bezig met z'n soort van zangcarriere... "
                    "nooit studeren, nooit aan het werk... alleen lage cijfers.."
                    "Als je het mij vraagt heeft hij wat mensen hier omgekocht om dat diploma te krijgen"
                    "maar ja, wie ben ik"
                    m "dus jullie hebben dat diploma uitgegeven?"
                    "oh ja... awkward... maar toch gedaan..."
                    "ik kan je nog wel meer vertellen.. "
                    m "oh dat is niet nodig hoor, bedankt"
                    "maar..."
                    m "tot ziens!"
                    n "en je hangt snel op voor deze persoon nog langer doorpraat..."
                    $ casus3.school_bel = "De school bestaat en heeft dit diploma uitgegeven"
                    return

                "San Yat-Sen University van zaak 4" if casus4.cas and casus4.vert:
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    n "je krijgt iemand aan de lijn maar deze persoon heeft nog nooit gehoord van deze school..."
                    $ casus4.school_bel = "De school bestaat niet onder het telefoon nummer dat je kreeg"
                    $ tijd += 1
                    $ casus4.res_used += 1
                    return


                "Flipper collega van zaak 5" if casus5.cas:
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    "Hallo Flipper College, je spreekt met Andrea"
                    m "hallo Andrea, je spreekt met MetaRobbin van DUO"
                    "Hallo Meta, wat kan ik voor je doen?"
                    m "ik bel over een aanvraag voor een diploma die we hebben gekregen van jullie school"
                    "mag ik de naam en de datum?"
                    m "ja de datum is 27 juni 1983 en de naam is... "
                    "dat is raar, toen bestonden we nog niet"
                    m "u bestond nog niet op die datum?"
                    "nee toen heten we Suzy College "
                    m "oh dan weet ik voldoende denk ik, ontzettend bedankt!"
                    "geen probleem, Meta!"
                    n "tuut tuut tuut"
                    $ casus5.school_bel = "De school bestond niet op de datum het diploma werd uitgereikt"
                    $ tijd += 1
                    $ casus5.res_used += 1
                    return

                "driespan van zaak 6" if casus6.cas:
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    "Hoi, je spreekt met de Driespan, met Mike"
                    m "hallo Mike, dit is MetaRobbin van DUO"
                    "hoi MetaRobbin, wat kan ik voor je doen?"
                    m "ik wil graag wat informatie over een diploma van Willem van Eijk"
                    "een momentje"
                    "ah hier, ja die hebben wij uitgegeven."
                    m "mooi, dat is alles wat ik wilde weten, bedankt"
                    "geen probleem!"
                    n "tuut, tuut, tuut"
                    $ casus6.school_bel = "De school heeft het diploma uitgereikt"
                    $ tijd += 1
                    $ casus6.res_used += 1
                    return

                "terug naar het kantoor":
                    return


        "terug naar kantoor":
            return

label informatiepunt:

    scene informatiepunt
    menu:
        "waarover wil je informatie?"
        "danzig school van zaak 1" if casus1.cas:
            $ tijd += 1
            $ casus1.res_used += 1
            n "het systeem kan deze school niet vinden"
            $ casus1.school_data = "De school kan niet gevonden worden door het systeem"
            $ informatie += 1
            return

        "B. Botje van zaak 1" if casus1.cas:
            $ tijd += 1
            $ casus1.res_used += 1
            n "Er is niet bijzonders te vinden over deze persoon"
            $ casus1.aanv_data = "Er is niet bijzonders te vinden over B. Botje"
            $ informatie += 1
            return

        "Zhengheng Middle School van zaak 2" if casus2.cas:
            $ tijd += 1
            $ casus2.res_used += 1
            n "het systeem  heeft deze school gevonden en bestond ook toen het diploma is uitgegeven"
            $ casus2.school_data = "De school bestaat en kan het diploma hebben uitgegeven"
            $ informatie += 1
            return

        "Yang Xinhai van zaak 2" if casus2.cas:
            $ tijd += 1
            $ casus2.res_used += 1
            n "Deze persoon komt niet voor in onze database"
            $ casus2.aanv_data = "Er is niet te vinden over Yang Xinhai"
            $ informatie += 1
            return

        "Rood College van zaak 3" if casus3.cas:
            $ tijd += 1
            $ casus3.res_used += 1
            n "Deze school bestond in de periode dat het diploma is uitgegeven"
            $ casus3.school_data = "De school bestaat en bestond toen het diploma werd uitgegeven"
            $ informatie += 1
            return

        "Marco B. van zaak 3" if casus3.cas:
            $ tijd += 1
            $ casus3.res_used += 1
            n "We zien wat vreemde activiteiten bij deze persoon"
            n "hij heeft op dit moment geen VoG"
            n "er loopt een onderzoek voor geweld tegen een ander persoon"
            $ casus3.aanv_data = "Marco B. heeft geen VoG en er loopt een onderzoek voor geweld"
            $ informatie += 1
            return

        "San Yat-Sen University van zaak 4" if casus4.cas:
            $ tijd += 1
            $ casus4.res_used += 1
            n "Het systeem kan niets vinden over deze school"
            $ casus4.school_data = "De school bestaat niet"
            $ informatie += 1
            return

        "Lin Shanshan van zaak 4" if casus4.cas:
            $ tijd += 1
            $ casus4.res_used += 1
            n "Deze persoon komt niet voor in onze database"
            $ casus4.aanv_data = "Er is niet te vinden over Lin Shanshan"
            $ informatie += 1
            return

        "Flipper College van zaak 5" if casus5.cas:
            $ tijd += 1
            $ casus5.res_used += 1
            n "De school bestaat, maar kan het diploma niet hebben uitgegeven"
            $ casus5.school_data = "De school bestaat, maar niet tijdens het moment van diploma uitgifte"
            $ informatie += 1
            return

        "Cor van Hout van zaak 5" if casus5.cas:
            $ tijd += 1
            $ casus5.res_used += 1
            n "Deze persoon komt voor in onze database"
            n "Er staat een vlag bij, maar kunnen niets meer vinden"
            $ informatie += 1

            menu:
                "wil je meet informatie opvragen over deze persoon?"
                "Ja":
                    #TODO meer info... tricky hier...
                    n "je vraagt de gegevens op van de AIVD en krijgt het gehele strafblad te zien van Cor"
                    $ casus5.aanv_data = "Cor heeft een enorm strafblad"
                    $ casus5.res_used += 1
                    $ informatie += 5
                    $ teveelinfo = True
                    return
                "Nee":
                    $ casus5.aanv_data = "Cor heeft een vlag bij zijn naam"
                    return
            return

        "driespan school van zaak 6" if casus6.cas:
            $ tijd += 1
            $ casus6.res_used += 1
            n "Deze school bestond in de periode dat het diploma is uitgegeven"
            $ casus6.school_data = "De school bestond ten tijde van uitgifte van het diploma"
            $ informatie += 1
            return

        "Willem van Eijk van zaak 6" if casus6.cas:
            $ tijd += 1
            $ casus6.res_used += 1
            n "Er is niet bijzonders te vinden over deze persoon"
            $ casus6.aanv_data = "Er is niet bijzonders te vinden over Willem van Eijk"

            $ informatie += 1
            return

        "terug naar kantoor":
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
                    return

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


label kantoor: #backbone van freeroam
    scene black
    while dag < 10:
        while tijd < 5:
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
            #TODO vrijemiddag

        call eventpicker
    jump oudwerknewstyle





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
                    text "{color=#000000}Tijd: [dag]:[tijd]{/color}"
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
                text "{color=#000000}Tijd: [dag]:[tijd]{/color}"
                text "{color=#000000}{b}Zaken{/b}"
                text "{color=#000000}open: [open]"
                text "{color=#000000}afgerond: [afgerond]"
                text "{color=#000000}{b}Resources{/b} "
                text "{color=#000000}budget: [budget]"
                text "{color=#000000}kosten: [kosten]"
                text "{color=#000000}gebruikt: [resuse]"



