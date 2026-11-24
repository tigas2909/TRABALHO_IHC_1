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

from ..conectarIa.resumidor import gerar_resumo
from ..funcoes.salvar_resumo import salvar_resumo
from ..funcoes.pdf import gerar_pdf

# Estado atual do sistema
aula_atual = None
modo_atual = 'inativo'
date = None
nome_arquivo = None


def iniciar_aula(materia, professor, data=None):
    global aula_atual, modo_atual, date, nome_arquivo

    if aula_atual is not None:
        return False

    date = datetime.now()
    nome_arquivo = date.strftime("aula_%d_%m_%Y_%H_%M")

    aula_atual = criar_aula(
        materia,
        professor,
        date
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



def finalizar_aula():
    global aula_atual, modo_atual, date, nome_arquivo

    if aula_atual is None:
        return False

    # Finalizar transcrição
    caminho = salvar_aula(aula_atual)

    # Limpar o estado da aula
    aula_atual = None
    modo_atual = "inativo"
    date = None
    nome_arquivo = None

    try:
        # Gerar resumo com Gemini
        resumo = gerar_resumo(caminho.name)

        # Salvar TXT
        caminho_txt = salvar_resumo(caminho.stem, resumo)

        # Gerar PDF
        caminho_pdf = gerar_pdf(resumo, caminho.stem)

        print("[OK] Resumo gerado!")
        print(f"[TXT] {caminho_txt}")
        print(f"[PDF] {caminho_pdf}")

    except Exception as erro:
        print(f"[ERRO] Falha ao gerar resumo ou PDF: {erro}")
        print(f"[INFO] Transcrição preservada em: {caminho}")
        return caminho

    # Enviar e-mail
    try:
        enviado = enviar_resumo_pdf(
            caminho_pdf.name,
            datetime.now().strftime("%d/%m/%Y")
        )

        if enviado:
            print("[OK] Resumo enviado por e-mail!")
        else:
            print("[ERRO] Falha ao enviar um ou mais e-mails.")

    except Exception as erro:
        print(f"[ERRO] Falha no envio de e-mail: {erro}")

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