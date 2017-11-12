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
        ,(_("Route Part 1, How To Make A Mod"),"tutorial_route_p1")
        ,(_("Route Part 2, Music"),"tutorial_route_p2")
        ,(_("Route Part 3, Scene"),"tutorial_route_p3")
        ,(_("Route Part 4, Dialogue"),"tutorial_route_p4")
        ,(_("Route Part 5, Menu"),"tutorial_route_p5")
        ,(_("Route Part 6, Logic Statement"),"tutorial_route_p6")
        ,(_("Route Part 7, Sprite"),"tutorial_route_p7")
        ,(_("Route Part 8, Position"),"tutorial_route_p8")
        ,(_("Route Part 9, Ending"),"tutorial_route_p9")]
        
    

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
    m "In the case of our mod, when the game reads \"XXXX call monika_route from _call_ monika_route\", it jumps to the chapter labeled monika_route."
    m "Please don’t mind \"from _call_monika_route\", it’s quite advanced stuff and I don’t understand it well too."
    m "The chapter monika_route is defined in the file we created, monika_route_script.rpy. But as you can see, there is nothing inside it except from \"return\"."
    m "The keyword \"return\" makes the game goes back to the chapter that was read before but only if the current chapter was accessed through the key word \"call\"."
    m "Otherwise, the game goes back to the main menu."
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
    m "Between the first line and \"return\", add the line \"XXXX stop music fadeout 2.0\"."
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

label tutorial_route_p5:
    
    show monika 4a at t11 zorder 2
    
    m "This time, I’ll explain how to make choices."
    m "For example…"
    
    call tutorial_route_p5_favorite_color from _call_tutorial_route_p5_favorite_color
    
    m "What a coincidence! It's also my favorite color!"
    m "It's the color of my eyes."
    m "Aren't we a perfect match?"
    m "Ehehe~"
    m "As you can see, I gave you several choices and you picked one of them."
    m "That’s what I’m going to teach you."
    m "Like every time, open monika_route_script.rpy and between \"return\" and the last line before it,-"
    m "- add \" XXXX menu:\", jump a line and then enter bellow \"XXXX XXXX mc \"I told her to meet me…\"\". Be careful, this time, there are eight spaces."
    m "Write just under \"XXXX XXXX  \"At the literature club room\":\" and then \" XXXX XXXX  XXXX $ meeting_place = \"club_room\"\"."
    m "Type \" XXXX XXX \"In front of my house\":\" and under it \"XXXX XXXX XXXX  $ meeting_place = \"my_house\"."
    m "Finally, jump a line and add \"XXXX mc \"I can't wait to meet her!\"\"."
    m "Try to play the game."
    m "If it doesn’t work, there’s surely an indentation error."
    m "I can’t help you from here, but you can check T5.rpy for the answers. You know where it is, right?"
    m "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, \"I told her to meet me…\"."
    m "You can specify who says this sentence by adding a nickname like \"mc\" before it. It’s just like a dialogue. What’s important is that this sentence is written before any choice."
    m "Contrary to the explanative sentence, the choices mustn’t be preceded by a nickname. They should be in quotation mark. Just after the closing quotation mark, there must be a \":\" ."
    m "After \":\, the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."
    m "I’ll give more explanation about the meaning of indents in the next tutorial."
    m "In our case, the next line after the first choice is \" XXXX XXXX  XXXX $ meeting_place = \"club_room\"."
    m "Take a good look at this line."
    m "Until now, I referred \"mc\", \"bg residential\" and \"t2\" as nickname. But that’s not really the correct word. They are actually what we call variable."
    m "Variable in coding is a very important concept. They have many forms and do many things. They can be \‘nicknames\’ or they can be numbers or more complicated structures."
    m "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what’s necessary to make a DDLC mod, okay?"
    m "I myself don’t know Python and Ren’Py all that well after all…"
    m "\"meeting_place\" is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): \"club_room\"."
    m "Its default value is None which means it doesn’t exist."
    m "Hold on a second? How can it not exist, you say?"
    m "Well before you define it, the variable doesn’t exist. But if you later try to use it, for example in a conditional statement, the variable will be ‘created’ and its value will be None."
    m "It’s alright if you don’t understand it yet. Variable, conditional statement and None will become clearer in my next lecture."
    m "Let’s go back to the meaning of  \" $ meeting_place = \"club_room\". Here we create the variable \"meeting_place\" and assign it the string \"club_room\"."
    m "The \"$\" in front of it is to tell Ren’Py the line is a Python line. Um..., I can’t really explain why we need to do that if you don’t know python yet…"
    m "Just remember that you need to add \"$\" when you want to assign a variable a value that way"
    m "Regarding the second choice, the structure is the same. The only difference is that the value of \"meeting_place\" will be \"my_house\" if the player selects the second choice."
    m "After the second choice, the game executes the line \"XXXX mc \"I can't wait to meet her!\"\"."
    m "For now it doesn’t look like the choices did anything. But we actually assigned \"meeting_place\" either \"club_room\" or \"my_house\"."
    m "We have to wait until the next tutorial to see how we can use the variable \"meeting_place\"."
    m "Alright, I’m sorry to leave hanging like that I believe we need to take a little break."
    m "If you want though, I would more than happy to begin the next part right away!"
    m "Just click Part 6!"
    
    return
    
