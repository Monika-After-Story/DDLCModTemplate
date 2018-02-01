# Welcome to the Modification Club!

The DDLC Mod Template is an easy way to get started building your own game mods for Doki Doki Literature Club that adhere to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) for fan mods.

### Getting Started
Follow these steps to set up the template.

1. Download and install the [Ren'Py SDK version 6.99.12](https://www.renpy.org/release/6.99.12). *(NOTE: The current version of DDLC is not compatible with .rpyc files generated with other versions of the Renpy SDK)*
2. Go to releases to download the [latest stable build](https://github.com/therationalpi/DDLCModTemplate/releases). For development builds, fork this repository or download the files by clicking the button labeled "Clone or Download" above.
3. Place the files in the Ren'py working directory (chosen during installation).
4. Download the DDLC files (available for free at http://ddlc.moe) & drop the `audio.rpa`, `images.rpa`, and `fonts.rpa` files from it into the /game directory. (Do **not** include the `scripts.rpa` file, as this will create conflicts.)
5. Launch the project in Ren'Py. It should compile & run.
6. Navigate the Ren'Py menu & select "Build Distributions." Check "DDLC Compatible Mod" and build the mod. This will create a cross-platform .ZIP file with files for the mod & installation instructions.

### Template Features
1. Import save data from DDLC. This will *not* affect the original game.
2. Build Packaging. Distribute cross-platform mods with ease thanks to Ren'Py.
3. Mod Installation instructions & guide. Run the game to get a short introduction by Monika!
4. Splash screen on first load. This adheres to the Team Salvato guidelines for creating fan mods of the game.
5. Customizable! Use as a starting point for any ideas you wish to create.

## DDLC-Toolkit

We're proud to be a submodule of the [DDLC-Toolkit](https://github.com/GarnetSunset/DDLC-Toolkit).
