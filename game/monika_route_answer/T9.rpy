#label monika_route:
#    
#    stop music fadeout 2.0
#    play music t2
#    
#    scene bg residential_day
#    with dissolve_scene_full
#    
#    mc "It has been four days since I joined the Literature Club. Today is Saturday and I finally decided to confess my feeling to Monika."
#    
#    menu:
#        
#        mc "I told her to meet me..."
#        "At the literature club room":
#                $ meeting_place = "club_room"
#        "In front of my house":
#                $ meeting_place = "my_house"
#                
#    mc "I can't wait to meet her!"
#    
#    if meeting_place == "club_room":
#        scene bg club_day
#        with wipeleft_scene
#        
#    elif meeting_place == "my_house":
#        scene bg house
#        with wipeleft_scene
#        
#    stop music fadeout 2.0
#    play music t2
#        
#    mc "She is already waiting for me when I arrive."
#    
#    show monika 1b at t11 zorder 2
#    
#    m "Hi [player]!"
#    
#    mc "You're already here? I hope I didn't make you wait for too long."
#    
#    m 2a "Don't worry, it's me who's early."
#    
#    show monika 5a at f11 zorder 3
#    
#    m "So what did you want to tell me?"
#    
#    menu:
#         
#        mc "Right. Monika, ..."
#        "I love you! Please go out with me!":
#            jump monika_normal_ending
#        "You are everything to me! Please marry me!":
#            jump monika_good_ending
#            
#    return
#    
#label monika_normal_ending:
#    
#    scene dark
#    with dissolve_scene_full 
#    
#    mc "She accepted my confession and we became lovers."
#    
#    "NORMAL ENDING."
#    
#    return
#    
#label monika_good_ending:
#    
#    scene white
#    with dissolve_scene_full 
#    
#    mc "She gladly accepted my proposal and we got married one year later."
#    
#    "GOOD ENDING."
#    
#    return