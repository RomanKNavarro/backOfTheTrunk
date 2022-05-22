# Back of The Trunk With Justifying String Methods
def organizer(dic, left, right):
    print('QUANTITY'.ljust(right, '.')  + 'ITEM'.rjust(left, '.'))
    for k, v in dic.items():
        print(str(v).ljust(left, '-') + k.rjust(right, '-'))
    
trunk = {'fetuses': '12 jar-fulls', 'yogurt': '5 half-liters', 'cold ham': '6 pounds', 'brooms': 'two'}

while True:
    print('You are about to leave the grocery store.\nWould you like to view a list of the current items in your trunk before leaving?')
    response = input()
    if response == 'no':
        print("Your car's trunk is closed down and you drive home.\n")
        break
    if response == 'yes':
        organizer(trunk, 20, 20)
        print('\nIs there any other item you wish to retrieve?\nif so, what\'s the name of it?')
        taipei = input()
        if taipei == 'no':
            print('understood\n')
            continue
        else:
            print('quantity?')
            quant = input()
            trunk.setdefault(taipei,quant)
            print('item(s) successfully added to the list\n')
            
            
            

            
'''# Back of The Trunk Original
trunk = {'fetuses': '12 jar-fulls', 'yogurt': '5 half-liters', 'cold ham': '6 pounds', 'brooms': 'two'}

while True:
    print('You are about to leave the grocery store. Would you like to view any current items in your trunk before leaving?')
    response = input()
    if response == 'no':
        print("Your car's trunk is closed down and you drive home.'")
        break


    if response in trunk:
              print(response + '? There\'s currently ' + trunk[response] + ' in the trunk')
    else:
        print(response + "? There's none to speak of in the trunk at the moment.")
        print('Would you like to return to the grocery store to retrieve ' + response + '? If so, how many?')

        taipei = input()
        if taipei == 'no':
              print('understood')
              continue
        else:
              trunk[response] = taipei
              print(taipei + ' added to trunk')'''




              

