Night Mode
==========
Configures the system to turn on/off the night mode. 

How to
------
To enable night mode, just run `./run.sh dark`. This will run all the scripts in the `bin/`. And each of the script in the `bin/` folder will make something *dark*. 

So far we have following scripts.

1. Sublime-text3-color-scheme. It changes the Ayu color scheme to it's dark/light variant. So Ayu color scheme should be installed.
2. Unity-gnome-terminal-profile. It changes the profile of the terminal assuming first one is *dark* profile and the second one is *light*


You are welcome to add more scripts in the `bin/` folder. Note, those scripts should be executable. And they should accept either `dark` or `light` as argument