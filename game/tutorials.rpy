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
        ,(_("How To Make A Simple Route, Part 1"),"tutorial_route_p1")
        ,(_("Route Part 2, Music"),"tutorial_not_done")
        ,(_("Route Part 3, Scene"),"tutorial_not_done")
        ,(_("Route Part 4, Dialogue"),"tutorial_not_done")
        ,(_("Route Part 5, Menu"),"tutorial_not_done")
        ,(_("Route Part 6, Logic Statement"),"tutorial_not_done")
        ,(_("Route Part 7, Sprite"),"tutorial_not_done")
        ,(_("Route Part 8, Position"),"tutorial_not_done")
        ,(_("Route Part 9, Ending"),"tutorial_not_done")]
        
    

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
    
    show monika 4a at t11 zorder 2
    
    m "I hope I managed to teach you something!"
    m 4b "I look foward to seeing your mods."
    m 5a "Until next time!"
    
    with dissolve
    
    return
    

#Tutorials 

label tutorial_not_done:
    
    m 4n "Ahaha...it looks like this tutorial is not done yet!"
    
    return
    
label tutorial_route_p1:
    
    show monika 4a at t11 zorder 2 
    
    m "There’s no better way to become better at poetry than writing poems."
    m "And in the same way, there’s no better way to become better at modding than making mods."
    m "So, let’s make a mod together! I have got the perfect idea."
    m "Let’s make my own route!"
    m "The one the game never gave us…"
    m "Of course, as both and I are new at programming, we should keep it simple."
    m "We’ll need Ren’Py but unfortunately I can’t access it from here."
    m "So I’m counting on you to help me."
    m "Make sure you follow exactly my instructions, okay? In coding, a single mistake can totally break a program."
    m "First, verify that you installed Ren’Py. Then make a copy of Doki Doki Literature Club’s directory and put it in the directory of Ren’Py."
    m "Rename the directory of the game \"DDLC Monika Route\"."
    m "Put the files of DDLC Mod Template inside DDLC Monika Route’s directory."
    m "Try to lunch Ren’Py and then try to start DDLC Monika Route."
    m "If there’s an error then you might have made a mistake with the files…Unfortunately, I can’t help you…If it works then we can go the next step."
    m "Go to DDLC Monika Route’s game directory and delete tutorial.rpy. This file is used to make the tutorials of DDLC Mod Template but we won’t need it to make my route."
    m "Then you need to edit script.rpy. You can edit it with any text editor. Open the file and find the line \"        call prologue from _call_prologue\"." 
    m "Replace it \"        call monika_route from _call_monika_route\"."
    m "Be very careful about the number of spaces! In Ren’Py and Python spaces are very important. I won’t go into details now, but you need to make sure to write exactly what I say."
    m "Double check that the spaces aren’t tabs."
    m "Once the line is replaced, save the file. Create an empty text file. Rename it monika_route_script.rpy. Check if the extension is .rpy. Rpy files are the type of files used for Ren’Py scripts."
    m "Open monika_route_script.rpy and write \"label monika_route:\". Then jump a line and write \"     return\". Save the file."
    m "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."
    m "In a book, each chapter are followed one after another. Chapter two is written after chapter two and so on. But in Ren’Py this is different."
    m "The order isn’t determined by the place of each chapter in the scripts but by the keywords \"label\", \"call\" and \"jump\""
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is \"start\". Then the game reads and executes what is inside the block under the label \"start\"." 
    m "When it reaches the keyword \"call\" or \"jump\", the game proceeds to the chapter whose label followed the keyword."
    m "In the case of our mod, when the game reads “        call monika_route from _call_ monika_route”, it jumps to the chapter labeled monika_route."
    m "Please don’t mind \"from _call_monika_route\", it’s quite advanced stuff and I don’t understand it well too."
    m "The chapter monika_route is defined in the file we created, monika_route_script.rpy. But as you can see, there is nothing inside it except from \"return\"."
    m "The keyword \"return\" makes the game goes back to the chapter that was read before but only if the current chapter was accessed through the key word \"call\"."
    m " Otherwise, the game goes back to the main menu."
    m "If you try to play the mod, you’ll see nothing when you click New Game. That’s because the game returns to the main menu as soon as it jumps to monika_route."
    m "Okay! Let’s stop here for now. I hope I didn’t overwhelm you with information…"
    m "If there’s still an error when you try playing the mod, there's a script named t1.rpy inside the folder named monika_route_answer. t1.rpy is what you should have written in monika_route_script.rpy."
    m "You can copy-paste the content of t1.rpy to monika_route_script.rpy but don’t forget to delete the # character in front of each line."
    m "In Python and Ren’Py, the # character tells your computer not to read and execute the line. A line with a # in front of it is nothing more than a comment that only you can read."
    m "This is all for now! When you are ready, begin the second part! I'm waiting for you."

    return
    
