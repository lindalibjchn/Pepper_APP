from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "192.168.1.101", 9559)
motion =  ALProxy("ALMotion", "192.168.1.101", 9559)
motion.setStiffnesses("Body", 1.0)
motion.moveInit()


