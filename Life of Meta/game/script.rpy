# Declare characters used by this game.
#sylvie
define s = Character(_("Sylvie"), image="sylvie", color="#c8ffc8")
image side sylvie = "sylvie blue normal.png"
#TODO plaatje vertaler
define ve = Character(_("Vertaler"), color="#c8ffc8")

#metarobbin
define m = Character(_("MetaRobbin"), color="#c8c8ff")
define kid = Character(_("[kidname]"), color="#c8c8ff")

#metamindy en metamama
#TODO plaatje metamama
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
#TODO receptionist
define receptionist = Character(_("receptionist"), image="sylvie1", color="#c8ffc8")
image side sylvie1 = im.Scale("sylvie green normal.png", 400, 700)
define a = Character(_("Ambtenaar"), image="sylvie", color="#c8ffc8")
image side sylvie = "sylvie blue normal.png"
image side sylvie surprised = "sylvie blue surprised.png"
image side sylvie giggle = "sylvie blue giggle.png"
image side sylvie smile = "sylvie blue smile.png"

#narrator
define n = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="images/n_bg.png", what_color="#ddd")
# define text = Character(None, what_style="centered_text", window_style="centered_window", window_xfill=True, window_yfill=True, window_background="images/n_bg.png", what_color="#ddd")

#images
image balie = im.Scale("counter.png", 1920,1080)
## image stadhuis = im.Scale("Stadhuis.jpg", 1920,1080)
image ditlablogo = im.Scale("46.png", 1920,500)
image ma = im.Scale("mindy.png", 400, 700)
image pa = im.Scale("s1-normal.png", 400, 700)

#image balie = im.Scale("balie.png", 1920,1080)

#random score die overal gebruikt kan worden
default rng = 1
default rng1 = 1
#werkscore voor hoe goed je werk doet
default score = 15
#score om te bepalen of je een booster hebt of niet
default booster = False
#score om te bepalen welk event je hebt afgerond zodat je doorgaat in het leven
default lasteventnr = 1
default toekomstevent = 1
#score om de toekomst in te gaan
default toestemming = False
#espresso score
default espresso = 0
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
default rusblock = False
default rusnot = False
default hol = False
default holnot = False
default apel = False
default apelnot = False
#variabelen voor teammeeting:
default teltimer = 1000
default zoektimer = 1000
#variabelen voor werkoud
default teveelinfo = False
default laat = False
default tijd = 1
default tijdperdag = 5

default dag = 0
#variabelen voor de score
default open = 0
default afgerond = 0
default kosten = 0
default resuse = 0
default budget = 15
default vert = 0
default informatie = 0
default foutediplomas = False
default aantekening = 0
default evil = 0
default mes = False

default casus1 = Casus()
default casus2 = Casus()
default casus3 = Casus()
default casus4 = Casus()
default casus5 = Casus()
default casus6 = Casus()

label start:

    jump born
return


label Alleenwerk:
#TODO weer opnieuw inbouwen na nieuwe werkwijze
        # "alleen de werkcasussen":
            $ werk = True

            jump werk


label test:
    jump toekomstbaan

return



label toekomstbaan:
#TODO koppelen aan nieuwe werkwijze
    scene baas
    with dissolve

    n "Je hebt het verder uitgedacht en denkt dat het werk een stuk simpeler kan worden door een blockchain"
    n "Zodra je op het werk bent plan je een overleg in met Sylvie"
    m "Hoi Sylvie, ik heb een idee. Wil je dat met mij bespreken?"
    s "Natuurlijk MetaRobbin, zeg het maar!"
    m "Je weet dat we iedere keer die diplomas controleren, terwijl veel van dat werk makkelijker kan."
    m "Wat nou als we alle diploma's die uitgegeven worden door een betrouwbare school goed keuren"
    m "Dan hoeven we een heleboel diplomas niet meer te controleren, alleen de moeilijke gevallen waarbij iemand de boel probeert te flessen of de gevallen waarbij we de school niet kennen"
    m "De persoon krijgt dan het diploma in zijn prive wallet."
    m "en als ze die dan nodig hebben, versturen ze die gewoon, of eigenlijk alleen datgene wat nodig is"
    s surprised "Ik snapte niet helemaal hoe dat ging... maar denk je dat dit kan werken?"
    m "Ja, ik kreeg het idee van de consentual-app"
    n "MetaRobbin kleurt gelijk rood..."
    s giggle "Oh ja, die ken ik wel... Dat is toch waar je toestemming geeft?"
    m "Ja die! Nou precies zo eigenlijk, maar in plaats van toestemming, geef je je diploma tijdelijk aan iemand anders."
    scene wallet1
    m "kijk zo werkt het ongeveer. zodra je slaagt voor je diploma kun je je diploma ophalen van de school"
    m "je bent dan zelf eigenaar van je diploma en mag ermee doen wat je wilt."
    m "wij noemen dat een verifiable credential"
    m "maar als je hem nodig hebt, kun je die tijdelijk aan iemand laten zien"
    s surprised "maar wie vertrouwt dat dan? je kunt toch zelf ook gewoon iets in die wallet zetten?"
    scene wallet2
    m "ja dat kan wel, maar dat heeft niet dezelfde waarde als ons diploma"
    m "wij gaan namelijk bijhouden wie betrouwbaar zijn en diplomas mogen uitgeven in een zogenaamd trusted issuer register"
    m "dus deze school is een trusted issuer"
    s - surprised "ah dat is handig... "
    s "maar hoe werkt het dan als je je diploma wilt laten zien?"
    scene wallet3
    m "kijk, als een bedrijf wil weten wat deze persoon hebt gedaan, dan geeft de persoon toestemming"
    m "in dit geval van zijn afstudeerrichting, dus ook niet het hele diploma"
    m "en het bedrijf weet dat het kan vertrouwen op de gegevens omdat het gekoppeld is aan een Trusted Issuer"
    s "maar die wallet? hoe werkt dat dan?"
    #TODO scene phonewallet
    m "kijk, hier zie je wat de gegevens zijn van die persoon van een diploma"
    m "als je een verzoek krijgt van dat bedrijf, kun je gewoon uitvinken wat je niet wilt laten zien"
    m "en vervolgens stuur je het op naar het bedrijf en kunnen zij er voor een bepaalde periode je gegevens inzien"
    s smile "oh wat een goed idee MetaRobbin!"
    s "wat voor werk hebben we dan nog over?"
    m "wij moeten beoordelen of scholen betrouwbaar zijn."
    m "als we eerst beginnen met publieke scholen uit nederland, dan hebben we het grootste gedeelte van ons register al klaar"
    m "voor de buitenlandse scholen moet we nog wat bedenken..."


    $ lasteventnr +=1
    jump randomtoekomstcasus
    return

label gameover:
    scene gameover
    pause
    return




label credits:
    "sounds from soundjay.com and pixabay.com"

#TODO Plaatjes niet goed
#TODO      Vertaling verduidelijking
#TODO      Functioneren ipv te laat...
#TODO      Achtergrond bij datenight
#TODO      Bij zaken opened terug
#TODO      Vertaling dag te laat openen
#TODO      Leukv tikfout
#TODO      Teveel werk bij te weinig casussen
#TODO      Einde casussen...