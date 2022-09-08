# file met alle informatiepunt vanuit de freeroam. scholen en aanvragers

label informatiepunt:

    scene informatiepunt
    menu:
        "waarover wil je informatie?"
        "danzig school van zaak 1" if casus1.cas:
            $ tijd += 1
            $ casus1.res_used += 1
            n "het systeem kan deze school niet vinden"
            $ casus1.school_data = "De school kan niet gevonden worden door het systeem"
            $ casus1.schoolinfo = True
            $ informatie += 1
            return

        "B. Botje van zaak 1" if casus1.cas:
            $ tijd += 1
            $ casus1.res_used += 1
            n "Er is niet bijzonders te vinden over deze persoon"
            $ casus1.aanv_data = "Er is niet bijzonders te vinden over B. Botje"
            $ informatie += 1
            return

        "Zhengheng Middle School van zaak 2" if casus2.cas and casus2.vert:
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

        "San Yat-Sen University van zaak 4" if casus4.cas and casus2.vert:
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