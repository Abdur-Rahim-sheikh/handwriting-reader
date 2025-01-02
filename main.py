from typing import Annotated
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from handwriting_reader import Converter
from io import BytesIO
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

converter = Converter()

@app.get("/")
def root():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)

@app.post("/uploadfiles")
async def file_converter(files: Annotated[
    list[UploadFile], File(description="Multiple files as upload file")
    ]):

    text = ""
    for file in files:
        content = BytesIO(await file.read())
        text += converter.convert(content)

    return {"extracted": text}
