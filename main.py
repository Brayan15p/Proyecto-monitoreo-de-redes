from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.user_service import login_inseguro

app = FastAPI()
templates = Jinja2Templates(directory="pagina_victima") 

@app.get("/", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def procesar_login(username: str = Form(...), password: str = Form(...)):
    usuario = login_inseguro(username, password)
    if usuario:
        return {"mensaje": f"✅ Bienvenido {username}"}
    else:
        return {"mensaje": "❌ Credenciales incorrectas"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
