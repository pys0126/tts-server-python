import os
import uvicorn
import pyttsx3
from typing import Union
from pyttsx3 import Engine
from utils import start_tts
from status_code import StatusCode
from json.decoder import JSONDecodeError
from fastapi import FastAPI, Request, Query
from config import host, port, workers, cache_path
from fastapi.responses import FileResponse, JSONResponse


# 初始化 pyttsx3 引擎
engine: Engine = pyttsx3.init()
# 实例化FastAPI
app: FastAPI = FastAPI()


@app.post("/tts")
async def tts(request: Request):
    try:
        request_data: dict = await request.json()
    except JSONDecodeError as e:
        print(e)
        return JSONResponse(content={
            "code": StatusCode.REQUEST_ERROR.value,
            "message": "请求数据错误"
        })
    text: str = request_data.get("text")
    if not text:
        return JSONResponse(content={
            "code": StatusCode.REQUEST_ERROR.value,
            "message": "请求数据错误"
        })
    tts_file_path: str = start_tts(text=text, engine=engine)
    return JSONResponse(content={
        "code": StatusCode.OK.value,
        "message": "成功",
        "filename": os.path.basename(tts_file_path)
    })


@app.get("/getAudio")
async def get_audio(filename: str = Query(...)):
    file_path: str = os.path.join(cache_path, filename)
    if not os.path.exists(file_path):
        return JSONResponse(content={
            "code": StatusCode.FILE_NOT_FOUND.value,
            "message": "访问的文件不存在"
        })
    return FileResponse(path=os.path.abspath(file_path), filename=os.path.basename(file_path))


if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port, workers=1)