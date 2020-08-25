import extra_functions as ef
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")


@app.get("/")
@app.get("/index")
def index_redir():
    return RedirectResponse(url="/home")


@app.get("/home")
def index():
    page_content = open("pages/index.html").read()

    page_content = ef.fillin_hf(page_content)

    return HTMLResponse(content=page_content)


@app.get("/linux")
def linux():
    page_content = open("pages/linux.html").read()

    page_content = ef.fillin_hf(page_content)

    return HTMLResponse(content=page_content)
