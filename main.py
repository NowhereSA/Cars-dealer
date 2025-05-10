from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from jinja2 import Environment, PackageLoader, select_autoescape

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
env = Environment(
    loader=PackageLoader("main"),
    autoescape=select_autoescape()
)
template = env.get_template("main.html")

@app.get("/", response_class=HTMLResponse)
def teste():
    return template.render()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)