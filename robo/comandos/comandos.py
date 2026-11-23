from datetime import datetime

from ..funcoes.email import (
    enviar_resumo_pdf,
    enviar_transcricao,
    enviar_resumo
)

from ..funcoes.salvarAula import (
    criar_aula,
    salvar_legenda,
    salvar_progresso,
    salvar_aula,
    recuperar_aula
)

# Estado atual do sistema
aula_atual = None
modo_atual = 'inativo'


def iniciar_aula(materia, professor, data=None):
    global aula_atual, modo_atual

    if aula_atual is not None:
        return False

    aula_atual = criar_aula(
        materia,
        professor,
        datetime.now()
    )

    salvar_progresso(aula_atual)

    modo_atual = "aula"

    return True


def registrar_legenda(texto):
    if aula_atual is None:
        return False

    salvar_legenda(
        aula_atual,
        texto,
        modo_atual
    )

    salvar_progresso(aula_atual)

    return True


def alterar_modo(novo_modo):
    global modo_atual

    if aula_atual is None:
        return False

    modo_atual = novo_modo

    return True


def finalizar_aula(nome_arquivo=None, data=None):
    global aula_atual, modo_atual

    if aula_atual is None:
        return False

    caminho = salvar_aula(aula_atual)

    aula_atual = None
    modo_atual = 'inativo'

    return caminho


def obter_aula_atual():
    return aula_atual


def obter_modo_atual():
    return modo_atual


# Comandos de envio de e-mail
def comando_enviar_pdf(email, arquivo, data):
    return enviar_resumo_pdf(arquivo, data, email)


def comando_enviar_resumo(email, arquivo, data):
    return enviar_resumo(arquivo, data, email)


def comando_enviar_transcricao(email, arquivo, data):
    return enviar_transcricao(arquivo, data, email)