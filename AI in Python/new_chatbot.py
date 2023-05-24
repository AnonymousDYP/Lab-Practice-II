import nltk
from nltk.chat.util import Chat, reflections
from datetime import date,datetime

def get_date():
    today=date.today()
    return today.strftime("%B %d, %Y")
def get_time():
    time=datetime.now()
    return time.strftime("%H:%M:%S")
pairs={
    "hi": "Hey there!!",
    "what is your name?": "I am a chatbot created for your convinence you can call me by any name :)",
    "how are you?": "I'm doing good. How about You?",
    "sorry": "Its alright",
    "i am fine": "Great to hear that, How can I help you?",
    "i am good": "Nice to hear that",
    "what is your age?": "I'm a computer program dude seriously you are asking me this?",
    "what do you want?": "Make me an offer I can't refuse",
    "who created this chatbot?": "It's a secret ;)",
    "which is your city?": 'Pune, Maharashtra',
    "how is weather in Pune?": "Weather in Pune is awesome like always",
    "what is the date":get_date(),
    "what's the time":get_time(),
}

def chat(command):
    for key in pairs:
        if key==command:
            return pairs[key]
    return "Enter a Valid Key "
if __name__== "__main__":
    print("Hey there! How can I help you today?")
    flag = True
    while(flag):
        command = input("Me: ").lower()
        if command == "quit":
            flag = False
            print("Thank you for using our intelligence services")
        else:
            print("Chatbot: ",chat(command))
        
        