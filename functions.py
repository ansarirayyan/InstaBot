from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.log.level = "trace"
opts.headless = True # enable headless mode to not get errors on env w/o desktop
driver = webdriver.Firefox(options=opts)

# isolates the username from the rest of the message content and searches for user
def isolateUserString(msg, searchCommand):
    print(msg); # DEBUG
    username = msg.replace(searchCommand, '')
    return (username) # should I put spaces between the thing and '('s or nah?

