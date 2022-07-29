# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("MetaRobbin"), color="#c8c8ff")
define v = Character(_("MetaMindy"), color="#a23af9")

#random score die overal gebruikt kan worden
default rng = 4
#werkscore voor hoe goed je werk doet
default score = 5
#score om te bepalen of je een booster hebt of niet
default booster = False
#score om te bepalen welk event je hebt afgerond zodat je doorgaat in het leven
default lasteventnr = 1
#score om de toekomst in te gaan
default toestemming = False

label start:

    menu:
        "ga naar werk spel":

            jump werk

        "begin metas leven":

            jump born

        "naar de toekomst van meta":

            jump toekomst

        "test events":

            jump covidevent
    return

label born:

    #geboorte van meta robin voorstellen van mama en papa meta...
    #aangifte van meta robin bij de gemeente
    #inschrijven meta bij een school
    #àanmelden voor stex met beperking
    #aanmelden stufi

    "dit zijn metapapa en metamama."

    "metamama staat op het punt om te bevallen en hiermee begint jouw leven."

    "je vernoemen je naar je overgrootvader en vanaf nu heet je MetaRobin"

    "natuurlijk moet je eerst aangemeld worden bij de gemeente om je registraties op orde te maken... "

    return


label afgestudeerd:

    jump werk

label toekomst:

    # moet nog verder uitgewerkt worden...
   scene gameover
   with fade
   return



label werk:

    # Start by playing some music.
    # play music "illurock.opus"

    scene duogroot
    with fade
    "Welkom bij Life of Meta!"

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

    jump intro

    return




label toekomstbaan:

    scene black
    with dissolve

    #andere baan...
    "Je hebt het verder uitgedacht en denkt dat het werk een stuk simpeler kan worden door een blockchain"
    "Zodra je op het werk bent plan je een overleg in met Sylvie"
    m "Hoi Sylvie, ik heb een idee. Wil je dat met mij bespreken?"
    s "Natuurlijk MetaRobbin, zeg het maar!"
    m "Je weet dat we iedere keer die diplomas checken, terwijl veel van dat check werk makkelijker kan."
    m "Als we die diplomas opvragen, via een wallet, die de personen hebben gekregen van de school."
    m "Dan hoeven we een heleboel diplomas niet meer te controleren, alleen de moeilijke gevallen waarbij iemand de boel probeert te flessen"
    s "Ik snapte niet helemaal hoe dat ging... maar denk je dat dit kan werken?"
    m "Ja, ik kreeg het idee van de consentual-app"
    m "Ehm... "
    "MetaRobbin kleurt gelijk rood..."
    s "Oh ja, die ken ik wel... Dat is toch waar je toestemming geeft?"
    m "Ja die! Nou precies zo eigenlijk, maar in plaats van toestemming, geef je je diploma tijdelijk."
    s "Oh dat is slim... Wat mij betreft mag je daarmee bezig! Dan hoef je de komende tijd geen diploma's te checken. "
    #nieuwe casus bouwen op de nieuwe manier!f

    jump eventpicker
    return

