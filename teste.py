from random import choice
import random
from corpo import *
from time import sleep
import os


dict = {'key1':{'palavra': 'Pai', 'dica': 'parente'},
'key2':{'palavra': 'Pao', 'dica': 'comida'},
'key3':{'palavra': 'Parque', 'dica': 'local'},
'key4':{'palavra': 'Passarinho', 'dica': 'animal'},
'key5':{'palavra': 'Peixe', 'dica': 'animal'},
'key6':{'palavra': 'Pijama', 'dica': 'vestimenta'},
'key7':{'palavra': 'Rato', 'dica': 'animal'},
'key8':{'palavra': 'Umbigo', 'dica': 'parte do corpo'},
'key9':{'palavra': 'Acender', 'dica': 'apagar'},
'key10':{'palavra': 'Afilhado', 'dica': 'parente'},
'key11':{'palavra': 'Ardiloso', 'dica': 'pessoa esperta'},
'key12':{'palavra': 'Aspero', 'dica': 'textura'},
'key13':{'palavra': 'Assombracao', 'dica': 'mal'},
'key14':{'palavra': 'Asterisco', 'dica': 'caractere'},
'key15':{'palavra': 'Basquete', 'dica': 'esporte'},
'key16':{'palavra': 'Caminho', 'dica': 'local'},
'key17':{'palavra': 'Champanhe', 'dica': 'bebida'},
'key18':{'palavra': 'Chiclete', 'dica': 'comida'},
'key19':{'palavra': 'Chuveiro', 'dica': 'objeto'},
'key20':{'palavra': 'Coelho', 'dica': 'animal'},
'key21':{'palavra': 'Convivencia', 'dica': ' frequencia'},
'key22':{'palavra': 'Coracao', 'dica': 'parte do corpo'},
'key23':{'palavra': 'Desalmado', 'dica': 'alma'},
'key24':{'palavra': 'Eloquente', 'dica': 'pessoa convincente'},
'key25':{'palavra': 'Esfirra', 'dica': 'comida'},
'key26':{'palavra': 'Esquerdo', 'dica': 'direcao'},
'key27':{'palavra': 'Excecao', 'dica': 'exclusivo'},
'key28':{'palavra': 'Fugaz', 'dica': 'rapido'},
'key29':{'palavra': 'Gororoba', 'dica': 'comida'},
'key30':{'palavra': 'Heterossexual', 'dica': 'opcao'},
'key31':{'palavra': 'Horrorizado', 'dica': 'pessoa assustada'},
'key32':{'palavra': 'Impacto', 'dica': 'mudanca'},
'key33':{'palavra': 'Independencia', 'dica': 'dinheiro'},
'key34':{'palavra': 'Modernidade', 'dica': 'periodo'},
'key35':{'palavra': 'Oftalmologista', 'dica': 'profissao'},
'key36':{'palavra': 'Otorrinolaringologista', 'dica': 'profisssao'},
'key37':{'palavra': 'Paralelepipedo', 'dica': 'forma'},
'key38':{'palavra': 'Pororoca', 'dica': 'estrondo'},
'key39':{'palavra': 'Prognostico', 'dica': 'prognose'},
'key40':{'palavra': 'Quarentena', 'dica': 'pandemia'},
'key41':{'palavra': 'Quimera', 'dica': 'mitologia'},
'key42':{'palavra': 'Refeicao', 'dica': 'comida'},
'key43':{'palavra': 'Reportagem', 'dica': 'conteudo'},
'key44':{'palavra': 'Sino', 'dica': 'objeto'},
'key45':{'palavra': 'Taciturno', 'dica': 'tomado pela tristeza'},
'key46':{'palavra': 'Visceral', 'dica': 'viceras'},
'key47':{'palavra': 'Afobado', 'dica': 'pessoa desesperada'},
'key48':{'palavra': 'Amendoim', 'dica': 'comida'},
'key49':{'palavra': 'Banheiro', 'dica': 'local'},
'key50':{'palavra': 'Caatinga', 'dica': 'bioma'},
'key51':{'palavra': 'Cachorro', 'dica': 'animal'},
'key52':{'palavra': 'Campeonato', 'dica': 'competicao'},
'key53':{'palavra': 'Capricornio', 'dica': 'signo'},
'key54':{'palavra': 'Catapora', 'dica': 'doenca'},
'key55':{'palavra': 'Corrupcao', 'dica': 'governo'},
'key56':{'palavra': 'Crepusculo', 'dica': 'periodo'},
'key57':{'palavra': 'Empenhado', 'dica': 'pessoa esforcada'},
'key58':{'palavra': 'Esparadrapo', 'dica': 'curativo'},
'key59':{'palavra': 'Forca', 'dica': 'jogo'},
'key60':{'palavra': 'Galaxia', 'dica': 'universo'},
'key61':{'palavra': 'Historia', 'dica': 'materia'},
'key62':{'palavra': 'Magenta', 'dica': 'cor'},
'key63':{'palavra': 'Manjericao', 'dica': 'comida'},
'key64':{'palavra': 'Menta', 'dica': 'comida'},
'key65':{'palavra': 'Moeda', 'dica': 'dinheiro'},
'key66':{'palavra': 'Oracao', 'dica': 'reza'},
'key67':{'palavra': 'Pacoca', 'dica': 'comida'},
'key68':{'palavra': 'Palavra', 'dica': 'palavra'},
'key69':{'palavra': 'Pedreiro', 'dica': 'profissao'},
'key70':{'palavra': 'Pneumonia', 'dica': 'doenca'},
'key71':{'palavra': 'Pulmao', 'dica': 'parte do corpo'},
'key72':{'palavra': 'Rotatoria', 'dica': 'direcao'},
'key73':{'palavra': 'Serenata', ' dica': 'tipo de cancao'},
'key74':{'palavra': 'Transeunte', 'dica': 'passageiro'},
'key75':{'palavra': 'Trilogia', 'dica': 'sequencia'},
'key76':{'palavra': 'Xicara', 'dica': 'objeto'}}

