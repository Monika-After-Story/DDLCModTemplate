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
#    return