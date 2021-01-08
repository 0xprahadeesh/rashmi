import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyjokes 

# chill tamizha creation .......


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
     engine.setProperty('voice',voice.id)
     engine.setProperty('volume',10.0)

# AUDIO
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate',150)
# TIME
def time():
        Time = datetime.datetime.now().strftime("%I hour:%M minute:%S seconds")
        speak(Time)
# DATE
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
 #welcome
def welcome():
    speak("hey there welcome to my world it brings you more excited!")
#wikipedia
def wiki():   
    wiki = input("wiki:")
    speak("searching")
    print("searching.....")
    result = wikipedia.summary(wiki, sentences=2)
    print(result)
    speak(result)
#songs
def songs():
    songs_dir = 'D:\\SONGS'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))
#fav song
def favouritesong():
    songs_dir = 'D:\\favourite'
    songs = os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,songs[0]))
#fav color
def colour():
    speak("my favourite colour is red")
#jokes
def jokes():
    engine.setProperty('rate',105)
    speak(pyjokes.get_joke())
#native place
def place():
    engine.setProperty('rate',110)
    speak("my native is russia")
#best friend
def bestfriend():
    speak("my best friend is always google and you")
#friend
def friend():
    speak("yes we will be friends and you can call me when ever you want")
#account
def account():
    speak("NO i don't have ")
#password
def password():
    engine.setProperty('rate',105)
    speak("NO i can't say my personal,Ask anything else")
    speak("whats your name please tell me")
    data = input("whats your name:")
    name = open('data.txt','w')
    name.write(data)
    name.close()
#foodie
def food():
    engine.setProperty('rate',150)
    speak("i was loved all kind non-veg dishes and i loved to eat chocalate so much")
#name
def name():
    speak("hello! I'm rashmika and am here to help you ! tell me what do you want?") 
#call me
def callme():
    speak("say hey rashmika!")

#life
def life():
    speak("yeah its fine i love my life")
# WISHES (INTRO)
def wishme():
    speak("Welcome back my dear!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("good morning dear!")
    elif hour >=12 and hour <18:
        speak("good afternoon dear!")
    elif hour >=16 and hour <=18:
        speak("good evening dear! do u had your coffee")
    else:
        speak("good night dear")
    speak("rashmika at your service Please tell how can i help you?")
# RECOGNIZER
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-us')
        print(query)
    
    except  Exception as u:
        print(u)
        speak("say once more")

        return "None"
    return query
#chrome    
def chrome():
    speak("what do i want to search")
    chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    search = input("website:")
    wb.get(chromepath).open_new_tab(search+'.com')
#about
def about():
    speak("To know more about me please scan this QR code")
    import qrcode.py

#idk
def idk():
    speak("i thought you never ask that question")


if __name__ == "__main__":
   while True:
        welcome()
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
            speak("time is precious so don't waste it")
        elif 'date' in query:
            date()
            speak("have a great day")
        elif 'wiki' in query:
            wiki()
        elif 'songs' in query:
            speak("here the some of the songs")
            songs()
            exit()
        elif 'song' in query:
            speak("do u want my favourite ok" )
            favouritesong()
        elif 'hai' in query:
            name()
        elif 'are you from' in query:
            place()
        elif 'account' in query :
            account()
        elif 'password' in query:
            password()
        elif 'food' in query:
            food()
        elif 'colour' in query:
            colour()
        elif 'friends' in query:
            friend()
        elif 'friend' in query:
            bestfriend()
        elif 'jokes' in query:
            jokes()
        elif 'your life' in query:
            life()
        elif 'name' in query:
            name()
        elif 'boring' in query:
            speak("wait, i will entertain you by telling joke ")
            jokes()
        elif 'search' in query:
            chrome()

        elif 'about you' in query:
            about()

        else:
            idk()   

takeCommand()
