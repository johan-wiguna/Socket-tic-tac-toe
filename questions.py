import json

x =  '[\
    {"question":"Which was the first planet to be discovered?", "correct-answer":"Earth", "incorrect-answers":["Mars", "Mercury", "Pluto"]},\
    {"question": "Which country inside the United Kingdom does NOT appear on its flag, The Union Jack?", "correct-answer":"Wales", "incorrect-answers":["Scottland", "Ireland", "Isle of Wight"]},\
    {"question":"Which city is the capital of Switzerland?", "correct-answer":"Bern", "incorrect-answers":["Zürich", "Frankfurt", "Wien"]},\
    {"question":"Who directed the 1973 film American Graffiti?", "correct-answer":"George Lucas", "incorrect-answers":["Steven Spielberg", "Ron Howard", "Quentin Tarantino"]},\
    {"question":"Which of the following countries banned the use of personal genetic ancestry test?", "correct-answer":"Germany", "incorrect-answers":["Austria", "Canada", "Sweden"]},\
    {"question":"Which of these Disney classics was released in 1970?", "correct-answer":"The Aristocats", "incorrect-answers":["101 Dalmatians", "The Fox and The Hound", "The Little Mermaid"]},\
    {"question":"Who won the 2014 FIFA World Cup?", "correct-answer":"Germany", "incorrect-answers":["Italy", "Argentina", "Portugal"]},\
    {"question":"Who developed Cyberpunk 2077?", "correct-answer":"CD Projekt", "incorrect-answers":["Ubisoft", "Electronic Arts", "Activision"]},\
    {"question":"Which of the following video games is not developed by Ubisoft?", "correct-answer":"Fallout", "incorrect-answers":["The Crew", "Steep", "Growtopia"]},\
    {"question":"What is the first board game ever made?", "correct-answer":"Senet", "incorrect-answers":["Clue", "Go", "Chess"]},\
    {"question":"What food was the character Pac Man modeled after?", "correct-answer":"Pizza", "incorrect-answers":["Orange", "Pancake", "Lemon"]},\
    {"question":"Who released the first flight simulator game?", "correct-answer":"Microsoft", "incorrect-answers":["Electronic Arts", "Nintendo", "Bandai Namco"]},\
    {"question":"A doctor with a PhD is a doctor of what?", "correct-answer":"Philosophy", "incorrect-answers":["Psychology", "Phrenology", "Physical Therapy"]},\
    {"question":"At what age did Elvis Presley died?", "correct-answer":"42", "incorrect-answers":["39", "40", "41"]},\
    {"question":"What is Queen\'s first album called?", "correct-answer":"Queen", "incorrect-answers":["Innuendo", "A Night at the Opera", "Sheer Heart Attack"]},\
    {"question":"Who is the first billionaire?", "correct-answer":"John D. Rockefeller", "incorrect-answers":["Jakob Fugger", "Bill Gates", "Andrew Carnegie"]},\
    {"question":"Which greek mathematician ran through the streets of Syracuse naked while shouting \'Eureka\' after discovering the principle of displacement?", "correct-answer":"Archimedes", "incorrect-answers":["Euclid", "Homer", "Eratosthenes"]},\
    {"question":"Which Variable Valve Timing technology is used by BMW?", "correct-answer":"VANOS", "incorrect-answers":["VVT-iw", "VVEL", "MultiAir"]},\
    {"question":"When was Tesla founded?", "correct-answer":"2003", "incorrect-answers":["2008", "2005", "2007"]},\
    {"question":"Which car tire manufacturer is famous for its \'Eagle\' brand of tires, and is the official tire supplier of NASCAR?", "correct-answer":"Goodyear", "incorrect-answers":["Pirelli", "Bridgestone", "Michelin"]},\
    {"question":"Enzo Ferrari was originally an auto racer for what manufacturer before founding his own car company?", "correct-answer":"Alfa Romeo", "incorrect-answers":["Auto Union", "Mercedes Benz", "Bentley"]},\
    {"question":"The dish Fugu, is made from what family of fish?", "correct-answer":"Pufferfish", "incorrect-answers":["Bass", "Salmon", "Mackerel"]},\
    {"question":"Which species of Brown Bear is not extinct?", "correct-answer":"Syrian Brown Bear", "incorrect-answers":["California Grizzly Bear", "Atlas Bear", "Mexican Grizzly Bear"]}]'

y = json.loads(x)

print(y[19]["question"])