#file met alle telefoon activietien tijdens de frearoma
# aanvrager opbellen en scholen opbellen

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