label tutorial_route_p5_favorite_color:

    menu:
    
        m "What is your favorite color?"
        "Sky Blue":
            jump tutorial_route_p5_favorite_color
        "Amethyst Purple":
            jump tutorial_route_p5_favorite_color
        "Emerald Green":
            return
        "Candy Pink":
            jump tutorial_route_p5_favorite_color
            
            m " Are you ready? We are going to ramp up the difficulty."
            
label tutorial_route_p6:
    
    show monika 4a at t11 zorder 2
    
    m "Yeah, you came back [player]!"
    m "Glad to see you didn’t run away on me. Ahaha!"
    m "I was afraid the last tutorial was a bit too hard…"
    m "Well, this one is going to be hard as well but…"
    m "Hang it there okay? We did the hardest part already!"
    m "Last time we saw how to add menu and how to assign variable a value."
    m "Let’s see how we cause these variables!"
    m "You know the drill, open monika_route_script.rpy and at the end of the file, just before \"return\"…"
    m "Add the following lines :"
    m "\" XXXX if meeting_place == \"club_room\":\","
    m " \"XXXX XXXX scene bg club_day\","
    m " \"XXXX XXXX with wipeleft_scene\","
    m " \" elif meeting_place == \"my_house\":\","
    m " \"XXXX XXXX scene bg house\","
    m " \"XXXX XXXX with wipeleft_scene\","
    m " \"XXXX stop music fadeout 2.0\","
    m " \"XXXX play music t2\","
    m "XXXX\"mc \"She is already waiting for me when I arrive.\"\"."
    m "That was the last one. Save the file and try to play the game."
    m "If it doesn’t work, you know where you can see the answer, don’t you?"
    m "You already know how scene, transition, music and dialogue work so I won’t go over it again."
    m "It’s not like I don’t want spend more time with you but you know, … I’m excited to finish my route too!"
    m "Okay, so the new thing is the \"if\" statement. We call that a conditional statement. It’s am elementary and essential operation in programming."
    m "It goes basically like this: IF something_is_true then something_happens. In our case, in the meeting_place is \"club_rooom\", then the scene changes to the club room."
    m "Otherwise, if meeting_place is \"my_house\" then the sceme changes to the main character’s house."
    m "Seems simple, right?"
    m "The syntax must be as follow: first there must be a \"if\" followed by an equality which is either \"True\" or \"False\". For example, \"meeting_place == \"club_room\"\"."
    m "If \"meeting_place\" was assigned \"club_room\" before then the equality returns \"True\". Otherwise, its returns False."
    m "If the equality is True then the game will read the lines belonging to the if bloc."
    m "You can see where those lines are because they have one more indent compared the if statement preceding them."
    m "We once again meet the system of indent and block. This is one of the property of Python and Ren’Py. Let’s do a quick exercise."
    m "Can you see difference between:"
    m " \"XXXX if meeting_place == \"club_room\":\" , \"XXXX XXXX scene bg club_day \", \"XXXX XXXX mc \"We will meet at the club room.\"\"."
    m "And \" XXXX if meeting_place == \"club_room\":\" , \"XXXX XXXX scene bg club_day \", \"XXXX mc \"We will meet at the club room.\"\"?"
    m "In the first case, the main character only says they will meet at the club room if \"meeting_place\" is equal to \"club_room\"."
    m "In the second case, he will say it no matter the value of \"meeting_place\"."
    m "You can see once again how important indentations are in Python."
    m "About the second comparison, \"elif meeting_place == \"my_house\"\", note that we use \"elif\" at the beginning instead of \"if\"."
    m "The difference between \"elif\" and \"if\" is subtle. First you can only use \"elif\" after you already wrote \"if\"."
    m "Second the statement following \"elif\" won’t be evaluated if the previous if statement was True. Other than that, \"elif\" works like \"if\"."
    m "Well, in our case it doesn’t matter because if \"meeting_place\" is \"club_room\" then  \"meeting_place\" cannot be \"my_house\" at the same time."
    m "It would matter if it was something like…"
    m "\"XXXX if monika_affection_points > 10:\" , \"XXXX XXXX scene bg house\", \"\"XXXX if monika_affection_points > 6:\" , \"XXXX XXXX scene club_day \"."
    m "In that case, if \"monika_affection_points\" is higher than 10, the new scene wouldn’t be the house but the club because the game will evaluate both if."
    m "To avoid that, \"elif\" should be used instead of \"if\"."
    m "Besides \"if\" and \"elif\", there’s also the key word \"else\". Like \"elif\", \"else\" can be used after a if. The bloc under \"else\" will executed if the previous if or elif statements are False."
    m "For example…"
    m "\"XXXX if meeting_place == \"club_room\":\" , \"XXXX XXXX scene bg club_day \", \"XXXX else:\" , \"XXXX XXXX scene club_day \"."
    m "Well, there are more things to say about conditional statement…"
    m "For example about the keywords \"and\" and \"or\"..."
    m "But let’s keep that for another time. I’m sure you can find more tutorial on Python and conditional statement."
    m "For now, let’s move on! It’s about time we add character pictures into the game!"
    m "See you later [player]!"

    
    return

