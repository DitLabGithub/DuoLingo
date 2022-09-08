#file met alle activiteiten van het bureau in de freeroam.
# nieuwe opdrachten
# vertaalopdracht
# spam
# lezen van vertaling

label mail:
    scene mail
    menu:
        "je gaat zitten achter je bureau en logt in je computer..."
        "inkomende opdrachten":
            menu:
                "welke zaak wil je openen?"
                "zaak 1" if casus1.cas == False and casus1.nogniet:
                    show dip1
                    n "je krijgt een diploma in handen van aanvrager B. Botje. Hij is van een Nederlandsche school Danzig"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus1.cas = True
                    $ tijd += 1
                    hide dip1
                    $ open += 1
                    return
                "zaak 2" if casus2.cas == False and casus2.nogniet:
                    show dip2
                    n "je krijgt een diploma in handen van aanvrager Yang Xinhai. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus2.cas = True
                    $ tijd += 1
                    hide dip2
                    $ open += 1
                    return
                "zaak 3" if casus3.cas == False and casus3.nogniet:
                    show dip3
                    n "je krijgt een diploma in handen van aanvrager Marco B.. Hij is van Rood, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus3.cas = True
                    $ tijd += 1
                    hide dip3
                    $ open += 1
                    return
                "zaak 4" if casus4.cas == False and casus4.nogniet:
                    show dip4
                    n "je krijgt een diploma in handen van aanvrager Lin Shanshan. Je kunt het diploma niet lezen"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus4.cas = True
                    $ tijd += 1
                    hide dip4
                    $ open += 1
                    return
                "zaak 5" if casus5.cas == False and casus5.nogniet:
                    show dip5
                    n "je krijgt een diploma in handen van aanvrager Cor van Hout. Het diploma komt van het Flipper college, een Nederlandsche school"
                    n "vanaf nu kun je informatie vergaren over deze aanvraag"
                    $ casus5.cas = True
                    $ tijd += 1
                    $ open += 1
                    hide dip5
                    return
                "zaak 6" if casus6.cas == False and casus6.nogniet:
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
