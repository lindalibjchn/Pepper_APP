from naoqi import ALProxy

log = ALProxy("ALLogger", "192.168.1.101", 9559)
log.info("python", "hello from Nao")

