from typing import Annotated
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
app = FastAPI()
from handwriting_reader import Converter
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
async def converter(files: Annotated[
    list[UploadFile], File(description="Multiple files as upload file")
    ]):

    text = ""
    for file in files:
        text += converter.convert(file.file)

    return {"extracted": text}
