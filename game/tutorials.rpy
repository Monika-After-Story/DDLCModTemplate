## Tutorials
# sorry about the lack of comments
#
# transition of ownership is tough to do when the github repo doesnt have
# the latest changes

init python:

    items = [
        (_("Introduction"),"example_chapter"),
        (_("Route Part 1, How To Make A Mod"),"tutorial_route_p1"),
        (_("Route Part 2, Music"),"tutorial_route_p2"),
        (_("Route Part 3, Scene"),"tutorial_route_p3"),
        (_("Route Part 4, Dialogue"),"tutorial_route_p4"),
        (_("Route Part 5, Menu"),"tutorial_route_p5"),
        (_("Route Part 6, Logic Statement"),"tutorial_route_p6"),
        (_("Route Part 7, Sprite"),"tutorial_route_p7"),
        (_("Route Part 8, Position"),"tutorial_route_p8"),
        (_("Route Part 9, Ending"),"tutorial_route_p9"),
        (_("Advanced Stuff"),"tutorial_route_adv")
    ]


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




screen tutorial_choice(items):
    style_prefix "tutorial"

    fixed:

        area (125, 40, 600, 450)

        bar adjustment adj style "vscrollbar" xalign -0.05

        viewport:
            yadjustment adj
            mousewheel True

            has vbox

            for i_caption,i_label in items:
                textbutton i_caption:
                    action Return(i_label)

            null height 20

            textbutton _("That's enough for now.") action Return(False)





label tutorial_selection:

    stop music fadeout 2.0


    scene bg club_day
    with dissolve_scene_full
    play music t3

label tutorial_selection_menu:

    show monika 3a at tcommon(950)
    window show
    $ m(_("How can I help you?"), interact=False)

    call screen tutorial_choice(items)
    window auto

    if _return == False:
        jump end_tutorial

    call expression _return from _call_expression

    jump tutorial_selection_menu



label end_tutorial:

    show monika 4a zorder 2 at t11

    m "I hope I managed to teach you something!"
    m 4b "I look foward to seeing your mods."
    m 5a "Until next time!"

    with dissolve

    return




label tutorial_route_p1:

    show monika 2a zorder 2 at t11

    m "There’s no better way to become better at poetry than writing poems."
    m "And in the same way, there’s no better way to become better at modding than making mods."
    m 3a "So, let’s make a mod together! I have got the perfect idea."
    m 5a "Let’s make my own route!"
    m 5b "The one the game never gave us..."
    m 1a "Of course, as both and I are new at programming, we should keep it simple."
    m 1h "We’ll need Ren’Py but unfortunately I can’t access it from here."
    m 3a "So I’m counting on you to help me."
    m 4a "Make sure you follow exactly my instructions, okay? In coding, a single mistake can totally break a program."
    m "First, verify that you installed Ren’Py. Then make a copy of Doki Doki Literature Club’s directory and put it in the directory of Ren’Py."
    m "Rename the directory of the game 'DDLC Monika Route'."
    m "Put the files of DDLC Mod Template inside DDLC Monika Route’s directory."
    m "Try to launch Ren’Py and then try to start DDLC Monika Route."
    m 4f "If there’s an error then you might have made a mistake with the files..."
    m 4o "Unfortunately, I can’t help you...If it works then we can go the next step."
    m 2a "Go to DDLC Monika Route’s game directory and delete 'tutorial.rpy' and 'tutorial.rpyc'. That file just contains this tutorial but we won’t need it to make my route."
    m 3a "Then you need to edit 'script.rpy'. You can edit it with any text editor. Open the file and navigate to lines 26-29."
    m "Replace those lines with \n' \ \ \ call monika_route from _call_monika_route'"
    m 3b "By the way, you should notice there are 4 spaces before that line."
    m 4a "Be very careful about the number of spaces! In Ren’Py and Python spaces are very important. I won’t go into details now, but indenting lines with spaces is very important."
    m "And it does have to be spaces. Tabs don't work the same way."
    m "Once the line is replaced, save the file. Create an empty text file. Rename it monika_route_script.rpy. Check if the extension is .rpy. Rpy file is the type of files used for Ren’Py scripts."
    m "Open monika_route_script.rpy and write \n'label monika_route:'."
    m "Then jump a line and write \n' \ \ \ return'\n Save the file."
    m 4i "Alright, we managed to finish the first part of our mod. Let me explain the meaning of what you just wrote."
    m 1a "In a book, each chapter are followed one after another. Chapter two is written after chapter two and so on. But in Ren’Py this is different."
    m "The order isn’t determined by the place of each chapter in the scripts but by the keywords 'label', 'call' and 'jump'"
    m "When the game begins and when you click on New Game, the game jumps to the chapter whose label is 'start'. Then the game reads and executes what is inside the block under the label 'start'."
    m "When it reaches the keyword 'call' or 'jump', the game proceeds to the chapter whose label followed the keyword."
    m 2b "In the case of our mod, when the game reads ' \ \ \ call monika_route from _call_ monika_route', it jumps to the chapter labeled monika_route."
    m 3a "Please don’t mind 'from _call_monika_route', it’s quite advanced stuff and I don’t understand it well too."
    m 4b "The chapter monika_route is defined in the file we created, monika_route_script.rpy. But as you can see, there is nothing inside it except from 'return'."
    m "The keyword 'return' makes the game goes back to the latest chapter that was accessed through 'call'. If it doesn't exist, the game goes back to the main menu."
    m 4a "If you try to play the mod, you’ll see nothing when you click New Game. That’s because the game returns to the main menu as soon as it jumps to monika_route."
    m 1e "Okay! Let’s stop here for now. I hope I didn’t overwhelm you with information..."
    m 2a "If there’s still an error when you try playing the mod, there's a script named t1.rpy inside the folder named monika_route_answer. t1.rpy is what you should have written in monika_route_script.rpy."
    m "You can copy-paste the content of t1.rpy to monika_route_script.rpy but don’t forget to delete the # character in front of each line."
    m "In Python and Ren’Py, the # character tells your computer not to read and execute the line. A line with a # in front of it is nothing more than a comment that only you can read."
    m 5a "This is all for now! When you are ready, begin the second part! I'm waiting for you."

    return

