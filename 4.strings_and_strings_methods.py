def before_four_point_six():
    flavor = "apple pie"
    print(flavor)

    print('''Negative string index''')
    print(flavor[-1])

    print('''Negative index string slicing''')
    print(flavor[-9:-6])

    print('''Maniputale Inmutable strings''')
    word = "goal"
    word = "f" + word[1:]
    print(word)


    print('''4.3 Manipulate Strings With Methods''')
    name = "Jean-luc Picard"
    print(name.lower())

    loud_voice = "Can you hear me yet?"
    print(loud_voice.upper())

    print('The .rstrip() method removes whitespace from the right side of a string:')
    name = "          Jean-luc Picard             "
    print(name, len(name))
    namerstrip = name.rstrip()
    print(namerstrip, len(namerstrip))

    print('The .lstrip() method removes whitespace from the right side of a string:')
    name = "          Jean-luc Picard             "
    print(name, len(name))
    namelstrip = name.lstrip()
    print(namelstrip, len(namelstrip))

    print('The .strip() method removes whitespace from both sides of a string:')
    name = "          Jean-luc Picard             "
    print(name, len(name))
    namestrip = name.strip()
    print(namestrip, len(namestrip))

    print('''Determine if a String Starts or Ends With a Particular String''')
    starship = "Enterprise"
    print(starship.startswith("en"))
    print(starship.startswith("En"))
    print(starship.endswith("rise"))

    print('''User Input''')
    prompt = "Hey, what's up? "
    user_input = input(prompt)
    print("You said:", user_input)

def four_point_six():
    print('Strings and Arithmetic Operators')

    print('Strings sum')
    num = "2"
    print(num + num)

    print('String multiplied by a number')
    num = "2"
    print(num * 3)
    print(3 * num)
    '''
    "12" * "3": Error multiplying 2 strings
    "3" + 3: Error adding string with number
    '''

    print('Converting Strings to Numbers')
    print(int("12"))
    print(float('12'))

    print('Converting Numbers to Strings')
    num_pancakes = 10
    print("I am going to eat " + str(num_pancakes) + " pancakes.")

def four_point_seven():
    print('Streamline Your Print Statements')
    name = "Zaphod"
    heads = 2
    arms = 3
    print(f"{name} has {heads} heads and {arms} arms")

    weight = 0.2
    animal = 'newt'
    print(f'{weight} kg is the weight of the {animal}')

def four_point_eight():
    print('Find a String in a String(Only the first occurrence)')
    phrase = "the surprise is in here somewhere"
    print(phrase.find("surprise"))
    print(phrase.find("eyjafjallajökull"))

    print('Replace a String in a String(All the occurrences)')
    my_story = "I'm telling you the truth; nothing but the truth!"
    my_story = my_story.replace("the truth", "lies")
    print(my_story)



#four_point_six()
#four_point_seven()
four_point_eight()