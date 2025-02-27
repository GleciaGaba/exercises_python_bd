import json

fichier = "settings.json"

with open(fichier, "r") as f:
    settings = json.load(f)

    print(settings.get("font-size"))

settings["font-size"] = 15

with open(fichier, "w") as f:
    json.dump(settings, f, indent=4)