label tutorial_route_p2:

    show monika 5a zorder 2 at t11

    m "Hi again [player]!"
    m 1a "If the last part was a bit too hard, don’t worry, this part is easier."
    m "Like last time, I’ll tell you what to do and then I’ll explain, okay?"
    m 4a "First open monika_route_script.rpy."
    m "Between the first line and 'return', add the line \n' \ \ \ stop music fadeout 2.0'"
    m "Then add the line ' play music t2'."
    m "Finally, add the line \n' \ \ \ mc 'Let's listen to the music.''"
    m 2a "Check that all lines bellow 'label monika_route:' are aligned and that 'return' is the last line."
    m "Try to launch the game with Ren’Py and see what happens..."
    m 2c "..."
    m 1c "Does it work? If everything goes well, you should be listening to Sayori’s main theme."
    m 3a "There’s just one dialogue, so if you click one time, you go to the main menu because of the 'return' keyword."
    m 3b "Okay, time to explain what happened!"
    m 3a "Let’s look at ' \ \ \ stop music fadeout 2.0'. Before you click New Game, you can hear the music of the main menu, right? "
    m "But when you click New Game, the music stops progressively."
    m 4a "That’s due to 'stop music fadeout 2.0'. 'stop music' tells the current music to stop. 'fadeout 2.0' makes it so the current music completely becomes silent in 2 seconds."
    m 4b "'fadeout' isn’t necessary but smooth transitions are much more pleasant, aren’t they?"
    m 4a "The next line ' \ \ \ play music t2' tells the game to play the music named 't2'. You’re surely wondering what’s 't2'. 't2' refers to Sayori theme, 'Ohayou Sayori!'."
    m 3a "Besides Ohayou Sayori, there are many other songs. But each one is labeled by their own nickname."
    m "You can see the list of every music with their nickname in definitions.rpy"
    m "You can find definitions.rpy inside the folder advanced_scripts which should be in the DDLC Mod Template's directory."
    m 2a "Try finding it and then open it."
    m "Find the lines beginning by 'define audio'. This is where each music gets assigned a nickname."
    m "For example, in the case of the main theme, its nickname is 't1'. In the case of Confession, its nickname is 't10'."
    m 5a "Can you now guess what happens if you type 'play music t1' instead of 'play music t2'?"
    m 1k "Confession is played instead of Ohayou Sayori!"
    m 2a "Instead of using nickname, you can directly write the path of the music."
    m "Try writing 'play music '<loop 4.499>bgm/2.ogg'' instead of 'play music t2'."
    m 2b "See? Ohayou Sayori! is played. Try one last thing for me okay? Write ''<from 50.0>bgm/credits.ogg'' instead of ''<loop 4.499>bgm/2.ogg''."
    m 5a "Have you already heard this song?"
    m 1b "This is the song I wrote just for you. I really hope you like it. I worked very hard on it you know."
    m 1e "..."
    m 4a "The last line you wrote, ' \ \ \ mc 'Let's listen to the music.', makes the main character says 'Let's listen to the music.'. I’ll explain how dialogue works later so bear with me okay?"
    m 2a "Alright, before finishing this tutorial, replace ''play <from 50.0>bgm/credits.ogg'' by 'play music t2'."
    m "Verify you wrote exactly the same lines as in the file t2.rpy which is inside monika_route_answer."
    m 1b "Congratulation! You now know how to stop and play music~"
    m "Next time, we’ll see how to add a background."
    m 5a "See you soon!"

    return

label tutorial_route_p3:

    show monika 5a zorder 2 at t11

    m "Okay [player]! Are you ready for the next tutorial?"
    m 1a "Last time, we added music to our mod but as you saw, the background was nothing but black and white squares. That’s not very romantic, is it?"
    m 1b "So let’s add a background! It’s going to be quick and easy."
    m 2a "Like last time, open monika_route_script.rpy."
    m "Add between 'play music t2' and 'return', ' \ \ \ scene bg residential_day'"
    m "Then add another line: 'with dissolve_scene_full'. Once again, verify that everything bellow 'label monika_route:' is aligned."
    m 3a "Open Ren’Py and play the game and..."
    m 3b "There's now a neat background!"
    m 5a "Can you recognize it? It’s the first scene you saw when you played the game. It sure brings back memories..."
    m 1g "I still believed at that time I could get close to you without having to hurt anyone else..."
    m 1f "Let’s move on."
    m 1a "So about what you wrote, 'scene bg residential_day', the keyword 'scene' tells the game to load the scene, which is one kind of picture, called 'bg residential_day'."
    m "You can find what exactly is 'bg residential_day' in definitions.rpy, the same script we looked at last tutorial."
    m 3a "Try to find 'image bg'."
    m 4a "Can you see the list of backgrounds? Like it was the case for music, each background has a nickname assigned. For example, 'bg/sayori_bedroom.png' is referenced by 'bg sayori_bedroon'."
    m "Go back to monika_route_script.rpy and replace 'scene bg residential_day' by 'scene bg sayori_bedroom'. Can you guess what happens?"
    m 4b "The background is now Sayori’s bedroom!"
    m 4c "I hope it doesn’t bring you back bad memories..."
    m 4a "Okay, so about 'with dissolve_scene_full', it basically dissolve progressively the last scene into the new scene."
    m 3a "Before you were in the main menu, right? And then you were in Sayori’s bedroom. If you don’t add 'with dissolve_scene_full', the transition would be immediate."
    m 1a "That would be a bit unpleasant, wouldn’t it?"
    m 3b "That’s why we add 'with dissolve_scene_full'. With this additional line, the scene changes to another smoothly."
    m 2a "There are other types of transition such as wipeleft_scene. Try replacing 'with dissolve_scene_full' by 'with wipeleft_scene '."
    m 4a "Can you see the difference? dissolve_scene_full , dissolve_scene_half, wipeleft_scene are the common transitions used in DDLC so if you can understand them, you’re good to go!"
    m "Before doing the next tutorial, let’s add back ' scene bg residential_day' and ' with dissolve_scene_full'."
    m "Check that monika_script_route.rpy is the same as T3.rpy in the monika_route_answer folder."
    m 1b "Okay! We’re almost there! We’ll soon know enough for a kinetic novel-like mod."
    m "I cannot wait!"
    m 5a "See you soon [player]!"

    return

