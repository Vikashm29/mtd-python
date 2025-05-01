print('WELCOME TO YOUR HOTEL "/PAKA SHALE\"')
user_choise = input('Enter your choise of meal(v and n):')

match(user_choise.lower()):
    case 'v' : 
        print('VEG Menu \n 1:Idli 2:Dose 3:Poori')
        item_choise = int(input('Enter your choise of food(1-3):'))

        match(item_choise):
            case 1 : print('Idli')
            case 2 : print('Dose')
            case 3 : print('Poori')
 
    case 'n' : 
        print('NONVEG Menu \n 1:Chicken Biryani 2:Mutton Biryani 3: Liver Fry')
        item_choise = int(input('Enter your choise of food(1-3):'))

        match(item_choise):
            case 1 : print('Chicken Biryani')
            case 2 : print('Mutton Biryani')
            case 3 : print('Liver Fry')
            case _ : print('Tale mamsa')
        
print('THANK YOU ! VISIT AGAIN')
