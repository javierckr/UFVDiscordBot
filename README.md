# UFVDiscordBot
Bot de discord para gestionar los canales de discord de la UFV


## Instructions

### Local install
# Linux
0. git clone https://github.com/javierckr/UFVDiscordBot.git
1. python3 -m pip install -r requirements.txt
2. Change Example.env to .env and paste your token
3. Run the bot python3 bot.py& python3 youtubedl.py
# Windous
### Heroku install

0. git clone https://github.com/javierckr/UFVDiscordBot.git
1. Add your .env secrets to heroku
2. Install this buildpacks on heroku:heroku/python https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git https://github.com/xrisk/heroku-opus.git
3. Deploy to heroku: git push heroku main
4. Enable dynos for the bot