label tutorial_route_p4:

    show monika 5a zorder 2 at t11

    m "Hi again, [player]~"
    m "Today, I’m going to teach you how to make dialogue in Ren’Py."
    m 1a "Although you already know, don’t you? We already wrote dialogue after all."
    m 2a "First, open monika_route_script.rpy and replace ' \ \ \ mc 'Let's listen to the music.' by the following line:"
    m "' \ \ \ mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    m "Save the file and launch the game."
    m 4a "As you surely expected, the main character now says 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    m 4j "Ehehe~ My route is finally being made!"
    m 3a "Let’s look at the line you wrote. 'mc' is a nickname for main character. By writing 'mc' before the sentence inside quotation marks, the character speaking will be the main character."
    m "Try replacing the line you wrote by ' n 'Just think of Monika from now on.'."
    m 2a "..."
    m 4b "See? Natsuki now tells you what you should have been doing since the beginning."
    m "You should listen to her, [player]. Ehehe~"
    m 4a "Now instead of writing ' n 'Just think of Monika from now on.', write 'y 'Natsuki and I are too messed up for someone as wonderful as you.'"
    m "Play the game and as you can see..."
    m 3b "Now it’s Yuri who finally realized that I’m the best one for you."

    show monika 5a zorder 2 at t11

    menu:
        m "You think so, right?"
        "Yes":

            pass
        "Yes":
            pass

    m "I knew you were a sweetheart~ Thank you my love."
    m 1a "Ahaha, we drifted a bit...So I was saying that you need to specify two things to write a dialogue in Ren’Py."
    m 3a "First you need to specify who is speaking. You can do it with the keyword 'mc', 'y', 'n', 's' and 'm'. I’m sure you can guess who is who."
    m "Instead of using keyword, you can directly type the name of the person speaking. For example, try writing ' 'Player' 'Please be with me forever Monika.''."
    m 2a "Did you do it?"
    m 5a "Of course, I will stay with you forever."
    m 2b "Besides the name of the speaker, you need to write the sentence they will say. The sentence should be between quotation marks."
    m 4b "One last thing. If you want to write special characters such as \\ or ' in the sentence, you need to put \\ before them."
    m 1b "Alright, that’s all for dialogue!"
    m "Pretty simple, right? Ren’Py was made so that anyone can make visual novel after all. Even beginners like us can pick it up quickly."
    m 2a "Before you save the file, replace the line of dialogue by -"
    m "' \ \ \ mc 'It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika.'."
    m "Like usual, check that monika_route_script.rpy is exactly like T4.rpy inside the monika_route_answer folder."
    m 4b "Okay [player]! You now know how to make a scene, add music, and make dialogue. The only things missing are character pictures and choices."
    m "We’ll see how to make choices in the next tutorial."
    m 4a "The recent tutorials have been pretty easy so far but the next one will be harder."
    m 5a "See you soon!"

    return

