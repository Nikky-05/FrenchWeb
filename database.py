from app import create_app
from app.models import db, Vocabulary, GrammarItem, ShortStory, Quiz, QuizQuestion

# Create app instance
app = create_app()

with app.app_context():
    # Drop and recreate tables to ensure a clean slate for "proper data"
    db.drop_all()
    db.create_all()

    # ======================================================
    # 🟦 Vocabulary (Expanded)
    # ======================================================
    vocab_data = [
        # Colors 🎨
        ("colors", "rouge", "red", "roo-zh"),
        ("colors", "bleu", "blue", "bluh"),
        ("colors", "vert", "green", "vehr"),
        ("colors", "jaune", "yellow", "zhohn"),
        ("colors", "noir", "black", "nwahr"),
        ("colors", "blanc", "white", "blahn"),
        ("colors", "rose", "pink", "rohz"),
        ("colors", "orange", "orange", "oh-rahn-zh"),
        
        # Numbers 🔢
        ("numbers", "un", "one", "un"),
        ("numbers", "deux", "two", "duh"),
        ("numbers", "trois", "three", "trwah"),
        ("numbers", "quatre", "four", "kahtr"),
        ("numbers", "cinq", "five", "sank"),
        ("numbers", "six", "six", "seess"),
        ("numbers", "sept", "seven", "set"),
        ("numbers", "huit", "eight", "weet"),
        ("numbers", "neuf", "nine", "nuhf"),
        ("numbers", "dix", "ten", "deess"),

        # Food 🍎
        ("food", "la pomme", "apple", "lah pom"),
        ("food", "le pain", "bread", "luh pan"),
        ("food", "le fromage", "cheese", "luh fro-mah-zh"),
        ("food", "le café", "coffee", "luh kah-fey"),
        ("food", "le lait", "milk", "luh leh"),
        ("food", "le poulet", "chicken", "luh poo-leh"),
        ("food", "le poisson", "fish", "luh pwah-sohn"),
        ("food", "la banane", "banana", "lah bah-nahn"),
        ("food", "l'eau", "water", "loh"),

        # Animals 🐶
        ("animals", "le chien", "dog", "luh shy-ah n"),
        ("animals", "le chat", "cat", "luh shah"),
        ("animals", "le cheval", "horse", "luh shuh-vahl"),
        ("animals", "l'oiseau", "bird", "lwah-zoh"),
        ("animals", "le lion", "lion", "luh lee-ohn"),
        ("animals", "le singe", "monkey", "luh san-zh"),
        ("animals", "le lapin", "rabbit", "luh lah-pan"),
        ("animals", "la vache", "cow", "lah vah-sh"),

        # Family 👨‍👩‍👧
        ("family", "la famille", "family", "lah fah-mee"),
        ("family", "la mère", "mother", "lah mehr"),
        ("family", "le père", "father", "luh pehr"),
        ("family", "la soeur", "sister", "lah suhr"),
        ("family", "le frère", "brother", "luh frehr"),
        ("family", "la grand-mère", "grandmother", "lah grahn-mehr"),
        ("family", "le grand-père", "grandfather", "luh grahn-pehr"),
        ("family", "le fils", "son", "luh feess"),
        ("family", "la fille", "daughter", "lah fee"),

        # Seasons 🌦️
        ("seasons", "le printemps", "spring", "luh prahn-tah̃"),
        ("seasons", "l'été", "summer", "leh-tay"),
        ("seasons", "l'automne", "fall/autumn", "loh-tohn"),
        ("seasons", "l'hiver", "winter", "lee-vair"),

        # Days of the Week 📅
        ("days", "lundi", "monday", "luhn-dee"),
        ("days", "mardi", "tuesday", "mar-dee"),
        ("days", "mercredi", "wednesday", "mehr-cruh-dee"),
        ("days", "jeudi", "thursday", "zhuh-dee"),
        ("days", "vendredi", "friday", "vahn-druh-dee"),
        ("days", "samedi", "saturday", "sam-dee"),
        ("days", "dimanche", "sunday", "dee-mahnsh"),

        # Months 🗓️
        ("months", "janvier", "january", "zhahn-vyay"),
        ("months", "février", "february", "fay-vree-ay"),
        ("months", "mars", "march", "marss"),
        ("months", "avril", "april", "ah-vreel"),
        ("months", "mai", "may", "may"),
        ("months", "juin", "june", "zhwan"),
        ("months", "juillet", "july", "zhwee-yay"),
        ("months", "août", "august", "ooh"),
        ("months", "septembre", "september", "sep-tahmbr"),
        ("months", "octobre", "october", "ok-toh-br"),
        ("months", "novembre", "november", "noh-vahmbr"),
        ("months", "décembre", "december", "day-sahmbr"),
    ]
    
    for cat, fr, en, pr in vocab_data:
        db.session.add(Vocabulary(category=cat, french=fr, english=en, pronunciation=pr))
    print("🗂️ Vocabulary database populated!")

    # ======================================================
    # 📘 Grammar (Expanded)
    # ======================================================
    grammar_data = [
        ("Articles", 
         "French has definite articles (**le, la, l', les**) and indefinite articles (**un, une, des**). "
         "Nouns always carry a gender. Use **le** for masculine singular nouns (_le livre_) and **la** for feminine ones (_la table_). "
         "If the noun starts with a vowel, use **l'** (_l'eau_)."),
         
        ("Gender", 
         "Every French noun is either **Masculine** or **Feminine**. Usually, words ending in 'e' or 'ion' are feminine, "
         "while most others are masculine. Examples: _Le vélo_ (M), _La voiture_ (F)."),
         
        ("Subject Pronouns", 
         "These are the foundations of sentences: **Je** (I), **Tu** (You singular), **Il/Elle/On** (He/She/One), "
         "**Nous** (We), **Vous** (You plural/formal), **Ils/Elles** (They)."),
         
        ("Verbs", 
         "Common 'ER' verbs like **manger** (to eat), **parler** (to speak), and **chanter** (to sing) follow a regular pattern. "
         "Irrigular but essential verbs include **être** (to be) and **avoir** (to have)."),
    ]

    for title, content in grammar_data:
        db.session.add(GrammarItem(title=title, content=content))
    print("📘 Grammar rules added!")

    # ======================================================
    # 📕 Short Stories (Expanded)
    # ======================================================
    stories_data = [
        ("Le Corbeau et le Renard by Jean de La Fontaine", 
         """<div style="text-align: center; margin-bottom: 20px;">
<audio controls style="width: 100%; max-width: 600px; border-radius: 30px;">
    <source src="/static/audio/story1_audio.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
</div>
<div style="text-align: center; margin-bottom: 30px;">
<img src="/static/images/corbeau_renard.png" alt="Le Corbeau et le Renard" style="max-width: 100%; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
</div>
Maître Corbeau sur un arbre perché,<br>
Tenoit en son bec un fromage.<br>
Maître Renard par l’odeur alleché<br>
Luy tint à peu prés ce langage:
﻿Et bon jour, Monsieur du Corbeau.<br>
Que vous êtes joly! que vous me ſemblez beau!<br>
﻿Sans mentir, ſi voſtre ramage<br>
﻿Se rapporte à voſtre plumage,<br>
Vous êtes le Phénix des hôtes de ces bois.<br>
À ces mots le Corbeau ne se ſent pas de joye:      <br>
﻿Et pour monſtrer ſa belle voix,<br>
Il ouvre un large bec, laiſse tomber ſa proye.     <br>
Le Renard s’en ſaiſit, & dit: Mon bon Monſieur,   <br>
﻿Apprenez que tout flateur<br>
Vit aux dépens de celuy qui l’écoute.<br>
Cette leçon vaut bien un fromage ſans doute.<br>
﻿Le Corbeau honteux & confus<br>
Jura, mais un peu tard, qu’on ne l’y prendroit plus.<br><br>
<strong>English Translation:</strong><br>
Master Crow perched on a tree, Was holding a cheese in his beak.<br>
Master Fox drawn by the smell Said something like this:<br>
“Well, Hello Mister Crow! How pretty you are! How handsome you seem to me!<br>
I’m not lying, if your voice Is like your plumage, You are the phoenix of all the inhabitants of these woods.”<br>
At these words, the Crow is overjoyed. And in order to show off his beautiful voice, He opens his beak wide, lets his prey fall. The Fox grabs it, and says: “My good man, Learn that every flatterer Lives at the expense of the one who listens to him. This lesson, without doubt, is well worth a cheese.”<br>
The Crow, ashamed and embarrassed, Swore, but a little late, that he would not be taken again.""" + """<br><hr><p style='font-size: 0.85rem; color: #7f8c8d; font-style: italic; text-align: right;'>- “Le Corbeau et le Renard” by Jean de La Fontaine, Wikimedia Commons.<br>- Illustration of Le Corbeau et le Renard, Picryl, n.d.</p>"""),
        ("Le Lièvre et la Tortue by Jean de la Fontaine", 
         """<div style="text-align: center; margin-bottom: 20px;">
<audio controls style="width: 100%; max-width: 600px; border-radius: 30px;">
    <source src="/static/audio/story2_audio.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
</audio>
</div>
Rien ne sert de courir; il faut partir à point:<br>
Le lièvre et la tortue en sont un témoignage.<br>
Gageons, dit celle-ci, que vous n’atteindrez point<br>
Sitôt que moi ce but. Sitôt! Êtes-vous sage?<br>
﻿Repartit l’animal léger:<br>
﻿Ma commère, il vous faut purger<br>
﻿Avec quatre grains d’ellébore.<br>
<div style="text-align: center; margin: 30px 0;">
<img src="/static/images/lievre_tortue.png" alt="Le Lièvre et la Tortue" style="max-width: 100%; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
</div>
— Sage ou non, je parie encore.<br>
﻿Ainsi fut fait; et de tous deux<br>
﻿On mit près du but les enjeux.<br>
﻿Savoir quoi, ce n’est pas l’affaire,<br>
﻿Ni de quel juge l’on convint.<br>
Notre lièvre n’avait que quatre pas à faire;<br>
J’entends de ceux qu’il fait lorsque, près d’être atteint,<br>
Il s’éloigne des chiens, les renvoie aux calendes,<br>
﻿Et leur fait arpenter les landes.<br>
Ayant, dis-je, du temps de reste pour brouter,     <br>
﻿Pour dormir, et pour écouter<br>
﻿D’où vient le vent, il laisse la tortue<br>
﻿Aller son train de sénateur.<br>
﻿Elle part, elle s’évertue;<br>
﻿Elle se hâte avec lenteur.<br>
Lui cependant méprise une telle victoire,<br>
﻿Tient la gageure à peu de gloire,<br>
﻿Croit qu’il y va de son honneur<br>
﻿De partir tard. Il broute, il se repose;<br>
﻿Il s’amuse à toute autre chose<br>
﻿Qu’à la gageure. À la fin, quand il vit<br>
Que l’autre touchait presque au bout de la carrière,<br>
Il partit comme un trait; mais les élans qu’il fit<br>
Furent vains: la tortue arriva la première.<br>
Eh bien! lui cria-t-elle, avais-je pas raison?<br>
﻿De quoi vous sert votre vitesse?<br>
﻿Moi l’emporter! et que serait-ce<br>
﻿Si vous portiez une maison?<br><br>
<strong>English Translation:</strong><br>
There is no point in running; You have to start on time: The hare and the tortoise are a testimony to this. "Let us wager," said the latter, "that you will not reach As soon as I this goal. Soon! Are you wise? Replied the light animal: My friend, you must purge With four grains of hellebore. "Wise or not, I bet again." And so it was done; and of both The stakes were set near. What they were, that's not the point, Nor which judge they agreed upon. Our hare had only four steps to take; I mean those he does when, on the point of being reached, He distances himself from the dogs, sends them away effortlessly, And makes them roam the moors. Having, I say, time to graze, To sleep, and to listen To where the wind comes from, he leaves the tortoise To go to his senator's pace. She leaves, she strives to do so; She hurries slowly. He, however, despises such a victory, Holds the wager to little glory, Believes that his honor requires That he start late. He grazes, he rests; He amuses himself with anything Rather than the bet. In the end, when he lives That the other was almost at the end of his career, He went off like a bolt, but the impulses he made Were in vain: the tortoise arrived first. Well! "Was I not right?" she cried. What is your speed good for? I won! And what would it be If you were carrying a house?""" + """<br><hr><p style='font-size: 0.85rem; color: #7f8c8d; font-style: italic; text-align: right;'>- “Le Lièvre et la Tortue” by Jean de La Fontaine, Wikimedia Commons.<br>- Illustration of Le Lièvre et la Tortue, Picryl, n.d.</p>"""),
    ]

    for title, content in stories_data:
        db.session.add(ShortStory(title=title, content=content))
    print("📚 Short stories added!")

    # ======================================================
    # 🧠 Quizzes (Expanded)
    # ======================================================
    quiz1 = Quiz(title="French Grammar Basics", description="Test your knowledge of basic French rules!")
    quiz2 = Quiz(title="Everyday French", description="Quiz about common items, food, and animals.")
    db.session.add_all([quiz1, quiz2])
    db.session.commit()

    # Quiz 1 Questions (Grammar)
    q1_questions = [
        ("Which article is feminine singular?", "le,la,les,un", "la"),
        ("How do you say 'I' in French?", "Je,Tu,Nous,Il", "Je"),
        ("What is the plural of 'le chat'?", "le chats,les chat,les chats,la chats", "les chats"),
    ]
    
    # Quiz 2 Questions (Vocabulary)
    q2_questions = [
        ("What is 'un chien'?", "a cat,a bird,a dog,a horse", "a dog"),
        ("What color is 'rouge'?", "blue,red,green,yellow", "red"),
        ("How do you say 'Bread'?", "le fromage,le pain,le lait,la pomme", "le pain"),
    ]

    for q, opt, ans in q1_questions:
        db.session.add(QuizQuestion(quiz_id=quiz1.id, quiz_name=quiz1.title, question=q, options=opt, answer=ans))
    
    for q, opt, ans in q2_questions:
        db.session.add(QuizQuestion(quiz_id=quiz2.id, quiz_name=quiz2.title, question=q, options=opt, answer=ans))

    db.session.commit()
    print("🧠 Comprehensive Quizzes and Questions added!")
    print("🎉 Proper data population complete!")
