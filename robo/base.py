from .funcoes.analise import analisar
from .comandos.comandos import obter_modo_atual


# Arquivos utilizados nos testes
ARQUIVOS = {
    "pdf": "teste_envio_email.pdf",
    "resumo": "teste.txt",
    "transcricao": "teste.json"
}

inicio = {
    'professor': None,
    'materia': None
}


def iniciar_aula(txt):
    inicio['professor'] = input('Nome do professor: ').strip()
    inicio['materia'] = input('Nome da matéria: ').strip()

    if not inicio['professor'] or not inicio['materia']:
        print('[ERRO] Informe o professor e a matéria.')
        return

    analisar(txt, inicio)


def iniciar_tarefa(txt):
    analisar(txt)


def iniciar_trabalho(txt):
    analisar(txt)


def iniciar_destaque(txt):
    analisar(txt)


def finalizar_aula(txt):
    analisar(txt)


def finalizar_tarefa(txt):
    analisar(txt)


def finalizar_trabalho(txt):
    analisar(txt)


def finalizar_destaque(txt):
    analisar(txt)


def iniciar():
    print("""
========================================
           SISTEMA IHC
========================================

Comandos de ativação de modos:
    1 - iniciar aula
    2 - iniciar tarefa
    3 - iniciar trabalho
    4 - iniciar destaque

Comandos de desativação de modos:
    1 - finalizar aula
    2 - finalizar tarefa
    3 - finalizar trabalho
    4 - finalizar destaque

Comando para sair:
    1 - sair

Durante uma aula, textos comuns serão
encaminhados ao analisador para registro.

========================================
""")

    while True:

        txt = input(f'[{obter_modo_atual()}]: ').strip()

        if not txt:
            continue

        comando = " ".join(txt.lower().split())

        if comando == 'iniciar aula':
            iniciar_aula(txt)

        elif comando == 'iniciar tarefa':
            iniciar_tarefa(txt)

        elif comando == 'iniciar trabalho':
            iniciar_trabalho(txt)

        elif comando == 'iniciar destaque':
            iniciar_destaque(txt)

        elif comando == 'finalizar aula':
            finalizar_aula(txt)

        elif comando == 'finalizar tarefa':
            finalizar_tarefa(txt)

        elif comando == 'finalizar trabalho':
            finalizar_trabalho(txt)

        elif comando == 'finalizar destaque':
            finalizar_destaque(txt)

        elif comando == 'sair':
            print('[SISTEMA] Encerrando...')
            break

        else:
            analisar(txt)


def main(args=None):
    iniciar()


if __name__ == '__main__':
    main()