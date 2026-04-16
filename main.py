# main.py

# 1. Import des outils nécessaires
from fastapi import FastAPI
from pydantic import BaseModel
import pyttsx3

# 2. Initialisation du moteur vocal
engine = pyttsx3.init()

# 3. Création de l'application API
app = FastAPI()

# 4. Définition du modèle de données (ce qu'on va recevoir)
class DriverData(BaseModel):
    fatigue_score: float
    eyes_closed: bool

# 5. Route de test
@app.get("/")
def home():
    return {"message": "Systeme decisionnel actif"}

# 6. Route principale : recevoir données conducteur
@app.post("/driver")
def receive_driver_data(data: DriverData):

    # 7. Affichage console (debug)
    print("Données reçues :", data)

    # 8. Logique décisionnelle simple
    if data.fatigue_score > 0.7 or data.eyes_closed:
        engine.say("Attention conducteur, restez vigilant")
        engine.runAndWait()
        return {"alert": "fatigue detectee"}

    return {"status": "ok"}