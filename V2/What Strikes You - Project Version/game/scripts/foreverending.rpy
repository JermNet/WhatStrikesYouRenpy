label forever:
    "It pleases greatly that we can roam this place forevermore."
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ renpy.pause(3.0, hard=True)
    $ bad_ending_1.grant()
    "Bad Ending: The World Will Remain The Same Forevermore"
    jump credits

    return