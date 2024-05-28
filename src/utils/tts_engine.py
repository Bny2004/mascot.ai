import pyttsx3
from yt_chat import yt_chat


engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

video_id = input("Enter YouTube Live Stream video ID: ")
chat = yt_chat(video_id)
while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            engine.say(c.message)
            engine.runAndWait()
engine.stop()


# if __name__ == "__main__":
#     while True:

#         try:
        
#             text = input(">>> ")
#             engine.say(text)
#             engine.runAndWait()

#             if text.lower() == "exit":
#                 engine.stop()
#                 break

#         except KeyboardInterrupt:
#             engine.stop()
#             break
