import json
from knowledge import Knowledge

def read():
    with open("./input.json", "r", encoding="utf_8") as file:
            file = json.load(file)
            
            knowledgeBase = Knowledge(file["MT"])
            for IF, THEN in file['rules'].items():
                knowledgeBase.addRule(IF, THEN)
            
            return knowledgeBase