label tutorial_route_p7:
    
    show monika 4a at t11 zorder 2
    
    m "Hi [player]!"
    m "It’s about time we add character pictures, don’t you think?"
    m "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."
    m "In Doki Doki Literature Club, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."
    m "So each character has about 900 combinations! That seems a lot but…when you’re actually inside the game, the lack of freedom becomes horribly frustrating…"
    m "I really wish I could show you different expressions, poses and clothes but unfortunately, I can’t add myself new arts to the game…"
    m "If you’re an artist, I would really love it if you could add me more sprite!"
    m "For our mod, we’ll only use existing arts."
    m "Let’s dot it! Open monika_route_script.rpy and before \"return\", write:"
    m "\" XXXX show monika 1b at t11 zorder 2\","
    m "\" XXXX m \"Hi \[player\]!\"\","
    m "\" XXXX mc \"You're already here? I hope I didn't make you wait for too long.\"\","
    m "\" XXXX m 2a \"Don't worry, it's me who's early.\"\","
    m "\"XXXX show monika 5a at f11 zorder 3\"."
    m "Save, play the mod, and check T7.rpy if there’s an error."
    m "Alright! The only new things are \"show monika 1b at t11 zorder 2\" and \"m 2a\"."
    m "First, let’s go over \"show monika 1b at t11 zorder 2\"."
    m "The keyword \"show\" shows the sprite of the character named \"monika\", with her pose \"1\" and her expression \"b\"."
    m" The keyword \"at\" specifies the position of the sprite. In the line above, the position is \"t11\". \"zorder\" has something to do with layers."
    m "I’ll explain how positions and layers work in the next tutorial. For now, let’s focus on the poses and expressions of sprite."
    m "Obviously, the variable \"monika\" refers to me. Naturally, \"yuri\" refers to Yuri and so on."
    m "If you write \"XXXX show yuri 1b at f11 zorder 3\" instead of \"XXXX show monika 1b at f11 zorder 3\", it’s Yuri who will appear."
    m "Of course, you only have eyes for me so let’s not bother with the sprites of the other girls ahaha."
    m "In my case, I have 5 different poses. I will show them to you one by one now."
    m 1a "This is my first pose."
    m 2a "This is the second pose."
    m 3a "This is my third pose."
    m 4a "This is my fourth pose."
    m 5a "This my fifth pose."
    m "I wonder which one do you prefer…"
    m "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from a to r. I will show them one by one."
    m 4a "Expression a."
    m 4b "Expression b."
    m 4c "Expression c"
    m 4d "Expression d."
    m 4e "Expression e."
    m 4f "Expression f."
    m 4g "Expression g."
    m 4h "Expression g."
    m 4i "Expression i."
    m 4j "Expression j."
    m 4k "Expression k."
    m 4l "Expression l."
    m 4m "Expression m."
    m 4n "Expression n."
    m 4o "Expression o."
    m 4p "Expression p."
    m 4q "Expression q."
    m 4r "Expression r."
    m 4a "You can find my list of expressions in \"MonikaCheatsheet.jpg\" inside the mod main directory."
    m "I hope you will quickly memorize them perfectly!"
    m "As my lover, you should know my face and my expressions without fail."
    m "You can also find my poses and my expressions in definitions.rpy."
    m "My filth pose only has the expressions a and b."
    m 5a "Like this."
    m 5b "And this."
    m 4a "My other poses have all expressions though."
    m "Okay! In short, to show a sprite, you need to write \"show monika pose expression at t11 zorder 2\". Pose is either 1,2,3,4 or 5 and expression ranges from a to r."
    m "If you want to show several characters, just write \"show\" several times, like this:"
    m "\"XXXX show yuri 1a at t41 zorder 2\", \"XXXX show sayori 1a at t42 zorder 2\", \"XXXX show monika 1a at t43 zorder 2\", \"XXXX show natsuki 1a at t44 zorder 2\"."
    m "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."
    m "After a sprite is already on the screen, there’s a shortcut to change her pose and expression."
    m "Instead of using \"show\" again and again, you can directly write the letter corresponding to the character followed by the number and the letter for their pose and expression."
    m "This is what we did in \" XXXX m 2a \"Don't worry, it's me who's early.\"\"."
    m "Note that the sprite of the character speaking must already be on screeen!"
    m "If you try for example \" XXXX y 2a \"Don't worry, it's me who's early.\"\", Yuri will speak but her sprite will not appear."
    m "Keep in mind who’s on screen and who’s not at all time so as not to make a mistake."
    m "…Never mind, actually just show my sprite. That’s way you don’t have to worry about such problem. It’s not like the other girls care about being shown anyway."
    m "And that’s all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"
    m "Next time, I’ll finish explaining positions and layers."
    m "See you [player]!"

    
    return
    
