# to make a mp3 karaoke which plays song on users command :/
from winsound import PlaySound
from xml.dom import InvalidAccessErr, InvalidCharacterErr
from playsound import playsound
class Songs():
    def __init__(self,song):
     self.song=song
    def listofsongs(self):
        print("*******List of songs*******")
        for songs in self.song:
            print("  *"  " " + songs )

    def songs(self):
        song =input("enter the song you would like to listen to:\t")
        print("***********Enjoy the song**************\n")
        if song=="lofi":
            playsound("D://lofi-study-112191.mp3")    
        elif song=="whip":   
            playsound("C:///Users/Mridul Pandey//Downloads//whip-110235.mp3")
        elif song=="sunflower":
            with open("lyrics.txt") as f:
                print(f.read())
            playsound("C://Users//Mridul Pandey//Downloads//Sunflower-(Spider-Man_-Into-the-Spider-Verse)---Post-Malone,-Swae-Lee(pagolworld.nl).mp3")
        elif song =="shape of you":
            with open("lyrics2.txt") as f:
                print(f.read())
            playsound("C://Users//Mridul Pandey//Downloads//Ed_Sheeran_-_Shape_Of_You (1).mp3")    
            
mridul=Songs(["shape of you","sunflower","rap god","whip","lofi","dance beats music"])

while (True):
    print("1.Display list of songs \n2.Play song \n3.Rate the songs \n4.Exit the mp3 player")
    n=int(input("enter the option no."))
    if  n==1:
        mridul.listofsongs()
    elif n==2:
        mridul.songs()
    elif n==3:
        p=input("enter the score out of 5:")
        print(f"you have rated this song {p}/5")
    elif n==4:
        print("##### Adios Amigos,Thank you for playing songs on mp3 player!######")
        break;

    

    



        


    
