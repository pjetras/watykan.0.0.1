import urllib.request
from PIL import Image
import keyboard
# import threading

papaj = (input("Wpisz liczbe yasuo:"))

if papaj == "010":
    urllib.request.urlretrieve(
            'https://static.wikia.nocookie.net/leagueoflegends/images/c/c9/Yasuo_Render.png/revision/latest/scale-to-width-down/229?cb=20200514001932',
            "Yasuo_Render.png")
    img = Image.open("Yasuo_Render.png")
    while True:
        img.show()


        
        # t1 = threading.Thread(target=img.show(), args = (2,))
        # t2 = threading.Thread(target=img.show(), args = (2,))
        # t3 = threading.Thread(target=img.show(), args = (2,))
        # t4 = threading.Thread(target=img.show(), args = (2,))
        # t5 = threading.Thread(target=img.show(), args = (2,))
        # t6 = threading.Thread(target=img.show(), args = (2,))
        # t7 = threading.Thread(target=img.show(), args = (2,))

        # t1.start()
        # t2.start()
        # t3.start()
        # t4.start()
        # t5.start()
        # t6.start()
        # t7.start()

        # urllib.request.urlretrieve(
        #     'https://scontent-waw1-1.xx.fbcdn.net/v/t1.6435-9/52392456_2462506270693320_8756022111207686144_n.jpg?stp=dst-jpg_p526x296&_nc_cat=108&ccb=1-5&_nc_sid=8024bb&_nc_ohc=JiSlUWYpg8YAX9emtFb&_nc_ht=scontent-waw1-1.xx&oh=00_AT-e7k7QgqG1v7gBDBCqojgLXBadDxIzw7jaklR5LWXkmQ&oe=62437A72',
        #     "papa.jpg")
        # img = Image.open("papa.jpg")

        # img.show()
        # urllib.request.urlretrieve(
        #     'https://scontent-waw1-1.xx.fbcdn.net/v/t1.6435-9/47682249_2413076482302966_6620690544890740736_n.jpg?stp=dst-jpg_p526x296&_nc_cat=111&ccb=1-5&_nc_sid=8024bb&_nc_ohc=1RBCFIp56fIAX8-CKXU&_nc_ht=scontent-waw1-1.xx&oh=00_AT9tY91B0XwyU8SgUbWCqIPiCtvKZaWuwxUF5AUSyyUBhQ&oe=62429EBB',
        #     "papa2.jpg")
        # img = Image.open("papa2.jpg")

        # img.show()
        if keyboard.is_pressed("p"):
            print("yasuo")
            break
