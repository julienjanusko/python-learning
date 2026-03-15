print("=== LISTE DE COURSES ===")
articles = []

while True:
    action = input("Action (ajouter/supprimer/afficher/quitter) : ").strip().lower()
    if action == "ajouter":
        article = input("Article : ").strip().lower()
        articles.append(article)
        print(f"✅ \"{article}\" ajouté !")
    elif action == "supprimer":
        article = input("Article : ").strip().lower()
        if article in articles:
            articles.remove(article)
            print(f"❌ \"{article}\" supprimé !")
        else:
            print("Cet article n'existe pas !")
    elif action == "afficher":
        if not articles:
            print("Il n'existe aucun article dans la liste !")
        else:
            for i, a in enumerate(articles):
                print(f"{i+1}. {a}")
    elif action == "quitter":
        print("👋 À plus !")
        break