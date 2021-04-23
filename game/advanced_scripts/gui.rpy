﻿################################################################################
## Initialization
################################################################################

## The init offset statement causes the init code in this file to run before
## init code in any other file.
# init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init -2 python:
    gui.init(1280, 720)
    #config.gl_resize = False


################################################################################
# GUI Configuration Variables
################################################################################

define -2 gui.hover_sound = "gui/sfx/hover.ogg"
define -2 gui.activate_sound = "gui/sfx/select.ogg"
define -2 gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg"

## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define -2 gui.accent_color = '#ffffff'

## The color used for a text button when it is neither selected nor hovered.
define -2 gui.idle_color = '#aaaaaa'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define -2 gui.idle_small_color = '#333'

## The color that is used for buttons and bars that are hovered.
define -2 gui.hover_color = '#cc6699'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define -2 gui.selected_color = '#bb5588'

## The color used for a text button when it cannot be selected.
define -2 gui.insensitive_color = '#aaaaaa7f'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define -2 gui.muted_color = '#6666a3'
define -2 gui.hover_muted_color = '#9999c1'

## The colors used for dialogue and menu choice text.
define -2 gui.text_color = '#ffffff'
define -2 gui.interface_text_color = '#ffffff'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define -2 gui.default_font = "gui/font/Aller_Rg.ttf"

## The font used for character names.
define -2 gui.name_font = "gui/font/RifficFree-Bold.ttf"

## The font used for out-of-game text.
define -2 gui.interface_font = "gui/font/Aller_Rg.ttf"

## The size of normal dialogue text.
define -2 gui.text_size = 24

## The size of character names.
define -2 gui.name_text_size = 24

## The size of text in the game's user interface.
define -2 gui.interface_text_size = 24

## The size of labels in the game's user interface.
define -2 gui.label_text_size = 28

## The size of text on the notify screen.
define -2 gui.notify_text_size = 16

## The size of the game's title.
define -2 gui.title_text_size = 38


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define -2 gui.main_menu_background = "menu_bg"
define -2 gui.game_menu_background = "game_menu_bg"

## Should we show the name and version of the game?
define -2 gui.show_name = False


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define -2 gui.textbox_height = 182

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define -2 gui.textbox_yalign = 0.99


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define -2 gui.name_xpos = 350
define -2 gui.name_ypos = -3

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define -2 gui.name_xalign = 0.5

## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define -2 gui.namebox_width = 168
define -2 gui.namebox_height = 39

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define -2 gui.namebox_borders = Borders(5, 5, 5, 2)

## If True, the background of the namebox will be tiled, if False, the
## background if the namebox will be scaled.
define -2 gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define -2 gui.text_xpos = 268
define -2 gui.text_ypos = 62

## The maximum width of dialogue text, in pixels.
define -2 gui.text_width = 744

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define -2 gui.text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define -2 gui.button_width = None
define -2 gui.button_height = 36

## The borders on each side of the button, in left, top, right, bottom order.
define -2 gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define -2 gui.button_tile = False

## The font used by the button.
define -2 gui.button_text_font = gui.interface_font

## The size of the text used by the button.
define -2 gui.button_text_size = gui.interface_text_size

# The color of button text in various states.
define -2 gui.button_text_idle_color = gui.idle_color
define -2 gui.button_text_hover_color = gui.hover_color
define -2 gui.button_text_selected_color = gui.selected_color
define -2 gui.button_text_insensitive_color = gui.insensitive_color

# The horizontal alignment of the button text. (0.0 is left, 0.5 is center,
# 1.0 is right).
define -2 gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define -2 gui.radio_button_borders = Borders(28, 4, 4, 4)

define -2 gui.check_button_borders = Borders(28, 4, 4, 4)

define -2 gui.confirm_button_text_xalign = 0.5

define -2 gui.page_button_borders = Borders(10, 4, 10, 4)