def jogar(dict):


    palavra_acertadas = []
    letras_erradas = []
    erros = 0
    chances = 6


    key, item = random.choice(list(dict.items()))
    #print(f"Chave encontrada: {key}")
    #print(f"Palavra encontrada: {item['palavra']}")
    #print(f"Dica encontrada: {item['dica']}")

    palavra_secreta = str(item['palavra'])

    for index in range(len(item['palavra'])):
        palavra_acertadas.insert(index, '_')

    print(palavra_acertadas)

    while True:
        sleep(0.5)
        print(f"DICA: {item['dica']}")

        chute = input("Chute: ").upper()

        if chute.upper() == palavra_secreta.upper():
            ganhou()
            break

        if chute in palavra_secreta.upper():
            if not chute in palavra_acertadas:
                print(f"TEM A LETRA [ {chute.upper()} ] NA PALAVRA SECRETA")

            for index, palavra in enumerate(palavra_secreta):
                if palavra.upper() == chute.upper():
                    palavra_acertadas[index] = chute

        else:
            erros += 1
            chances -= 1
            corpo(erros, chances)
            if not chute in letras_erradas:
                letras_erradas.append(chute)

        if not erros == 6:
            print(f"PALAVRA: {palavra_acertadas}")

        if erros == 6:
            perdeu(palavra_secreta)
            break

        if not '_' in palavra_acertadas:
            ganhou()
            break

        print()
        print(f"Caracteres tentados: {letras_erradas}")

    #numeros.remove(item['palavra'])

if __name__ == '__main__':
    while True:
        os.system('cls')
        jogar(dict)
        print()
        jogar_dnv = input("Jogar denovo? (S/N)").upper()
        if jogar_dnv != 'S':
            break

