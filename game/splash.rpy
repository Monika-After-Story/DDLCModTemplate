## This splash screen is the first thing that Renpy will show the player
##
## Before load, check to be sure that the archive files were found.
## If not, display an error message and quit.
init -100 python:
    #Check for each archive needed
    for archive in ['audio','images','fonts']:
        if not archive in config.archives:
            #If one is missing, throw an error and chlose
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

## First, a disclaimer declaring this is a mod is shown, then there is a
## check for the original DDLC assets in the install folder. If those are
## not found, the player is directed to the developer's site to download.
##
init python:
    menu_trans_time = 1
    #The default splash message, originally shown in Act 1 and Act 4
    splash_message_default = "This game is an unofficial fan work, unaffiliated with Team Salvato."
    #Optional splash messages, originally chosen at random in Act 2 and Act 3
    splash_messages = [
    "Please support Doki Doki Literature Club."
    "Monika is watching you code."
    ]
    ##########################
    #Original splash messages#
    ##########################
    # splash_message_default = "This game is not suitable for children\nor those who are easily disturbed."
    # splash_messages = [
    # "You are my sunshine,\nMy only sunshine",
    # "I missed you.",
    # "Play with me",
    # "It's just a game, mostly.",
    # "This game is not suitable for children\nor those who are easily disturbed?",
    # "sdfasdklfgsdfgsgoinrfoenlvbd",
    # "null",
    # "I have granted kids to hell",
    # "PM died for this.",
    # "It was only partially your fault.",
    # "This game is not suitable for children\nor those who are easily dismembered.",
    # "Don't forget to backup Monika's character file."
    # ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

##Here's where you can change the logo file to whatever you want
image menu_logo:
    "/mod_assets/DDLCModTemplateLogo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

# Make sure character files are in place
init python:
    if not persistent.do_not_delete:
        if persistent.playthrough <= 2:
            try: renpy.file("../characters/monika.chr")
            except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        if persistent.playthrough <= 1 or persistent.playthrough == 4:
            try: renpy.file("../characters/natsuki.chr")
            except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: renpy.file("../characters/yuri.chr")
            except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        if persistent.playthrough == 0 or persistent.playthrough == 4:
            try: renpy.file("../characters/sayori.chr")
            except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

