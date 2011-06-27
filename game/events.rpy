# This file contains the events that will be part of the game. It's
# expected that the user will add and remove events as appropriate
# for this game.


# ---------------------------
# Morning
# ---------------------------
init:
    $ event("grocery_store_1", "act == 'grocery_store'", event.once(), event.only(), priority=200)
    $ event("grocery_store_2", "act == 'grocery_store'", event.once(), event.only(), priority=210)
    $ event("grocery_store_3", "act == 'grocery_store'", event.once(), event.only(), priority=220)
    $ event("grocery_store_4", "act == 'grocery_store'", event.only(), priority=230)

    $ event("library_1", "act == 'library'", event.once(), event.only(), priority=200)
    $ event("library_2", "act == 'library'", event.once(), event.only(), priority=210)
    $ event("library_3", "act == 'library'", event.once(), event.only(), priority=220)
    $ event("library_4", "act == 'library'", event.only(), priority=230)

    $ event("radio_1", "act == 'radio'", event.once(), event.only(), priority=200)
    $ event("radio_2", "act == 'radio'", event.once(), event.only(), priority=210)
    $ event("radio_3", "act == 'radio'", event.once(), event.only(), priority=220)
    $ event("radio_4", "act == 'radio'", event.only(), priority=230)

    $ stat_increment_amount = 1

# Grocery store
label grocery_store_1:
    scene bg grocery
    with fade
    
    "The shelves of the grocery store were full, like they'd just been stocked."
    "I'd never had fresh coconut before, so I broke one open on a cash register and made a small breakfast of it."

    $ curiosity += stat_increment_amount
    return

label grocery_store_2:
    scene bg grocery
    with fade
    
    "Some of the fruit and vegetables at the grocery store were starting to rot."
    "I dug around looking for something interesting to eat, some new and unusual breakfast."
    "Eventually, I settled on canned cactus. They tasted a bit like green beans."

    $ curiosity += stat_increment_amount
    return
    
label grocery_store_3:
    scene bg grocery
    with fade

    "The grocery store was beginning to smell like an alleyway."
    "I steered clear of the produce and butchery sections, and focused on canned goods."
    "After rejecting shelves of chili, soup, and vegetables, I finally found a can of cuban-style black beans. That sounded like a reasonable breakfast."
    
    $ curiosity += stat_increment_amount
    return

label grocery_store_4:
    scene bg grocery
    with fade

    "The smell of rotting meat overwhelmed me, and I had to leave."

    scene black
    with fade
    
    return

# Library
label library_1:
    scene bg library
    with fade
    
    "The large front doors of the public library were unlocked."
    "It was quiet. That was nothing new."
    "On the front counter, a small pile of books was waiting to be returned to the shelf."
    "I picked up the top book -- 'The Quiet Earth,' by Craig Harrison."
    "Since no one else was going to re-shelve it, I thought I might as well."
    "If anyone ever came back, at least they'd be able to find the books they were looking for."
    "I put the book back on the shelf, in the 'science fiction' section."
    
    $ memory += stat_increment_amount
    
    return

label library_2:
    scene bg library
    with fade
    
    "The air in the library seemed a bit stale."
    "I took another book from the front counter. 'The Girl Who Owned a City,' by O.T. Nelson."
    "It was a story set in Chicago, where I grew up. I flipped through the book looking for familiar street names."
    "After a few minutes, I put the book back on the shelf, in the 'young adult' section."
    
    $ memory += stat_increment_amount
    return

label library_3:
    scene bg library
    with fade

    "The air conditioning system at the library must have broken down."
    "I almost choked on the warm, dusty air circulating through the building."
    "I took the next book from the front counter. 'The World Without Us,' by Alan Weisman."
    "The short blurb on the back sounded interesting, but I didn't really feel like reading."    
    "I put the book back on the shelf, in the 'popular science' section."

    $ memory += stat_increment_amount
    return

