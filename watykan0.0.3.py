import threading, urllib.request, random
from PIL import Image

def main():
    threads_list = []
    urllib.request.urlretrieve('https://scontent-waw1-1.xx.fbcdn.net/v/t1.6435-9/52392456_2462506270693320_8756022111207686144_n.jpg?stp=dst-jpg_p526x296&_nc_cat=108&ccb=1-5&_nc_sid=8024bb&_nc_ohc=JiSlUWYpg8YAX9emtFb&_nc_ht=scontent-waw1-1.xx&oh=00_AT-e7k7QgqG1v7gBDBCqojgLXBadDxIzw7jaklR5LWXkmQ&oe=62437A72',"papa.jpg")
    urllib.request.urlretrieve('https://www.wykop.pl/cdn/c3201142/comment_1588762974PT17UhAFoREy0oxY3JSkSD,w400.jpg',"w400.jpg")
    urllib.request.urlretrieve('https://scontent-waw1-1.xx.fbcdn.net/v/t1.6435-9/47682249_2413076482302966_6620690544890740736_n.jpg?stp=dst-jpg_p526x296&_nc_cat=111&ccb=1-5&_nc_sid=8024bb&_nc_ohc=1RBCFIp56fIAX8-CKXU&_nc_ht=scontent-waw1-1.xx&oh=00_AT9tY91B0XwyU8SgUbWCqIPiCtvKZaWuwxUF5AUSyyUBhQ&oe=62429EBB',"papa2.jpg")
    urllib.request.urlretrieve('https://i.redd.it/prlzjv5fnhq51.jpg', 'prlzjv5fnhq51.jpg')
    urllib.request.urlretrieve('https://i.redd.it/y27qeog5j1p61.jpg', 'y27qeog5j1p61.jpg')
    urllib.request.urlretrieve('https://i.redd.it/bubrf4adg1c71.png', 'bubrf4adg1c71.png')

    img0 = Image.open("papa2.jpg")
    img1 = Image.open("w400.jpg")
    img2 = Image.open("papa.jpg")
    img3 = Image.open("prlzjv5fnhq51.jpg")
    img4 = Image.open("y27qeog5j1p61.jpg")
    img5 = Image.open("bubrf4adg1c71.png")

    images = [img0, img1, img2, img3, img4, img5]

    while True:

        for _ in range(20):
            img = random.choice(images)
            t = threading.Thread(target = img.show)
            t.start()
            threads_list.append(t)
        for thread in threads_list:
            thread.join()
        
if __name__ == "__main__":
    main()
