# Auto Restart Minecraft Server

This file allows you to restart your Minecraft server (hosted locally), if it stops.

**Place it in the root of the server**

*Configuration:*

  1. Open [auto_run.py](auto_run.py) in a code/text editor

  2. Change {command} to the server command. --> Open **run.sh** or **run.bat** and Copy-Paste the last line (java @user_jvm...)

  3. Run your server once, stop it and get the last line, without the useless information | [15:56:18] [Server thread/INFO] [minecraft/MinecraftServer]: ThreadedAnvilChunkStorage: All dimensions are saved --> **All dimensions are saved**

  4. Change {text_line} to the previously retrieved line

  5. Open [config_file.py](config_file.py). Modify {text_line} by the line recovered previously and launch it.

  6. In 'auto-run.py' change {number} to the number previously displayed.

Your files are ready. All you have to do is launch [auto_run.py](auto_run.py) !

[![My Skills](https://skillicons.dev/icons?i=py,idea,github&theme=light)](https://skillicons.dev)
