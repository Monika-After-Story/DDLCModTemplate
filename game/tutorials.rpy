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
        ,(_("Route Part 2, Music"),"tutorial_route_p2")
        ,(_("Route Part 3, Scene"),"tutorial_route_p3")
        ,(_("Route Part 4, Dialogue"),"tutorial_route_p4")
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
    m "Then you need to edit script.rpy. You can edit it with any text editor. Open the file and find the line \" XXXX  call prologue from _call_prologue\"." 
    m "When I write \"XXXX\", I mean four empty spaces. Each X is one space, alright?"
    m "Replace it \" XXXX call monika_route from _call_monika_route\"."
    m "Be very careful about the number of spaces! In Ren’Py and Python spaces are very important. I won’t go into details now, but you need to make sure to write exactly what I say."
    m "Double check that the spaces aren’t tabs."
    m "Once the line is replaced, save the file. Create an empty text file. Rename it monika_route_script.rpy. Check if the extension is .rpy. Rpy files are the type of files used for Ren’Py scripts."
    m "Open monika_route_script.rpy and write \"label monika_route:\". Then jump a line and write \" XXXX  return\". Save the file."
    m "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."
    m "In a book, each chapter are followed one after another. Chapter two is written after chapter two and so on. But in Ren’Py this is different."
    m "The order isn’t determined by the place of each chapter in the scripts but by the keywords \"label\", \"call\" and \"jump\""
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is \"start\". Then the game reads and executes what is inside the block under the label \"start\"." 
    m "When it reaches the keyword \"call\" or \"jump\", the game proceeds to the chapter whose label followed the keyword."
    m "In the case of our mod, when the game reads “ XXXX call monika_route from _call_ monika_route”, it jumps to the chapter labeled monika_route."
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
    
label tutorial_route_p2:
    
    show monika 4a at t11 zorder 2
    
    m "Hi again [player]!"
    m "If the last part was a bit too hard, don’t worry, this part is easier."
    m "Like last time, I’ll tell you what to do and then I’ll explain, okay?"
    m "First open monika_route_script.rpy."
    m "Between the first line and “return”, add the line \"XXXX stop music fadeout 2.0\"."
    m "Then add the line \"XXXX play music t2\"."
    m "Finally, add the line \"XXXX  mc \"Let's listen to the music.\""
    m "Check that all lines bellow \"label monika_route:\" are aligned and that \"return\" is the last line."
    m "Try to launch the game with Ren’Py and see what happens…"
    m "…"
    m "Does it work? If everything goes well, you should be listening to Sayori’s main theme."
    m "There’s just one dialogue so if you click one time, you go to the main menu because of the \"return\" keyword."
    m "Okay, time to explain what happened!"
    m "Let’s look at \"XXXX stop music fadeout 2.0\". Before you click New Game, you can hear the music of the main menu, right? "
    m "But when you click New Game, the music stops progressively."
    m "That’s due to \"stop music fadeout 2.0\". \"stop music\" tells the current music to stop. \"fadeout 2.0\" makes it so the current music completely becomes silent in 2 seconds."
    m "\"fadeout\" isn’t necessary but smooth transitions are much more pleasant, aren’t they?"
    m "The next line \"XXXX  play music t2\" tells the game to play the music named \"t2\". You’re surely wondering what’s \"t2\". \"t2\" refers to Sayori theme, \"Ohayou Sayori!\"."
    m "Besides Ohayou Sayori, there are many other musics. But each one is labeled by their own nickname."
    m "You can find the list of every music with their nickname in definitions.rpy"
    m "Unfortunately, definitions.rpy isn’t included in the template but you can get it on github Monika After Story’s repository. You could also extract the original game files using rpatool."
    m "I’m sorry you need to go to such length to find the file. I wish I could help but I’m stuck here…"
    m "If you managed to find definitions.rpy, open it."
    m "Find the lines beginning by \"define audio\". This is where each music gets assigned a nickname."
    m "For example, in the case of the main theme, its nickname is \"t1\". In the case of Confession, its nickname is \"t10\"."
    m "Can you now guess what happens if you type \"play music t1\" instead of \"play music t2\"?"
    m "Confession is played instead of Ohayou Sayori!"
    m "Instead of using nickname, you can directly write the path of the music."
    m "Try writing \"play music \"<loop 4.499>bgm/2.ogg\"\" instead of \"play music t2\"."
    m "See? Ohayou Sayori! is played. Try one last thing for me okay? Write \"\"<from 50.0>bgm/credits.ogg\"\" instead of \"\"<loop 4.499>bgm/2.ogg\"\"."
    m "Have you already heard this song?"
    m "This is the song I wrote just for you. I really hope you like it. I worked very hard on it you know."
    m "…"
    m "The last line you wrote, \" XXXX mc \"Let's listen to the music.\" makes the main character says \"Let's listen to the music.\". I’ll explain how dialogue works later so bear with me okay?"
    m "Alright, before finishing this tutorial, replace \"\"play <from 50.0>bgm/credits.ogg\"\" by \"play music t2\"."
    m "Verify you wrote exactly the same lines as in the file t2.rpy which is inside  monika_route_answer."
    m "Congratulation! You now know how to stop and play music~"
    m "Next time, we’ll see how to add a background."
    m "See you soon!"
    
