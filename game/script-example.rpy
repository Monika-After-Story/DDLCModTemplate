##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label example_chapter:
    stop music fadeout 2.0

    #This set's up the scene with a background and music
    scene bg club_day
    with dissolve_scene_full
    play music t3

    # Most of the story will be told using "Say" statements
    # They take the form of a short nickname, follow by their statement in quotes.
    m "...[player]?"

    #You will also want to show characters of other images
    show monika 1 at t11 zorder 2
    m "Ah! What a nice surprise!"

    #Character images are their name followed by a number and letters
    #The trailing letter is generally the facial expression
    show monika 1b at t11 zorder 2
    m "Welcome to the club!"
    m "The Modification Club."

    #The number is the pose
    show monika 3 at t11 zorder 2
    m " I started this club after I had some difficulties changing code in Doki Doki Literature Club."

    #Faces and poses can be changed inline if you are not changing positions of the character(s).
    #For face reference, view the image files of the character you are trying to manipulate,
    #and choose the face image letter that most accurately displays the emotion you are trying to convey.

    #Refer to the Character Pose Cheat Sheet(This doesn't exist yet!) to find out which number corresponds to which pose!

    m 3l  "It turns out that bad coding can really hurt people."
    m 3j "That's why I wanted to make this club to teach people how to mod responsibly!"

    m 2a "First, you need the right template."
    m 2b "This template you're looking at right now!"
    $ config.developer = "auto"
    if config.developer:
        m 2b "Looks like you're ahead of me on that one."
        m "Way to take the initiative!"
    else:
        m 2b "You can find the source for it online at https://github.com/therationalpi/DDLCModTemplate"
        m "If you haven't already, of course."

    m 1a "Then you need to add files from DDLC."
    m "You'll want to put those in the /game folder of the template."
    if config.developer:
        m 1b "Again, that's something you already know."
        m 1l "Please let me know if I'm boring you!"
    else:
        m 1b "Kind of like what you did to make this demo work!"

    m 1a "Finally, you're going to want to download the Ren'Py SDK."
    m 2a "That's at https://www.renpy.org/latest.html"
    if config.developer:
        m 2j"I promise I'll get to the good stuff now."
    else:
        m 2a "You'll be using that to write and test your scripts."

    m 4a "So now that you have everything, it's time to get started!"
    m 4b "Start by opening up your /game folder"
    m 4c "You'll notice there aren't a lot of files in there."
    m 4a "Most of the data we'll be using is coming from DDLC."
    m "Including all of the user interface and system coding."
    m 4k "All you need to bring are the stories you want to tell!"
    m 4c "Of course, if you really want to dig deep and change how the game works..."
    m 4b "That's possible too."

    m 1j "That reminds me..."
    m 1k "I haven't asked about you or the game you want to make."
    m 5 "Ahaha~! How silly of me!"



    default knows_python=False
    default knows_renpy=False

    #Note: the choice function does not allow inline changes in the first line.
    menu:

        m "How experienced are you with coding?"
        "I'm an experienced coder":
            $experience_level = 2
            m 5 "Really? That's very impressive!"
            show monika 1m at t11 zorder 2
            with Dissolve(0.3)
            m 1m "I'm new to this, myself, so maybe I'll end up learning more from you, instead!"
        "I've coded before":
            $experience_level = 1
            m 5 "That's good."
            show monika 1j at t11 zorder 2
            with Dissolve(0.3)
            m 1j "Building a mod for DDLC should feel very natural, then!"
        "New to coding":
            $experience_level = 0
            m 5 "Really? This should be fun then!"
            show monika 1m at t11 zorder 2
            with Dissolve(0.3)
            m 1m "I'm pretty new to this myself..."
            m 1n "So it's a little a weird for me to be someone's teacher."
            m 1k "But I'll try my best!"

    if experience_level > 0:
        m 2a "Since you've coded before, you might like to know that this game was built using Renpy."
        m "It's a very popular platform for making visual novels."

        show monika 1a at t11 zorder 2

        menu:
            m "Have you used Renpy before?"
            "Yes.":
                $knows_renpy = True
                m 1b "Sounds like you're ahead of the game, then."
            "No.":
                m 1e "Well, don't worry about that."
                m 1b "Renpy is actually very easy once you get used to it."

        m 3a "For more advanced coding, python might be necessary."
        m 3c "Renpy is actually built with Python..."
        m 3j "So the sky's the limit for modding if you know how to use it!"

        show monika 1a at t11 zorder 2
        menu:
            m "Are you familiar with python?"
            "Yes.":
                $knows_python = True
                if not knows_renpy:
                    m 1a"That might help you pick up Renpy a little quicker, then."
                    m 3a "But there are some things that makes Renpy's python a bit different."
                    m 3j "I'll try to call them out when they come up."
                else:
                    m 1b "Sounds like you're in great shape for this!"
                    m 1j "You have all the skills you need to make whatever you want."
                    m 1k "I'm excited to see what you come up with."
            "No.":
                if not knows_renpy:
                    m 2c "Well, any coding experience will help a lot."
                    m 2a "Python is made to be an easy language to pick up, after all."
                else:
                    m 2d "Don't sell yourself short, [player]."
                    m 2a "I'm sure you picked up a few tricks from Renpy already."
                    m 2j "But I'll be sure to share a few I've picked up with you, too."

    m 1c "Now, about the mod you want to make."
    m "How difficult of a project is it going to be?"
    m 1d "Is it mostly going to be standard scripts with a few choices and special effects..."
    m 5 "...or will you be creating lots of new systems to really change the game?"

    menu:
        m "So, which do you plan on making?"
        "Basic.":
            $advanced = False
            m 5 "Starting off with something simple?"
            show monika 3b at t11 zorder 2
            with Dissolve(0.3)
            m 3b "I think that's a good way to go."
            m 3a "Making a simple script is a lot like writing a play."
            m 1a"But the actors are us characters, and we'll always do just what you direct from us..."
            m 1m "..for better or worse."
        "Advanced.":
            $advanced = True
            m 5 "Trying for something a little more complicated?"
            show monika 1e at t11 zorder 2
            with Dissolve(0.3)
            m 1e "Well, I'll try to share all the tools I have with you."
            m 1k "Hopefully you'll find what you need to make your perfect game!"

    m 2b "Now that I know more about you and your project, we're really ready to get started!"
    m "I've prepared a few lessons to help get you started!"
    m 2a "And when we're done, you'll have made your first mod."

    #This makes sure we skip the intro the next time you play
    $ persistent.playthrough = 1

    jump tutorial_selection

    return
