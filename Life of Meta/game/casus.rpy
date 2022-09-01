init -1 python:
    class Casus:
        def __init__(self):
            self.cas = False
            self.aanv_bel = "De aanvrager is nog niet gebeld"
            self.aanv_belb = False
            self.aanv_data = "Er zijn nog geen gegevens opgevraagd van de aanvrager"
            self.school_bel = "De school is nog niet gebeld"
            self.school_data = "Er zijn nog geen extra gegevens bekend van de school"
            self.vertaling = "Dit diploma is nog niet vertaald"
            self.besluit = "Je hebt nog geen besluit genomen"
            self.vertklaar = 100
            self.schoolinfo = False
            self.vert = False
            self.res_used = 0


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

