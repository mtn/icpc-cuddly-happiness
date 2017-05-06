correct = set()
tries = {}
score = 0

def process(line,correct,tries,score):
    time, prob, corr = line.split(' ')
    time = int(time)
    corr = (corr=='right')
    if corr:
        correct.add(prob)
        score += time + tries.get(prob,0) * 20
    elif prob not in correct:
        tries[prob] = tries.get(prob,0) + 1
    return correct,tries,score
line = input()
while line != '-1':
    correct,tries,score = process(line,correct,tries,score)
    line = input()

print('{} {}'.format(len(correct),score))

