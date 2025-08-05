from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/verify", response_class=HTMLResponse)
def verify(request: Request, message: str = Form(""), file: UploadFile = File(None)):
    try:
        if file is not None:
            content = file.file.read().decode("utf-8")
        else:
            content = message

        result = subprocess.run(
            ["gpg", "--verify"],
            input=content.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stderr.decode()

        if "Good signature" in output or "Assinatura válida" in output:
            status = "VALID"
        else:
            status = "INVALID"

        return templates.TemplateResponse("result.html", {
            "request": request,
            "result": status,
            "output": output
        })

    except Exception as e:
        return templates.TemplateResponse("result.html", {
            "request": request,
            "result": "ERROR",
            "output": str(e)
        })
