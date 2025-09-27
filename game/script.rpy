define fox = Character("Fox", color="#FFA500", image="fox") # tiger
define ariel = Character("Ariel", color="#FFC0CB", image="ariel") # bunny
define gerald = Character("Gerald", color="#90EE90", image="gerald") # frog
define computer = Character("Computer", color="#F5F5DC", image="computer") # cat
define carpet = Character("Carpet", color="#654321", image="carpet") # axolotl
define acorn = Character("Acorn", color="#A0522D", image="acorn") # squirrel
define mc = Character("You", color="#ffffff") # you lol

transform resized_lowered:
    zoom 0.9
    yalign 1.0
    yoffset 300

transform resize_carpet:
    zoom 0.7
    yalign 1.0
    yoffset 450

transform resize_acorn:
    zoom 0.85
    xalign 0.4
    yalign 1.0
    yoffset 600

transform resize_fox:
    zoom 0.75
    yalign 1.0
    yoffset 650

transform resize_ariel:
    zoom 0.95
    yalign 1.0
    yoffset 1000

image computer = At("computer.png", resized_lowered)
image fox = At("fox.png", resize_fox)
image ariel = At("ariel.png", resize_ariel)
image gerald = At("gerald.png", resized_lowered)
image carpet = At("carpet.png", resize_carpet)
image acorn = At("acorn.png", resize_acorn)

init python:
    my_characters = ["computer", "fox", "ariel", "gerald", "carpet", "acorn"]
    
    def hide_my_chars():
        for char in my_characters:
            renpy.hide(char)

label start:

    # initial dorm scene - talk w/ IT head, then alarms sound

    $ hide_my_chars()
    show computer at center

    mc "Computer... something feels off..."
    computer "Off? Off is an understatement. Oxygen levels dropping. Life support is… compromised."
    mc "Compromised? You mean a glitch?"
    computer "No. Sabotage. Someone cut the main line. Oxygen tank is leaking. We have… limited time."
    mc "Limited how?"
    computer "Three hours at most. Maybe less if the breach worsens. And yes, that’s a hard limit."
    mc "That's not great."
    computer "Not great is an understatement. You need to find the culprit before the whole crew suffocates."
    mc "Sounds like… detective work."
    computer "Exactly. Interrogate. Accuse. Save the ship. Time starts now."
    mc "Great. So we’re playing murder mystery under pressure now."
    computer "Precisely. Your oxygen supply is tied to your success."

    label ask_loop:
        menu:
            "I don't understand - I need a recap":
                mc "Uhhh... can I get a recap?"
                fox "...OK... fine..."
                jump start
            "Got it, I'll get started":
                jump pick_interrogation

label pick_interrogation:
    menu:
        "Interrogate Fox":
            jump interrogate_fox
        "Interrogate Ariel":
            jump interrogate_ariel
        "Interrogate Gerald":
            jump interrogate_gerald
        "Interrogate Computer":
            jump interrogate_computer
        "Interrogate Carpet":
            jump interrogate_carpet
        "Interrogate Acorn":
            jump interrogate_acorn
        "Conclude The Investigation":
            jump accuse_saboteur

    jump game_over
label scene_2:

label interrogate_fox:
    $ hide_my_chars()
    show fox at center
    fox "Let's talk. But make it fast."
    jump pick_interrogation

label interrogate_ariel:
    $ hide_my_chars()
    show ariel at center
    ariel "You think I did it? Prove it."
    jump pick_interrogation

label interrogate_gerald:
    $ hide_my_chars()
    show gerald at center
    gerald "Ribbit— I mean, no comment."
    jump pick_interrogation

label interrogate_computer:
    $ hide_my_chars()
    show computer at center
    computer "Interrogating the system? Bold."
    jump pick_interrogation

label interrogate_carpet:
    $ hide_my_chars()
    show carpet at center

    mc "So... where were you when the alarms went off?"
    carpet "Dreamland, man. Out cold. Didn’t hear a thing until the sirens quit."
    menu:
        "Weren't you walking around...?":
            carpet "Nah, they must’ve seen someone else. I was sleepy..."
        "Convenient timing.":
            carpet "Yeah, ‘convenient’ is my middle name."
    mc "Anyone see you around then?"    
    carpet "Nope. Guess that makes me innocent, right?"
    menu:
        "Or very unaccountable.":
            carpet "What? No!"
        "Funny, Computer says you wandered into the server room.":
            carpet "Oh right!  I did get lost.  But only for a sec.  Bathroom mix-up."
    mc "Why so tired all the time?"
    carpet "Because carrying this crew on my back is exhausting."
    menu:
        "That's a joke":
            carpet "Yeah, I know.  But it’s true."
        "Nobody remembers you carrying anything":
            carpet "Not even my blanket!"
    mc "So you were asleep... but also in the server room... but also nobody saw you.  That adds up to nothing, Carpet!"
    carpet "You're twisting my words, man.  Totally twisting them!"
    mc "That'll be all for now..."
    jump pick_interrogation

label interrogate_acorn:
    $ hide_my_chars()
    show acorn

    acorn "You've got THREE minutes.  I've got to get back to the cockpit.  We're running out of oxygen, and someone's got to save us.  Also, the ship doesn't steer itself!"
    mc "Well, funnily enough, it kind of does... but anyway, why're you acting so responsible all of a sudden?"
    acorn "Shush, someone's trying to kill us.  Focus!"
    mc "Where were you when the alarm hit?"
    acorn "At the helm.  Where else?  Someone's gotta look after it..."
    menu:
        "Anyone see you?":
            acorn "No witnesses.  Don't need 'em.  I know my job."
        "That's convenient.":
            acorn "Yeah, I know, can I get back to my work?"
    mc "Did you notice anything off?"
    acorn "Gerald came through.  Reeked of burnt wires.  Asked dumb questions.  Then left."
    menu:
        "You didn't stop him?":
            acorn "Not my department.  I steer, I don't babysit."
        "Why mention the smell?":
            acorn "Because you should pay attention..."
    mc "Why are you so hostile?"
    acorn "Because I don't like being accused."
    menu:
        "Sounds defensive.":
            acorn "Sounds accurate."
        "How do I trust you?":
            acorn "I'm innocent!"
    mc "You've got a mouth on you, and you constantly try to get out of answering questions."
    acorn "Look, I've got better things to do."
    mc "Fine, fine.  That'll be all for now..."
    jump pick_interrogation

label accuse_saboteur:
    $ hide_my_chars()
    menu:
        "Accuse Fox":
            jump accuse_fox
        "Accuse Ariel":
            jump accuse_ariel
        "Accuse Gerald":
            jump accuse_gerald
        "Accuse Computer":
            jump accuse_computer
        "Accuse Carpet":
            jump accuse_carpet
        "Accuse Acorn":
            jump accuse_acorn

label accuse_fox:
    $ hide_my_chars()
    show fox
    fox "You're a dead tiger."
    jump game_over

label accuse_ariel:
    $ hide_my_chars()
    show ariel
    ariel "You're a dead bunny."
    jump game_over

label accuse_gerald:
    $ hide_my_chars()
    show gerald
    gerald "You're a dead frog."
    jump game_over

label accuse_computer:
    $ hide_my_chars()
    show computer
    computer "You're a dead cat."
    jump game_over

label accuse_carpet:
    $ hide_my_chars()
    show carpet
    carpet "You're a dead axolotl."
    jump game_over

label accuse_acorn:
    $ hide_my_chars()
    show acorn
    acorn "You're a dead squirrel."
    jump game_over

label game_over:
    return
