import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/css", StaticFiles(directory="css"), name="css")


@app.get("/")
@app.get("/index")
def index():
    page_content = open("pages/index.html").read()
    time = datetime.datetime.now()
    tstr = f"{time.hour}:{time.minute}"
    page_content = page_content.replace("%TIME%", tstr)

    return HTMLResponse(content=page_content)
