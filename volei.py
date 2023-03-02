pontos = list()
jogador = dict()
time = list()

while True:
    # strip retorna a cópia de uma string com determinados caracteres removidos do inicio e do fim
    # str = "0000000this is string example....wow!!!0000000";
    # print(str.strip('0'))
    # retorno: this is string example....wow!!! //thats not larissa :p
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas sets {jogador["Nome"]} jogou? '))

    if partidas > 0:
        for c in range(0, partidas):
            pontos.append(int(input(f'     Quantos pontos no {c+1}º set? ')))
        jogador['Pontos'] = pontos[:]
        jogador['Total'] = sum(pontos)
    time.append(jogador.copy())

    while True:
        op = str(input('Cadastrar mais um jogador? [S/N]')).upper().strip()[0]
        if op in 'SN':
            jogador.clear()
            pontos.clear()
            break
        print('Opção inválida! Tente novamente.')
    if op == 'N':
        break

print('-='*20)
print(f'{"Cod":<5}{"NOME":<10}{"Total":<10}{"Pontos":<10}')
for i, j in enumerate(time):
    print(f'{i:<5}{j["Nome"]:<10}{j["Total"]:<10}{j["Pontos"]}')


print('-='*20)
while True:
    aux = int(input('Mostrar os dados de qual jogador? (999 sair) '))
    if aux == 999:
        break
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[aux]["Nome"]}')
        for i, j in enumerate(time[aux]["Pontos"]):
            print(f'     No {i+1}º set fez {j} ponto(s)')