from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)
#template = env.get_template("main.html")
templates = Jinja2Templates(directory="templates")

# teste
carro = {"desc": "oi"}

@app.get("/", response_class=HTMLResponse)
def teste(request: Request):
    return templates.TemplateResponse("buying.html", {"request": request, "cars": carro})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)