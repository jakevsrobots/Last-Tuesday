# ------------------------
# Dream 1
# ------------------------
label dream_1:
    "That night, I had a dream ..."

    scene bg hallway
    with pixellate

    "... A long hallway, maybe a school or a city building."
    "I walked slowly forward through a punishing flourescent light."
    "I could hear a noise from room at the end of the hall, a repeating tone, like a bell."
    "Suddenly, a tinny voice clattered over the intercom."
    
    "Voice" "How did you get in here?"

    menu:
        "Where am I?":
            jump dream_1_where
        "Who are you?":
            jump dream_1_who

label dream_1_where:
    "Voice" "You are in the city. But you shouldn't be."

    $ curiosity += 1
    
    jump dream_1_end

label dream_1_who:
    "Voice" "I am the authority. I make the rules."

    $ empathy += 1
    
    jump dream_1_end

label dream_1_end:
    "Voice" "You have to leave."

    scene black
    with pixellate
    
    "I woke up before dawn, my heart pounding in my throat."
    jump day

# ------------------------
# Dream 2
# ------------------------
label dream_2:
    "That night, I had a dream ..."

    scene bg hallway
    with pixellate

    "... That same long hallway. I walked toward the room at the end of the hall, and the bell sound grew louder."

    scene bg closet
    with fade

    "I passed a janitor's closet and stopped to look inside."

    menu:
        "It reminded me of work.":
            jump dream_2_work
        "I wondered where the janitor was.":
            jump dream_2_janitor

label dream_2_work:
    "I missed staying late in the building, cleaning the empty halls and picking things up from office floors."
    "When the staff had gone home, I could just focus on my work and listen to the air conditioner drone."

    $ memory += 1
    
    jump dream_2_end

label dream_2_janitor:
    "Maybe he'd gone home early. But I could tell the floors still needed mopping."
    "Maybe he'd had an emergency. I could do him a favor by cleaning up a bit."

    $ empathy += 1
    
    jump dream_2_end
    
label dream_2_end:
    scene black
    with pixellate
    
    "It was still dark when I woke up, feeling strangely comforted."
    jump day
    
# ------------------------
# Dream 3
# ------------------------
label dream_3:
    "That night, I had a dream ..."

    scene bg hallway
    with pixellate

    "... That same long hallway. I walked to the room at the end of the hall, following the sound of the bell."

    scene bg phone
    with fade

    "When I reached the office, I found a phone ringing on the desk."
    "I lifted the receiver and put it to my ear."

    "Voice on Phone" "Who is this?"

    menu:
        "Who is {i}this{/i}?":
            jump dream_3_who
        "This is the janitor.":
            jump dream_3_janitor

label dream_3_who:
    "Voice on Phone" " ... "
    "It wasn't quite silent, but the voice wasn't talking anymore."
    "I could hear something like soft music coming from the other end of the line."
    "The music slowly got louder, then suddenly cut off."

    $ curiosity += 1
    
    jump dream_3_end    

label dream_3_janitor:
    "Voice on Phone" "Please empty the recycling bin on your way out."
    "Voice on Phone" "And please --"

    $ memory += 1
    
    jump dream_3_end

label dream_3_end:
    "The voice snapped into focus. Suddenly, it was all I could hear."
    "Voice on Phone" "You have to leave."

    scene black
    with pixellate
    
    "I woke up in the dark, disoriented, but somehow not afraid."
    jump day

    
# ------------------------
# Dream 4
# ------------------------
label dream_4:
    "That night, I had a dream ..."

    scene bg hallway
    with pixellate

    "I was in the same hallway. The ringing sound was gone."
    "But I could hear something behind me, like a murmuring or a shuffling."

    scene bg door
    with fade

    "I quickly turned around and found myself facing a row of doors."
    "The noise grew louder as I stepped forward and slowly pushed one open..."
    
    jump ending_router


label ending_router:
    "curiosity=%(curiosity)d, empathy=%(empathy)d, memory=%(memory)d"
    
    python:
        highest_stat = 0

        for stat in [curiosity, empathy, memory]:
            if stat > highest_stat:
                highest_stat = stat

    if highest_stat == curiosity:
        jump ending_1
    elif highest_stat == empathy:
        jump ending_2
    elif highest_stat == memory:
        jump ending_3    
    
# ------------------------
# Ending 1 - curiosity
# ------------------------
label ending_1:
    scene bg europe_street
    with fade

    "I found myself in a foreign city, with cobblestone streets and archaic lampposts."
    "The streets are empty, the city deserted."
    "But it's a place I've never seen, a whole new environment to explore, street by nameless street."

    scene black
    with fade
    
    "I hope I never wake up."
    ".:. Ending 1."
    
    $ renpy.full_restart()
    
# ------------------------
# Ending 2 - empathy
# ------------------------
label ending_2:
    scene bg cafeteria
    with fade

    "I found myself in a cafeteria."
    "This is my cafeteria -- the one in my building."
    "It's empty, except for the staff. They're taking their afternoon break."
    "I can just walk over to them and sit down, have a cup of coffee, make small talk about the building."

    scene black
    with fade
    
    "I hope I never wake up."
    ".:. Ending 2."

    $ renpy.full_restart()    

# ------------------------
# Ending 3 - memory
# ------------------------
label ending_3:
    scene bg cafeteria
    with fade

    "I found myself in a room full of filing cabinets."
    "This must be the city archives, where all the city's records are kept."
    "If no one is going to use this room anymore, I guess it's up to me."
    "I'll have to go through all the records and read them. {i}Someone{/i} should know about this city."
    "I'll just start reading from the closest drawer: 'Licenses, Small Business.'"

    scene black
    with fade
    
    "I hope I never wake up."
    ".:. Ending 3."

    $ renpy.full_restart()    