label library_4:
    scene bg library
    with fade
    
    "When I opened the door to the library, I was hit with a wave of dust and warm air."
    "With the air conditioning system broken, I knew that the only chance for these books to stay preserved was to keep the building sealed."
    "The library door would have to stay shut."
    
    return

# Radio
label radio_1:
    scene bg radio
    with fade

    "I found a car with the keys still in the ignition. It wouldn't start, but I could turn on the radio.."
    "It was just static."
    "I turned the tuning dial all the way down and very slowly moved up through the stations."
    "For a moment, I heard something that sounded like a voice ..."
    "But it was just interference."
    $ empathy += stat_increment_amount
    return

label radio_2:
    scene bg radio
    with fade

    "The radio seemed a bit quieter that day."
    "I dialed the tuning knob further up the spectrum."
    "One signal stood out from the rest: a repeating buzzer, like a doorbell or a car alarm."
    "I wondered if was some kind of machine left running alone, or just interference from a broadcast tower bending in the wind."
    
    $ empathy += stat_increment_amount
    return

label radio_3:
    scene bg radio
    with fade
    
    "I switched on the car radio, but could barely hear it."
    "I raised the volume as high as it would go, pressed my ear to the speaker, and started tuning for stations."
    "I hit upon something that sounded almost like music ..."
    "But then it was gone. The car battery had died completely."
    "Later, I wondered if I had even heard music at all -- or if the hiss of radio static had just started to {b}sound{/b} like music."
    
    $ empathy += stat_increment_amount
    return

label radio_4:
    scene bg radio
    with fade
    
    "I couldn't get the radio to switch back on. The car battery was completely drained."
    return

# ---------------------------
# Afternoon
# ---------------------------
init:
    $ event("park_1", "act == 'park'", event.once(), event.only(), priority=200)
    $ event("park_2", "act == 'park'", event.once(), event.only(), priority=210)
    $ event("park_3", "act == 'park'", event.once(), event.only(), priority=220)
    $ event("park_4", "act == 'park'", event.only(), priority=230)
    
    $ event("newspaper_1", "act == 'newspaper'", event.once(), event.only(), priority=200)
    $ event("newspaper_2", "act == 'newspaper'", event.once(), event.only(), priority=210)
    $ event("newspaper_3", "act == 'newspaper'", event.once(), event.only(), priority=220)
    $ event("newspaper_4", "act == 'newspaper'", event.only(), priority=230)
    
    $ event("cleaned_house_1", "act == 'cleaned_house'", event.once(), event.only(), priority=200)
    $ event("cleaned_house_2", "act == 'cleaned_house'", event.once(), event.only(), priority=210)
    $ event("cleaned_house_3", "act == 'cleaned_house'", event.once(), event.only(), priority=220)
    $ event("cleaned_house_4", "act == 'cleaned_house'", event.only(), priority=230)

# Park    
label park_1:
    scene bg park
    with fade
    
    "I liked the city park, but had never spent much time there."
    "It was small, but lush, with a man-made lake in the middle."
    "I remember the ground was wet, soft, almost like mud. Even though it hadn't rained in weeks."
    
    $ curiosity += stat_increment_amount
    return

label park_2:
    scene bg park
    with fade
    
    "The ground at the park was definitely turning to mud."
    "When I reached the small lake at the middle, I noticed that the pumps had turned off."
    "I guess they needed some human maintenance."
    "With no one there to operate them, the park was turning into a swamp."
    
    $ curiosity += stat_increment_amount
    return

label park_3:
    scene bg park
    with fade
    
    "It was getting difficult to trudge through the swampy park without being totally mired."
    "I found a small pumping station, but it was padlocked shut."
    "The lake had turned a deep, brownish gray. Everything was sinking together."
    
    $ curiosity += stat_increment_amount
    return

label park_4:
    scene bg park
    with fade

    "I tried to enter the park, but almost lost a shoe. The small man-made lake had completely seeped into the grassy land around it."
    "The park had turned into a swamp."
    
    return

