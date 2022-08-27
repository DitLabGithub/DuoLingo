label oudwerknewstyle:
    default Location = "kantoor"
    n "tijd om op te staan. Koffie en ontbijt en je favoriete krant terwijl op de achtergrond het nieuws aanstaat"
    $ tijd = 0
    $ dag += 1
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
            n "je pakt een dubbele espresso. zoveel caffiene. het lijkt erop of je vandaag meer kunt dan anders!"
            #TODO max 1 keer per  dag tijd aftrek. misschien na 2 een nahcte niet slapen?
            $ tijd += -1
            return

        "neem een latte machiatto met lactosevrije amandelmelk en glutenvrije vanille creme":
            n "Sorry robbin. Maar eh. dit lijkt mij echt niet de bedoeling!"
            $ score = 0
            jump badending

        "neem een warme chocolademelk":
            n "je neemt een warme chocolademelk. heerlijk..."
            return


label toilet:
    scene toilet
    menu:
        "[Location]"
        "keuze1":
            return

        "kezue2":
            return

label mail:
    scene mail
    menu:
        "je gaat zitten achter je bureau en logt in je computer..."
        "inkomende opdrachten":
            menu:
                "welke zaak wil je openen?"
                "zaak 1" if cas1 == False:
                    show dip1
                    n "je krijgt een diploma in handen van aanvrager B. Botje. Hij is van een Nederlandsche school Danzig"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas1 = True
                    $ tijd += 1
                    hide dip1
                    return
                "zaak 2" if cas2 == False:
                    show dip2
                    n "je krijgt een diploma in handen van aanvrager Yang Xinhai. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas2 = True
                    $ tijd += 1
                    hide dip2
                    return
                "zaak 3" if cas3 == False:
                    show dip3
                    n "je krijgt een diploma in handen van aanvrager Marco B.. Hij is van Rood, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas3 = True
                    $ tijd += 1
                    hide dip3
                    return
                "zaak 4" if cas4 == False:
                    show dip4
                    n "je krijgt een diploma in handen van aanvrager Lin Shanshan. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas4 = True
                    $ tijd += 1
                    hide dip4
                    return
                "zaak 5" if cas5 == False:
                    show dip5
                    n "je krijgt een diploma in handen van aanvrager Cor van Hout. Het diploma komt van het Flipper college, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas5 = True
                    $ tijd += 1
                    hide dip5
                    return
                "zaak 6" if cas6 == False:
                    show dip6
                    n "je krijgt een diploma in handen van aanvrager Willem van Eijk. Hij is van de Driespan en in het Nederlands"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ cas6 = True
                    $ tijd += 1
                    hide dip6
                    return

        "vertaling aanvragen":
            menu:
                "welk diploma wil je laten vertalen?"
                "zaak 1" if cas1:
                    show dip1
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ cas1 = True
                    $ vertaling1 = "De vertaling is aangevraagd"
                    hide dip1
                    $ tijd += 1
                    $ vert1klaar = dag + 1
                    $ res_used1 += 1
                    return
                "zaak 2" if cas2:
                    show dip2
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    hide dip2
                    $ vertaling2 = "De vertaling is aangevraagd"
                    $ tijd += 1
                    $ vert2klaar = dag + 1
                    $ res_used2 += 1
                    return
                "zaak 3" if cas3:
                    show dip3
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ cas3 = True
                    hide dip3
                    $ vertaling3 = "De vertaling is aangevraagd"
                    $ tijd += 1
                    $ vert3klaar = dag + 1
                    $ res_used3 += 1
                    return
                "zaak 4" if cas4:
                    show dip4
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ cas4 = True
                    $ vertaling4 = "De vertaling is aangevraagd"
                    hide dip4
                    $ vert4klaar = dag + 1
                    $ res_used4 += 1
                    return
                "zaak 5" if cas5:
                    show dip5
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ cas5 = True
                    $ vertaling5 = "De vertaling is aangevraagd"
                    hide dip5
                    $ vert5klaar = dag + 1
                    $ res_used5 += 1
                    return
                "zaak 6" if cas6:
                    show dip6
                    n "Je stuurt het diploma op naar een vertaller. Houd je mail in de gaten, want het duurt natuurlijk even voor je een reactie krijgt"
                    $ tijd += 1
                    $ cas6 = True
                    $ vertaling6 = "De vertaling is aangevraagd"
                    hide dip6
                    $ vert6klaar = dag + 1
                    $ res_used6 += 1
                    return

        "spam":
            n "moet nog worden uitgewerkt"
            #TODO spam uitwerken
            return

        "vertalingen inzien":
            menu:
                "zaak 1" if dag == vert1klaar:
                    n "je opent de mail van de vertaler"
                    v "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ vert1klaar = 1200
                    $ vertaling1 = "Dit diploma is in het Nederlands"
                    return

                "zaak 2" if dag == vert2klaar:
                    n "je opent de mail van de vertaler"
                    v "Het was niet makkelijk, maar dit diploma is vertaald vanuit het Chinees. De school heet Zhengheng Middle School en het lijkt erop dat hij voor slager heeft geleerd "
                    $ tijd += 1
                    $ vert2klaar = 1200
                    $ vertaling2 = "Dit diploma is vertaald naar het Nederlands, afkomstig van de Zhengheng Middle School. Richting: Slager "
                    $ vert2 is True
                    return

                "zaak 3" if dag == vert3klaar:
                    n "je opent de mail van de vertaler"
                    v "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ vert3klaar = 1200
                    $ vertaling3 = "Dit diploma is in het Nederlands"
                    return

                "zaak 4" if dag == vert4klaar:
                    n "je opent de mail van de vertaler"
                    v "Dit diploma komt van Sun Yat Sen University en de richting is tekenen of kunst"
                    $ tijd += 1
                    $ vert4klaar = 1200
                    $ vertaling4 = "Dit diploma is vertaald naar het Nederlands, afkokmstig van Sun Yat-Sen University, en ze heeft tekenen of kunst afgerond"
                    $ vert4 is True
                    return

                "zaak 5" if dag == vert5klaar:
                    n "je opent de mail van de vertaler"
                    v "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ vert5klaar = 1200
                    $ vertaling5 = "Dit diploma is in het Nederlands"
                    return

                "zaak 6" if dag == vert6klaar:
                    n "je opent de mail van de vertaler"
                    v "misschien moet je nog een kop koffie nemen... want dit diploma was al in het Nederlands"
                    $ tijd += 1
                    $ vert6klaar = 1200
                    $ vertaling6 = "Dit diploma is in het Nederlands"
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
                "B. Botje van de eerste zaak" if cas1 and aanv_bel1b == False:
                    play sound "audio/bellen.mp3"
                    n "je belt B. Botje"
                    stop sound
                    "met Berend!"
                    m "Hallo, je spreekt met MetaRobbin van DUO, ik heb een paar vragen over je aanvraag, komt dat uit"
                    "natuurlijk! zeg het maar"
                    $ tijd += 1
                    $ res_used1 += 1
                    menu:
                        "Wat wil je vragen?"
                        "vraag naar school" if school1info:
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
                            $ besluit1 = "je hebt deze zaak afgewezen"
                            s "geen probleem, MetaRobbin! goed werk!"
                            $ aanv_bel1 = "je hebt gebeld en bent bedreigd door de aanvrager"
                            $ aanv_bel1b = True
                            return
                        "vraag naar de school" if school1info == False:
                            m "Welke school heb je gezeten?"
                            "op een school in Zuidlaren, vernoemd naar een Boot van een zeevaarder, Danzig. niet te verwaren met de plaats of de band natuurlijk..."
                            m "ah ik snap het"
                            "maar dat staat toch op het diploma?"
                            m "ja klopt... de school kwam me alleen niet bekend voor, maar dat ligt aan mij denk ik"
                            $ aanv_bel1 = "De aanvrager is gebeld en zegt dat hij van de school Danzig komt"
                            m "bedankt voor de info, ik ga ermee aan de slag"
                            "geen probleem, succes!"
                            $ aanv_bel1b = True
                            return
                        "je hebt niets te vragen":
                            m "ehm nee laat maar, ik moet eerst wat anders onderzoeken"
                            "geen probleem"
                            return

                "Yang Xinhai van de tweede zaak" if cas2 and aanv_bel2b == False:
                    play sound "audio/bellen.mp3"
                    n "je laat de telefoon over gaan en hoort een stem aan de andere kant van de lijn"
                    stop sound
                    "Nǐ hǎo"
                    n "je legt uit wat je wilt"
                    "Wǒ bù míngbái"
                    n "de persoon verstaat geen Nederlands en lijkt alleen Chinees te spreken"
                    n "teleurgesteld hang je weer op"
                    $ aanv_bel2 = "Yang Xinhai spreekt geen Nederlands"
                    $ aanv_bel2b == True
                    $ tijd += 1
                    $ res_used2 += 1
                    return

                "Marco B. van de derde zaak" if cas3 and aanv_bel3b == False:
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
                    $ aanv_bel3 = "Marco B. heeft geen tijd voor uitleg"
                    $ aanv_bel3b = True
                    $ tijd += 1
                    $ res_used3 += 1
                    return

                "Lin Shanshan van de vierde zaak" if cas4 and aanv_bel4b == False:
                     play sound "audio/bellen.mp3"
                     n "je laat de telefoon over gaan en hoort een stem aan de andere kant van de lijn"
                     stop sound
                     "Nǐ hǎo"
                     n "je legt uit wat je wilt"
                     "Wǒ bù míngbái"
                     n "de persoon verstaat geen Nederlands en lijkt alleen Chinees te spreken"
                     n "teleurgesteld hang je weer op"
                     $ aanv_bel4 = "Lin Shanshan spreekt geen Nederlands"
                     $ aanv_bel4b = True
                     $ tijd += 1
                     $ res_used4 += 1
                     return

                "Cor van Hout van de vijfde zaak" if cas5 and aanv_bel5b == False:
                    play sound "audio/bellen.mp3"
                    n "je belt en de telefoon gaan over"
                    stop sound
                    "hallo?"
                    m "Hallo Cor? je spreekt met metarobbin van DUO"
                    "ja dit is Cor, wat kan ik voor je doen?"
                    $ tijd += 1
                    $ res_used5 += 1
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
                            $ aanv_bel5 = "Je hebt Cor gesproken, maar hij hangt steeds op"
                            $ aanv_bel5b = True
                            return
                        "vraag naar de school" if school5info is False:
                            m "ik zie dat je heb gestudeerd aan Flipper college?"
                            "ja dat klopt"
                            m "in 1981?"
                            "ja dat zou kunnen"
                            m "ah okay, dan weet ik genoeg, bedankt!"
                            "geen probleem, doeg!"
                            n "tuut tuut tuut"
                            $ aanv_bel5 = "Je hebt Cor gesproken, en hij bevestigd dat hij op die school heeft gezeten"
                            $ aanv_bel5b = True
                            return
                        "je hebt niets te vragen":
                            m "nou eigenlijk niets"
                            "oh, geen probleem, doeg!"
                            n "tuut tuut tuut"
                            $ aanv_bel5 = "Je hebt Cor gesproken, en hij heeft niets gezegd"
                            $ aanv_bel5b = True
                            return

                "Bel Willem van Eijk van zaak 6" if cas6 and aanv_bel6b == False:
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
                    $ aanv_bel6 = "Je hebt Willem gesproken, maar het was weinig zinvol"
                    $ aanv_bel6b = True
                    $ res_used6 += 1
                    return


        "Scholen opbellen":
            menu:
                "Welke school wil je bellen?"
                "Danzig van zaak 1" if cas1:
                    n "Je zoekt het nummer op van de school maar kan het niet vinden..."
                    $ tijd += 1
                    $ res_used1 += 1
                    $ school_bel1 = "De school heeft geen telefoonnummer"
                    return


                "Zhengheng Middle School van zaak 2" if cas2 and vert2:
                    $ tijd += 1
                    $ res_used2 += 1
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    "Nǐ hǎo zhè shì Zhengheng Middle School"
                    n "helaas... alleen Chinees..."
                    n "gelukkig heb je de naam van de school gehoord, je weet alleen niet of de school dit diploma heeft uitgegeven"
                    $ school_bel2 = "De school bestaat, maar je kunt niet achterhalen of dit diploma is uitgegeven"
                    return


                "Rood van zaak 3" if cas3:
                    $ tijd += 1
                    $ res_used3 += 1
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
                    $ school_bel3 = "De school bestaat en heeft dit diploma uitgegeven"
                    return

                "San Yat-Sen University van zaak 4" if cas4 and vert4:
                    play sound "audio/bellen.mp3"
                    n "je belt met de school"
                    stop sound
                    n "je krijgt iemand aan de lijn maar deze persoon heeft nog nooit gehoord van deze school..."
                    $ school_bel4 = "De school bestaat niet onder het telefoon nummer dat je kreeg"
                    $ tijd += 1
                    $ res_used4 += 1
                    return


                "Flipper collega van zaak 5" if cas5:
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
                    $ school_bel5 = "De school bestond niet op de datum het diploma werd uitgereikt"
                    $ tijd += 1
                    $ res_used5 += 1
                    return

                "driespan van zaak 6" if cas6:
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
                    $ school_bel6 = "De school heeft het diploma uitgereikt"
                    $ tijd += 1
                    $ res_used6 += 1
                    return

                "terug naar het kantoor":
                    return


        "terug naar kantoor":
            return