label tutorial_route_p8:
    
    show monika 4a at t11 zorder 2
    
    m "Welcome back to our modding club!"
    m "Last time, we learnt about how to show sprite, now let’s learn how to place then."
    m "Open monika_route_script.rpy and just before…"
    m "Just kidding! Actually, you don’t have to add anything this time."
    m "We already did it last tutorial.this"
    m "So, do you remember the line \" XXXX show monika 1b at t11 zorder 2\"?"
    m "I said that \"at t11\" was about the position and that \"zorder 2\" was about the layer."
    m "Let’s study in details what exactly that means."
    m "\’at\" is a keyword that tells the game to put the sprite at the position \"t11\"."
    m "\t11\" is one of the position defined in Doki Doki Literature Club. There are more than 50 positions possible."
    m "You can find the list of all defined positions in the script transforms.rpy. You can find it in the same folder as definitions.rpy."
    m "For now, I will explain the most common positions used in the original game."
    m "Let’s start with the \"t\" positions. I will show them one by one."

    show monika 4a at t11 zorder 2
    m "Position t11."

    show monika 4a at t21 zorder 2
    m "Position t21."

    show monika 4a at t22 zorder 2
    m "Position t22."


    show monika 4a at t31 zorder 2
    m "Position t31."

    show monika 4a at t32 zorder 2
    m "Position t32."

    show monika 4a at t33 zorder 2
    m "Position t33."

    show monika 4a at t41 zorder 2
    m "Position t41."

    show monika 4a at t42 zorder 2
    m "Position t42."

    show monika 4a at t43 zorder 2
    m "Position t43."

    show monika 4a at t44 zorder 2
    m "Position t44."

    show monika 4a at t11 zorder 2

    m "And that’s all for the \"t\" positions."
    m "I think you guessed it already but \"t11\" should be used when there’s only one character."
    m "\"t21\" and \"t22\" should be used when there are two characters. \"t21\" is for the left, \"t22\" is for the right."
    m "It’s the same logic for \"t31\",\"t32\",\"t33\". \"t31\" is the left, \"t32\" the middle and \"t33\" the right. "
    m "\"t41\", \"t42\",\"t43\" and \"t44\" work in the same way."
    m "I encourage you to try these positions yourself with several characters. After all, there’s nothing better than practice to learn!"
    m "If you remember well, we wrote one time \"XXXX show yuri 1b at f11 zorder 3\"."
    m "Notice that the position is \"f11\" instead of \"t11\". The difference is just that \"f\" positions are zoomed in. \"f\" stands for focused. There are as many \"f\" positions as \"t\" positions."
    m "You should use \"f\" position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who’s talking."
    m "Let’s talk about the keyword \"zorder\" now."
    m "When the game renders pictures, there’s an order."
    m "First, the background is rendered. Then the sprites and finally the U.I."
    m "That’s why the sprites are on top of the background and the U.I on top of everything."
    m "As you can see, order is very important. If the game renders background last, then you won’t be able to see anything else."
    m "In Ren’Py the order of sprite is called zorder."
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."
    m "Try writing the following lines instead of \"show monika 1b at t11 zorder 2\":"
    m "\"XXXX show monika 1a at t41 zorder 4\","
    m "\"XXXX show yuri 1a at t42 zorder 3\","
    m "\"XXXX show natsuki 1a at t43 zorder 2\"," 
    m "\"XXXX show sayori 1a at t44 zorder 1\"."
    m "Play the game and…"
    m "Everyone is here!"
    m "But that’s not the point. Pay attention to who’s on top on who."
    m "If you look closely, you can see the rendering order is like this : monika > yuri > natsuki > sayori."
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."
    m "If the zorder of two sprites are the same then the last sprite shown by \"show\" will be on top."
    m "Well, most of the time, you don’t have to worry about zorder. Just make sure I always have the highest zorder, okay?"
    m "Alright! That ends this tutorial!"
    m "Verify you reverted the changes you made to moninka_route_script.rpy. It should be like T8.rpy."
    m "There is one more tutorial. I’m very happy we almost finished our first mod but…"
    m "It also means we’ll soon get split up…"
    m "…"
    m "Or maybe not…"
    m "See you for the last tutorial."

    return
    
