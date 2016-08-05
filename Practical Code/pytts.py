import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')

text = "A bear walks into a bar and says to the bartender, I'll have a pint of beer and a.......... packet of peanuts."
for voice in voices:
    if 'ZIRA' in voice.id:
        engine.setProperty('voice', voice.id)
        engine.say(text)
engine.runAndWait()
