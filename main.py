from functions import *

import discord
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

client = discord.Client()
#driver = webdriver.Firefox()
# I DON'T NEED TO ANY SELENIUM INITIALIZATION CUZ DONE IN OTHER FILE LOOOOOOOOOL

i = 0;
searchCommand = 'i s ';

# TODO: make it look nice by adding an embedment and perhaps putting profile pic

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global username
    global i

    if message.author == client.user:
        return

    if message.content.startswith(searchCommand):
        i = 0

        username = isolateUserString(message.content, searchCommand);
        print (username) # DEBUG

        driver.get("https://www.instagram.com/" + username)

        print(driver.current_url)

        # check if user actually exists (or is accessible to us)
        # TODO: add a sign in feature so that ppl can access priv accounts
        h2 = driver.find_element_by_tag_name("h2")
        print (h2.text)
        if (h2.text == "Sorry, this page isn't available."):
            await message.channel.send("User does not exist!")
            pictura = driver.find_elements_by_tag_name("img")
            pictura[0].get_attribute('src') # profile pic if index is 0
        elif (driver.current_url == "https://www.instagram.com/accounts/login/"):
            print(":::::::::::::::::::::::redirected to login page")

        else:
            await message.channel.send("User found!")

        # document.getElementsByTagName("h2")[0].innerHTML save so I don't lose
        # TODO: THIS CODE IS HELLA MESSY DIDN'T WANT ANY SELENIUM STUFF IN MAIN

    if message.content == ("i current"): # DEBUG
        #global username # WHY CAN'T THIS LINE AND THE ONE BELOW BE ONE??????????
        print(username)

    if message.content == (">"):
        pics = driver.find_elements_by_tag_name("img")
        try:
            while (True):
                if (pics[i].get_attribute('alt').endswith("profile picture")):
                    print(pics[i].get_attribute('alt').find("profile picture"))
                    i = i + 1
                    print("::::::::::::::INDEX: " + str(i))
                else:
                    break
            await message.channel.send (pics[i].get_attribute('src'))
            i = i + 1
        except IndexError:
            await message.channel.send ("No more pictures!")



client.run('NzgxMjkwNTY5NDEzNTU4MzA2.X77fiw.u57Jv7QwxscMn8gG3fGAMZG4Sw0')
