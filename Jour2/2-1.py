print("=== LISTE DE COURSES ===")
articles = []

while True:
    action = input("Action (ajouter/supprimer/afficher/quitter) : ").strip().lower()
    if action == "ajouter":
        article = input("Article : ").strip().lower()
        articles.append(article)
        print(f"{article} ajouté !")
    elif action == "supprimer":
        article = input("Article : ").strip().lower()
        if article in articles:
            articles.remove(article)
            print(f"{article} supprimé !")
        else:
            print(f"{article} non trouvé !")
    elif action == "afficher":
        if not articles:
            print("Ta liste est vide !")
        else:
            print("Ta liste : ")
            for i, article in enumerate(articles):
                print(f"{i+1}. {article}")
    elif action == "quitter":
        print("Au revoir !")
        break
    else:
        print("Action inconnue !")