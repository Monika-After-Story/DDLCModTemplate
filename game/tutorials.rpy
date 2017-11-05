## This file is used to write the tutorials
## When you make a mode using this template, you may delete this file
## and modify the lines nested in #### #### in script-example.rpy

#When you begin the game, you will redirected to two different routes
#First route: if you did not read the introduction yet, the game jumps to it
#Second route: if you already read the introduction, the game jumps to the tutorial menu

label prologue:
    
    if not persistent.introduction_read:
        jump example_chapter
    else:
        jump tutorial_selection
    
    
## This part of the code is used to create the tutorial selection screen.
    
#Each tutorial is defined by its name (caption) and its label,
#items is the list of caption and label of each tutorial
#init python is necessary because items is a List, a python object

init python: 

    items = [(_("Introduction"),"example_chapter") 
        ,(_("DDLC Mod Template"),"tutorial_not_done")
        ,(_("DDLC Original Files"),"tutorial_not_done")
        ,(_("Writing Dialogue"),"tutorial_not_done")
        ,(_("Background and Sprite "),"tutorial_not_done")
        ,(_("Sound and Music"),"tutorial_not_done")
        ,(_("Transition"),"tutorial_not_done")
        ,(_("DDLC Sprite Detail"),"tutorial_not_done")
        ,(_("DDLC Screen Position"),"tutorial_not_done")
        ,(_("In-Game Menus and Python "),"tutorial_not_done")
        ,(_("Transitions"),"tutorial_not_done")
        ,(_("DDLC Glitch"),"tutorial_not_done")]
        
    

#Define the properties of the object textbutton. textbutton is made by two parts:
#button and button_text. To customize textbutton, both botton and button_text need to be modified
#This part is usually found in gui.rpy

define adj = ui.adjustment()
define gui.tutorial_button_width = 500
define gui.tutorial_button_height = None
define gui.tutorial_button_tile = False
define gui.tutorial_button_borders = Borders(25, 5, 25, 5)

define gui.tutorial_button_text_font = gui.default_font
define gui.tutorial_button_text_size = gui.text_size
define gui.tutorial_button_text_xalign = 0.0
define gui.tutorial_button_text_idle_color = "#000"
define gui.tutorial_button_text_hover_color = "#fa9"

#Define the styles used for tutorial_vbox, tutorial_button and tutorial_button_text
#The line properties gui.button_properties("tutorial_button") assigns all attributes of gui.tutorial_button to the style tutorial_button and the style tutorial_button_text

style tutorial_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing 5

style tutorial_button is default:
    properties gui.button_properties("tutorial_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style tutorial_button_text is default:
    properties gui.button_text_properties("tutorial_button")
    outlines []

#Tutorial selection screen
#This screen was based on the tutorial screen of Tutorial of Ren'Py
    
screen tutorial_choice(items):
        style_prefix "tutorial"
        
        fixed:
            
            area (125, 40, 600, 450)
                
            bar adjustment adj style "vscrollbar" xalign -0.05
            
            viewport:
                yadjustment adj
                mousewheel True
                
                vbox:
                                    
                    for i_caption,i_label in items:
                        textbutton i_caption:
                            action Return(i_label)                 
                        
                    null height 20

                    textbutton _("That's enough for now.") action Return(False)
                            
        
#If the player has already read the introduction, then the game jumps directly to the tutorial menu
#Otherwise, the game first jumps to the introduction (example_chapter_explanation)
        
label tutorial_selection:

    stop music fadeout 2.0

    #This set's up the scene with a background and music
    scene bg club_day
    with dissolve_scene_full
    play music t3

    #let's see if the menu works...
    
    show monika 3a at tcommon(950)
    
    $ m(_("How can I help you?"), interact=False)

    call screen tutorial_choice(items)
    
    if _return is False:
        jump end_tutorial
    
    call expression _return from _call_expression
            
    jump tutorial_selection

#When you end the tutorial

label end_tutorial:
    
    show monika 4a at t11
    
    m "I hope I managed to teach you something!"
    m 4b "I look foward to seeing your mods."
    m 5a "Until next time!"
    
    with dissolve
    
    return
    

#Tutorials 

label tutorial_not_done:
    
    m 4n "Ahaha...it looks like this tutorial is not done yet!"
    
    return
    
