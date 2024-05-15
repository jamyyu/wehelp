from typing import Annotated
from fastapi import FastAPI, Form, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
from pydantic import BaseModel


con=mysql.connector.connect(
    user="root",
    password="sE19921118!!",
    host="localhost",
    database="website"
)
cursor=con.cursor()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="jamy", https_only=True, max_age=None)


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/signup")
async def signup(
    request: Request,
    name: Annotated[str, Form()],
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]  
):
    cursor.execute("SELECT username FROM member WHERE username=%s ",(username,))
    data=cursor.fetchone()
    if data:
        error_message = "帳號已經被註冊"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    else:    
        cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)",(name, username , password))
        con.commit()
        return RedirectResponse(url="/", status_code=303)


@app.post("/signin")
async def signin(
    request: Request,
    username: Annotated[str, Form()],  
    password: Annotated[str, Form()] 
):
    cursor.execute("SELECT id, name, username FROM member WHERE username=%s and password=%s",(username, password))
    data=cursor.fetchall()
    if data:
        request.session["SIGNED-IN"] = True
        request.session["memberid"] = data[0][0]
        request.session["name"] = data[0][1]
        request.session["username"] = data[0][2]
        return RedirectResponse(url="/member",status_code=303)
    else:
        error_message = "帳號、密碼輸入錯誤"
        return RedirectResponse(url=f"/error?message={error_message}", status_code=303)
    
    
@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if request.session.get("SIGNED-IN"):
        cursor.execute("SELECT member.id, member.name, message.content, message.id FROM message INNER JOIN member ON message.member_id = member.id ORDER BY message.id DESC")
        data=cursor.fetchall()
        return templates.TemplateResponse("member.html", {"request": request, "name":request.session["name"], "data":data , "member_id":request.session["memberid"]})
    else:
        return RedirectResponse(url="/", status_code=303)
    

@app.get("/api/member")
async def api_member(request: Request ,username: str = Query(...)):
    if not request.session.get("SIGNED-IN"):
        return JSONResponse(content={"data": None}, status_code=401)
    cursor.execute("SELECT id, name, username FROM member Where username=%s",(username,))
    data=cursor.fetchone()
    if data:
        response_data = {
                "id": data[0],
                "name": data[1],
                "username": data[2]
            }
        return JSONResponse(content={"data":response_data})
    else:
        return JSONResponse(content={"data": None}, status_code=404)


class UpdateName(BaseModel):
    name: str

@app.patch("/api/member")
async def api_member(request: Request, updatename:UpdateName):
    id= request.session["memberid"]
    name = updatename.name
    if not request.session.get("SIGNED-IN"):
        return JSONResponse(content={"error": True}, status_code=401)
    if not id or not name:
        return JSONResponse(content={"error": True}, status_code=400)
    cursor.execute("UPDATE member SET name =%s Where id=%s",(name, id))
    con.commit()
    request.session["name"] = name
    return JSONResponse(content={"ok": True}, status_code=200)
    

@app.get("/error", response_class=HTMLResponse)
async def show_error(request: Request, message: str):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})


@app.get("/signout")
async def redirect_signout(request: Request):
    request.session["SIGNED-IN"] = False
    del request.session["memberid"]
    del request.session["name"]
    del request.session["username"]
    return RedirectResponse(url="/", status_code=303)


@app.post("/creatMessage")
async def creat_message(
    request: Request,
    content: Annotated[str, Form()]
):
    member_id = request.session["memberid"]
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)",(member_id, content))
    con.commit()
    return RedirectResponse(url="/member", status_code=303)



class Item(BaseModel):
    messageid: int

@app.post("/deleteMessage")
async def delete_message(
    request: Request,
    item: Item
):
    messageid = item.messageid
    cursor.execute("SELECT message.member_id FROM message WHERE message.id=%s",(messageid,))
    data=cursor.fetchone()
    memberid = data[0]
    member_id = request.session["memberid"]
    if memberid == member_id:
        cursor.execute("DELETE FROM message WHERE message.id=%s",(messageid,))
        con.commit()
        return RedirectResponse(url="/member", status_code=303)

    
    

    












