# main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from excel_parser import parse_excel
from timetable import optimize_timetable
from models import Timetable

app = FastAPI()

@app.get("/")
async def read_root():
    with open("static/index.html", "r") as file:
        return HTMLResponse(content=file.read())

@app.post("/optimize/")
async def optimize_timetable_route(file: UploadFile = File(...)):
    data = await file.read()
    students, courses = parse_excel(data)
    timetable = optimize_timetable(students, courses)
    return {"timetable": timetable}

# requirements.txt
fastapi
uvicorn
pandas
openpyxl