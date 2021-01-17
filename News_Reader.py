import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    pass
news=requests.get("http://newsapi.org/v2/everything?q=bitcoin&from=2020-11-30&sortBy=publishedAt&apiKey=36ff21b9bbce4ce182063448555caa96")
news=news.text
print(news)
print(type(news))
news=json.loads(news)
print(news)
print(type(news))
n=1
for data in news["articles"]:
    asd=f" Head Line {n}" + data["title"]
    n+=1
    speak(asd)
