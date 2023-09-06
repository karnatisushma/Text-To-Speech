import  pyttsx3

text_speech = pyttsx3.init()
rate = text_speech.getProperty('rate')
text_speech.setProperty('rate',180)
print(rate)

answer = input("Enter what you want to covert to speech :")
text_speech.say(answer)
text_speech.runAndWait()