player_hp = 100
enemy_hp = 100
arma = {'principal': 'Espada de Madeira', 'dano': 8}
print('Atacar?')
print('\t1 - SIM\n\t2 - NAO')
attack = str(input('>>> '))
if attack == '1':
    print('Atacando')
    print(f'Voce acaba de dar {arma["dano"]} de dano no inimigo!')
    enemy_hp -= arma['dano']
    print(enemy_hp)
