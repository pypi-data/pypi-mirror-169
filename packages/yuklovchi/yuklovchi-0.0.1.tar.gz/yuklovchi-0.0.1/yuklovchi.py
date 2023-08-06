from pywebio import start_server, config
from pywebio.output import *
from pywebio.input import *
from pytube import *
from instaloader import *



def app():
    link = input(placeholder="URL tashlang")
    toast("Yuklanmoqda...")
    try:
        youtube = YouTube(link)
        youtube.streams.get_highest_resolution().download(output_path="Dowloaded")
        toast("Muvaffaiqiyatli yuklandi!")
    except:
        toast("Xatolik Yuz berdi!")

    

    profile_name = input ( "Instagram nomini yozing: " )
    toast( "Yuklanmoqda..." )
    instaloader . Instaloader ( ) . download_profile ( profile_name , profile_pic_only = False )
    toast( "Muvaffaqqiyatli yuklandi!" )



start_server(app, debug=True)
