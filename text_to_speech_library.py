import gtts
import playsound

text = input("Enter something here: ")

sound = gtts.gTTS(text, lang ="hi" )

sound.save("sound.mp3")
playsound.playsound("sound.mp3")
print("Playing the sound...")







