from fastapi import FastAPI
import pyttsx3

app = FastAPI()
engine = pyttsx3.init()

@app.post("/driver")
def driver(data: dict):

    fatigue = data["fatigue_score"]
    eyes = data["eyes_closed"]

    if fatigue > 0.7 or eyes:
        engine.say("Attention conducteur, danger")
        engine.runAndWait()
        return {"status": "danger"}

    if fatigue > 0.4:
        engine.say("Restez concentré")
        engine.runAndWait()
        return {"status": "attention"}

    return {"status": "ok"}