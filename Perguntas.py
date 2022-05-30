perguntas = {
    'pergunta1' : {
        'pergunta' : 'Quanto é 10 + 15?' ,
        'respostas' : {'a':30, 'b':25, 'c': 20},
        'resposta_certa': 'b'
    },
    'pergunta2' : {
        'pergunta': 'Quanto é 10*3?',
        'respostas' : {'a':30, 'b':45, 'c': 50},
        'resposta_certa': 'a'
    }
}
print()
while True:
    respostas_certas = 0
    for x, y in perguntas.items():
        print(f'{x} : {y["pergunta"]}')

        print('Respostas')
        for z,w in y['respostas'].items():
            print(f'[{z}] {w}')
        print()

        resposta_user = input('Qual sua resposta ?')
        if resposta_user == y['resposta_certa']:
            print('Parabens, voce acertou!')
            print()
            respostas_certas += 1
        else:
            print('voce errou ! Tente novamente')
    print()
    print(f'Você acertou {respostas_certas} respotas')

    print()
    print('1- tentar novamente')
    print('2- Sair')
    resp_final = int(input('O que voce deseja fazer?'))
    if resp_final == 1:
        print('REINICIANDO O JOGO!')
    else:
        print('Saindo....')
        break





