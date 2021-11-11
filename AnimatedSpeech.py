
from naoqi import ALProxy

annimationSpeech = ALProxy("ALAnimatedSpeech", "192.168.1.101", 9559)

ttw = {"hello":["hey", "yo"],
       "everything": ["everybody"]}

annimationSpeech.addTagsToWords(ttw)
# annimationSpeech.say("Hello! ^start(Think_2) Sorry, what do you mean? ^wait(Think_2)")

# annimationSpeech.say("^start(animations/Stand/Gestures/Enthusiastic_4) Look what I can do while speaking!")
# annimationSpeech.say("^start(animations/Stand/Gestures/Enthusiastic_4) Look what I can do while speaking! ^stop(animations/Stand/Gestures/Enthusiastic_4) Now I am animated by the ALSpeakingMovement module")
# annimationSpeech.say("^startTag(me) My name is Pepper.")
# annimationSpeech.say("^startTag() Hello Na, nice to meet you. ^stopTag(yoo-hoo) My name is Pepper.")

# annimationSpeech.say("^startSound(my_sound_set/my_sound,80) That's cool. ^waitSound(my_sound_set/my_sound)")
# annimationSpeech.say("^pCall(ALMotion.wakeUp()) Ok, I wake up.")

annimationSpeech.say("everybody. Look I can stop moving ^mode(disabled) and after I can resume moving ^mode(contextual), you see ?")
# configurationBody = {"bodyLanguageMode":"contextual"}
# annimationSpeech.say("Hello, I am Pepper", configurationBody)