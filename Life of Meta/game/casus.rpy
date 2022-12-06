init python:
    class Casus:
        def __init__(self):   #, cas, aanv_bel, aanv_belb, aanv_data, school_bel, school_data, vertaling, besluit, vertklaar, schoolinfo, vert, res_used
            self.cas = False    ## casus is gesloten (false) of open (true)
            self.aanv_bel = "De aanvrager is nog niet gebeld"  ##aanvrager notitie voor het bellen
            self.aanv_belb = False ##aanvrager is gebeld of niet
            self.aanv_data = "Er zijn nog geen gegevens opgevraagd van de aanvrager"  ##aanvrager notitie over opvragen gegevens
            self.school_bel = "De school is nog niet gebeld" ##school notitie bij bellen
            self.school_data = "Er zijn nog geen extra gegevens bekend van de school" ##school notitie bij informatie aanvraag
            self.vertaling = "Dit diploma is nog niet vertaald" ##vertalings notitie van diploma
            self.besluit = "Je hebt nog geen besluit genomen" ##besluit genomen of niet
            self.nogniet = True  #als false, dan is de casus afgesloten en komt niet meer terug
            self.vertklaar = 1000 #optie voor vertaling klaar. 100 is extreem nummer, wordt naar dag berekend als speler op vertaling aanvrager klikt
            self.schoolinfo = False #schoolinfo is aangevraagd bij true
            self.vert = False #vertaling is aangevraagd bij true
            self.res_used = 0 #resources gebruikt. wordt gebruikt voor totale berekening

#    self.started_translating = None
#    self.saw_translation = False

# def start_translating(self, dag):
#     self.started_translating = dag
#
# def started_translating(self):
#     return self.started_translating is not None
#
# def is_translated(self, current_dag):
#     if self.started_translating is None:
#         return False
#     return self.started_translating > current_dag
#
# def view_translation(self):
#     self.saw_translation = True
#
# def has_viewed_translation(self):
#     return self.saw_translation

init python:
    config.developer = True
    config.console = True
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
    Places[8] = Place(1700,700, "toilet1", False)