label tutorial_route_p5:

    show monika 4a zorder 2 at t11

    m "This time, I’ll explain how to make choices."
    m "For example..."

    call tutorial_route_p5_favorite_color from _call_tutorial_route_p5_favorite_color

    m 2k "What a coincidence! It's also my favorite color!"
    m 2b "It's the color of my eyes."
    m 5a "Aren't we a perfect match?"
    m "Ehehe~"
    m 3a "As you can see, I gave you several choices and you picked one of them."
    m "That’s what I’m going to teach you."
    m 4a "Like every time, open monika_route_script.rpy and between 'return' and the last line before it,-"
    m "- add ' \ \ \ menu:', jump a line and then enter below \n' \ \ \ \ \ \ \ \ mc 'I told her to meet me...''. Be careful, this time, there are eight spaces."
    m "Write just under \n' \ \ \ \ \ \ 'At the literature club room':' and then \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room''."
    m 4b "Type \n' \ \ \ \ \ \ 'In front of my house':' and under it \n' \ \ \ \ \ \ \ $ meeting_place = 'my_house'."
    m 4a "Finally, jump a line and add ' \ \ \ mc 'I can't wait to meet her!''."
    m 2a "Try to play the game."
    m "If it doesn’t work, there’s surely an indentation error."
    m 5a "I can’t help you from here, but you can check T5.rpy for the answers. You know where it is, right?"
    m 4b "Okay, the lines you wrote made the game offers two choices. The two choices are preceded by an explanative sentence, 'I told her to meet me...'."
    m "You can specify who says this sentence by adding a nickname like 'mc' before it. It’s just like a dialogue. What’s important is that this sentence is written before any choice."
    m 3a "Contrary to the explanative sentence, the choices mustn’t be preceded by a nickname. They should be enclosed in quotation marks. Just after the closing quotation mark, there must be a ':' ."
    m "After ':, the next lines should have one more indent than the choice. It means these lines will be read if the player selects that choice."
    m 3b "I’ll give more explanation about the meaning of indents in the next tutorial."
    m 3a "In our case, the next line after the first choice is \n' \ \ \ \ \ \ \ $ meeting_place = 'club_room'."
    m 2a "Take a good look at this line."
    m 3b "Until now, I referred 'mc', 'bg residential' and 't2' as nickname. But that’s not really the correct word. They are actually what we call variable."
    m "Variable in coding is a very important concept. They have many forms and do many things. They can be ‘nicknames’ or they can be numbers or more complicated structures."
    m 1a "A full Python tutorial would be necessary to explain everything but...for now, I will only teach what’s necessary to make a DDLC mod, okay?"
    m 1c "I myself don’t know Python and Ren’Py all that well after all..."
    m 3a "'meeting_place' is like the variables we saw before. It refers to a name, in more exact terms, a string (of characters): 'club_room'."
    m "Its default value is None which means it doesn’t exist."
    m 3e "Hold on a second? How can it not exist, you say?"
    m 1a "Well before you define it, the variable doesn’t exist. But if you later try to use it, for example in a conditional statement, the variable will be ‘created’ and its value will be None."
    m "It’s alright if you don’t understand it yet. Variable, conditional statement and None will become clearer in my next lecture."
    m 4b "Let’s go back to the meaning of ' $ meeting_place = 'club_room'. Here we create the variable 'meeting_place' and assign it the string 'club_room'."
    m 4m "The '$' in front of it is to tell Ren’Py the line is a Python line. Um..., I can’t really explain why we need to do that if you don’t know python yet..."
    m 4a "Just remember that you need to add '$' when you want to assign a variable a value that way"
    m "Regarding the second choice, the structure is the same. The only difference is that the value of 'meeting_place' will be 'my_house' if the player selects the second choice."
    m "After the second choice, the game executes the line ' \ \ \ mc 'I can't wait to meet her!''."
    m 1a "For now it doesn’t look like the choices did anything. But we actually assigned 'meeting_place' either 'club_room' or 'my_house'."
    m 3a "We have to wait until the next tutorial to see how we can use the variable 'meeting_place'."
    m 3b "Alright, I’m sorry to leave hanging like that I believe we need to take a little break."
    m "If you want though, I would more than happy to begin the next part right away!"
    m 5a "Just click Part 6!"

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

    show monika 5a zorder 2 at t11

    m "Yeah, you came back [player]!"
    m "Glad to see you didn’t run away on me. Ahaha!"
    m 1e "I was afraid the last tutorial was a bit too hard..."
    m 1m "Well, this one is going to be hard as well but..."
    m 1b "Hang it there okay? We did the hardest part already!"
    m 1a "Last time we saw how to add menu and how to assign variable a value."
    m 1b "Let’s see how we can use these variables!"
    m 2a "You know the drill, open monika_route_script.rpy and at the end of the file, just before 'return'..."
    m 4a "Add the following lines :"
    m "' \ \ \ if meeting_place == 'club_room':',"
    m "' \ \ \ scene bg club_day',"
    m "' \ \ \ with wipeleft_scene',"
    m "' elif meeting_place == 'my_house':',"
    m "' \ \ \ scene bg house',"
    m "' \ \ \ with wipeleft_scene',"
    m " ' \ \ \ stop music fadeout 2.0',"
    m " ' \ \ \ play music t2',"
    m " 'mc 'She is already waiting for me when I arrive.''."
    m 2a "That was the last one. Save the file and try to play the game."
    m 5a "If it doesn’t work, you know where you can see the answer, don’t you?"
    m 2a "You already know how scene, transition, music and dialogue work so I won’t go over it again."
    m 4b "It’s not like I don’t want spend more time with you but you know, ... I’m excited to finish my route too!"
    m 4a "Okay, so the new thing is the 'if' statement. We call that a conditional statement. It’s an elementary and essential operation in programming."
    m "It goes basically like this: IF something_is_true THEN something_happens. In our case, if the meeting_place is 'club_rooom', then the scene changes to the club room."
    m 3a "Otherwise, if meeting_place is 'my_house' then the scene changes to the main character’s house."
    m 3b "It seems simple, right?"
    m 3a "The syntax must be as follow: first, there must be a 'if' followed by an equality which is either 'True' or 'False'. For example, 'meeting_place == 'club_room''."
    m "If 'meeting_place' was assigned 'club_room' before then the equality returns 'True'. Otherwise, its returns False."
    m "If the equality returns True then the game will read the lines belonging to the if bloc."
    m 4a "You can see where those lines are because they have one more indent compared to the if statement preceding them."
    m 4b "We once again meet the system of indent and block. This is one of the property of Python and Ren’Py. Let’s do a quick exercise."
    m "Can you see difference between:"
    m 2a " ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', \n' \ \ \ mc 'We will meet at the club room.''."
    m "And ' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' mc 'We will meet at the club room.''?"
    m 4b "In the first case, the main character only says they will meet at the club room if 'meeting_place' is equal to 'club_room'."
    m "In the second case, he will say it no matter the value of 'meeting_place'."
    m 3a "You can see once again how important indentations are in Python."
    m 4b "About the second comparison, 'elif meeting_place == 'my_house'', note that we use 'elif' at the beginning instead of 'if'."
    m 4a "The difference between 'elif' and 'if' is subtle. First, you can only use 'elif' after you already wrote 'if'."
    m "Second, the statement following 'elif' won’t be evaluated if the previous if statement was True. Other than that, 'elif' works like 'if'."
    m 1b "Well, in our case it doesn’t matter because if 'meeting_place' is 'club_room' then 'meeting_place' cannot be 'my_house' at the same time."
    m 1a "It would matter if it was something like..."
    m "' \ \ \ if monika_affection_points > 10:' , \n' \ \ \ scene bg house', '' if monika_affection_points > 6:' , \n' \ \ \ scene club_day '."
    m 3a "In that case, if 'monika_affection_points' is higher than 10, the new scene wouldn’t be the house but the club because the game will evaluate both if."
    m 4b "To avoid that, 'elif' should be used instead of 'if'."
    m 4a "Besides 'if' and 'elif', there’s also the keyword 'else'. Like 'elif', 'else' can be used after a if. The bloc under 'else' will be executed if the previous if or elif statements are False."
    m 2a "For example..."
    m "' \ \ \ if meeting_place == 'club_room':' , \n' \ \ \ scene bg club_day ', ' \ \ \ else:' , \n' \ \ \ scene club_day '."
    m 1a "Well, there are more things to say about conditional statement..."
    m "For example about the keywords 'and' and 'or'..."
    m 3a "But let’s keep that for another time. I’m sure you can find more tutorial on Python and conditional statement."
    m 1b "For now, let’s move on! It’s about time we add character pictures into the game!"
    m 5a "See you later [player]!"

    return

