import random

def nine_point_two():
    foo = ['rice', 'beans']
    #print(foo)
    foo.append('broccoli')
    #print(foo)
    foo.extend(('bread', 'pizza'))
    #print(foo)
    #print(foo[:2])
    #print(foo[-1])
    breakfast = "eggs, fruit, orange juice".split(', ')
    print(breakfast)
    lengths = [len(string) for string in breakfast]
    print(lengths)
    print(type(lengths))


def nine_point_three():
    data = ((1,2), (3,4))
    [print(f'Row {i} sum {sum(tup)}') for i, tup in enumerate(data)]

    numbers = [4, 3, 2, 1]
    numbers_copy = numbers[:]
    numbers_copy.sort()
    print(numbers_copy)

def nine_point_four():
    '''Challenge: List of lists'''
    
    def enrollment_stats(list_of_lists):
        enrollment = [university[1] for university in list_of_lists]
        tuition_fees = [university[2] for university in list_of_lists]

        return (enrollment, tuition_fees)
    

    def mean(list):
        return sum(list) / len(list)
    

    def median(list):
        if len(list) % 2 != 0: #none
            return list[len(list)//2]
        else:
            num_1 = list[len(list)/2]
            num_2 = list[len(list)/2 + 1]
            return (num_1 + num_2) / 2


    universities = [
                        ['California Institute of Technology', 2175, 37704],
                        ['Harvard', 19627, 39849],
                        ['Massachusetts Institute of Technology', 10566, 40732],
                        ['Princeton', 7802, 37000],
                        ['Rice', 5879, 35551],
                        ['Stanford', 19535, 40569],
                        ['Yale', 11701, 40500]
                    ]
    enrollment, tuition_fees = enrollment_stats(universities)
    enrollment.sort()
    tuition_fees.sort()
    print(f'Total number of students = {sum(enrollment):,}')
    print(f'Total tuition = {sum(tuition_fees):,}')
    print(f'Students: Mean = {mean(enrollment):,.2f}  and Median = {median(enrollment)}')
    print(f'Tuition: Mean = {mean(tuition_fees):,.2f}  and Median = {median(tuition_fees)}')


def nine_point_five():
    '''Challenge: Wax Poetic'''
    Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    Adjectives  = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    Prepositions = ["against", "after","into", "beneath", "upon", "for", "in", "like", "over", "within"]
    Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]



    n = [random.choice(Nouns) for _ in range(3)]
    v = [random.choice(Verbs) for _ in range(3)]
    adj = [random.choice(Adjectives) for _ in range(3)]
    prep = [random.choice(Prepositions) for _ in range(2)]
    adv = random.choice(Adverbs)
    art = "An" if adj[0][0] in "aeiou" else "A"


    print(f'{art} {adj[0]} {n[0]}')
    print(f'{art} {adj[0]} {n[0]} {v[0]} {prep[0]} the {adj[1]} {n[1]}')
    print(f'{adv}, the {n[0]} {v[1]}')
    print(f'the {n[1]} {v[2]} {prep[1]} a {adj[2]} {n[2]}')


nine_point_five()