
import speech_recognition as sr            # import speech_recognition for voice recognition
import pyttsx3                             # import pyttsx3  for voice to be written or printed or to speak
import pywhatkit                           # import pywhatkit  for playing song in youtube
import datetime                            # import datetime  to tell date and time
import wikipedia                           # import wikipedia  is used to search in wikipedia and give result
import pyjokes                             # import pyjokes for listening jokes

listener = sr.Recognizer()                  # It is a speech recogonizer function
engine = pyttsx3.init()                     # It is used for alexa to speak and intializing the engine
voices = engine.getProperty('voices')       # it is used to get voices in the libaray
engine.setProperty('voice', voices[1].id)       # it is used to select or set the voices present in the library. 0 is for male and 1 is for female.

def talk(text):                             # it is 'talk' function which has text as a parameter and text is message you want your alexa to say
    engine.say(text)                        # it is used to let alexa say what is in the text in her voice
    engine.runAndWait()

def take_command():                                      # 'take_command()' funcion
    try:                                                 # try block
        with sr.Microphone() as source:                  # it is used to use microphone to listen from the user
            print("Hi, I am alexa")
            talk('Hi....I am your alexa')
            print("listening...")
            talk('listening')                            # it is used speak/talk

            voice = listener.listen(source)              # it listen to the source(user)
            command = listener.recognize_google(voice)   # it is used to recongize the voice using google
            command = command.lower()                    # voice in small letter
            if 'alexa' in command:                       # if commamnd .... if word alexa is in command statement then it will exceute the next line oyherwise goes out of that format
                command = command.replace('alexa', '')   # it is used to replace word alexa so that it does not itself uses the word alexa ....it is only used to address alexa
                print(command)                           # printing the command

    except:                                              # except block
        pass
    return command                                        # return command line

def run_alexa():                                          # 'run_alexa' fuction
    command = take_command()                              # instailizing the command with 'take_command()'
    print(command)                                        # calling 'take_command()' function
    if 'play' in command:                                 # if statement ... if play is in command
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)                          # statement from pywhatkit library to open youtube

    elif 'time' in command:                                # elif statement ... if time is in command
        time = datetime.datetime.now().strftime('%I:%M %p')     # it is to give current time and also mention its format
        print(time)
        talk('Current time is' + time)                     # tells the time

    elif ' date' in command:                               # elif statement ... if date is in command
        date = datetime.datetime.now().strftime('%d/ %m /%y')    # it is to give current date and also mention its format
        print(date)
        talk('Current date is' + date)                     # tells the date


    elif 'who' in command:                                 # elif statement ... if who is in command
        person = command.replace('who', '')                # it replaces who
        info = wikipedia.summary(person,1)                 # it is a wikipedia function which is used to search in wikipedia about the person and tells only 1 line if you use 'who' keyword in the front.
        print(info)
        talk(info)                                         # tells about the person

    elif 'what' in command:                                # elif statement ... if what is in command
        thing = command.replace('what', '')                # it replaces what
        info = wikipedia.summary(thing,1)                  # it is a wikipedia function which is used to search in wikipedia about the thing/object and tells only 1 line if you use 'what' keyword in the front.
        print(info)
        talk(info)                                         # tells about the thing

    elif 'date with me' in command:                        # elif statement
        talk('Sorry I am not interested')

    elif 'are you single' in command:                       # elif statement
        talk('I am in a relationship with wifi')

    elif 'sexy' in command:                                 # elif statement
        talk('Fuck off you creep')
        talk('You donot have mother sister or what ....Gaandu')

    elif 'joke' in command:                                  # elif statement
        talk(pyjokes.get_joke())

    elif 'bad day for me' in command:                        # elif statement
        talk(' Its okay everything will be alright')

    elif 'what are you doing' in command:                    # elif statement
        talk('Nothing much just hanging out ')

    elif 'siri' in command:                                  # elif statement
        talk('who is siri')
        talk('I donot like her')

    elif 'thanks for helping me' in command:                 # elif statement
        talk('Your welcome')


    else:                                                    # else statement
        talk('Please say it again.')

run_alexa()                                    # calling 'run_alexa' function