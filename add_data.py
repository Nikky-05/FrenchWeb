import sqlite3
import os

db_path = r'c:\Users\shail\learn_french_site(2)\learn_french_site(2)\learn_french_site\app\learn_french.db'

stories = [
    {
        "title": "Cendrillon - Partie 1",
        "content": """Il était une fois une jeune fille appelée Cendrillon.
Elle vivait avec sa belle-mère et ses deux demi-sœurs qui la
forçaient à faire tout le travail de la maison.
Un jour, le roi invita toutes les jeunes filles du pays à un grand bal.
La marraine de Cendrillon, qui était une fée, transforma une
citrouille en carrosse et les souris en chevaux.
Elle donna à Cendrillon une belle robe et des pantoufles de verre.
Au bal, le prince dansa seulement avec elle.
Mais à minuit, Cendrillon dut partir vite et perdit une pantoufle.
Le prince chercha la jeune fille dans tout le royaume.
Quand il trouva Cendrillon, la pantoufle lui allait parfaitement.
Ils se marièrent et vécurent heureuses."""
    },
    {
        "title": "Cendrillon - Histoire Complète",
        "content": """Il était une fois une jeune fille très gentille appelée Cendrillon.
Elle vivait avec sa belle-mère et ses deux demi-sœurs qui la
forçaient à faire tout le travail de la maison.
Un jour, le roi invita toutes les jeunes filles du pays à un grand bal.
La marraine de Cendrillon, qui était une fée, transforma une
citrouille en carrosse et les souris en chevaux.
Elle donna à Cendrillon une belle robe et des pantoufles de verre.
Au bal, le prince dansa seulement avec elle.
Mais à minuit, Cendrillon dut partir vite et perdit une pantoufle.
Le prince chercha la jeune fille dans tout le royaume.
Quand il trouva Cendrillon, la pantoufle lui allait parfaitement.
Ils se marièrent et vécurent heureux pour toujours."""
    }
]

grammar_items = [
    {
        "title": "Les Articles (Articles)",
        "content": "En français, il existe trois types d'articles : définis (le, la, les), indéfinis (un, une, des) et partitifs (du, de la, des). Ils s'accordent en genre et en nombre avec le nom."
    },
    {
        "title": "Le Genre des Noms (Gender)",
        "content": "Tous les noms en français ont un genre : masculin ou féminin. En général, les noms se terminant par 'e' sont souvent féminins, mais il y a de nombreuses exceptions."
    },
    {
        "title": "Le Sujet (Subject)",
        "content": "Le sujet est la personne ou la chose qui fait l'action. Les pronoms sujets sont : je, tu, il/elle/on, nous, vous, ils/elles."
    },
    {
        "title": "Le Verbe (Verb)",
        "content": "Le verbe exprime une action ou un état. Les verbes se conjuguent selon le temps, le mode, et la personne."
    }
]

def add_content():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Add stories
    for s in stories:
        cur.execute("INSERT INTO stories (title, content) VALUES (?, ?)", (s["title"], s["content"]))
    
    # Add grammar items
    for g in grammar_items:
        cur.execute("INSERT INTO grammar (title, content) VALUES (?, ?)", (g["title"], g["content"]))
    
    conn.commit()
    conn.close()
    print("Content added successfully!")

if __name__ == "__main__":
    add_content()
