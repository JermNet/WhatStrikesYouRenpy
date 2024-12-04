label room4:

    scene room 4 with dissolve
    $ timer += 1
    "A nice sight shows itself."

    label room4menu:
        scene room 4 with dissolve        
        menu:
            "Rotate Right":
                jump room1
            
            "Rotate Left":
                jump room3
            
            "Inspect This Area":
                scene room 4 with dissolve:
                    zoom 1.2
                "This is your favourite place, isn't it?"
                "You don't even need to answer, I know it's the case."
                "Don't be shy about it either, just let me ask that one question..."
                "{b}What Strikes You?{/b}"
                menu:
                    "Your Cassette Player":
                        "It's quite the technical marvel, I must admit."
                        "...Despite being more than few decades behind the times."
                        "Though, I ought not say things like that."
                        thinking "..."
                        if found_music == True:
                            if not music:
                                "What are you doing?"
                                thinking "..."
                                "Oh, I see, that \"clicky button\" did serve a purpose after all."
                                "My apologies for my earlier rudeness."
                                "...Though, I do have to ask why you removed the key aspect of functionality of something you cherish so much..."
                                "No, never mind, I know that look. You don't want to talk about it, do you?"
                                thinking "..."
                                "Yes, you're right. I am quite a fan of your music."
                                "Do you have it fixed now?"
                                thinking "..."
                                "Perfect."
                                "What music are you going to play?"
                                menu: 
                                    "Something pleasant":
                                        stop music fadeout 0.5
                                        $ renpy.pause(0.5, hard=True)
                                        play music "captivate tsukihime.mp3" fadein 0.5
                                        $ renpy.pause(1.5, hard=True)
                                        "Yes, this is quite pleasant, isn't it?"
                                        $ music = True
                                
                                "This piece of machinery runs on battery power, does it not?"
                                thinking "..."
                                "My thoughts exactly. Let's take it with us."
                                "I'm sure our whole world will feel different with a little bit of different music..."
                                "...Actually, there's something I'd like to ask you."
                                "You were planning to take your music with you the whole time, right?"
                                thinking "..."
                                "For that reason too, yes..."
                                "Back outside..."
                                "W-Well, maybe we should have a walk around inside to get prepared."

                            else:
                                "Looking around like this is quite nice..."
                                "We ought to do this for as long as we can."
                                "Forever would be nice, but I'm well aware that's unreasonable."
                                "...Just know it means a lot."
                        
                        else:
                            "...You're being even quieter than normal..."
                            "Is there something you wish to tell me?"
                            thinking "..."
                            "Nothing? Hmm..."
                            "Fine, I believe you."
                            scene room 4 with dissolve
                            $ renpy.pause(1.5, hard=True)
                            "Aren't we eager?"
                            "You may have been done, but I wasn't"
                            scene room 4 with dissolve:
                                zoom 1.2
                            thinking "..."
                            "Don't worry, I won't ask anything that will make you uncomfortable."
                            "...I just want to listen to some music is all..."
                            "I'm more than certain you know how to work this machine, yes?"
                            stop music fadeout 0.5
                            $ renpy.pause(0.5, hard=True)
                            play music "quarter moon tsukihime.mp3" fadein 0.5
                            thinking "..."
                            "Hmm, quite the track..."
                            "Not something you have on tape, if I recall though..."
                            "Oh, that's the radio part, isn't it?"
                            "I'm not fond of the radio."
                            "I'm actually fairly fond of your music to be perfectly honest."
                            "I'd like to listen to it."
                            thinking "..."
                            "No, no, the one that's in there right now is perfectly fine."
                            "There's nothing wrong with wanting to listen to it, right?"
                            "There hasn't been in the past..."
                            "Alright, I'll come out and ask it..."
                            "What is wrong with that piece of machinery?"
                            thinking "..."
                            "You won't even tell me that much? Fine."
                            thinking "..."
                            "Oh, I see. You want to fix it."
                            "...Yes, you are quite fond of your music."
                            "I'm actually surprised that it's in a not completely working state."
                            thinking "..."
                            "You think you have something to fix it around here?"
                            "Wonderful, I'm looking forward to listening to it with you."
                            stop music fadeout 0.5
                            $ renpy.pause(0.5, hard=True)
                            play music "cresent moon tsukihime.mp3" fadein 0.5
                            thinking "..."
                            "No, don't worry, I truly was honest when I said I wasn't fond of the radio, turning it off was the right call."
                            "I'll leave it to you to find what you think you have to fix your piece of machinery."
                        if not (persistent.cassette_player):
                            $ persistent.cassette_player = True
                            $ striking_checker.add_progress(1)

                    "Your Piggy Bank":
                        "I see..."
                        "Wait a minute, what do you mean?"
                        "Do you mean the literal interpretation of those words?"
                        thinking "..."
                        "Yes, well there's clearly one that's a pig but there's also one that's clearly a dog on a house."
                        "Yet, somehow that's not called a doggy on housey bank."
                        thinking "..."
                        "You're right, I do feel foolish."
                        "Though, I can't really understand what use you have for money here."
                        thinking "..."
                        "I suppose the designs aren't bad."
                        "I didn't know you collected them."
                        "How many do you have?"
                        thinking "..."
                        "What's with that look?"
                        "I feel as though almost anyone would be quite depressed when only having 3 coins, not happy."
                        "Especially when you have two piggy banks."
                        thinking "..."
                        "Yes, I suppose I did say there's no use for money here."
                        "...And you are far from most people..."
                        "Still, if collecting them makes you happy, one would think that only having 3 would still make you upset."
                        thinking "..."
                        "...That's just like you."
                        "\"I'd be happy with the first of the 3.\""
                        "Just like you indeed."
                        $ piggy_bank_2 = True
                        if not (persistent.piggy_bank):
                            $ persistent.piggy_bank = True
                            $ striking_checker.add_progress(1)

                    "Your Pen Collection":
                        "A collection of pens... How practical."
                        "Though, clearly some of them are far from practical."
                        "I don't really understand collecting things..."
                        "Though I do appriciate the people who do."
                        "I can just be completely happy with one thing and one thing alone."
                        "That should be very clear to you, I feel."
                        thinking "..."
                        "You're right, we haven't really talked about the pens at all."
                        "Why'd you look at them in the first place?"
                        thinking "..."
                        "...I don't like people wasting my time, you know."
                        "Let's just... Let's just look around else where then."
                        if not (persistent.pen_collection):
                            $ persistent.pen_collection = True
                            $ striking_checker.add_progress(1)
                        
    
    jump room4menu



    return