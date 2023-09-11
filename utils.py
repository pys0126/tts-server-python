from config import cache_path
from pyttsx3 import Engine
import hashlib
import os


def start_tts(text: str, engine: Engine, volume: int = 1, rate: int = 120) -> str:
    """
    生成语音
    参数：
        text：需要转成语音的文本
        engine：语音引擎
        volume：音量
        rate：语速
    返回值：语音路径
    """
    filename: str = generate_md5(data=text) + ".wav"
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
    save_file_path: str = os.path.join(cache_path, filename)
    if os.path.exists(save_file_path):
        return save_file_path
    # 设置语音属性
    engine.setProperty("volume", volume)  # 设置音量，范围为0到1
    engine.setProperty("rate", rate)  # 设置语速，默认为200
    engine.save_to_file(text=text, filename=save_file_path)
    engine.runAndWait()
    return save_file_path


def generate_md5(data: str) -> str:
    """
    生成md5
    参数：
        data: 原文
    返回值: md5密文
    """
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode("utf-8"))
    return md5_hash.hexdigest()

if __name__ == "__main__":    
    engine: Engine = Engine()
    start_tts(text="5、2、1、3、9、4", engine=engine, rate=100)