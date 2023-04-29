# Sistema de perguntas e respostas de Conhecimentos Gerais.

from time import sleep
print('--- Teste seus conhecimentos ---')
print()

perguntas = [
    {
        'Pergunta': 'Quais os principais autores do Barroco no Brasil?',
        'Opções' : [
            'Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira',
            'Miguel de Cervantes, Gregório de Matos e Danthe Alighieri',
            'Padre Antônio Vieira, Padre Manuel de Melo e Gregório de Matos',
            'Castro Alves, Bento Teixeira e Manuel Botelho de Oliveira',
            'Álvares de Azevedo, Gregório de Matos e Bento Teixeira'],
        'Resposta' : 'Gregório de Matos, Bento Teixeira e Manuel Botelho de Oliveira',
    },
    {
        'Pergunta': 'Quanto tempo a luz do Sol demora para chegar à Terra?',
        'Opções' : [
            '12 minutos',        
            '1 dia',
            '12 horas',
            '8 minutos',
            '12 segundos',
        ],
        'Resposta' : '8 minutos'
    },
    {
        'Pergunta': 'Em que ordem surgiram os modelos atômicos?',
        'Opções' : [
            'Thomson, Dalton, Rutherford, Rutherford-Bohr',
            'Rutherford-Bohr, Rutherford, Thomson, Dalton',
            'Dalton, Rutherford-Bohr, Thomson, Rutherford',
            'Dalton, Thomson, Rutherford-Bohr, Rutherford',
            'Dalton, Thomson, Rutherford, Rutherford-Bohr',
        ],
        'Resposta' : 'Dalton, Thomson, Rutherford, Rutherford-Bohr'
    },    
    {
        'Pergunta': 'Em que período da pré-história o fogo foi descoberto?',
        'Opções' : [
            'Neolítico',        
            'Paleolítico',
            'Idade dos Metais',
            'Período da Pedra Polida',
            'Idade Média',
        ],
        'Resposta' : 'Paleolítico'
    },
    {
        'Pergunta': '(2015) A Comissão de Valores Mobiliários (CVM) é um órgão que regula e fiscaliza o mercado de capitais no Brasil, sendo:',
        'Opções' : [
            'subordinada ao Banco Central do Brasil',        
            'subordinada ao Banco do Brasil',
            'subordinada à Bolsa de Valores de São Paulo (BOVESPA)',
            'independente do poder público',
            'vinculada ao poder executivo (Ministério da Fazenda)',
        ],
        'Resposta' : 'vinculada ao poder executivo (Ministério da Fazenda)'
    },
    {
        'Pergunta': '(2007) Em 2006, o IBGE completou 70 anos de sua fundação. Esse instituto foi criado no contexto histórico da(o):',
        'Opções' : [
            'Ditadura Militar, de Costa e Silva',        
            'Transição Democrática, de José Sarney',
            'Estado Novo, de Getúlio Vargas',
            'Plano de Metas, de Juscelino Kubitschek',
            'Milagre Brasileiro, de Ernesto Geisel',
        ],
        'Resposta' : 'Estado Novo, de Getúlio Vargas'
    },
]
contador = qtd_acertos = 0

for pergunta in perguntas:
    print(f'Pergunta 0{contador+1}: ', pergunta['Pergunta'])
    contador += 1
    print()

    options = pergunta['Opções']
    qtd_options = len(options)
    acertou = False

    for indice, valor in enumerate(options):
        print(f'{indice}) {valor}')
    print()

    int_escolha = None
    escolha = input('Escolha uma opção: ')
    if escolha.isdigit():
        int_escolha = int(escolha)

    if int_escolha is not None:
        if int_escolha >= 0 and int_escolha < qtd_options:
            if options[int_escolha] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        qtd_acertos += 1
        print('\n--- Acertou! ---')
    else:
        print('\n--- Errou! ---')
    print()

porcentagem = qtd_acertos / len(perguntas) * 100
print('--- FIM! ---')
print('Carregando os resultados...')
sleep(1.5)
print(f'\nVocê acertou {qtd_acertos} de {len(perguntas)} perguntas.')
print(f'Com um aproveitamento de {porcentagem:.0f}%.')
print()