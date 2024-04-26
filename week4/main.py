from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="jamy", https_only=True, max_age=None)


@app.get("/", response_class=HTMLResponse)
async def signin_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/square/{positivenumber}", response_class=HTMLResponse)
async def calculate_square(request: Request, positivenumber: int):
    square = positivenumber ** 2
    return templates.TemplateResponse("square.html", {"request": request, "square":square})


@app.post("/signin")
async def signin(
    request: Request,
    username: Annotated[str, Form()] = None,  
    password: Annotated[str, Form()] = None  
):
    if username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    elif not username or not password:
        error_message = "請輸入帳號、密碼"
    else:
        error_message = "帳號、密碼輸入錯誤"
    return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    
    
@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if request.session.get("SIGNED-IN"):
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        return RedirectResponse(url="/", status_code=303)


@app.get("/error", response_class=HTMLResponse)
async def show_error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})


@app.get("/signout")
async def redirect_signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)