label informatiepunt:

    scene informatiepunt
    menu:
        "waarover wil je informatie?"
        "danzig school van zaak 1" if cas1:
            $ tijd += 1
            $ res_used1 += 1
            n "het systeem kan deze school niet vinden"
            $ school_data1 = "De school kan niet gevonden worden door het systeem"
            return

        "B. Botje van zaak 1" if cas1:
            $ tijd += 1
            $ res_used1 += 1
            n "Er is niet bijzonders te vinden over deze persoon"
            $ aanv_data1 = "Er is niet bijzonders te vinden over B. Botje"
            return

        "Zhengheng Middle School van zaak 2" if cas2:
            $ tijd += 1
            $ res_used2 += 1
            n "het systeem  heeft deze school gevonden en bestond ook toen het diploma is uitgegeven"
            $ school_data2 = "De school bestaat en kan het diploma hebben uitgegeven"
            return

        "Yang Xinhai van zaak 2" if cas2:
            $ tijd += 1
            $ res_used2 += 1
            n "Deze persoon komt niet voor in onze database"
            $ aanv_data2 = "Er is niet te vinden over Yang Xinhai"
            return

        "Rood College van zaak 3" if cas3:
            $ tijd += 1
            $ res_used3 += 1
            n "Deze school bestond in de periode dat het diploma is uitgegeven"
            $ school_data3 = "De school bestaat en bestond toen het diploma werd uitgegeven"
            return

        "Marco B. van zaak 3" if cas3:
            $ tijd += 1
            $ res_used3 += 1
            n "We zien wat vreemde activiteiten bij deze persoon"
            n "hij heeft op dit moment geen VoG"
            n "er loopt een onderzoek voor geweld tegen een ander persoon"
            $ aanv_data3 = "Marco B. heeft geen VoG en er loopt een onderzoek voor geweld"
            return

        "San Yat-Sen University van zaak 4" if cas4:
            $ tijd += 1
            $ res_used4 += 1
            n "Het systeem kan niets vinden over deze school"
            $ school_data4 = "De school bestaat niet"
            return

        "Lin Shanshan van zaak 4" if cas4:
            $ tijd += 1
            $ res_used4 += 1
            n "Deze persoon komt niet voor in onze database"
            $ aanv_data4 = "Er is niet te vinden over Lin Shanshan"
            return

        "Flipper College van zaak 5" if cas5:
            $ tijd += 1
            $ res_used5 += 1
            n "De school bestaat, maar kan het diploma niet hebben uitgegeven"
            $ school_data5 = "De school bestaat, maar niet tijdens het moment van diploma uitgifte"
            return

        "Cor van Hout van zaak 5" if cas5:
            $ tijd += 1
            $ res_used5 += 1
            n "Deze persoon komt voor in onze database"
            n "Er staat een vlag bij, maar kunnen niets meer vinden"

            menu:
                "wil je meet informatie opvragen over deze persoon?"
                "Ja":
                    #TODO meer info... tricky hier...
                    n "je vraagt de gegevens op van de AIVD en krijgt het gehele strafblad te zien van Cor"
                    $ aanv_data5 = "Cor heeft een enorm strafblad"
                    $ res_used5 += 1
                    return
                "Nee":
                    $ aanv_data5 = "Cor heeft een vlag bij zijn naam"
                    return
            return

        "driespan school van zaak 6" if cas6:
            $ tijd += 1
            $ res_used6 += 1
            n "Deze school bestond in de periode dat het diploma is uitgegeven"
            $ school_data6 = "De school bestond ten tijde van uitgifte van het diploma"
            return

        "Willem van Eijk van zaak 6" if cas6:
            $ tijd += 1
            $ res_used6 += 1
            n "Er is niet bijzonders te vinden over deze persoon"
            $ aanv_data6 = "Er is niet bijzonders te vinden over Willem van Eijk"
            return

        "terug naar kantoor":
            return

