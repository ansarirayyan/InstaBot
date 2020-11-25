from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# isolates the username from the rest of the message content and searches for user
def isolateUserString(msg, searchCommand):
    print(msg); # DEBUG
    username = msg.replace(searchCommand, '')
    return (username) # should I put spaces between the thing and '('s or nah?
