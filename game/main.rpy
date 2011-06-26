image bg bedroom_night = "images/bedroom-night.png"
image bg bedroom_morning = "images/bedroom-morning.png"
image bg outside_apartment = "images/outside-apartment.png"
image bg bus_stop = "images/bus-stop.png"
image bg freeway = "images/freeway.png"
image bg downtown = "images/downtown.png"

image bg grocery = "images/grocery-aisle.png"

# Set up a default theme.
init python:
    register_stat("Curiosity", "curiosity", 0, 100)
    register_stat("Empathy", "empathy", 0, 100)
    register_stat("Memory", "memory", 0, 100)

    dp_period("Morning", "morning_act")
    dp_choice("Explored a grocery store", "grocery_store")       # curiosity
    dp_choice("Went to the library", "library")                  # memory
    dp_choice("Dialed a radio", "radio")                         # empathy
    
    dp_period("Afternoon", "afternoon_act")
    dp_choice("Explored a building", "building")                 # curiosity
    dp_choice("Collected magazines", "magazines")                # memory
    dp_choice("Cleaned someone's house", "cleaned_house")        # empathy
    
    dp_period("Evening", "evening_act")
    dp_choice("Explored a movie theater", "theater")             # curiosity
    dp_choice("Practiced my Spanish", "spanish")                 # memory
    dp_choice("Turned on a television", "television")            # empathy    
    
# This is the entry point into the game.
label start:
    $ game_round = 0
    $ dreams_had = []

    scene black
    
    jump day
    
    scene bg bedroom_night
    with fade
    
    "On Tuesday night, I fell asleep to the sounds of traffic outside my bedroom window."

    scene black
    with pixellate
    "I had a dream, but I can't remember it ... "
    "... something about a river ... running water ..."

    scene bg bedroom_morning
    with pixellate
    "The next morning, I awoke to an eerie and stifling silence."
    "Blinking in the glare of the morning sun, I walked through my living room and opened the front door."

    scene bg outside_apartment
    with fade

    "Nothing looked out of place, really, but ... absolute silence."
    "I'd never experienced anything like it."

    scene bg bedroom_morning
    with fade

    "I dressed quickly, then went back out to head to work, still a bit unnerved."

    scene bg bus_stop
    with fade

    "My watch read 8:45 by the time I reached the bus stop. It was deserted."
    "Usually I'd wait there, bumping shoulders with office workers and food handlers waiting for the crowded bus ride downtown."
    "But the morning commuter rush was nowhere to be seen."
    "So I waited."

    scene bg bus_stop
    with fade

    "I waited for an uncomfortable half-hour or so."
    "Not a single car passed on the street."
    "Finally, I gave up and started walking."

    scene bg freeway
    with fade

    "Eventually, I reached the freeway."
    "It was empty, too."

    scene bg downtown
    with fade

    $ renpy.music.play("audio/last-tuesday-guitar.ogg", loop=True, fadein=30)
    
    "By the time I reached my building downtown, I knew I was alone."

    scene black
    with fade

    jump day

    
# This is the label that is jumped to at the start of a day.
label day:
    $ game_round += 1
    #$ game_round = 2

    # Here, we want to set up some of the default values for the
    # day planner. In a more complicated game, we would probably
    # want to add and remove choices from the dp_ variables
    # (especially dp_period_acts) to reflect the choices the
    # user has available to him.

    $ morning_act = None
    $ afternoon_act = None
    $ evening_act = None
    
    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.

    show bg bedroom_morning
    with fade
    
    call day_planner(["Morning", "Afternoon", "Evening"])
    
    # We process each of the three periods of the day, in turn.
label morning:
    show black
    with fade
    
    # Tell the user what period it is.
    centered "Morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below. 
    $ period = "morning"
    $ act = morning_act

    # Ensure that the stats are in the proper range.
    $ normalize_stats()
    
    # Execute the events for the morning.
    call events_run_period

    # That's it for the morning, so we fall through to the
    # afternoon.

label afternoon:
    show black
    with fade

    centered "Afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    $ normalize_stats()
    
    call events_run_period


label evening:
    show black
    with fade
    
    centered "Evening"

    $ period = "evening"
    $ act = evening_act

    $ normalize_stats()
    
    call events_run_period
    

label night:

    # This is now the end of the day, and not a period in which
    # events can be run. We put some boilerplate end-of-day text
    # in here.

    centered "Night"

    # We call events_end_day to let it know that the day is done.
    call events_end_day


    # Figure out if a dream should happen, and if so which one
    $ dream_to_have = 0
    
    python:
        highest_stat = 0
        for stat in [curiosity, empathy, memory]:
            if stat > highest_stat:
                highest_stat = stat
                
        if highest_stat >= 25 and 1 not in dreams_had:
            dream_to_have = 1
            dreams_had.append(1)
        elif highest_stat >= 50 and 2 not in dreams_had:
            dream_to_have = 2
            dreams_had.append(2)
        elif highest_stat >= 75 and 3 not in dreams_had:
            dream_to_have = 3
            dreams_had.append(3)
        elif highest_stat >= 100 and 4 not in dreams_had:
            dream_to_have = 4
            dreams_had.append(4)            

    if dream_to_have == 0:
        "I slept."
        
        scene black
        with fade
    elif dream_to_have == 1:
        jump dream_1
    elif dream_to_have == 2:
        jump dream_2
    elif dream_to_have == 3:
        jump dream_3
    elif dream_to_have == 4:
        jump dream_4
    
    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day
         

# This is a callback that is called by the day planner. One of the
# uses of this is to show the statistics to the user.
label dp_callback:

    # Add in a line of dialogue asking the question that's on
    # everybody's mind.
    if game_round == 1:
        $ narrator("With nothing else to do, I ...", interact=False)
    else:
        $ narrator("The next day, I ... ", interact=False)

    #$ display_stats()

    return

