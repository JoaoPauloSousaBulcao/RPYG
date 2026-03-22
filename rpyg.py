import random
import os
import time


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
    
def limparTela():
    os.system('cls')

for i, player in enumerate(filaPrioridade) : 
    print(f' {i + 1}º - {player['Classe']}')

time.sleep(5)
limparTela()

def verificarVivo(grupoPlayer):
    contarMortos = 0
    statusGrupo = False
    for player in grupoPlayer:
        if player['Status'] == 'Morto' : contarMortos += 1
    
    if contarMortos >= len(grupoPlayer) : statusGrupo = True

    #print(contarMortos)
    #print(statusGrupo)
    
    return statusGrupo




while True: 
    for index, player in enumerate(filaPrioridade):
        
        if player['HP'] > 0 :

            if filaPrioridade[index]['Type'] == 'Hero' : 
                limparTela()

                print(f'Escolhe a ação que o {player['Classe']} irá fazer:')
                action = int(input('1 - Lutar \n2 - Fugir \nAção: '))
                time.sleep(2)
                match action : 
                    case 1:
                        actionFight = int(input('Escolhe qual ação irá realizar \n1 - Bater \n2 - Habilidade \nAção: '))
                        time.sleep(2)
                        match actionFight:
                            case 1:
                                enemyChoises = []
                                print('Escolhe me qual inimigo irá bater')
                                enemyChoise = 1
                                for index, playerEnemy in enumerate(filaPrioridade):
                                    
                                    #print(playerEnemy)
                                    if playerEnemy['Type'] == 'Enemy' and playerEnemy['Status'] != 'Morto': 
                                        enemy = {
                                            'indexChoise' : enemyChoise,
                                            'indexEnemy' : index
                                        }
                                        enemyChoises.append(enemy)
                                        enemyIndex = index
                                        print(f'{enemyChoise} - {playerEnemy['Classe']}')
                                        enemyChoise += 1
                                enemyChoise = int(input('Inimigo: '))
                                time.sleep(2)
                                for enemy in enemyChoises : 
                                    if enemy['indexChoise'] == enemyChoise : enemyChoisedIndex = enemy['indexEnemy']
                                #print(enemyChoisedIndex)
                                #enemyChoised = enemyChoises[enemy['indexEnemy']]
                                #print(filaPrioridade[enemyChoisedIndex]['HP'])
                                print(f'{player["Classe"]} bateu em {filaPrioridade[enemyChoisedIndex]['Classe']}.\n')
                                filaPrioridade[enemyChoisedIndex]['HP'] -= player['Power']
                                if filaPrioridade[enemyChoisedIndex]['HP'] <= 0 : 
                                    filaPrioridade[enemyChoisedIndex]['Status'] = 'Morto'
                                    
                                    filaInimigos = [player for player in filaPrioridade if player['Type'] == 'Enemy' ]
                                    if verificarVivo(filaInimigos) == True : 
                                        print('Todos os inimigos morreram. Você Ganhou.')
                                        time.sleep(10)
                                        break
                                    else: print(f'{filaPrioridade[enemyChoisedIndex]['Classe']} morreu.')
                                time.sleep(2)

                                
                                #print(filaPrioridade[enemyChoisedIndex]['HP'])

                                #enemyChoiseParty = partyTotal[]
                            # enemyChoise -= enemyChoise
                            # enemyPartyChoise = partyEnemys[enemyChoise]

                            # print(enemyPartyChoise)
            
            
            else :
                limparTela()
                countHeros = []

                for index, playerHero in enumerate(filaPrioridade) : 
                    if playerHero['Type'] == 'Hero' and playerHero['Status'] != 'Morto': countHeros.append(index)
                    #print(countHeros)

                heroChoise = random.choice(countHeros)
                #print(heroChoise)

                
                print(f'{player['Classe']} bateu em {filaPrioridade[heroChoise]['Classe']}\n')

                filaPrioridade[heroChoise]['HP'] -= player['Power']
                time.sleep(2)
                if filaPrioridade[heroChoise]['HP'] <= 0 : 
                    filaPrioridade[heroChoise]['Status'] = 'Morto'
                    print(f'{filaPrioridade[heroChoise]['Classe']} morreu.')
                    filaHerois = [player for player in filaPrioridade if player['Type'] == 'Hero' ]
                    if verificarVivo(filaHerois) == True : 
                        print('Todos os herois morreram. Você Perdeu.')
                        time.sleep(10)
                        break
                else: print(f'{filaPrioridade[heroChoise]['Classe']} está com {filaPrioridade[heroChoise]['HP']} pontos de vida.\n')
                time.sleep(2)
                

                #heroChoise = random.randint(len(countHeros))
                #heroChoise -= heroChoise

                #filaPrioridade[heroChoise]['HP'] -= player['Power']
                #print(f'{filaPrioridade[heroChoise]['HP']}')

        else:
            limparTela()
            player['Status'] = 'Morto'
            print(f'{player['Classe']} está morto.\n')
            time.sleep(2)
        



        
       # print(player['Classe'])