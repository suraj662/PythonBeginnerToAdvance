#Rule Based AI Python ChatBot
import datetime
import time
from urllib.parse import uses_relative

name = input("Swagaat h,Enter the name :")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning" , name)
elif 12 <= presentHour <= 17:
    print("Good Afternoon" , name)
else:
    print("Good Evening" , name)


print("Namaste! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses ]
response = {
    "hello": "Hi, welcome. How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better developer",
    "happy": "Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho"
}


# Method/Function to get response of ChatBot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return response[eachKey]


    return "I am not able to tell that yet. Mai jald hi ye sikh lunga"


# Take user input
while True:
    userInput= input("Please ask your question:")
    reply= getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if "bye" in userInput.lower():
        break