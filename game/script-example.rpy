##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label example_scene:
    stop music fadeout 2.0
    
    #This set's up the scene with a background and music
    scene bg club_day
    with dissolve_scene_full
    play music t3
    
    #Most of the story will be told using "Say" statements
    #They take the form of a short nickname, follow by their statement in quotes.    
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
    
    
    m "It turns out that bad coding can really hurt people."
    m "That's why I wanted to make this club to teach you how to mod responsibly!"
    
    m "First, you need the right template."
    m "This template you're looking at right now!"
    $ config.developer = "auto"
    if config.developer:
        m "Looks like you're ahead of me on that one."
        m "Way to take the initiative!"
    else:
        m "You can find the source for it online at https://github.com/therationalpi/DDLCModTemplate"
        m "If you haven't already, of course."
        
    m "Then you need to add files from DDLC."
    m "You'll want to put those in the /game folder of the template."
    if config.developer:
        m "Again, that's something you already know."
        m "Please let me know if I'm boring you!"
    else:
        m "Kind of like what you did to make this demo work!"
    
    m "Finally, you're going to want to download the Ren'Py SDK."
    m "That's at https://www.renpy.org/latest.html"
    if config.developer:
        m "I promise I'll get to the good stuff now."
    else:
        m "You'll be using that to write and test your scripts."
        
    m "So now that you have everything, it's time to get started!"
    m "Start by opening up your /game folder"
    m "You'll notice there aren't a lot of files in there."
    m "Most of the data we'll be using is coming from DDLC."
    m "Including all of the user interface and system coding."
    m "All you need to bring are your scenes!"
    m "Of course, if you really want to dig deep and change how the game works..."
    m "That's possible too."
    
    m "That reminds me..."
    m "I haven't asked much about what sort of game you want to make."
    m "Or even how much experience you have."
    m "How silly of me, Ahaha~!"
    
    default experience_level=0
    default knows_python=False
    default knows_renpy=False
    menu:
        m "How experienced are you with coding?"
        "I'm an experienced coder":
            $experience_level = 2
        "I've coded before":
            $experience_level = 1
        "New to coding":
            $experience_level = 0
            
    if experience_level > 0:
        menu:
            m "Are you familiar with python?"
            "Yes.":
                $knows_python = True                
            "No":
                pass
        menu:
            m "Have you used Renpy before?"
            "Yes":
                $knows_renpy = True
            "No":
                pass
                
    m "Now, about the mod you want to make."
    m "How advanced do you expect it to be?"
    
    return