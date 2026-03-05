from app import db, create_app
from app.models import Vocabulary

def add_new_vocab():
    app = create_app()
    with app.app_context():
        new_data = [
            # Seasons
            {"category": "seasons", "french": "Le printemps", "english": "Spring", "pronunciation": "luh prahn-tah̃"},
            {"category": "seasons", "french": "L’été", "english": "Summer", "pronunciation": "leh-tay"},
            {"category": "seasons", "french": "L’automne", "english": "Fall/Autumn", "pronunciation": "loh-tohn"},
            {"category": "seasons", "french": "L’hiver", "english": "Winter", "pronunciation": "lee-vair"},
            
            # Days of the week
            {"category": "days", "french": "Lundi", "english": "Monday", "pronunciation": "luhn-dee"},
            {"category": "days", "french": "Mardi", "english": "Tuesday", "pronunciation": "mar-dee"},
            {"category": "days", "french": "Mercredi", "english": "Wednesday", "pronunciation": "mehr-cruh-dee"},
            {"category": "days", "french": "Jeudi", "english": "Thursday", "pronunciation": "zhuh-dee"},
            {"category": "days", "french": "Vendredi", "english": "Friday", "pronunciation": "vahn-druh-dee"},
            {"category": "days", "french": "Samedi", "english": "Saturday", "pronunciation": "sam-dee"},
            {"category": "days", "french": "Dimanche", "english": "Sunday", "pronunciation": "dee-mahnsh"},
            
            # Months
            {"category": "months", "french": "Janvier", "english": "January", "pronunciation": "zhahn-vyay"},
            {"category": "months", "french": "Février", "english": "February", "pronunciation": "fay-vree-ay"},
            {"category": "months", "french": "Mars", "english": "March", "pronunciation": "marss"},
            {"category": "months", "french": "Avril", "english": "April", "pronunciation": "ah-vreel"},
            {"category": "months", "french": "Mai", "english": "May", "pronunciation": "may"},
            {"category": "months", "french": "Juin", "english": "June", "pronunciation": "zhwan"},
            {"category": "months", "french": "Juillet", "english": "July", "pronunciation": "zhwee-yay"},
            {"category": "months", "french": "Août", "english": "August", "pronunciation": "ooh"},
            {"category": "months", "french": "Septembre", "english": "September", "pronunciation": "sep-tahmbr"},
            {"category": "months", "french": "Octobre", "english": "October", "pronunciation": "ok-toh-br"},
            {"category": "months", "french": "Novembre", "english": "November", "pronunciation": "noh-vahmbr"},
            {"category": "months", "french": "Décembre", "english": "December", "pronunciation": "day-sahmbr"},
        ]
        
        for item in new_data:
            # Check if it already exists to avoid duplicates
            existing = Vocabulary.query.filter_by(french=item["french"], english=item["english"]).first()
            if not existing:
                vocab = Vocabulary(**item)
                db.session.add(vocab)
        
        db.session.commit()
        print("Successfully added Seasons, Days, and Months to Vocabulary!")

if __name__ == "__main__":
    add_new_vocab()
