import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')

with open('voicetext.txt') as f:
    text = f.read().splitlines()
for voice in voices:
    if 'Kimber' in voice.id:
        print voice.id
        VoiceID = voice.id
        # print 'speed now is ' + str(engine.getProperty('rate') )

engine.setProperty('voice', VoiceID)
engine.setProperty('rate', 100)
for line in text:
    engine.say(text)
engine.runAndWait()

