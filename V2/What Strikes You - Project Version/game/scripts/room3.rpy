label room3:

    scene room 3 with dissolve
    $ timer += 1
    if timer >= 10 and music:
        jump endings
    "A fearful sight shows itself."

    label room3menu:
        scene room 3 with dissolve
        menu:
            "Rotate Right":
                jump room4
            
            "Rotate Left":
                jump room2
            
            "Inspect This Area":
                scene room 3 with dissolve:
                        zoom 1.2
                "There's nothing really here to inspect to be quite honest."
                "Nothing of interest anyway."
                "If you ask me, it seems like you're grasping at straws."
                "Though, I really would be remiss to not do my duty of asking that question..."
                "{b}What Strikes You?{/b}"
                menu:
                    "The Concept Of Love":
                        "Are you quite alright?"
                        "It is quite the striking thing, I must admit."
                        "I'm just curious as to why you're thinking that now of all times."
                        "Though, perhaps it's a question best left unanswered."
                        "I'm sure you have you reasons, but you ought to share them with someone very special."
                        "That's how I feel about the matter, anyway."
                        "I wouldn't be surprised at all if you thought differently."
                        thinking "..."
                        "Hmm, you think the same thing?"
                        "Colour me surprised."
                        if not (persistent.of_love):
                            $ persistent.of_love = True
                            $ striking_checker.add_progress(1)
                    
                    "The Voice Speaking":
                        "Me?"
                        "You're talking about me, right?"
                        thinking "..."
                        "Yes, there us no one else to talk to, true..."
                        "Sorry, I'm just quite shocked you would ask."
                        "Really, what do you even want to know?"
                        "I'll answer anything..."
                        "Within reason, of course."
                        menu:
                            "Ask Something Meaningful":
                                "You want to know who I am?"
                                "My sincerest apologies, but sadly that's something not within reason."
                                thinking "..."
                                "Yes, it may be for you, but not for me."
                                "I would tell you if I could, but I truly can't."
                                "Tell you what, I feel bad for not being able to answer your question, so I'll tell you something I'm sure you'd like to know..."
                                "Your continued existence pleases me greatly."
                            
                            "Ask Something That Serves You":
                                "You have quite the interesting question."
                                "\"Are you the voice in my head?\""
                                "That was a serious question, right?"
                                thinking "..."
                                "Of course, you always have been quite earnest; I don't think I've ever heard you ask a non-honest question."
                                "So, to answer your question, no."
                                "In fact, if I were the voice in your head, I'd recommend it that you stop talking to yourself so much."
                                "But, since I'm not, talk as much as you'd like."
                                "Which isn't very much at all, I know, but it's enough."

                            "Don't Ask Anything":
                                "You get my hopes up..."
                                "...Only to let me down..."
                                "Seriously, I wouldn't even be bothered if you didn't seem so indifferent to wasting my time."
                                "It doesn't even matter to me really, I'm just conceptually annoyed."
                                "Wouldn't you be?"
                                "Wait, don't answer that."
                                while i < loop:
                                    $ i +=1
                                    "."
                                $ i = 0
                                "See, wasn't that incredibly annoying?"
                        if not (persistent.voice_speaking):
                            $ persistent.voice_speaking = True
                            $ striking_checker.add_progress(1)
                    
                    "The Ability To Leave":
                        "You... Wish to leave?"
                        thinking "..."
                        "No, it doesn't upset me at all."
                        "I'm simply shocked."
                        "When's the last time you've left here without your music?"
                        "Aren't you scared?"
                        "...No, that's a stupid question, you clearly are."
                        "That's what puzzles me all the more."
                        "Why do you wish to leave if you're scared?"
                        thinking "..."
                        "Something you must do?"
                        "I see..."
                        "It must be important."
                        thinking "..."
                        "Yes, if you don't have to go the whole way, it will be much easier, that's good."
                        "I don't think it's even possible to go the full way anymore in the first place."
                        thinking "..."
                        "Yes, I'll be with you."
                        "It would be against what I stand for to not go."
                        "But please, let me ask you something."
                        "Are you sure you want to go?"
                        menu:
                            "Go":
                                "I see."
                                "Despite your fear, there is no stopping you."
                                "Let's go then."
                                scene house 1 with dissolve
                                
                                # Use this as what is basically the same as a main-thread safe sleep. "hard=True" means that the pause cannot be skipped by clicking/pressing space like you would do to advance text.
                                $ renpy.pause(1.5, hard=True)
                                
                                # Use stop to stop the music, works in reverse compared to play
                                stop music fadeout 0.5
                                scene house 2 with dissolve
                                $ renpy.pause(1.5, hard=True)
                                "You're shaking."
                                thinking "..."
                                "I know, I won't ask if you're sure again."
                                thinking "..."
                                "There's something you want me to remember?"
                                "You know my memory gets worse the farther we go."
                                thinking "..."
                                "Yes. The length of the gravel path. If I remember, and you forget, I will tell you, however unlikely that may be."
                                "Let us go once more."
                                while i < loop2:
                                    $ i += 1
                                    $ renpy.pause(1.5, hard=True)
                                    scene walk 1 with dissolve
                                    $ renpy.pause(1.5, hard=True)
                                    scene walk 2 with dissolve
                                $ i = 0
                                $ renpy.pause(1.5, hard=True)
                                scene house 3 with dissolve
                                "We've returned."
                                thinking "..."
                                "Hello?"
                                scene house 1 with dissolve
                                $ renpy.pause(0.5, hard=True)
                                scene room 3 with dissolve
                                if not (renpy.music.is_playing('music')):
                                    play music "cresent moon tsukihime.mp3" fadein 0.5
                                thinking "..."
                                "Ah, my apologies."
                                "I understand that was hard for you."
                                "...It was hard for me too."
                                thinking "..."
                                "No, sorry, I can't remember a thing from a few moments after we went outdoors."
                                thinking "..."
                                "You think you've got it? That's quite good."
                                "I do hope you got what you hoped to achieve out of that experience."
                                $ to_leave_2 = True
                            
                            "Stay":
                                "They say hesitation is the enemy of growth..."
                                "But to be quite honest, I cannot blame you."
                                "Just..."
                                "That determination you had, it tells me it might be a place we have to go."

                        if not (persistent.to_leave):
                            $ persistent.to_leave = True
                            $ striking_checker.add_progress(1)


    jump room3menu


    return