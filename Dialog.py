from naoqi import ALProxy

topic_path = "home/nao/naoqi/myDialog.top"
ALDialog = ALProxy("ALDialog", "192.168.1.101", 9559)
ALDialog.setLanguage("English")
topf_path = topic_path.decode('utf-8')
topic_name = ALDialog.loadTopic("/home/nao/naoqi/myDialog.top")
ALDialog.activateTopic(topic_name)

ALDialog.subscribe('my_dialog_example')

try:
    raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")
finally:
    # stopping the dialog engine
    ALDialog.unsubscribe('my_dialog_example')

    # Deactivating the topic
    ALDialog.deactivateTopic(topic_name)

    # now that the dialog engine is stopped and there are no more activated topics,
    # we can unload our topic and free the associated memory
    ALDialog.unloadTopic(topic_name)