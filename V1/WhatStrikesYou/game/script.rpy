# These are characters, aka the name that appears when this character is speaking. They're global, existing across all script files in this directory and deeper. Params can be in any order, and basically and kind of modification to text can be made (italics, color, etc.). Prefixing a param with "what_" changes the character's text when they are speaking instead of their name.

define thinking = Character(what_italic=True, what_color="#800080")
define them = Character(what_italic=True)
define player = Character(what_color="#800080")

# Normal variables basically work that same as python, and can be used with if statements (which are also the same) and such.
default timer = 0
default i = 0
default loop = 10
default loop2 = 4
default found_music = False
default music = False
default code = None

# Can take the game to this line using "jump start".
label start:

    # Goes to the label named "room1", which can be in any script file in this directory or deeper.
    jump room1

    return
