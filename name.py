from questionclass  import Question


question_prompt = [
    "I kiss my mother before i die. What am i?\n(A) Matches\n(B) Knockouts\n(C) Pen\n\n,",
    "I am so fragile that saying my name breaks it. What am i?\n(A) Glass\n(B) Teacup\n(C) Silence\n\n, ",
    "I fill up a room but take no space. What am i?\n(A) Light\n(B) Darkness\n(C) Shadow\n\n,",
    "I break when dropped but smile back at you if you smile at me. What am i?\n(A) Glass\n(B) Mirror\n(C)Phone\n\n, ",
    "It turns once and what is out cannot get in, neither can what is in get out?\n(A) Key\n(B) Spoon\n(C) Spade\n\n, ",
    "What breaks but never falls and falls but never break?\n(A) Day and Night\n(B) Sun and Moon\n(C) Tea and Bread\n\n,",
    "I go through cities and countries but never moves. What am i?\n(A) Bags\n(B) River\n(C) Road\n\n, ",
    "I have a tail and head but no body. What am i?\n(A) Zero\n(B) Plates\n(C) Coin\n\n, ",
    "You can catch me but never throw me. What am i?\n(A) Cold\n(B) Heat\n(C) Snow\n\n, ",
    "What has a single eye but still cannot see with it?\n(A) Needle\n(B) Pin\n(C) Pen\n\n,",
    "It has rooms but no walls, no corners?\n(A)Tearoom\n(B) Mushrooms\n(C) Rommies\n\n,",
    "I am easy to lift but hard to throw. What am i?\n(A) Feather\n(B) Baby\n(C) Pencil\n\n, ",
    "What jumps when walking and sits when standing?\n(A) Humans\n(B) Lion\n(C) Kangaroo\n\n, ",
    "I only have two words but thousand spaces. What am i?\n(A) Post office\n(B) Stamp duty\n(C) Tax levy\n\n, ",  
    "What is born tall but grows short with age?\n(A) Candle\n(B) Pen\n(C) Lanterns\n\n, ",
    "The more i am taken, the more they are left behind. What is it?\n(A) Footstep\n(B) Footsteps\n(C) Slippers\n\n, ",
    "I eat to live and drink to die. what am i?\n(A) Light\n(B) Fire\n(C) Gas\n\n, ",
    "I promise, i offend, i direct and i fight. What am i?\n(A) Hand\n(B) Mouth\n(C) Legs\n\n, ",
    "I am purchased for eating, but never eaten. What am i?\n(A) Plates\n(B) Sweets\n(C) Tea\n\n, ",
    "I fly without wings, cry without eyes. What am i?\n(A) Sun\n(B) Cloud\n(C) Wind\n\n, ",
    "No matter how hard you try, you can never see me again. What am i?\n(A) Tomorrow\n(B) Future\n(C) Yesterday\n\n, " ,
    "The shorter i am, the bigger i am. What am i?\n(A) Temper\n(B) Feelings\n(C) Calm\n\n, ",
    "I have a big mouth but never speak. What am i?\n(A) Door\n(B) Window\n(C) Jar\n\n,  ",
    "What cycles everytime but never gets tired at the end of the day?\n(A) Clock\n(B) Tyres\n(C) Moon\n\n,  ",
    "I can only speak back your words when spoken to me. What am i?\n(A) Echo\n(B) Transparent\n(C) Opaque\n\n, ",
    "I am a band but can never play music. What am i?\n(A) Ring\n(B) Rubber band\n(C) Music\n\n, ",
    "I travel the world while staying in corner. What am i\n(A) Stamp\n(B) Shoes\n(C) Travelling bag\n\n, ",
    "What starts with E and ends with E, but has only one letter in it?\n(A) Eye\n(B) Envelope\n(C) Elope\n\n, ",
    "What has to be broken before usage?\n(A) Glass\n(B) Mirror\n(C) Egg\n\n, ",
    "What is full of water but still holds water?\n(A) Bathroom\n(B) Sponge\n(C) Sink\n\n, ",
    "I go up and never come down. What am i?\n(A) Water\n(B) River\n(C) Age\n\n, ",
    "What goes up and down but never moves?\n(A) Lift\n(B) Stairs\n(C) Flight\n\n, ",
    "what gets wet while drying?\n(A) Towel\n(B) Wrapper\n(C) Diapers\n\n, ",
    "I have branches but no fruits or trees. What am i?\n(A) Pineapple\n(B) Bank\n(C) Oranges\n\n, ",
    "The more of me, the less you see. What am i?\n(A) Light\n(B) Beach\n(C) Darkness\n\n, ",
    "I follow and copy your moves, but you cannot catch or touch me. What am i?\n(A) Echo\n(B) Laughter\n(C) Shadow\n\n, ",
    "What has a many keys but cannot open a single key?\n(A) Padlock\n(B) Piano\n(C) Door\n\n, ",
    "What is black when clean and white when dirty?\n(A) Chalk\n(B) Classroom\n(C) Chalkboard\n\n, ",
    "I have hands but cannot clap. What am i?\n(A) Clock\n(B) Wheels\n(C) Time\n\n, ",
    "What has many teeth but cannot bite?\n(A) Worms\n(B) Centipede\n(C) Comb\n\n, ",
    "I have words but never speaks. What am i?\n(A) Phones\n(B) Books\n(C) Schools\n\n,  ",
    "What building has the most stories?\n(A) Library\n(B) Ancient buildings\n(C) Supermarket\n\n, ",
    "I have four legs but cannot move. What am i?\n(A) Fridge\n(B) Table\n(C) Television\n\n, ",

 ]


questions = [
    Question(question_prompt[0] , "A"),
    Question(question_prompt[1] , "C"),
    Question(question_prompt[2] , "A"),
    Question(question_prompt[3] , "B"),
    Question(question_prompt[4] , "A"),
    Question(question_prompt[5] , "A"),
    Question(question_prompt[6] , "C"),
    Question(question_prompt[7] , "C"),
    Question(question_prompt[8] , "A"),
    Question(question_prompt[9] , "A"),
    Question(question_prompt[10] , "B"),
    Question(question_prompt[11] , "A"),
    Question(question_prompt[12] , "C"),
    Question(question_prompt[13] , "A"),
    Question(question_prompt[14] , "A"),
    Question(question_prompt[15] , "A"),
    Question(question_prompt[16] , "B"),
    Question(question_prompt[17] , "A"),
    Question(question_prompt[18] , "A"),
    Question(question_prompt[19] , "B"),
    Question(question_prompt[20] , "C"),
    Question(question_prompt[21] , "A"),
    Question(question_prompt[22] , "C"),
    Question(question_prompt[23] , "A"),
    Question(question_prompt[24] , "A"),
    Question(question_prompt[25] , "B"),
    Question(question_prompt[26] , "A"),
    Question(question_prompt[27] , "B"),
    Question(question_prompt[28] , "C"),
    Question(question_prompt[20] , "B"),
    Question(question_prompt[30] , "C"),
    Question(question_prompt[31] , "B"),
    Question(question_prompt[32] , "A"),
    Question(question_prompt[33] , "B"),
    Question(question_prompt[34] , "C"),
    Question(question_prompt[35] , "C"),
    Question(question_prompt[36] , "B"),
    Question(question_prompt[37] , "C"),
    Question(question_prompt[38] , "A"),
    Question(question_prompt[39] , "C"),
    Question(question_prompt[40] , "B"),
    Question(question_prompt[41] , "A"),
    Question(question_prompt[42] , "B"),

]

def run_trial(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 5
    print("You got " + str(score) + " / " + str(len(questions * 5)))

run_trial(questions)

