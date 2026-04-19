import pyttsx3

# initialisation du moteur vocal
engine = pyttsx3.init()

# texte à prononcer
message = "Systeme actif. Test vocal reussi"

print("Execution du test audio...")

# dire le message
engine.say(message)                                                                                                                                         

# exécuter la parole
engine.runAndWait()

print("Fin du test")