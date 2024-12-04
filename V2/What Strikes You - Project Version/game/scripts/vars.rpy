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

default misused_canister_2 = False
default spiked_sphere_2 = False
default to_leave_2 = False
default piggy_bank_2 = False
# True false, only need these for a progress achievement so checking the same thing over and over doesn't progress it.
init python:
    if not hasattr(persistent, 'oblong_stick'):
        persistent.oblong_stick = False
    if not hasattr(persistent, 'misused_canister'):
        persistent.misused_canister = False
    if not hasattr(persistent, 'imprisoned_case'):
        persistent.imprisoned_case = False
    if not hasattr(persistent, 'bobbed_sponge'):
        persistent.bobbed_sponge = False
    if not hasattr(persistent, 'obtuse_mushroom'):
        persistent.obtuse_mushroom = False
    if not hasattr(persistent, 'spiked_sphere'):
        persistent.spiked_sphere = False
    if not hasattr(persistent, 'of_love'):
        persistent.of_love = False
    if not hasattr(persistent, 'voice_speaking'):
        persistent.voice_speaking = False
    if not hasattr(persistent, 'to_leave'):
        persistent.to_leave = False
    if not hasattr(persistent, 'cassette_player'):
        persistent.cassette_player = False
    if not hasattr(persistent, 'piggy_bank'):
        persistent.piggy_bank = False
    if not hasattr(persistent, 'pen_collection'):
        persistent.pen_collection = False
