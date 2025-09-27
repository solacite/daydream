define fox = Character("Fox", color="#FFA500", image="fox") # tiger
define ariel = Character("Ariel", color="#FFC0CB", image="ariel") # bunny
define gerald = Character("Gerald", color="#90EE90", image="gerald") # frog
define computer = Character("Computer", color="#F5F5DC", image="computer") # cat
define carpet = Character("Carpet", color="#654321", image="carpet") # dog
define nicky = Character("Nicky", color="#FA8072", image="nicky") # axolotl
define acorn = Character("Acorn", color="#A0522D", image="acorn") # squirrel
define mc = Character("You", color="#ffffff") # you lol

label start:

    # initial dorm scene - talk w/ IT head, then alarms sound

    scene bg dorms

    show fox at left

    mc "Wtf???"
    fox ""
    fox "Once you add a story, pictures, and music, you can release it to the world!"
    label ask_loop:
        menu:
            "Ask Fox about the game":
                mc "What's this game about?"
                fox "It's a game about a fox who wants to be a hero."
            "Nevermind":
                mc "What's this game about?"
                fox "It's a game about a fox who wants to be a hero."
                jump ask_loop
    fox "You won!"
    jump game_over


label game_over:
    scene bg dorms
    show fox at right
    fox "You win!"
    return
