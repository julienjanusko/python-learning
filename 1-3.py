print("━━━━━━━━━━━━━━━━━")
print("=== QUIZ INFORMATIQUE ===")
print()

questions = [
    {
        "question": "Que veut dire HTML ?",
        "choix": ["A: HyperText Markup Language", 
                  "B: How To Make Lasagna", 
                  "C: High Tech Modern Language"],
        "reponse": "A"
    },
    {
        "question": "Que veut dire HTML ?",
        "choix": ["A: HyperText Markup Language", 
                  "B: How To Make Lasagna", 
                  "C: High Tech Modern Language"],
        "reponse": "A"
    },
    {
        "question": "Que veut dire HTML ?",
        "choix": ["A: HyperText Markup Language", 
                  "B: How To Make Lasagna", 
                  "C: High Tech Modern Language"],
        "reponse": "A"
    },
    {
        "question": "Que veut dire HTML ?",
        "choix": ["A: HyperText Markup Language", 
                  "B: How To Make Lasagna", 
                  "C: High Tech Modern Language"],
        "reponse": "A"
    },
    {
        "question": "Que veut dire HTML ?",
        "choix": ["A: HyperText Markup Language", 
                  "B: How To Make Lasagna", 
                  "C: High Tech Modern Language"],
        "reponse": "C"
    },
 ]

nb_questions = len(questions)
i = 1
score = 0

for i, q in enumerate(questions):
    print(f"Question {i}/{nb_questions}")
    print(q["question"])
    for choix in q["choix"]:
        print(choix)
        reponse = input("Ta réponse : ").strip().upper()
        if reponse in ['A', 'B', 'C']:
            break

    if q["reponse"] == reponse:
        print("✅ Correct !")
        score += 1
    else:
        print("Faux :( !")
    print()
    print()

score_percetange = score/nb_questions*100
print ("=== RÉSULTAT ===")
print(f"Votre score total est de : {score}/{nb_questions} ({score_percetange}%)")

if score_percetange == 0:
    print("Nul!")
elif score_percetange <=40:
    print("Mauvais")
elif score_percetange <=70:
    print("Ok")
else:
    print("Excellent !")