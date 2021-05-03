import json

# x = [{"question": "What is this?", "correct-answer": "This is this.", "wrong-answer": ("That", "Those", "These")},
# {"question": "Pick one!", "correct-answer": "One", "wrong-answer": ("1", "Something", "01")}]

x =  '[{"question":"What is this?", "correct-answer":"This is this.", "wrong-answer": ["That", "Those", "These"]},\
    {"question": "Pick one!", "correct-answer": "One", "wrong-answer": ["1", "Something", "01"]}]'

y = json.loads(x)

print(y[0]["question"])