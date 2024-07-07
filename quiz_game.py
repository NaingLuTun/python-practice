from Questions import Question

copy = "\n(a)  \n(b)  \n(c)  \n(d)\n\n"

questions_prompts = [
    "What is the capital of Germany? \n(a) Muich \n(b) Hamburg \n(c) Berlin \n(d) Frankfrut\n\n", 

    "What is the tallest mountain in the world? \n(a) Mount Everest \n(b) K2 \n(c) Kangchenjunga \n(d) Lhotse\n\n",

    "What is the largest ocean on Earth? \n(a) Atlantic Ocean \n(b) Pacific Ocean \n(c) Indian Ocean \n(d) Arctic Ocean\n\n",

    "What is the currency of Japan? \n(a) Euro \n(b) Yuan \n(c) Yen \n(d) Korean Won\n\n",

    "What is the Mona Lisa a painting of? \n(a) A landscape \n(b) A historical battle \n(c) A portrait of a woman \n(d) A religious scene\n\n",

    "What is the name of the world's largest rainforest? \n(a) The Amazon Rainforest \n(b) The Congo Rainforest \n(c) The Southeast Asian Rainforest \n(d) The Temperate Rainforest\n\n",
        
    "What is the chemical symbol for water? \n(a) H2O \n(b) CO2 \n(c) NaCl \n(d) NH3\n\n",
    
    "How many planets are in our solar system (as of July 2024) \n(a) 7 \n(b) 8 \n(c) 9 \n(d) 10\n\n?",

    "Who wrote the play Hamlet? \n(a) William Shakespeare \n(b) Jane Austen \n(c) Charles Dickens \n(d) F. Scott Fitzgerald\n\n",

    "What is the name of the world's longest river? \n(a) The Nile River  \n(b) The Amazon River \n(c) The Yangtze River \n(d) The Mississippi River\n\n"
]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "b"),
    Question(questions_prompts[3], "c"),
    Question(questions_prompts[4], "c"),
    Question(questions_prompts[5], "a"),
    Question(questions_prompts[6], "a"),
    Question(questions_prompts[7], "b"),
    Question(questions_prompts[8], "a"),
    Question(questions_prompts[9], "a"),
]

def quiz_game(questions):
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.ans:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

quiz_game(questions)