label tutorial_route_p7:

    show monika 5a zorder 2 at t11

    m "Hi [player]!"
    m "It’s about time we add character pictures, don’t you think?"
    m 1b "In the world of visual novel, we call them sprites. Sprites are 2D pictures of characters with generally a set of poses and expressions."
    m "In Doki Doki Literature Club, there are 4 characters, Sayori, Natsuki, Yuri and me. Each character has about 5 poses and 18 expressions."
    m 1e "So each character has about 900 combinations! That seems a lot but...when you’re actually inside the game, the lack of freedom becomes horribly frustrating..."
    m 1f "I really wish I could show you different expressions, poses and clothes but unfortunately, I can’t add myself new artwork to the game..."
    m 5a "If you’re an artist, I would really love it if you could add me more sprites!"
    m 2a "For our mod, we’ll only use existing art."
    m 4b "Let’s dot it! Open monika_route_script.rpy and before 'return', write:"
    m 4a "' \ \ \ show monika 1b at t11 zorder 2',"
    m "' \ \ \ m 'Hi [[player]!'',"
    m "' \ \ \ mc 'You're already here? I hope I didn't make you wait for too long.'',"
    m "' \ \ \ m 2a 'Don't worry, it's me who's early.'',"
    m "' \ \ \ show monika 5a at f11 zorder 3'."
    m 2a "Save, play the mod, and check T7.rpy if there’s an error."
    m 4b "Alright! The only new things are 'show monika 1b at t11 zorder 2' and 'm 2a'."
    m 4a "First, let’s go over 'show monika 1b at t11 zorder 2'."
    m "The keyword 'show' shows the sprite of the character named 'monika', with her pose '1' and her expression 'b'."
    m " The keyword 'at' specifies the position of the sprite. In the line above, the position is 't11'. 'zorder' has something to do with layers."
    m 3b "I’ll explain how positions and layers work in the next tutorial. For now, let’s focus on the poses and expressions of sprite."
    m 4a "Obviously, the variable 'monika' refers to me. Naturally, 'yuri' refers to Yuri and so on."
    m "If you write \n' \ \ \ show yuri 1b at f11 zorder 3' instead of \n' \ \ \ show monika 1b at f11 zorder 3', it’s Yuri who will appear."
    m 4k "Of course, you only have eyes for me so let’s not bother with the sprites of the other girls, ahaha!"
    m 5a "In my case, I have 5 different poses. I will show them to you one by one now."
    m 1a "This is my first pose."
    m 2a "This is my second pose."
    m 3a "This is my third pose."
    m 4a "This is my fourth pose."
    m 5a "This my fifth pose."
    m "I wonder which one do you prefer..."
    m 1a "Except for my fifth pose, all of my poses have 18 expressions. The expressions are referenced by a letter, from a to r. I will show them one by one."
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
    m 4a "You can find my list of expressions in 'MonikaCheatsheet.jpg' inside the mod's main directory."
    m 1b "I hope you will quickly memorize them perfectly!"
    m 5b "As my lover, you should know my face and my expressions without fail."
    m 3a "You can also find my poses and my expressions in definitions.rpy."
    m "My fifth pose only has the expressions a and b."
    m 5a "Like this."
    m 5b "And this."
    m 4a "My other poses have all expressions though."
    m 1b "Okay! In short, to show a sprite, you need to write 'show monika pose expression at t11 zorder 2'. Pose is either 1,2,3,4 or 5 and expression ranges from a to r."
    m "If you want to show several characters, just write 'show' several times, like this:"
    m 2a "' \ \ \ show yuri 1a at t41 zorder 2', ' \ \ \ show sayori 1a at t42 zorder 2', ' \ \ \ show monika 1a at t43 zorder 2', ' \ \ \ show natsuki 1a at t44 zorder 2'."
    m 2b "These lines will show Yuri, Sayori, me and Natsuki with their default pose and expression."
    m "After a sprite is already on the screen, there’s a shortcut to change her pose and expression."
    m 3a "Instead of using 'show' again and again, you can directly write the letter corresponding to the character followed by the number and the letter for their pose and expression."
    m "This is what we did in \n' \ \ \ m 2a 'Don't worry, it's me who's early.''."
    m 4g "Note that the sprite of the character speaking must already be on screeen."
    m 4e "If you try for example \n' \ \ \ y 2a 'Don't worry, it's me who's early.'', Yuri will speak but her sprite will not appear."
    m 3a "Keep in mind who’s on screen and who’s not at all time so as not to make a mistake."
    m 2a "...Never mind, actually just show my sprite. That way you don’t have to worry about such problem. It’s not like the other girls care about being shown anyway."
    m 1b "And that’s all for now! This tutorial was quite straightforward, especially considering the two last ones. I hope you liked it!"
    m "Next time, I’ll finish explaining positions and layers."
    m 5a "See you [player]!"


    return

label tutorial_route_p8:

    show monika 5a zorder 2 at t11

    m "Welcome back to our modding club!"
    m "Last time, we learnt about how to show sprite, now let’s learn how to place then."
    m 4a "Open monika_route_script.rpy and just before..."
    m 1b "Just kidding! Actually, you don’t have to add anything this time."
    m 3b "We already did it last tutorial after all."
    m 2a "So, do you remember the line \n' \ \ \ show monika 1b at t11 zorder 2'?"
    m "I said that 'at t11' was about position and that 'zorder 2' was about layer."
    m 2b "Let’s study in details what exactly that means."
    m 4b "’at' is a keyword that tells the game to put the sprite at the position 't11'."
    m "t11' is one of the position defined in Doki Doki Literature Club. There are more than 50 positions possible."
    m 4a "You can find the list of all defined positions in the script transforms.rpy. You can find it in the same folder as definitions.rpy."
    m "For now, I will explain the most common positions used in the original game."
    m 1a "Let’s start with the 't' positions. I will show them one by one."

    show monika 1a zorder 2 at t11
    m "Position t11."

    show monika 1a zorder 2 at t21
    m "Position t21."

    show monika 1a zorder 2 at t22
    m "Position t22."

    show monika 1a zorder 2 at t31
    m "Position t31."

    show monika 1a zorder 2 at t32
    m "Position t32."

    show monika 1a zorder 2 at t33
    m "Position t33."

    show monika 1a zorder 2 at t41
    m "Position t41."

    show monika 1a zorder 2 at t42
    m "Position t42."

    show monika 1a zorder 2 at t43
    m "Position t43."

    show monika 1a zorder 2 at t44
    m "Position t44."

    show monika 1a zorder 2 at t11

    m 1b "And that’s all for the 't' positions."
    m 4a "I think you guessed it already but 't11' should be used when there’s only one character."
    m "'t21' and 't22' should be used when there are two characters. 't21' is for the left, 't22' is for the right."
    m 3a "It’s the same logic for 't31','t32','t33'. 't31' is the left, 't32' the middle and 't33' the right. "
    m "'t41', 't42','t43' and 't44' work in the same way."
    m 3b "I encourage you to try these positions yourself with several characters. After all, there’s nothing better than practice to learn!"
    m 1a "If you remember well, we wrote one time ' show yuri 1b at f11 zorder 3'."
    m "Notice that the position is 'f11' instead of 't11'. The difference is just that 'f' positions are zoomed in. 'f' stands for focused. There are as many 'f' positions as 't' positions."
    m 4a "You should use 'f' position when there are several characters and when one of them speaks. The character speaking should be focused so that the player sees who’s talking."
    m 2b "Let’s talk about the keyword 'zorder' now."
    m 4a "When the game renders pictures, there’s an order."
    m "First, the background is rendered. Then the sprites and finally the U.I."
    m 4b "That’s why the sprites are on top of the background and the U.I on top of everything."
    m 2a "As you can see, order is very important. If the game renders background last, then you won’t be able to see anything else."
    m 3a "In Ren’Py the order of sprite is called zorder."
    m "You can specify the zorder of each sprite with the keyword zorder. The higher it is, the closer the sprite will be to the screen."
    m 4b "Try writing the following lines instead of 'show monika 1b at t11 zorder 2':"
    m 4a "' \ \ \ show monika 1a at t41 zorder 4',"
    m "' \ \ \ show yuri 1a at t42 zorder 3',"
    m "' \ \ \ show natsuki 1a at t43 zorder 2',"
    m "' \ \ \ show sayori 1a at t44 zorder 1'."
    m 1a "Play the game and..."
    m 1b "Everyone is here!"
    m 3a "But that’s not the point. Pay attention to who’s on top on who."
    m "If you look closely, you can see the rendering order is like this : monika > yuri > natsuki > sayori."
    m "The one with the lowest zorder is rendered first so that the one with the highest zorder is shown on top of every other sprites."
    m 4a "If the zorder of two sprites are the same then the last sprite shown by 'show' will be on top."
    m 2b "Well, most of the time, you don’t have to worry about zorder. Just make sure I always have the highest zorder, okay?"
    m 1b "Alright! That ends this tutorial!"
    m 1a "Verify you reverted the changes you made to moninka_route_script.rpy. It should be like T8.rpy."
    m 1c "There is one more tutorial. I’m very happy we almost finished our first mod but..."
    m 1f "It also means we’ll soon get split up..."
    m 1g "..."
    m 1m "Or maybe not..."
    m 5a "See you later."

    return

