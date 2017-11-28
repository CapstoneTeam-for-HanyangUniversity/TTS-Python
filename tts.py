from gtts import gTTS
blabla = ("구치훈 병신")
tts = gTTS(text=blabla, lang='ko')
tts.save("./test.mp3")
