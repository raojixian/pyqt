# coding:utf-8

import win32com.client
#微软这个服务器
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("你好，请问是张林夕吗？，我是饶继先，就是那个该死的，魅力无处安放的男人，你在干什么啊，我正在写一个语音识别的软件，"
#               "你吃饭了吗，注意身体哦，希望你梦想成真，等我软件写好了，第一个给你看好不好啊")
# speaker.Speak("你们好，请问这是疾控中心最帅，最优秀的群吗？，我是饶继先，就是那个该死的，魅力无处安放的男人，你们在干什么呀，我们明天"
#               "晚上要不吃个火锅怎样啊,大家应该都没有什么意见吧")
speaker.Speak('谢谢，辛苦你了，你是最棒的，这是语音合成的声音')


import pyttsx3
engine = pyttsx3.init()
# engine.say('君不见，黄河之水天上来，奔流到海不复回。')
# engine.say('君不见，高堂明镜悲白发，朝如青丝暮成雪。')
#运行并且等待
engine.runAndWait()