# Newspaper
label newspaper_1:
    scene bg newspaper
    with fade

    "I found a newspaper on the street; it was a bit damp but still legible."
    "The headline was something about the military -- some investigation."
    "I studied it carefully, but didn't quite have the context to make sense of it."
    "Still, I committed the details to memory. Perhaps it would be the last headline, I thought."
    
    $ memory += stat_increment_amount
    return

label newspaper_2:
    scene bg newspaper
    with fade

    "The newspaper's ink was running; it was difficult to make out words."
    "The 'Arts and Culture' section had an article about a new exhibit at the modern art museum."
    "It was a large-scale installation made of dead fruit-flies."
    "I wondered if bats had already eaten it."
    
    $ memory += stat_increment_amount
    return

label newspaper_3:
    scene bg newspaper
    with fade

    "The pages of the newspaper were stuck together. Peeling them apart, I could tell I was destroying it."
    "I was able to make out a classified ad in the back -- still legible because the buyer had paid extra for bold text."
    "He sounded lonely."
    
    $ memory += stat_increment_amount
    return

label newspaper_4:
    scene bg newspaper
    with fade

    "The newspaper had turned into a stack of blotted, grayish pulp. I could just barely make out the cover photo."

    return


# House

label cleaned_house_1:
    scene bg living_room
    with fade

    "Years ago, before I started working for the office building downtown, I worked for a maid service."
    "I found a house nearby, and thought I might go in and do some dusting."
    "If the people who lived there ever came back, they might not want to deal with all that dust."
    "The dust was already collecting on the coffee table."
    "I swept it off, and straightened some magazines."
    
    $ empathy += stat_increment_amount
    return

label cleaned_house_2:
    scene bg living_room
    with fade

    "I went back to the same house. It wasn't dusty anymore."
    "I took some time to clean the dishes in the sink and pick up a few stray plates."
    "I wondered if the people living here had last eaten breakfast or dinner ... it was impossible to tell."

    $ empathy += stat_increment_amount
    return

label cleaned_house_3:
    scene bg living_room
    with fade

    "The house was getting much better."
    "I folded some clean clothes I found in a laundry basket and set them on the bed."
    "There were two women's blouses of very different sizes. A mother and daughter? Sisters? Or lovers?"

    $ empathy += stat_increment_amount
    return

label cleaned_house_4:
    scene bg living_room
    with fade

    "The house was very clean. If the people who lived there had come back the next day, I'm sure they would have been comfortable."
    "But they didn't."

    return

# ---------------------------
# Evening
# ---------------------------
init:
    $ event("theater_1", "act == 'theater'", event.once(), event.only(), priority=200)
    $ event("theater_2", "act == 'theater'", event.once(), event.only(), priority=210)
    $ event("theater_3", "act == 'theater'", event.once(), event.only(), priority=220)
    $ event("theater_4", "act == 'theater'", event.only(), priority=230)

    $ event("spanish_1", "act == 'spanish'", event.once(), event.only(), priority=200)
    $ event("spanish_2", "act == 'spanish'", event.once(), event.only(), priority=210)
    $ event("spanish_3", "act == 'spanish'", event.once(), event.only(), priority=220)
    $ event("spanish_4", "act == 'spanish'", event.only(), priority=230)

    $ event("television_1", "act == 'television'", event.once(), event.only(), priority=200)
    $ event("television_2", "act == 'television'", event.once(), event.only(), priority=210)
    $ event("television_3", "act == 'television'", event.once(), event.only(), priority=220)
    $ event("television_4", "act == 'television'", event.only(), priority=230)

# Theater
label theater_1:
    scene bg theater
    with fade

    "There was a theater near the financial district that used to show old movies."
    "I'd always plan to go there and see some classic or another, but never quite made it."
    "The front door was locked, but I could see a key on the desk just inside the ticket booth."
    "There was a small hole in the glass, where the cashier and the customer would exchange money for tickets."
    "I struggled to reach my hand through. It was a tight fit. I managed to grasp a ticket stub, but that's all."

    $ curiosity += stat_increment_amount
    return

