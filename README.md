# Send-memes-to-a-discord-server-with-Python
Simple guide to set up a python bot that dowload images from a specific subreddit and send it to a discord server channel.

## BEFORE YOU START
  Before you start is you must set up ruffly 2 things: a python discord bot and a reddit account.
  We will use the bot to send the images and the reddit account to search the memes.

### discord.py bot
  If for some reason you don't have a discord bot yet I recommend [this video](https://www.youtube.com/watch?v=nW8c7vT6Hl4) to set it up.
  If you are familiar with discord bots or you own one you can skip this part.

### reddit account (praw)
  Now we need to set up a reddit account to scrape subreddits for memes, if you are not familiar I recommend [this video](https://www.youtube.com/watch?v=gIZJQmX-55U).
  
### requirements
  You will need praw, urllib, time, os, discord.

## SET UP
  Clone the repo or copy the files or whatever.
  
  _Remember to:_
  
    -Insert your bot token at the and of token at the end of bot.py
    
    -Fill meme.py with your reddit account information
    
    -Update the directory where the memes will be saved if you change it

## RUN
  Run bot.py then when the bot is online 
  Then you will be able to get memes calling your meme function from your discord server by writing _.memes (name of the subreddit)_.

### Example
  To execute the script follow these steps:
      
      -python bot.py
      
  From discord:
      
      -.memes dankmemes
      
      