label baas:
    #TODO zaak sluiten na besluit
    scene baas
    menu:
        "wil je een besluit nemen over een casus?"
        "casus 1" if cas1:
            menu:
                "wat wil je besluiten over casus 1"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit1 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer, als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used1 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit1 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used1 += 1
                    return
        "casus 2" if cas2:
            menu:
                "wat wil je besluiten over casus 2"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit2 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used2 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit2 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used2 += 1
                    return
        "casus 3" if cas3:
            menu:
                "wat wil je besluiten over casus 3"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit3 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used3 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit3 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used3 += 1
                    return
        "casus 4" if cas4:
            menu:
                "wat wil je besluiten over casus 4"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit4 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used4 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit4 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used4 += 1
                    return
        "casus 5" if cas5:
            menu:
                "wat wil je besluiten over casus 5"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit5 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used5 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit5 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used5 += 1
                    return
        "casus 6" if cas6:
            menu:
                "wat wil je besluiten over casus 5"
                "verzoek afwijzen":
                    s "okay, dan wijzen we deze af."
                    m "ja dat lijkt me het beste... het klopt allemaal niet"
                    $ besluit6 = "je hebt deze zaak afgewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used6 += 1
                    return
                "verzoek toewijzen":
                    s "okay, dan wijzen we dit verzoek toe"
                    m "ja, alles is in orde met dit verzoek"
                    $ besluit6 = "je hebt deze zaak toegewezen"
                    s "ik zie je weer als je een andere zaak wilt afhandelen!"
                    $ tijd += 1
                    $ res_used6 += 1
                    return

        "terug naar kantoor":
            return



