from random import randint
comp_v = 0
pessoa_v = 0
while comp_v <= 3 and pessoa_v <=3:
    comp = randint(0, 10)
    pessoa = int(input('Digite um número entre 0 e 10: '))
    IP_pessoa = input('Escolha entre par (P) e ímpar (I): ').strip().upper()[0]
    while IP_pessoa != 'P' and IP_pessoa != 'I':
        print('\033[31mDado não compativel! Digite novamente.\033[m')
        IP_pessoa = input('Escolha entre par (P) e ímpar (I): ').strip().upper()[0]
    total = comp + pessoa
    if total%2 == 0 and IP_pessoa == 'P':
        print('-='*15)
        print('\n \033[32mVocê venceu a rodada !!!! \033[m\n')
        print('-=' * 15)
        pessoa_v += 1
    elif total % 2 == 0 and IP_pessoa == 'I':
        print('-=' * 15)
        print('\n \033[31mO computador venceu a rodada !!!!\033[m \n')
        print('-=' * 15)
        comp_v += 1
    elif total%2 != 0 and IP_pessoa == 'P':
        print('-=' * 15)
        print('\n \033[31mO computador venceu a rodada !!!!\033[m \n')
        print('-=' * 15)
        comp_v += 1
    elif total % 2 != 0 and IP_pessoa == 'I':
        print('-=' * 10)
        print('\n \033[32mVocê venceu a rodada !!!!\033[m \n')
        print('-=' * 10)
        pessoa_v += 1
    if comp_v == 3 or pessoa_v == 3:
        break

if comp_v == 3:
    print('\033[31mO computador ganhou o jogo \033[m')
elif pessoa_v == 3:
    print('\033[32mVocê ganhou o jogo \033[m!!!!!')
print('\n'
      'O resultado do jogo foi {} para você e {} para o computador'.format(pessoa_v,comp_v))