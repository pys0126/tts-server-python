from pyttsx3 import Engine
import pyttsx3
import time

engine: Engine = pyttsx3.init()

def start(text: str, save_path: str):
    # 设置语音属性
    engine.setProperty("volume", 1)  # 设置音量，范围为0到1
    engine.setProperty("rate", 130)  # 设置语速，默认为200
    engine.save_to_file(text=text, filename=save_path)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        text: str = input("input text: ")
        t1 = time.time()
        start(
            text=text,
            save_path="./ouput.wav"
        )
        t2 = time.time()
        print("文本长度：", len(text))
        print("耗时：", t2 - t1, "\n")