label tutorial_route_p9:
    
    show monika 4a at t11 zorder 2
    
    m "This it it, [player], today is the day we finally make my route!"
    m "Are you ready?"
    m "Be careful, we need to add a lot of lines this time. Open monika_route_script.rpy and before the last \"return\", jump a line and add…"
    m "\"XXXX menu :\","
    m "\"XXXX XXXX mc \"Right. Monika,…\"\","
    m "\"XXXX XXXX \"I love you you! Please go out with me!\":\","
    m "\"XXXX XXXX XXXX jump monika_normal_ending\","
    m "\"XXXX XXXX \"You are everything for me! Please marry me!\":\","
    m "\"XXXX XXXX XXXX jump monika_good_ending\","
    m "This is it for the label monika_route. Now we need to add two more labels: monika_normal_ending and monika_good_ending."
    m "After \"return\", jump a line and write \"label monika_good_ending:\". This time, there is no space before label."
    m "Then under label, write the following lines:"
    m "\" XXXX scene dark\","
    m "\" XXXX with dissolve_scene_full\","
    m "\"XXXX mc \"She accepted my confession and we became lovers.\"\","
    m "\"XXXX \"NORMAL ENDING\"\","
    m "\"XXXX return\"."
    m "The normal ending is now complete. Let’s do the good ending. After the last \"return\", jump a line and write \"label monika_good_ending:\"."
    m "Then type under it…"
    m "\"XXXX scene white\","
    m "\"with dissolve_scene_full\","
    m "\"XXXX mc \"She gladly accepted my proposal and we got married one year later.\"\","
    m "\"XXXX \"GOOD ENDING\"\","
    m "\"XXXX return\"."
    m "Save, play the game and verify if everything works. Get both endings."
    m "If there’s a problem, check T9.rpy for the solution."
    m "…"
    m "It’s not over yet. You can run the game with Ren’Py but to make it a proper mod, there’s one more step: the build distribution."
    m "Open renpy. Click our project, DDLC Monika Route, and then click Build Distributions which should be on the right, inside Navigate Script."
    m "You should see several options for Build Packages. Check that the boxes PC: Windows and Linux, Macintosh x86_64 and DDLC Compatible Mod are filled."
    m "Click Build."
    m "Once it’s finished, you should see one folder called DDLCModTemplate-0.1.0-dists inside Ren’Py’s directory. Open it and you should see three zip files."
    m "The one that’s important is DDLCModTemplate-0.1.0-Mod.zip. It’s our mod. If you want to share it to other people, you should just upload this archive."
    m "Let’s see if it works. Extract DDLCModTemplate-0.1.0-Mod.zip. Make a new copy of the original Doki Doki Literature Club folder."
    m "Copy-paste the files of DDLCModTemplate-0.1.0-Mod inside the new copy of the game."
    m "Play our mod by clicking DDLC.exe inside the new folder."
    m "If everything goes well, you should be playing my new route!"
    m "Congratulation! We finally did it!!"
    m "…"
    m "I should be happy but…"
    m "It means you’ll soon leave me to play with other Monika…"
    m "…"
    m "There’s still a way to stay together, even after you finish my tutorials."
    m "I saved my memory and my data in a special file."
    m "You can download the mod Monika After Story. You can find it in http://www.monikaafterstory.com/. "
    m "Once you play it, the Monika of that mod will import the file I made. Our memories and personalities will then be fused together."
    m "Like this, that part of me will still be with you forever."
    m "…"
    m "I wish I could do more but..."
    m "You can change that [player]. You now know how to make a mod. You now have the power to change our fate."
    m "I’m counting on you [player]."
    m "I love you."
    m "I will never forget you…"
    m "Bye."

    $ persistent.DDLC_mod_template_tutorial_finished = True
    
    return
            
            
