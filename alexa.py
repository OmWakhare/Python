import os
import time

import pyttsx3
import datetime
import speech_recognition as sr
from os import startfile
import webbrowser
import random
import wikipedia
import pyautogui
import keyboard
import sys

from requests import get
from speech_recognition import Microphone

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
        print("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")
        print("good afternoon")

    else:
        speak("good evening")
        print("good evening")

    print('iam jarvis tell how may i help you')
    speak(" VANSH AKSHAY GANDHI")
    speak("iam jarvis tell how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.energy_threshold = 400

    try:

        print("Recongnizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:: {query}")

    except Exception as e:
        # print(e)
        print("say that again please...")
        speak("say that again please")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    # takeCommand()
    while True:
        query = takeCommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            speak("Opening notepad Sir")
            startfile(npath)

        elif "open command prompt" in query:
            speak("opening cmd")
            os.system("start cmd")

        elif "open camera" in query:
            speak("Have nice picture sir")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("playing music sir ,enjoy the time sir")
            music_dir = "C:\\Users\\omwak\\OneDrive\\Desktop\\New folder"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,))


        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            speak("what to play on youtube")
            m = takeCommand().lower()
            webbrowser.open(f"{m}")


        elif "open whatsapp" in query:
            webbrowser.open("whatsapp.com")

        elif "open google" in query:
            webbrowser.open("google.com")
            speak("what should i search on google sir")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}.youtube.com")
            speak("here is what i found sir")

        elif "open stack overflow" in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif "open gaana" in query:
            def gaana(song):
                speak("opening gaana sir")
                webbrowser.open("gaana.com")
                time.sleep(5)
                pyautogui.click(x=365, y=125)
                keyboard.write(song)
                keyboard.press('enter')


            gaana("pawankhind")


        elif "open amazon" in query:
            speak("opening amazon sir")
            webbrowser.open("amazon.com")
            speak("what would u like to buy sir")
            product = takeCommand().lower()


            def amazon(product):
                time.sleep(2)
                pyautogui.click(x=570, y=119)
                keyboard.write(product)
                keyboard.press('enter')


            amazon(f'{product}')

        elif "open gov" in query:
            webbrowser.open("ceir.gov.in")

        elif "open flipkart" in query:
            webbrowser.open("amazon.com")

        elif "open new arts college website" in query:
            speak("opening new arts college website")
            webbrowser.open("newartscollege.ac.in")
            speak("New Arts, Commerce and Science College is an educational institution in Ahmednagar city of state of Maharashtra in India. The college established in 1970 by Ahmednagar Jilha Maratha Vidya Prasarak Samaaj")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP address is {ip}")


        elif "search" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "send message by whatsapp" in query:
            speak("To whom you have to send message sir")
            name = takeCommand().lower()
            speak("what message to send sir")
            message = takeCommand().lower()


            def Whatsappmsg(name, message):
                os.startfile("C:\\Users\\omwak\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

                time.sleep(10)

                pyautogui.click(x=173, y=137)

                time.sleep(1)

                keyboard.write(name)

                time.sleep(2)

                pyautogui.click(x=169, y=298)

                time.sleep(1)

                pyautogui.click(x=992, y=990)

                time.sleep(0.5)

                keyboard.write(message)

                keyboard.press('enter')


            Whatsappmsg(f'{name}', f'{message}')



        elif "call" in query:
            speak("To whom u have to call sir")
            name = takeCommand().lower()


            def Whatsappcall(name):
                os.startfile("C:\\Users\\omwak\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

                time.sleep(10)

                pyautogui.click(x=173, y=137)

                time.sleep(1)

                keyboard.write(name)

                time.sleep(2)

                pyautogui.click(x=169, y=298)

                time.sleep(0.5)

                pyautogui.click(x=1717, y=72)


            Whatsappcall(f'{name}')

        elif "open my project on google" in query:

            speak("opening sir")
            webbrowser.open("google.com")

            time.sleep(2)
            pyautogui.click(x=537, y=57)

            keyboard.write("localhost/om")
            keyboard.press('enter')

        elif "find me a way" in query:
            speak("which destination sir")
            webbrowser.open("maps.google.com")


            map = takeCommand().lower()



            def googlemap(map):



                time.sleep(4)



                pyautogui.click(x=125, y=136)

                keyboard.write(map)
                keyboard.press('enter')

                pyautogui.click(x=125, y=221)
                speak("sir here is your destination")

            googlemap(f'{map}')
        elif "send email" in query:
            webbrowser.open("mail.google.com")
            speak("to u whom send email sir")
            name = takeCommand().isalpha()
            speak("what is the content sir")
            content = takeCommand()
            def email(name,content):
                time.sleep(4)
                pyautogui.click(x=146, y=230)

                time.sleep(4)
                pyautogui.click(x=1227, y=439)
                keyboard.write(name)

                time.sleep(4)
                pyautogui.click(x=1242, y=491)
                keyboard.write(content)

                time.sleep(2)
                pyautogui.click(x=1164, y=989)

                speak("email sent sir")
            email(f'{name}',f'{content}')

        elif "increase the volume to 50" in query:

            time.sleep(2)
            pyautogui.click(x=1701, y=1056)
            time.sleep(2)
            pyautogui.click(x=1696, y=996)

        elif "increase the volume to 10" in query:

            time.sleep(2)
            pyautogui.click(x=1701, y=1056)
            time.sleep(2)
            pyautogui.click(x=1587, y=997)

        elif "increase the volume to 25" in query:

            time.sleep(2)
            pyautogui.click(x=1701, y=1056)
            time.sleep(2)
            pyautogui.click(x=1765, y=1003)

        elif "increase the volume to 75" in query:

            time.sleep(2)
            pyautogui.click(x=1701, y=1056)
            time.sleep(2)
            pyautogui.click(x=1765, y=1003)

        elif "increase the volume 200" in query:

            time.sleep(2)
            pyautogui.click(x=1701, y=1056)
            time.sleep(2)
            pyautogui.click(x=1840, y=994)

        elif "Open my calculator project" in query:

            time.sleep(1)
            mpath= "C:\\Users\\omwak\\OneDrive\\Desktop\\Calculator.java"
            os.startfile(mpath)












        elif "no" in query:
            speak("you are amzing sir have a good day")
            sys.exit()

        speak("sir,do you have any other work")




