import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')

text = "A bear walks into a bar and says to the bartender, I'll have a pint of beer and a.......... packet of peanuts."
for voice in voices:
    if 'Kimber' in voice.id:
	print voice.id
        print 'speed now is ' + str(engine.getProperty('rate') )
        engine.setProperty('voice', voice.id)
        engine.setProperty('rate', 100)
        # engine.setProperty('voice', voice.id)
        engine.say(text)
engine.runAndWait()