label archief:
    scene archief
    menu:
        "Je bent in het [Location]. Welke zaak wil je inzien?"
        "casus 1" if cas1:
            n "[aanv_bel1]\n[aanv_data1]\n[school_bel1]\n[school_data1]\n[vertaling1]\n\n[besluit1]"
            jump archief
        "casus 2" if cas2:
            n "[aanv_bel2]\n[aanv_data2]\n[school_bel2]\n[school_data2]\n[vertaling2]\n\n[besluit2]"
            jump archief
        "casus 3" if cas3:
            n "[aanv_bel3]\n[aanv_data3]\n[school_bel3]\n[school_data3]\n[vertaling3]\n\n[besluit3]"
            jump archief
        "casus 4" if cas4:
            n "[aanv_bel4]\n[aanv_data4]\n[school_bel4]\n[school_data4]\n[vertaling4]\n\n[besluit4]"
            jump archief
        "casus 5" if cas5:
            n "[aanv_bel5]\n[aanv_data5]\n[school_bel5]\n[school_data5]\n[vertaling5]\n\n[besluit5]"
            jump archief
        "casus 6" if cas6:
            n "[aanv_bel6]\n[aanv_data6]\n[school_bel6]\n[school_data6]\n[vertaling6]\n\n[besluit6]"
            jump archief

        "terug naar kantoor":
            return


