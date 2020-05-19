#This is a copy of transforms.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Explanation for console.rpy
#This script defines the placements and animations used for putting images on
#screen. Useful for blocking with characters and other things

#########
####Transforms to place characters on the screen in proper positions based on whether there are 2, 3, or 4 characters in the scene.

#tcommon isn't used by itself, but is the starting point for other transforms
transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03 #Move the character 3% offscreen, so they can hop and bounces
        zoom z*0.95 alpha 0.00 #Default scale down image to reduce pixelization
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00 #By default, fade and scale in.
        #yanchor 1.0 ypos 1.03
    on replace: #For changing expressions
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80): #This version doesn't fade or scale the character in. They just appear.
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03

# This pulls out the character that's talking and makes them a bit bigger
transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:
        #yanchor 0.527 ypos 0.5
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00 #Make focus character 5% bigger
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0

#This causes the character to sink down dejectedly
transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06

#This makes the character hop up for 0.1 seconds
transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0

#Like hop, but for a focused character
transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0

#Character dips down for a second and comes back up
transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0

#The character wobbles from side to side and up and down like they're antsy
transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat

#Fly in rapidly from the left
transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x

#Used when hiding sprites with dissolve to mirror the show effect
transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:
        #yanchor 0.510 ypos 0.5
        easein .25 zoom z*0.95 alpha 0.00 yoffset -20
transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300


#Normal positioning and animation, based on number of characters on screen
#First number is how many characters, second is the character's position
transform t41: #Leftmost of 4 characters
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44: #Rightmost of 4 characters
    tcommon(1080)
transform t31: #Leftmost of 3 characters
    tcommon(240)
transform t32:
    tcommon(640)
transform t33: #Rightmost of 3 characters
    tcommon(1040)
transform t21: #Leftmost of 2 characters
    tcommon(400)
transform t22:#Rightmost of 2 characters
    tcommon(880)
transform t11: #One centered character
    tcommon(640)

#Same positioning as before, but pop in quickly
transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)

#Same positioning as before, but make the character the focus
transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)

#Same positioning, but use the sink animation
transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)

#Same positioning, but use a hop animation
transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)

#Same positioning, but hop the character into focus
transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)

#Same positioning, but with a dip animation
transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)

#Same positioning, but fly in from the left
transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)

########
##Speacial transitions for scenechanges and such

#When MC opens his eyes to Sayori's face in her exclusive
transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00

#A slow fade in for a new cg
transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

#A little wiggle for natsuki in the closet
transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0

transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat

#A little zoom for saving Natsuki from falling boxes
transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200

#Override the default dissolve with a faster one
define dissolve = Dissolve(0.25)

#Special dissolves for CG and scene changes
define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)

#Special a series of dissolves for a full scene change
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0), #Fade to black for 1 second
    Solid("#000"), Pause(1.0), #Wait 1 second
    Solid("#000"), Dissolve(1.0), #Fade out of black for 1 second
    True])

#Fade out from black for start of a new scene
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

#Fade out to black
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

#Fade out from black
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

#Sudden blackness
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

#Override wipeleft with a proper-looking wipe that has a nice fade to it
define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)

#Wipe to black, pause for .25 seconds, then wipe to the next scene (indicates the passing of time between scenes)
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])

define tpause = Pause(0.25)

###White noise and effects
#Radio static displayable
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

#Used to make a noise overlay semi-transparent
transform noise_alpha:
    alpha 0.25

#Have the noise faid in to 40%
transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40

####Vignette and effects
#Vignette around the edge of the screen
image vignette:
    truecenter
    "images/bg/vignette.png"

#Have the vignette fade in over 25 seconds
transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00
#A random flickering in and out of the vignette
transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0

transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat

#Rewind effect used in Act 2 where the screen bounces up and down, left and right
transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

#Heartbeat effect where the screen pulses like a heartbeat
#Used with creepy yuri and in the final act
transform heartbeat:
    heartbeat2(1)

transform heartbeat2(m):
    truecenter
    parallel:
        0.144
        zoom 1.00 + 0.07 * m
        easein 0.250 zoom 1.00 + 0.04 * m
        easeout 0.269 zoom 1.00 + 0.07 * m
        zoom 1.00
        1.479
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.5 + 0.02 * m
        easeout_bounce 0.3 xalign 0.5 - 0.02 * m
        repeat

#Jerky random motion for yuri's pupils
transform yuripupils_move:
    function yuripupils_function

init python:
    def yuripupils_function(trans, st, at):
        trans.xoffset = -1 + random.random() * 9 - 4
        trans.yoffset = 3 + random.random() * 6 - 3
        return random.random() * 1.2 + 0.3

#Have a character pop in instantly with a given transparency
transform malpha(a=1.00):
    i11
    alpha a
