import os
from auth import Login
from deal import FindShoesById
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from discord.ext import commands
import discord
import time


# inicializace driveru
driver = webdriver.Firefox(executable_path=r'C:\DRIVERS\geckodriver.exe')
load_dotenv()
token = os.getenv('BOT_KEY')
acc_email = os.getenv('EMAIL')
acc_pass = os.getenv('PASSWORD')
shoes_id = os.getenv('SHOES_ID')
shoes_size = os.getenv('SHOES_SIZE')
payment_option = os.getenv('PAYMENT_OPTION')

Login(driver=driver,email=acc_email,password=acc_pass)
FindShoesById(driver=driver,shoe_id=shoes_id,shoe_size=shoes_size)

# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)
# client.run(token)