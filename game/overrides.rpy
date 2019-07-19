## This file is for overriding specific declarations from DDLC
## Use this if you want to change a few variables, but don't want
## to replace entire script files that are otherwise fine.

## Normal overrides
## These overrides happen after any of the normal init blocks in scripts
## Use these to chagne variables on screens, effects, etc
init 10 python:
    pass

## Late overrides
## These overrides happen aftre prety much everything else in startup.
## Use these to change displayables and other late definitions in renpy.
init 501 python:
    pass

## Early overrides
## These overrides happen befoer the normal init blcosk in scripts
## Use these in the rare event taht you need to overwrite some variable
## before it's called in another init blcok
## You probably wont use this
init -10 python:
    pass

## Super early overrides
## These get called before any of the init blocks are read, before the
## persistent data is read. Basically right after RenPy loads itself but
## before the game / mod is loaded.
## You almost never will need this
python early:
    pass