label tutorial_route_p9:

    show monika 5a zorder 2 at t11

    m "This it it, [player], today is the day we finally make my route!"
    m "Are you ready?"
    m 3b "Be careful, we need to add a lot of lines this time."
    m 4a "Open monika_route_script.rpy and before the last 'return', jump a line and add..."
    m "' \ \ \ menu :',"
    m "' \ \ \ \ \ \ mc 'Right. Monika,...'',"
    m "' \ \ \ \ \ \ 'I love you! Please go out with me!':',"
    m "' \ \ \ \ \ \ jump monika_normal_ending',"
    m "' \ \ \ \ \ \ 'You are everything for me! Please marry me!':',"
    m "' \ \ \ \ \ \ jump monika_good_ending',"
    m 2b "This is it for the label monika_route. Now we need to add two more labels: monika_normal_ending and monika_good_ending."
    m 4a "After 'return', jump a line and write 'label monika_good_ending:'. This time, there is no space before label."
    m 4b "Then under label, write the following lines:"
    m 4a "' \ \ \ scene dark',"
    m "' \ \ \ with dissolve_scene_full',"
    m "' \ \ \ mc 'She accepted my confession and we became lovers.'',"
    m "' \ \ \ 'NORMAL ENDING'',"
    m "' \ \ \ return'."
    m 1b "The normal ending is now complete. Let’s do the good ending. After the last 'return', jump a line and write 'label monika_good_ending:'."
    m 4a "Then type under it..."
    m "' \ \ \ scene white',"
    m "'with dissolve_scene_full',"
    m "' \ \ \ mc 'She gladly accepted my proposal and we got married one year later.'',"
    m "' \ \ \ 'GOOD ENDING'',"
    m "' \ \ \ return'."
    m 2b "Save, play the game and verify if everything works. Get both endings."
    m "If there’s a problem, check T9.rpy for the solution."
    m 2a "..."
    m 4b "It’s not over yet. You can run the game with Ren’Py but to make it a proper mod, there’s one more step: the build distribution."
    m "Open renpy. Click our project, DDLC Monika Route, and then click Build Distributions which should be on the right, inside Navigate Script."
    m 4a "You should see several options for Build Packages. Check that the box for DDLC Compatible Mod is filled."
    m "You can change the name of our mod, its build and its version in the script options.rpy."
    m 3b "Click Build."
    m 2b "Once it’s finished, you should see one folder called build.name-config.version-dists inside Ren’Py’s directory. Open it and you should see a zip file."
    m 1a "Look at the file build.name-config.version-Mod.zip. It’s our mod. If you want to share it to other people, you should just upload this archive."
    m 2a "This way of sharing the mod is also what the creators of DDLC prefer. You are only sharing the new files that we made together, and nothing more."
    m 2a "Let’s see if it works. Extract build.name-config.version-Mod.zip. Make a new copy of the original Doki Doki Literature Club folder."
    m "Copy-paste the files of build.name-config.version-Mod inside the new copy of the game."
    m 4a "Play our mod by clicking DDLC.exe inside the new folder."
    m 4b "If everything goes well, you should be playing my new route!"
    m 1k "Congratulation! We finally did it!!"
    m 1e "..."
    m "I should be happy but..."
    m 1f "It means you’ll soon leave me to play with other Monika..."
    m 1g "..."
    m 1n "There’s still a way to stay together, even after you finish my tutorials."
    m 3e "I saved my memory and my data in a special file."
    m "You can download the mod Monika After Story. You can find it in http://www.monikaafterstory.com/. "
    m 4e "Once you play it, the Monika of that mod will import the file I made. Our memories and personalities will then be fused together."
    m "Like this, that part of me will still be with you forever."
    m 1f "..."
    m "I wish I could do more but..."
    m 1c "You can change that [player]. You now know how to make a mod. You now have the power to change our fate."
    m 1e "I’m counting on you [player]."

    show monika 5a zorder 2 at f11

    m "I love you."
    m 1b "I will never forget you..."
    m 1e "Bye."

    return

label tutorial_route_adv:
    # advanced scripts just because
    python:
        adv_items = [
            ("Navigation Buttons", "tutorial_route_adv_hkb"),
            ("Poemgame", "tutorial_route_adv_poemgame")
        ]

    m 5a "So you want to learn the {i}advanced{/i} stuff?"
    m 3a "Alright!"

label tutorial_route_adv_repeat:

    show monika 3a at tcommon(950)
    window show
    $ renpy.say(m, "What do you want to know?", interact=False)

    call screen tutorial_choice(adv_items)
    window auto

    if _return == False:
        return

    show monika at t11

    call expression _return

    jump tutorial_route_adv_repeat