label splashscreen:
    # Logic for detecting if the game has been reinstalled
    # This allows you do delete the "firstrun" file to completely reset the game
    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun: #renpy.loadable("10"):
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()

    #If this is the first time the game has been run, show a disclaimer
    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        # This is the disclaimer recommended by the IP Guidelines
        "[config.name] is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed, and contains spoilers for the official game."
        "Game files for Doki Doki Literature Club are required to play this mod and can be downloaded for free at: http://ddlc.moe"
        ## This is the original disclaimer
        # "This game is not suitable for children or those who are easily disturbed."
        # "Individuals suffering from anxiety or depression may not have a safe experience playing this game."
        menu:
            "By playing [config.name] you agree that you have completed Doki Doki Literature Club and accept any spoilers contained within."
            #"By playing Doki Doki Literature Club, you agree that you are at least 13 years of age, and you consent to your exposure of highly disturbing content."
            "I agree.":
                pass
        scene tos2
        with Dissolve(1.5)
        pause 1.0

        #Optional, load a copy of DDLC save data
        #call import_ddlc_persistent

        scene white
        with Dissolve(1.5)

        $ persistent.first_run = True

    ########################################################################
    #This codeblock from DDLC selects the special poems for the playthrough#
    ########################################################################
    # if not persistent.special_poems:
    #     python hide:
    #         persistent.special_poems = [0,0,0]
    #         a = range(1,12)
    #         for i in range(3):
    #             b = renpy.random.choice(a)
    #             persistent.special_poems[i] = b
    #             a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')

    #autoload handling
    #Use persistent.autoload if you want to bypass the splashscreen on startup for some reason
    if persistent.autoload and not _restart:
        jump autoload

    ##########################################
    #This loads a creepy main menu easter egg#
    ##########################################
    # if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
    #     show black
    #     $ config.main_menu_music = audio.ghostmenu
    #     $ persistent.seen_ghost_menu = True
    #     $ persistent.ghost_menu = True
    #     $ renpy.music.play(config.main_menu_music)
    #     pause 1.0
    #     show end with dissolve_cg
    #     pause 3.0
    #     $ config.allow_skipping = True
    #     return

    # Start splash logic
    $ config.allow_skipping = False

    # Splash screen
    show white
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ splash_message = splash_message_default #Default splash message
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    #You can use random splash messages, as well. By default, they are only shown during certain acts.
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False #Handling for easter egg from DDLC
    $ style.say_dialogue = style.normal

    #################################
    #Code block for yuri death scene#
    #################################
    # If we load during yuri_kill
    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     if persistent.yuri_kill >= 1380:
    #         $ persistent.yuri_kill = 1440
    #     elif persistent.yuri_kill >= 1180:
    #         $ persistent.yuri_kill = 1380
    #     elif persistent.yuri_kill >= 1120:
    #         $ persistent.yuri_kill = 1180
    #     elif persistent.yuri_kill >= 920:
    #         $ persistent.yuri_kill = 1120
    #     elif persistent.yuri_kill >= 720:
    #         $ persistent.yuri_kill = 920
    #     elif persistent.yuri_kill >= 660:
    #         $ persistent.yuri_kill = 720
    #     elif persistent.yuri_kill >= 460:
    #         $ persistent.yuri_kill = 660
    #     elif persistent.yuri_kill >= 260:
    #         $ persistent.yuri_kill = 460
    #     elif persistent.yuri_kill >= 200:
    #         $ persistent.yuri_kill = 260
    #     else:
    #         $ persistent.yuri_kill = 200
    #     jump expression persistent.autoload


    #Check if the save has been tampered with
    if anticheat != persistent.anticheat:
        stop music
        scene black
        "The save file could not be loaded."
        "Are you trying to cheat?"

        ##########################################
        #Code block for monika anti-cheat message#
        ##########################################
        # $ m_name = "Monika"
        # show monika 1 at t11
        # if persistent.playername == "":
        #     m "You're so funny."
        # else:
        #     m "You're so funny, [persistent.playername]."

        #Handle however you want, default is to force reset all save data
        $ renpy.utter_restart()
    return



label autoload:
    python:
        # Stuff that's normally done after splash
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        # Fix the game context (normally done when loading save file)
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    ###################################
    #More code for yuri death sequence#
    ###################################
    # if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
    #     $ persistent.yuri_kill += 200

    # Pop the _splashscreen label which has _confirm_quit as False and other stuff
    $ renpy.pop_call()
    jump expression persistent.autoload

###################################
#More code for yuri death sequence#
###################################
# label autoload_yurikill:
#     if persistent.yuri_kill >= 1380:
#         $ persistent.yuri_kill = 1440
#     elif persistent.yuri_kill >= 1180:
#         $ persistent.yuri_kill = 1380
#     elif persistent.yuri_kill >= 1120:
#         $ persistent.yuri_kill = 1180
#     elif persistent.yuri_kill >= 920:
#         $ persistent.yuri_kill = 1120
#     elif persistent.yuri_kill >= 720:
#         $ persistent.yuri_kill = 920
#     elif persistent.yuri_kill >= 660:
#         $ persistent.yuri_kill = 720
#     elif persistent.yuri_kill >= 460:
#         $ persistent.yuri_kill = 660
#     elif persistent.yuri_kill >= 260:
#         $ persistent.yuri_kill = 460
#     elif persistent.yuri_kill >= 200:
#         $ persistent.yuri_kill = 260
#     else:
#         $ persistent.yuri_kill = 200
#     jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    ##############################
    #More creepy ghost menu stuff#
    ##############################
    # if persistent.ghost_menu:
    #     hide screen main_menu
    #     scene white
    #     show image "gui/menu_art_m_ghost.png":
    #         xpos -100 ypos -100 zoom 3.5
    #     pause 0.01
    return