label kantoor:
    while dag < 10:
        while tijd < 5:
            "tijd:[tijd], dag:[dag]"
            #$ Location_img = Location.lower()
            $ Location = renpy.call_screen("MapScreen", _layer="screens")
            #if renpy.has_image(Location_img, exact=True):
            #scene expression Location_img
            #call expression Location_img
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
            #TODO vrijmiddag

        call eventpicker
    jump badending


init python:

    class Place(object):
        def __init__(self, x, y, name, IsActive):
            self.x = x
            self.y = y
            self.name = name
            self.IsActive = IsActive
        @property
        def avatar(self):
            icon = self.name.lower() + "_icon.png"
            return(icon)

    Places = []
    t = 0

    while t < 50:
        Places.append(Place(0,0,"", False))
        t += 1

    Places[0] = Place(680,500, "archief", True)
    Places[1] = Place(350,200, "koffieapparaat", True)
    Places[2] = Place(900,225, "mail", True)
    Places[3] = Place(1650,550, "telefoon", True)
    Places[4] = Place(1900,800, "toilet", True)
    Places[5] = Place(3000,1200, "kantoor", False)
    Places[6] = Place(1650,75, "baas", True)
    Places[7] = Place(25,375, "informatiepunt", True)



screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1000
        background "kantoor.png"
        for q in Places:
            if q.IsActive:
                imagebutton:
                    xpos q.x
                    ypos q.y
                    #text q.name
                    hover q.avatar
                    idle q.avatar
                    action Return(q.name)







