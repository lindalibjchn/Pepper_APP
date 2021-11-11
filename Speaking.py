from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "192.168.1.101", 9559)
tts.say("That's cool")

