label room2:

    scene room 2 with dissolve
    $ timer += 1
    "A disturbing sight shows itself."

    label room2menu:
        scene room 2 with dissolve
        menu:
            "Rotate Right":
                jump room3
            
            "Rotate Left":
                jump room1
            
            "Inspect This Area":
                scene room 2 with dissolve:
                        zoom 1.2
                "You want to inspect {i}this{/i} area?"
                thinking "..."
                "But they're staring at me..."
                thinking "..."
                "...Fine, but I only ask you this because I absolutely have to."
                "{b}What Strikes You?{/b}"
                menu:
                    "The Bobbed Sponge":
                        "Ugh, why would you pick that one?"
                        thinking "..."
                        "No, I don't like cartoons. Thank you for asking."
                        "In fact, I don't like fiction in general."
                        "Why watch something false when there's something much more interesting and much more real before my very eyes?"
                        thinking "..."
                        "Oh yes, there's you as well, I suppose."
                        "Moving on, was there any point in looking at that vile creature in more detail?"
                        "No?"
                        "No."
                        "Good."
                        if not (persistent.bobbed_sponge):
                            $ persistent.bobbed_sponge = True
                            $ striking_checker.add_progress(1)

                    "The Obtuse Mushroom":
                        "I do hope the irony of you calling anything obtuse is not lost on you, because it certainly isn't on me."
                        "...Though, I do see where you're coming from..."
                        "I'm not even sure how you came up with a mushroom, I'm only getting the \"obtuse\" part."
                        "It's very clearly a creature of some sort..."
                        "And its lacking of appendages is quite saddening."
                        thinking "..."
                        "Oh, right, you wanted to look at the creature."
                        "If you're looking for a good cry, then go on ahead."
                        thinking "..."
                        "...Quite sad indeed."
                        if not (persistent.obtuse_mushroom):
                            $ persistent.obtuse_mushroom = True
                            $ striking_checker.add_progress(1)

                    "The Spiked Sphere":
                        "It is an odd thing indeed."
                        "For what reason one would be compelled to own such a thing is further beyond me than its existence in the first place."
                        "Of course, don't tell me why."
                        "This would be much less interesting if you did."
                        "Speaking of less interesting, you seem to be doing something of that very nature at this moment."
                        "What are you doing?"
                        thinking "..."
                        "Counting?"
                        "I didn't realize I was so... Unenthralling..."
                        "To you personally, anyway."
                        "What are you counting?"
                        thinking "..."
                        "The spines?"
                        "...At least it's related... Not that I understand why you're doing such a thing."
                        "..."
                        "Fine, I'll come out and ask it. Why are you counting the spines of that creature?"
                        menu:
                            "Don't Tell":
                                "Really now...?"
                                "Well, I won't convince you."
                                "And want to know why I won't convince you?"
                                "I won't convince you because..."
                                "I'm."
                                "Not."
                                "Telling."
                            "Lie":
                                "You're counting them because... You think you'll be surprised...?"
                                "Are you daft?"
                                thinking "..."
                                "Fine, if you insist so much, I'll count with you."
                                "1"
                                "2"
                                "3"
                                "4"
                                "5"
                                "6"
                                "7"
                                "..."
                                "..."
                                "..."
                                "Please find some new hobbies."
                                $ spiked_sphere_2 = True 
                        if not (persistent.spiked_sphere):
                            $ persistent.spiked_sphere = True
                            $ striking_checker.add_progress(1)

    jump room2menu

    return