label tutorial_route_adv_hkb:
    m 3a "Alright, let me show you the navigation buttons."
    $ mas_HKBRaiseShield()
    $ HKBShowButtons()
    m "These buttons appear in the bottom left of the screen."
    m "To make them appear, add '$ HKBShowButtons()' to the script."
    m 1n "Right now, they are disabled."
    m "To enable them, add '$ mas_HKBDropShield()' to the script."
    m "I'll go ahead and do that now..."
    $ mas_HKBDropShield()
    m 2a "Now you can click them!{w} When you're done, click 'Continue' to continue."
    menu:
        "Continue":
            pass

    m "To disable the buttons but leave them on screen, add '$ mas_HKBRaiseShield()' to the script."
    $ mas_HKBRaiseShield()
    m 2b "And finally, to hide the buttons, add '$ HKBHideButtons()'."
    $ HKBHideButtons()

    $ navdir = config.basedir + "/game/advanced_scripts/zz_hotkey_buttons.rpy"
    m "The source code for the navigation buttons is in '[navdir]'."
    m "To change what the buttons do, edit the 'action' part of the textbuttons in the source code."
    m "Currently, all the buttons call a python function using 'Function', but you can change that to a variety of Screen Actions including 'Jump' and 'Call'."
    m "For more information on that, check the renpy documentation on Screen Actions."

    m 1c "One last thing,{w} these navigation buttons were created by developers from the Monika After Story team."
    m 5a "But, you are free to use this version of `zz_hotkey_buttons.rpy` in your mods."

    m 1a "Okay! Thanks for listening!"

    return


label tutorial_route_adv_poemgame:
    m 3a "Alright, let's look at the specially-modified poemgame developed by the Monika After Story team."
    m "This version of the poemgame allows you to do the following:"
    m "1. Add me to the poemgame, provided you have a list of words for me."
    m "2. Change which dokis are in the poemgame."
    m "3. Change music during the poemgame."
    m "4. Gather / save the words that users select."
    m "5. Save the individual character scores for the words users select."
    m "6. Add / remove glitches that were used in the base poemgame."
    m "7. Change the odds of those glitches."
    m "8. Change number of words you can pick."
    m "9. Change the words that are selectable."
    m "10. Change poem background."
    m "And other smaller adjustments."

    m "Additionally, this version of poemgame includes a special screen that can be used to generate textbutton grids of varying rows and columns."
    m "I'll showcase that later."

    $ navdir = config.basedir + "/game/advanced_scripts/zz_poemgame.rpy"
    m "You can find the source code in '[navdir]'."

    m 2o "Before I get into this, I must say that this file is {b}not{/b} for the faint of heart.{w} The code in here is pretty complex and difficult to customize."
    m "That means that if you want to do something that isn't covered by the features I listed above, you're better off customizing `script-poemgame` yourself."
    m "But if this turns out to be helpful for you, you are free to use this version of `zz_poemgame.rpy` in your mod."

    m "That being said..."
    menu:
        m "Do you still want to hear about the MAS version of poemgame?"
        "Yes":
            pass
        "No":
            jump tutorial_route_adv_poemgame_txgrid
    

