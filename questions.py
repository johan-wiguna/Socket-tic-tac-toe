import json

x =  '[{"question":"Which was the first planet to be discovered?", "correct-answer":"Earth", "wrong-answer": ["Mars", "Mercury", "Pluto"]},\
    {"question": "Which country inside the United Kingdom does NOT appear on its flag, The Union Jack?", "correct-answer": "Wales", "wrong-answer": ["Scottland", "Ireland", "Isle of Wight"]},\
    {"question":"Which city is the capital of Switzerland?", "correct-answer":"Bern", "wrong-answer": ["Zürich", "Frankfurt", "Wien"]},\
    {"question":"Who directed the 1973 film American Graffiti?", "correct-answer":"George Lucas", "wrong-answer": ["Steven Spielberg", "Ron Howard", "Quentin Tarantino"]},\
    {"question":"Which of the following countries banned the use of personal genetic ancestry test?", "correct-answer":"Germany", "wrong-answer": ["Austria", "Canada", "Sweden"]},\
    {"question":"Which of these Disney classics was released in 1970?", "correct-answer":"The Aristocats", "wrong-answer": ["101 Dalmatians", "The Fox and The Hound", "The Little Mermaid"]},\
    {"question":"Who won the 2014 FIFA World Cup?", "correct-answer":"Germany", "wrong-answer": ["Italy", "Argentina", "Portugal"]},\
    {"question":"Who developed Cyberpunk 2077?", "correct-answer":"CD Projekt", "wrong-answer": ["Ubisoft", "Electronic Arts", "Activision"]},\
    {"question":"Which of the following video games is not developed by Ubisoft?", "correct-answer":"Need for Speed", "wrong-answer": ["The Crew", "Steep", "Growtopia"]},\
    {"question":"What is the first board game ever made?", "correct-answer":"Senet", "wrong-answer": ["Clue", "Go", "Chess"]},\
    {"question":"What food was the character Pac Man modeled after?", "correct-answer":"Pizza", "wrong-answer": ["Orange", "Pancake", "Lemon"]},\
    {"question":"Who released the first flight simulator game?", "correct-answer":"Microsoft", "wrong-answer": ["Electronic Arts", "Nintendo", "Bandai Namco"]},\
    {"question":"A doctor with a PhD is a doctor of what?", "correct-answer":"Philosophy", "wrong-answer": ["Psychology", "Phrenology", "Physical Therapy"]},\
    {"question":"At what age did Elvis Presley died?", "correct-answer":"42", "wrong-answer": ["39", "40", "41"]}]'

y = json.loads(x)

print(y[7]["question"])