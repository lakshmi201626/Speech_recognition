import pyttsx3
txt_sp=pyttsx3.init()
text=input('enter the text..\n')

voices=txt_sp.getProperty('voices')
for voice in voices:
    print('ID',voice.id)

txt_sp.setProperty('voice',voices[1].id)
txt_sp.say(text)
txt_sp.runAndWait()

#voices
# ID HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0
# ID HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0