label theater_2:
    scene bg theater
    with fade

    "I found a piece of rope in the alley behind the theater, and I thought maybe I could use it to snare the keys from the ticket booth."
    "I held the rope between my index and middle fingers, and pushed it thorugh the window."
    "I swung it back and forth to gain momentum a few times, then snapped my wrist toward the key."
    "But the rope slipped out of my fingers and fell on the floor."

    $ curiosity += stat_increment_amount
    return

label theater_3:
    scene bg theater
    with fade

    "I found a bent but solid piece of wire in the street outside the theater."
    "I bent the end of it into a hook, and pushed it carefully through the ticket booth window."
    "I managed to hook the key with the wire, then slowly slid it back across the desk and out of the window."
    "The key didn't work in the front door. I walked around to the alley and tried a door there -- but no luck."
    "I guess it must have been the bathroom key?"

    $ curiosity += stat_increment_amount
    return

label theater_4:
    scene bg theater
    with fade

    "The theater was locked shut, and my key didn't work. I gave up and moved on."

    return

# Spanish
label spanish_1:
    scene bg spanish
    with fade
    
    "I found some notes I'd taken in a Spanish class a few years before, at a community college."
    "Flipping through them, I realized I'd spent much more time drawing weird, angry faces than actually writing down Spanish verbs and nouns."
    "But there were a few in there. I thought I might as well brush up. Maybe become the only Spanish-speaking person in the city ..."
    "City -- Ciudad."
    
    $ memory += stat_increment_amount
    return

label spanish_2:
    scene bg spanish
    with fade
    
    "I flipped through my Spanish notes. Next to a drawing of what might have been a super-hero, or maybe a porn star, was the word 'contexto.'"
    "I assumed that meant 'context.'  There wasn't anything else written near it."
    
    $ memory += stat_increment_amount
    return

label spanish_3:
    scene bg spanish
    with fade
    
    "As I worked through my Spanish notes, they were making less and less sense."
    "I couldn't remember what might have been going on in my life at the end of that class that would have distracted me so much."
    "I found one English/Spanish noun pair, near a sketch of a car parked on an empty highway: 'tranquilo.'"
    "'Quiet.'"
    
    $ memory += stat_increment_amount
    return

label spanish_4:
    scene bg spanish
    with fade
    
    "My Spanish notes didn't even make sense near the end. I don't think most of the words were even completely written down."
    "They weren't going to do me any more good. But I'd refreshed myself on a little Spanish, in the meantime."
    
    return

# Television
label television_1:
    scene bg tv
    with fade
    
    "The television in my apartment still worked, but there were no stations broadcasting."
    "I sat for a while in the dark, watching white noise, flipping channels compulsively."
    "I thought about all the people in the TV shows that were no longer being broadcast."
    "Those characters and all their problems just ... ceased to exist?"
    
    $ empathy += stat_increment_amount
    return

label television_2:
    scene bg tv
    with fade
    
    "I set the TV to channel 9 and pretended I was watching a nature show."
    "I imagined the narrator was documenting a new form of TV static: its mating habits, its nasty and brutish living conditions."
    "I imagined that it pained the narrator to describe."
    
    $ empathy += stat_increment_amount
    return

label television_3:
    scene bg tv
    with fade
    
    "It was difficult to remember television before the static."
    "I tried to pick a channel and imagine a news program, a game show, something ...."
    "For a while, I pretended to watch a black-and-white cartoon about fleas in a snowstorm."
    
    $ empathy += stat_increment_amount
    return

label television_4:
    scene bg tv
    with fade
    
    "I switched the TV on, but at that point it was just noise."
    "I couldn't remember any shows to pretend."
    
    return
