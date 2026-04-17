""" 
 # main.py

from fastapi import FastAPI
import pyttsx3

# Initialisation du moteur vocal
engine = pyttsx3.init()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Systeme decisionnel actif"}

# Nouvelle route : alerte vocale
@app.get("/alert")
def alert():
    engine.say("Attention conducteur, restez vigilant")
    engine.runAndWait()
    return {"status": "alerte envoyee"} """