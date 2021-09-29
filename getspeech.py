#!/usr/bin/python

import requests, json, base64, sys, os, pathlib, time
now = str(time.time()).replace(".", "")

apikey="AIzaSyBUrG7YyqBHH-TcgwACamVt3mlNU2u5dR4"
url=r"https://texttospeech.googleapis.com/v1beta1/text:synthesize?fields=audioContent&key=%s"%apikey

request = """
{
    "voice":
    {
        "languageCode": "pt-BR",
        "name": "pt-BR-Wavenet-A"
    },
    "input":
    {
        "text":"{text}"
    },
    "audioConfig":
    {
        "audioEncoding":"mp3"
    }
}
"""

# Go through lines of input file and create mp3 from each with the given file name
r=request.replace("{text}","Boa tarde ")
#print r
r = requests.post(url, data=r, allow_redirects=False)
j = json.loads(r.text)

audio = base64.b64decode(j['audioContent'])
pathlib.Path("audios/"+now+"-audio.mp3").write_bytes(audio)

#Convert to WAV file for pbx system
#os.system("mpg321 -w %s.wav %s.mp3"%(fn,fn))