#define -2 gui.quick_button_borders = Borders(10, 4, 10, 0)
define -2 gui.quick_button_text_size = 14
define -2 gui.quick_button_text_idle_color = "#522"
define -2 gui.quick_button_text_hover_color = "#fcc"
define -2 gui.quick_button_text_selected_color = gui.accent_color
define -2 gui.quick_button_text_insensitive_color = "#a66"

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define -2 gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define -2 gui.choice_button_width = 420
define -2 gui.choice_button_height = None
define -2 gui.choice_button_tile = False
define -2 gui.choice_button_borders = Borders(100, 5, 100, 5)
define -2 gui.choice_button_text_font = gui.default_font
define -2 gui.choice_button_text_size = gui.text_size
define -2 gui.choice_button_text_xalign = 0.5
define -2 gui.choice_button_text_idle_color = "#000"
define -2 gui.choice_button_text_hover_color = "#fa9"


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define -2 gui.slot_button_width = 276
define -2 gui.slot_button_height = 206
define -2 gui.slot_button_borders = Borders(10, 10, 10, 10)
define -2 gui.slot_button_text_size = 14
define -2 gui.slot_button_text_xalign = 0.5
define -2 gui.slot_button_text_idle_color = gui.idle_small_color
define -2 gui.slot_button_text_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define -2 config.thumbnail_width = 256
define -2 config.thumbnail_height = 144

## The number of columns and rows in the grid of save slots.
define -2 gui.file_slot_cols = 3
define -2 gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define -2 gui.navigation_xpos = 80

## The vertical position of the skip indicator.
define -2 gui.skip_ypos = 10

## The vertical position of the notify screen.
define -2 gui.notify_ypos = 45

## The spacing between menu choices.
define -2 gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define -2 gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define -2 gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define -2 gui.pref_button_spacing = 0

## The spacing between file page buttons.
define -2 gui.page_spacing = 0

## The spacing between file slots.
define -2 gui.slot_spacing = 10


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames that are introduced by player code.
define -2 gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define -2 gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## The frame that is used as part of the skip screen.
define -2 gui.skip_frame_borders = Borders(16, 5, 50, 5)

## The frame that is used as part of the notify screen.
define -2 gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Should frame backgrounds be tiled?
define -2 gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written code.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define -2 gui.bar_size = 36
define -2 gui.scrollbar_size = 12
define -2 gui.slider_size = 30

## True if bar images should be tiled. False if they should be linearly scaled.
define -2 gui.bar_tile = False
define -2 gui.scrollbar_tile = False
define -2 gui.slider_tile = False

## Horizontal borders.
define -2 gui.bar_borders = Borders(4, 4, 4, 4)
define -2 gui.scrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define -2 gui.vbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define -2 gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define -2 gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define -2 config.history_length = 50

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define -2 gui.history_height = None

## The position, width, and alignment of the label giving the name of the
## speaking character.
define -2 gui.history_name_xpos = 150
define -2 gui.history_name_ypos = 0
define -2 gui.history_name_width = 150
define -2 gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define -2 gui.history_text_xpos = 170
define -2 gui.history_text_ypos = 5
define -2 gui.history_text_width = 740
define -2 gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define -2 gui.nvl_borders = Borders(0, 10, 0, 20)

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define -2 gui.nvl_height = 115

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define -2 gui.nvl_spacing = 10

## The position, width, and alignment of the label giving the name of the
## speaking character.
define -2 gui.nvl_name_xpos = 430
define -2 gui.nvl_name_ypos = 0
define -2 gui.nvl_name_width = 150
define -2 gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define -2 gui.nvl_text_xpos = 450
define -2 gui.nvl_text_ypos = 8
define -2 gui.nvl_text_width = 590
define -2 gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define -2 gui.nvl_thought_xpos = 240
define -2 gui.nvl_thought_ypos = 0
define -2 gui.nvl_thought_width = 780
define -2 gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define -2 gui.nvl_button_xpos = 450
define -2 gui.nvl_button_xalign = 0.0



################################################################################
# Mobile devices
################################################################################

init -2 python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(60, 14, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    if renpy.variant("small"):

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 36
        gui.button_text_size = 34
        gui.label_text_size = 36

        ## Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100

        # text alignment
        gui.text_xalign = 0.5

        ## Change the size and spacing of items in the game menu.
        gui.choice_button_width = 1240

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20

        ## Quick buttons.
        gui.quick_button_text_size = 20
