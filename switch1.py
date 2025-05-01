user_choise = input('Enter your choise of meal(v and n):')

match(user_choise.lower):
    case 'v' : print('VEG')
user_choise = int(input('Enter your choise of food(1-3):'))

match(user_choise):
    case 1 : print('Idle')
    case 2 : print('Dose')
    case 3 : print('poori')
 
    case 'n' : print('NONVEG')
user_choise = int(input('Enter your choise of food(1-3):'))

match(user_choise):
    case 1 : print('Chicken Biryani')
    case 2 : print('Mutton Biryani')
    case 3 : print('Liver Fry')
    case _ : print('tale mamsa')


