from fastapi import FastAPI
from pydantic import BaseModel
import pyttsx3

# -----------------------
# INIT
# -----------------------

app = FastAPI()
engine = pyttsx3.init()

# -----------------------
# DATA MODEL
# -----------------------

class DriverData(BaseModel):
    fatigue_score: float
    eyes_closed: bool

# -----------------------
# CORE LOGIC (SÉPARÉE)
# -----------------------

def analyze_and_speak(fatigue, eyes):

    print("Analyse:", fatigue, eyes)

    if fatigue < 0.4 and not eyes:
        return "ok"

    if 0.4 <= fatigue <= 0.7:
        engine.say("Attention, restez concentré")
        engine.runAndWait()
        return "fatigue_legere"

    if fatigue > 0.7 or eyes:
        engine.say("Danger, reveillez vous")
        engine.runAndWait()
        return "fatigue_elevee"

# -----------------------
# ROUTE API
# -----------------------

@app.post("/driver")
def driver(data: DriverData):

    result = analyze_and_speak(
        data.fatigue_score,
        data.eyes_closed
    )

    return {"result": result}
