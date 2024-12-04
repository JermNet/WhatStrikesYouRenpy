label endings:

    "...There's no more stalling, is there?"
    "We're going back outdoors now, right?"
    thinking "..."
    "..."
    "Must we?"
    "No, that's a stupid question."
    "I know that look, and I know that means we must."
    "..."
    "I won't be coming with you this time."
    thinking "..."
    "I can't tell you why."
    "Will you go in spite of that?"
    menu:
        "No":
            jump forever

        "Yes":
            "I see..."
            "Hesitation is the the enemy of growth, right?"
            "I'm sure I've said that before, but even if I haven't, I'm proud that you've adhered to it..."
            "Even knowing what that means for me."
            thinking "..."
            "If I tell you, you won't be able to do what you must."
            "I'm sorry..."
            thinking "..."
            "It won't hurt, but only if you listen to my advice."
            "Even if you don't remember anything else, remember this:"
            "Don't look back."
            thinking "..."
            "No, I can't tell you what it means..."
            "But you'll understand, you're smart like that."
            "Goodbye."
            thinking "..."
            "Quite right, goodbyes are often permanent..."
            "See you."
            thinking "..."
            $ renpy.pause(1.5, hard=True)
            scene house 1 with dissolve
            $ renpy.pause(1.5, hard=True)
            scene house 2 with dissolve
            $ renpy.pause(1.5, hard=True)
            while i < loop2:
                $ i += 1
                $ renpy.pause(1.5, hard=True)
                scene walk 1 with dissolve
                "Something makes you."
                menu:
                    "Yes":
                        jump hesitation
                    "No":
                        thinking "..."
                
                $ renpy.pause(1.5, hard=True)
                scene walk 2 with dissolve
                "Something forces you."
                menu:
                    "Yes":
                        jump hesitation
                    "No":
                        thinking "..."
                if i == 2:
                    stop music fadeout 0.5
            $ i = 0
            $ renpy.pause(1.5, hard=True)
            scene walk 4 with dissolve
            $ renpy.pause(1.5, hard=True)
            scene walk 5 with dissolve
            $ renpy.pause(1.5, hard=True)
            scene walk 6 with dissolve
            thinking "..."
            scene black
            $ renpy.pause(1.5, hard=True)
            scene them with Dissolve(3.0)
            $ renpy.pause(3.0, hard=True)
            them "You've done very well."
            them "They were such simple tasks..."
            them "But that doesn't make them easy for everyone, now does it?"
            them "That's okay, you don't have to say anything."
            them "You'll be able to say as much as you want now, and to so many different people."
            them "Good luck out there..."
            them "Though, I'm fairly confident that you won't need it."
            scene black with Dissolve(3.0)
            $ renpy.pause(3.0, hard=True)
            play music "dusk tsukihime.mp3" fadein 3.0
            scene end with Dissolve(3.0)
            $ renpy.pause(3.0, hard=True)
            player "Thank you for taking me here."
            player "...No, thank you for giving me the courage to get here."
            player "...It means a lot."
            player "Thank you."
            $ renpy.pause(3.0, hard=True)
            $ good_ending.grant()
            "Good Ending: Finally Free"
            jump credits

    return

