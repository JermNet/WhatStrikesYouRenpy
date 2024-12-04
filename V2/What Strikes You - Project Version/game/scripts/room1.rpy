label room1:
    
    # The scene keywords means we're going to display a background image, meaning that it overwrites sprites and other backgrounds. It looks for pngs and jpgs in the "images" folder, and to call a background to be shown, you write the name after scene, including spaces, but not including file type. Images files must also be all lower case. A transition can be specified using the "with" key word after the file name, and then the built in transition.
    scene room 1 with dissolve
    $ timer += 1

    # Music can be played much in the same way that scenes and sprites can, the biggest difference being that the file does have to be specified, including the path if it's not in the root of the "audio" folder. A fadein/fadeout can be specified after the file name, as well as volume. You can also play "sound" and "voice" with the three together basically serving as 3 different audio channels.
    if not (renpy.music.is_playing('music')):
        play music "cresent moon tsukihime.mp3" fadein 0.5

    "An unusual sight shows itself."
    
    # Ths is a menu, aka Ren'Py's version of an if statement. It determines what code belongs to what based on the indents and colons, and despite how it looks, they can be nested no problem. The choices are also displayed on the screen near the center, with exact location depending on the number of choices.
    label room1menu:
        scene room 1 with dissolve
        menu:
            "Rotate Right":
                jump room2
            
            "Rotate Left":
                jump room4
            
            "Inspect This Area":
                # A colon after a statement indicates doing something a bit more advanced, in this case, a zoom.
                scene room 1 with dissolve:
                    zoom 1.2
                "I'm not sure what could interest you in an area such as this, but I'll still ask..."
                "{b}What Strikes You?{/b}"
                menu:
                    "The Oblong Stick":
                        "It's a stick that's... Oblong..."
                        "It's likely used for something, but whatever that something is probably not very important."
                        "The striking factor is shockingly low, in fact."
                        if not (persistent.oblong_stick):
                            $ persistent.oblong_stick = True
                            $ striking_checker.add_progress(1)
                    
                    "The Misused Canister":
                        "The world cannot comprehend such irony..."
                        "Is what I would say if using misusing canisters to contain rubbish was an uncommon practice."
                        "Seriously though, you'll get rats if you don't empty that thing."
                        "I hate rats."
                        "Rats."
                        "Raaaaats..."
                        "Mice are much better."
                        "They're skiddish, so worse case they just steal some of your cheese."
                        "People don't keep rats as pets for a reason."
                        "Wait, do they?"
                        "Hmm..."
                        menu:
                            "I'm sure they do":
                                "Well, you've just gone and ruined my day."
                                "It wasn't going great anyway, but you've just made it worse."
                                "Ugh, rats..."
                                "You know what? Maybe you do have rats and you don't even know."
                                "Maybe someone who has rats wants to pet them?"
                                "Hmm?"
                                "Is that what you want? To pet your rats in your little rat rubbish bin?"
                                
                                # To use characters, just write the variable name before the text in quotes.
                                thinking "..."
                                "Go on, it's not a retorical question."
                                menu:
                                    "Oooh, rats!":
                                        $ misused_canister_2 = True
                                        "...You're serious?"
                                        "Oh, {i}that{/i} look..."
                                        "You are serious..."
                                        "Don't tell me you're going to reach..."
                                        "Into..."
                                        "There..."
                                        "Great..."
                                        "Well, at least there are no rats in there."
                                        "Did you even get anything out of that experience other than potential disease?"
                                        "Oh? A piece of paper?"
                                        "Out of sick, {b}sick{/b} curiosity, what's on it?"
                                        thinking "..."
                                        "Let's see... \"I hate the direction clocks go! All 4 of them, I hate it!\""
                                        thinking "..."
                                        "I guess we all have something we hate..."
                                        "Though, mine is far less... Disturbing..."
                                    
                                    "Eeew, rats!":
                                        "Thank goodness."
                                        "If you really mean that, make sure you clean that out soon."
                            
                            "If they do, I don't want to meet them":
                                "My thoughts exactly."
                                "If you really mean that, make sure you clean that our before you don't want to meet yourself."
                        if not (persistent.misused_canister):
                            $ persistent.misused_canister = True
                            $ striking_checker.add_progress(1)
                    
                    "The Imprisoned Case":
                        "It's a locked case of some sort... Yours, I presume."
                        "Something's screaming at me that you don't, but I think it polite to ask."
                        "Do you remember the combination?"
                        menu:
                            "Most likely":
                                "I would have prefered a yes, but go ahead. It's four numbers, right?"
                                $ code = renpy.input("What is the combination?")
                                
                                if code.isdigit():
                                    $ code = int(code)
                                    if code == 3874:
                                        if not misused_canister_2 or not spiked_sphere_2 or not to_leave_2 or not piggy_bank_2:
                                            $ cheater.grant()
                                        "Hmm, my apologies for underestimating the capabilities of your memory."
                                        "That's to say, you've cracked it."
                                        "What's so important to you that you've decided to lock it away in the first place?"
                                        thinking "..."
                                        "What?"
                                        "Care to repeat that so I know I'm understanding you correctly?"
                                        thinking "..."
                                        "A... And I quote... \"Clicky button\"?"
                                        "Not something of value?"
                                        "Not something that means something?"
                                        "Not something embarassing?"
                                        "Not something disturbing?"
                                        "But a... \"Clicky button\"?"
                                        thinking "..."
                                        "You say it {i}is{/i} something of value?"
                                        "Even if we're not talking monetary, I still find that more than hard to believe."
                                        "...I suppose if you truly mean that, you'll decide to prove it at some point..."
                                        "I do hope I live another 50 years."
                                        $ found_music = True

                                    else:
                                        "You know, this would have been much less embarassing if you had answered honestly."
                                        "Much less of a waste of time, as well."
                                        "Either way, you don't know the combination and that's really all that matters at the end of the day."
                                        "Actually, for all I know, what's in there is useless, that might not even matter."
                                        "Whatever the case, I'm sure that if you want what's in there, you'll find a way to get it."
                                else:
                                    "How does one even put that in a numeric combination?"
                                    "The least you could do is pull just one leg instead of both."
                            
                            "Probably not":
                                "I had figured as much."
                                "Well, at least you're being honest about it."
                                "Much better than making a fool of yourself if you ask me."
                                "Anyway, if you'd like to get into that case, don't ask me."
                                "I'm sure you've got something or other around here to remember what the combination is, at least."
                        if not (persistent.imprisoned_case):
                            $ persistent.imprisoned_case = True
                            $ striking_checker.add_progress(1)
                jump room1menu

    return