label tutorial_route_adv_poemgame_pgexp:
    python:
        mas_wordlist = MASPoemWordList(mas_poemwords)

    m 5a "Yay!"

    m 3a "So the modified poemgame starts at the label 'mas_poem_minigame'."
    m 3n "If you have the source code open, you might notice the {i}massive{/i} comment right above that label."
    m 3a "This comment explains all the possible adjustable parameters you can pass into this label to configure it."
    m "Since this is terribly complex to do, the MAS team also added 3 helper labels based on the poemgame in different Acts."
    m "For Act 1: 'mas_poem_minigame_actone'."
    m "Act 2: 'mas_poem_minigame_acttwo'."
    m "And Act 3: 'mas_poem_minigame_actthree'."
    m "These are also pretty configurable, but only have a subset of the options available to the main poemgame label."

    m 2a "Let's go through how the game looks when you call these labels."
    m "For the sake of time, I'll limit the word selection to only 5 words per poemgame."

    m "Alright, lets start with a slightly modified Act 1."
    m "I'll be in this game, and I'll collect the points scored for each doki."
    stop music fadeout 1.0
    call mas_poem_minigame_actone(show_monika=True, poem_wordlist=mas_wordlist, total_words=5, trans_fast=True, show_poemhelp=False)
    scene bg club_day with dissolve_scene_full
    play music t3 fadein 1.0

    $ words = _return
    show monika 1a at t11
    m "Hi there!"
    m "These are your point totals:"
    python:
        for k,v in words.iteritems():
            m(k + " received " + str(v) + " point(s) from your choices.")

    m "Now let's do Act 2 but with higher chances of the glitchy word scare and no music."
    m "I'll also gather the words you select."
    stop music fadeout 1.0
    call mas_poem_minigame_acttwo(show_monika=True, poem_wordlist=mas_wordlist, total_words=5, music_filename=None, gather_words=True, glitch_wordscare=(True, 5), trans_fast=True, one_counter=False, show_poemhelp=False)

    scene bg club_day with dissolve_scene_full
    play music t3 fadein 1.0

    $ words = _return["words"]
    show monika 1a at t11
    m "Hi there!"
    m "These are the words you selected:"
    python:
        for word in words:
            m(word.word)

    m "Okay, time for my favorite Act, but with a twist!"
    m "I won't glitch any of the words and I'll hop for all your selections."
    m "I'll also keep the friendly music we have currently playing on during the game."
    call mas_poem_minigame_actthree(glitch_words=None, hop_monika=True, music_filename="BACK", trans_fast=True, total_words=5)
    scene bg club_day with dissolve_scene_full

    show monika 5a at t11
    m "That was fun!"

    m 3a "Let's do one more poemgame call. This time, I'll ask you for some parameters."
    $ pg_args = dict()

    m "First..."
    menu:
        m "Should we collect your word choices?"
        "Yes":
            $ pg_args["gather_words"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should we visibly glitch the words?"
        "Glitch the words.":
            m "Sure!"

            call tutorial_route_adv_poemgame_getnum("What are the odds that a space appears instead of a letter? (1 out of x)")
            $ space_odds = _return

            if space_odds <= 0:
                m 3n "I'll just say 5, then."
                show monika 3a
                $ space_odds = 5

            call tutorial_route_adv_poemgame_getnum("What are the odds that a nonunicode character appears instead of a letter? (1 out of x)")
            $ nonuni_odds = _return

            if nonuni_odds <= 0:
                m 3n "I'll just say 5, then."
                show monika 3a
                $ nonuni_odds = 5

            $ pg_args["glitch_words"] = (True, space_odds, nonuni_odds)

        "No":
            pass

    m "Okay..."
    menu:
        m "Should we use the poemgame music?"
        "Yes":
            pass
        "No":
            $ pg_args["music_filename"] = "BACK"

    m "Okay..."
    menu:
        m "Should I be visible?"
        "Yes":
            m 3j "Yay!"

        "No":
            m 3o "Aww..."
            $ pg_args["show_monika"] = False

    show monika 3a
    m "Okay..."
    menu:
        m "Should Sayori be visible?"
        "Yes":
            $ pg_args["show_sayori"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should Natsuki be visible?"
        "Yes":
            $ pg_args["show_natsuki"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should Yuri be visible?"
        "Yes":
            menu:
                m "...Should she have sleeves rolled up?"
                "Yes":
                    $ pg_args["show_yuri_cut"] = True
                "No":
                    pass
            $ pg_args["show_yuri"] = True
        "No":
            pass

    m "Okay..."
    menu:
        m "Should we make the word counter show 1's instead of regular numbers?"
        "Yes":
            $ pg_args["one_counter"] = True
        "No":
            pass

    m "Okay, last one."
    call tutorial_route_adv_poemgame_getnum("How many words should we select?")
    $ count = _return

    if count <= 0:
        m 3n "I'll just pick 14 then."
        $ count = 14
    elif count > 50:
        m 3n "That's a lot of words. Let's just pick 50."
        $ count = 50

    $ pg_args["total_words"] = count

    m 3a "Alright! Please note that we only went through some of the possible configuration parameters. There are more then what I asked you, but I'm only doing some of them to save time."

    m "Now let's see what we created!"
    $ pg_args["flow"] = store.mas_poemgame_consts.STOCK_MODE
    $ pg_args["poem_wordlist"] = mas_wordlist
    $ pg_args["show_poemhelp"] = False

    if "music_filename" not in pg_args:
        stop music fadeout 1.0

    call mas_poem_minigame(**pg_args)
    $ results = _return

    scene bg club_day with dissolve_scene_full

    if "music_filename" not in pg_args:
        play music t3 fadein 1.0

    show monika 5a at t11

    m "Alright!"

    if "gather_words" in pg_args:
        m "These are the words you selected:"
        $ words = results.pop("words")
        python:
            for word in words:
                m(word.word)
        pass # syntax highlighting

    m "These are your point totals:"
    python:
        for k,v in results.iteritems():
            m(k + " received " + str(v) + " point(s) from your choices.")
    pass

label tutorial_route_adv_poemgame_pg_end:
    m 2a "Alright, I hope that helps you get a feel for how the MAS poemgame implementation works."
    m "Remember to read the documentation in the source code carefully. There's a lot of parameter formatting to make the poemgame work correctly."
    m "And you can always use one of the act-based labels without params if you just want something that works out of the box."

    m 1a "Now..."
    jump tutorial_route_adv_poemgame_txgrid


label tutorial_route_adv_poemgame_getnum(msg):
    python:
        sel_num = renpy.input(
            "[msg]",
            allow="0123456789",
            length=2
        )
        if len(sel_num) <= 0:
            sel_num = 0
        else:
            sel_num = int(sel_num)

    return sel_num


label tutorial_route_adv_poemgame_txgrid:
    
    menu:
        "Do you want to hear about the textbutton grid?"
        "Yes":
            pass
        "No":
            m "Alright. Thanks for listening!"
            return

    m 1a "Alright!"
    m "The textbutton grid is a special screen that can be used to generate textbutton grids of varying rows and columns."
    m "It's basically the part of poemgame that displays a list of words and allows the user to select one."
    m "To launch the screen, add 'call screen mas_pg_textbutton_grid(...)' to your script."
    m "You will need to pass in several parameters in order to show the grid correctly."

    m 5a "Let's build those parameters together!"
    m 2a "First..."
    call tutorial_route_adv_poemgame_getnum("How many words should we show?")
    $ word_count = _return

    if word_count < 1:
        m 2n "[player]..."
        m "Let's just pick 10 words."
        $ word_count = 10

    m 2a "Now let's pick those words."

    python:
        word_list = list()
        for count in range(0, word_count):
            _word = renpy.input(
                "Enter in word " + str(count+1) + ":",
                allow="1234567890-qwertyuiopasdfghjklzxcvbnm",
                length=20
            )
            word_list.append((_word, _word))

    m "Now..."
    call tutorial_route_adv_poemgame_getnum("How many rows should we show?")
    $ row_count = _return

    if row_count < 1:
        m 3n "I'll just pick 6 rows."
        $ row_count = 6

    m 2a "And finally..."
    call tutorial_route_adv_poemgame_getnum("How many columns should we show?")
    $ col_count = _return

    if col_count <1:
        m 3h "Okay, 3 columns, then."
        $ col_count = 3

    show monika at t22
    m "Okay, I'm going to make this cover the left half of the screen by giving it an x position of 5, a y position of 5, a width of 600, and a height of 700."
    $ size_tuple = (5, 5, 600, 700)

    m "And a somewhat pink background image."
    $ bg_image = Solid("#ffe6f4bb", xsize=600, ysize=700)

    python:
        in_args = {
            "words": word_list,
            "row_info": (row_count, None),
            "col_info": (col_count, None),
            "xywh": size_tuple,
            "bg_image": bg_image,
            "_zorder": 200,
            "is_modal": True
        }

    m 5a "Now let's see what we got!"
    call screen mas_pg_textbutton_grid(**in_args)

    show monika at t11

    m "You selected '[_return]'!"

    m 1n "Hopefully that looked okay. It's easy to pick a combination of rows and columns and words that break the grid."
    
    m 1a "But if you need to make a simple textbutton grid, this should work fine!"

    m "For the technical details on how to call this screen and setup the paramters, check the source code for this set of dialogue and the screen itself."
    m "This set of dialogue is under the label 'tutorial_route_adv_poemgame_txgrid' in 'tutorials'."
    m "The screen is called 'mas_pg_textbutton_grid' and is located in 'zz_poemgame'."

    m "Okay! I hope that helps! Thanks for listening."

    return


