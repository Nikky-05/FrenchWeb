-- Run in MySQL (adjust user/database names if needed)
CREATE DATABASE IF NOT EXISTS learn_french;
USE learn_french;

-- Sample inserts (tables are created by SQLAlchemy if not present)
INSERT INTO Vocabulary (category, french, english, pronunciation, created_at)
VALUES
('Colors','Noir','Black','nwar', NOW()),
('Colors','Blanc','White','blahn', NOW()),
('Numbers','un','one','uhn', NOW()),
('Animals','le chien','dog','luh chien', NOW()),
('Food','la pomme','apple','lah pom', NOW());

INSERT INTO GrammarItem (title, content, created_at)
VALUES
('Articles','Definite articles: le, la, l\' , les. Indefinite articles: un, une, des.', NOW()),
('Negation','Use ne...pas around the verb. Example: Je ne parle pas anglais.', NOW());

INSERT INTO Story (title, content) VALUES
('Le Petit Chaperon Rouge','Il était une fois une petite fille...'),
('Cendrillon','Il était une fois une jeune fille très gentille...');

INSERT INTO QuizQuestion (quiz_name, question, options, answer)
VALUES
('Quiz 1','Choose the correct article: ___ livre (book)','la|le|les|l\'','le'),
('Quiz 2','Which sentence is correct?','Je ai un crayon.|J\'ai un crayon.|Je as un crayon.|J\'ai une stylo.','J\'ai un crayon.');
