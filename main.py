import random

asked_words = []
def load():
    file = open('lettters.txt', 'r')
    word_list = file.read().split('\n')
    file.close()
    return word_list

def selector(word_list):
    possible_word = random.choice(word_list)
    while possible_word in asked_words:
        possible_word = random.choice(word_list)

    return possible_word



def check(word, ans):
    word = word.strip()
    if word.upper() == ans or word in word_list:
        return True
    return False

def question(ans):
    ques = list('_' for i in range(len(ans)))
    ww = ans
    while ww == ans:
        possible_pos = list(i for i in range(len(ans)))
        for i in ans:
            word_index = random.choice(possible_pos)
            ques[word_index] = i
            possible_pos.remove(word_index)
        ww = ' '.join(ques)
    return ww

def hint(ans, no_hint):
    wo = list('_' for i in range(len(ans)))
    if no_hint <= 2:
        for i in range(0,len(ans), 3):
            wo[i] = ans[i]

    if no_hint == 2:
        for i in range(0,len(ans), 4):
            wo[i] = ans[i]

    return ' '.join(wo)


no_of_turns = 10
word_list = load()
no_hints = 5

score = 0
correct = False
print('You have 5 hints')
print('You cannot use more than two hints in one question')
print('Type h for hint or type answer')

print()
while no_of_turns >= 0:
    answer = selector(word_list)
    asked_words.append(answer)
    ques = question(answer)
    print()
    print(ques)
    print()
    user_ans = input('WORD: ').upper()
    ask_hint = 0
    while user_ans == 'h' or user_ans == 'H':
        if no_hints == 0:
            print('No hints left')
            print()
            user_ans = input('WORD: ').upper()
            break
        if ask_hint > 2:
            print('Cannot use more than two hints on one question')
            print()
            user_ans = input('WORD: ').upper()
            break
        ask_hint += 1
        no_hints -= 1
        print(hint(answer, ask_hint))
        print('No of hints left:',no_hints)
        print()
        user_ans = input('WORD: ').upper()

    if check(user_ans, answer):
        print('CORRECT!')
        score += 1
        print('Your score is:',score)
    else:
        no_of_turns -= 1
        print('WRONG!')
        print('Correct word :', answer)
        print('No of lives left:', no_of_turns)

    print()

print('Your score was {}'.format(score))










