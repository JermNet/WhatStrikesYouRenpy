label hesitation:
    stop music fadeout 0.5
    $ renpy.pause(1.5, hard=True)
    scene house 3 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene house 1 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene room 3 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene room 2 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene room 1 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene room 4 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene room 3 with dissolve
    $ renpy.pause(1.5, hard=True)
    scene black with Dissolve(3.0)
    $ renpy.pause(3.0, hard=True)
    $ bad_ending_2.grant()
    "Bad Ending: Hesitation Is The Enemy Of Growth"
    jump credits

    return