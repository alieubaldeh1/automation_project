from instabot import Bot 

bot = Bot() 

username = 'jamtan.code'
password = os.environ.get('password')
image = 'automateIG.jpg'
text = 'Automated with Python Script by Alieu Baldeh'

bot.login(username=username, password=password)
bot.upload_photo("automateIG.jpg", caption=text)
