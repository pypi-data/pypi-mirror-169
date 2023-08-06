from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
import instaloader
def app():
    ig = instaloader.Instaloader()
    dp = input("Enter Insta username : ")
    put_text(dp)
    ig.download_profile(dp , profile_pic_only=False)
#The file is also downloaded to the local disk
#Файл также скачивается на локальный диск
#Fayl(-lar)  lokal diskga ham yuklanadi
start_server(app)




