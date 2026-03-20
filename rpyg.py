import random


slash = {
    'Damage' : 7,
    'Custe' : 0,
    'Type' : 'Damage',
    'Atribute' : 'Cortante',
}

fire = {
    'Damage' : 8,
    'Custe' : 2,
    'Type' : 'Damage',
    'Atribute' : 'Fogo',
}

ice = {
    'Damage' : 8,
    'Custe' : 2,
    'Type' : 'Damage',
    'Atribute' : 'Gelo',
}

thunder = {
    'Damage' : 7,
    'Custe' : 2,
    'Type' : 'Damage',
    'Atribute' : 'Energia',
}

cure = {
    'Damage' : 8,
    'Custe' : 2,
    'Type' : 'Buff',
    'Atribute' : 'Luz',
}



warrior = {
    'Type' : 'Hero',
    'Classe' : 'Guerreiro',
    'Status' : 'Padrão',
    'Level' : 1,
    'HPMaximo' : 40,
    'HP' : 40,
    'SP' : 10,
    'Power' : 5,
    'Skill' : [slash],
    'Init' : 0
}

mage = {
    'Type' : 'Hero',
    'Classe' : 'Mago',
    'Status' : 'Padrão',
    'Level' : 1,
    'HPMaximo' : 10,
    'HP' : 10,
    'SP' : 40,
    'Power' : 1,
    'Skill' : [fire, ice],
    'Init' : 0
}


cleric = {
    'Type' : 'Hero',
    'Classe' : 'Clerigo',
    'Status' : 'Padrão',
    'Level' : 1,
    'HPMaximo' : 20,
    'HP' : 20,
    'SP' : 30,
    'Power' : 3,
    'Skill' : [cure],
    'Init' : 0
}


lizardMan1 = {
    'Type' : 'Enemy',
    'Classe' : 'Home Lagarto 1',
    'Status' : 'Padrão',
    'Level' : 1,
    'HPMaximo' : 50,
    'HP' : 50,
    'SP' : 10,
    'Power' : 4,
    'Skill' : [slash, thunder],
    'Init' : 0
}

lizardMan2 = {
    'Type' : 'Enemy',
    'Classe' : 'Home Lagarto 2',
    'Status' : 'Padrão',
    'Level' : 1,
    
    'HPMaximo' : 50,
    'HP' : 50,
    'SP' : 10,
    'Power' : 4,
    'Skill' : [slash, thunder],
    'Init' : 0
}






partyHeros = [warrior, cleric]

partyEnemys = [lizardMan1, lizardMan2]

partyTotal = partyHeros + partyEnemys



#Colocar iniciativa randomicamente

for player in partyTotal : 
    player['Init'] = random.randint(1, 20)
    print(f'{player['Classe']} : {player['Init']}')


print('\n')

filaPrioridade = sorted(partyTotal, key=lambda player : player['Init'], reverse=True)

for i, player in enumerate(filaPrioridade) : 
    print(f' {i + 1}º - {player['Classe']}')




while True: 
    for index, player in enumerate(filaPrioridade):
        print(f'Escolhe a ação que o {player['Classe']} irá fazer:')
        action = int(input('1 - Lutar \n2 - Fugir \nAção: '))
        match action : 
            case 1:
                actionFight = int(input('Escolhe qual ação irá realizar \n1 - Bater \n2 - Habilidade \nAção: '))
                match actionFight:
                    case 1:
                        print('Escolhe me qual inimigo irá bater')
                        for player in filaPrioridade:
                            #print(player)
                            if player['Type'] == 'Enemy' : 
                               print(f'{player['Classe']}')
                        enemyChoise = int(input('Inimigo: '))
                        print(f'Bateu em ')
                        #enemyChoiseParty = partyTotal[]
                       # enemyChoise -= enemyChoise
                       # enemyPartyChoise = partyEnemys[enemyChoise]

                       # print(enemyPartyChoise)

        


       # print(player['Classe'])