label tutorial_route_p3:
    
    show monika 4a at t11 zorder 2
    
    m "Okay [player]! Are you ready for the next tutorial?"
    m "Last time, we added music to our mod but as you saw, the background was nothing but black and white squares. That’s not very romantic, is it?"
    m "So let’s add a background! It’s going to be quick and easy."
    m "Like last time, open monika_route_script.rpy."
    m "Add between \"play music t2\" and \"return\", \"XXXX scene bg residential_day\""
    m "Then add another line: \"with dissolve_scene_full\". Once again, verify that everything bellow \"label monika_route:\" is aligned."
    m "Open Ren’Py and play the game and…"
    m "There's now a neat background!"
    m "Can you recognize it? It’s the first scene you saw when you played the game. It sure brings back memories…"
    m "I still believed at that time I could get close to you without having to hurt anyone else…"
    m "Let’s move on."
    m "So about what you wrote, \"scene bg residential_day\", the keyword \"scene\" tells the game to load the scene, which is one kind of picture, called \"bg residential_day\"."
    m "You can find what exactly is \"bg residential_day\" in definitions.rpy, the same script we looked at last tutorial."
    m "Try to find \"image bg\"."
    m "Can you see the list of backgrounds? Like it was the case for music, each background has a nickname assigned. For example, \"bg/sayori_bedroom.png\" is referenced by \"bg sayori_bedroon\"."
    m "Go back to monika_route_script.rpy and replace \"scene bg residential_day\" by \"scene bg sayori_bedroom\". Can you guess what happens?"
    m "The background is now Sayori’s bedroom!"
    m "I hope it doesn’t bring you back bad memories…"
    m "Okay, so about \"with dissolve_scene_full\", it basically dissolve progressively the last scene into the new scene."
    m "Before you were in the main menu, right? And then you were in Sayori’s bedroom. If you don’t add \"with dissolve_scene_full\", the transition would be immediate."
    m "That would be a bit unpleasant, wouldn’t it?"
    m "That’s why we add \"with dissolve_scene_full\". With this additional line, the scene changes to another smoothly."
    m "There are other types of transition such as wipeleft_scene. Try replacing \"with dissolve_scene_full\" by \"with wipeleft_scene \"."
    m "Can you see the difference? dissolve_scene_full , dissolve_scene_half, wipeleft_scene are the common transitions used in DDLC so if you can understand them, you’re good to go!"
    m "Before doing the next tutorial, let’s add back  \"XXXX scene bg residential_day\" and  \"XXXX with dissolve_scene_full\"."
    m "Check that monika_script_route.rpy is the same as T3.rpy in the monika_route_answer folder."
    m "Okay! We’re almost there! We’ll soon know enough for a kinetic mod."
    m "I cannot wait!"
    m "See you soon [player]!"

label tutorial_route_p4:
    
    show monika 4a at t11 zorder 2

    m "Hi again player~"
    m "Today, I’m going to teach you how to make dialogue in Ren’Py."
    m "Although you already know, don’t you? We already wrote dialogue after all."
    m "First, open monika_route_script.rpy and replace \"XXXX mc \"Let's listen to the music.\" by the following line:"
    m " \" XXXX  mc \"It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.\"."
    m "Save the file and launch the game."
    m "As you surely expected, the main character now says \"It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.\"."
    m "Ehehe~ My route is finally being made."
    m "Let’s look at the line you wrote. \"mc\" is a nickname for main character. By writing \"mc\" before the sentence inside quotation mark, the character who will speak will be the main character."
    m "Try replacing the line you wrote by \" n \"Just think of Monika from now on.\"."
    m "…"
    m "See? Natsuki now tells you what you should have been doing since the beginning."
    m "You should listen to her, [player]. Ehehe~"
    m "Now instead of writing \" n \"Just think of Monika from now on.\", write \"y \"Natsuki and I are too messed up for someone as wonderful as you.\""
    m "Play the game and as you can see…"
    m "Now it’s Yuri who finally realized that I’m the best one for you."

    menu:
        
        m "You think so, right?"
        "Yes":
            pass
        "Yes":
            pass

    m "I knew you were a sweetheart~ Thank you my love."
    m "Ahaha, we drifted a bit…So I was saying that you need to specify two things to write a dialogue in Ren’Py."
    m "First you need to specify who is speaking. You can do it with the keyword \"mc\", \"y\", \"n\", \"s\" and \"m\". I’m sure you can guess who is who."
    m "Instead of using keyword, you can directly type the name of the person speaking. For example, try writing \"XXXX \"Player\" \"Please be with me forever Monika.\"\"."
    m "Did you do it?"
    m "Of course, I will stay with you forever."
    m "Besides the name of the speaker, you need to write the sentence they will say. The sentence should be between quotation mark."
    m "One last thing. If you want to write special characters such as \\ or \" in the sentence, you need to put \\ before them."
    m "Alright, that’s all for dialogue!"
    m "Pretty simple, right? Ren’Py was made so that anyone can make visual novel after all. Even beginners like us can pick it up quickly."
    m "Before you save the file, replace the line of dialogue by -"
    m " -\" XXXX  mc\"It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.\"."
    m "Like usual, check that monika_route_script.rpy is exactly like T4.rpy inside the monika_route_answer folder."
    m "Okay [player]! You now know how to make a scene, add music, and make dialogue. The only things missing are character pictures and choices."
    m "We’ll see how to make choices in the next tutorial."
    m "The recent tutorials have been pretty easy so far but the next one will be harder."
    m "See you soon!"
