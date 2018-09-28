#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reconhecimento_voz.py
#  
#  Copyright 2018 Aroldo <AroldoAROLDO-NOT>

import speech_recognition as sr
import sys
import pyttsx3


def get_audio():

	r = sr.Recognizer()
	engine = pyttsx3.init()
	engine.setProperty('voice',b'brazil')

	with sr.Microphone() as s:
		r.adjust_for_ambient_noise(s)
		palavra = ""
		while True:
			audio = r.listen(s)
			try:
				palavra = r.recognize_google(audio,language='pt')
			except sr.UnknownValueError:
				engine.say('Não entendi o que você falou!')
				engine.runAndWait()
			print(palavra)

	return palavra


def main(args):

	print("retorno",get_audio())
    
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



'''
	if palavra == "tudo bem":
		engine.say('Tudo sim e com você?')
		engine.runAndWait()
	if palavra == "desligar":
		engine.say('Adeus, até a próxima!')
		engine.runAndWait()
		sys.exit()
	palavra = ""
'''