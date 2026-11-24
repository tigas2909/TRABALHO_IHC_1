import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

raiz_projeto = Path(__file__).resolve().parents[2]
load_dotenv(raiz_projeto / ".env")

pasta_arquivos = raiz_projeto / "arquivos"

caminho_resumo_pdf = pasta_arquivos / "resumo_pdf"
caminho_resumo = pasta_arquivos / "resumo"
caminho_transcricoes = pasta_arquivos / "transcricoes"
caminho_emails = pasta_arquivos / "emails" / "emails.txt"


def enviar_email(destinatario, arquivo, tipo_arquivo, assunto):
    try:
        remetente = os.getenv("REMETENTE")
        senha = os.getenv("SENHA")

        if not remetente or not senha:
            print("[ERRO] Credenciais de e-mail não configuradas.")
            return False

        caminho = Path(arquivo)

        if not caminho.is_file():
            print(f"[ERRO] Arquivo não encontrado: {caminho}")
            return False

        mensagem = EmailMessage()

        mensagem["From"] = remetente
        mensagem["To"] = destinatario
        mensagem["Subject"] = assunto

        mensagem.set_content("Segue o arquivo em anexo.")

        with caminho.open("rb") as documento:
            mensagem.add_attachment(
                documento.read(),
                maintype="application",
                subtype=tipo_arquivo,
                filename=caminho.name
            )

        print(f"[INFO] Enviando e-mail para: {destinatario}")

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(mensagem)

        print(f"[OK] E-mail enviado para: {destinatario}")

        return True

    except FileNotFoundError as erro:
        print(f"[ERRO] Arquivo não encontrado: {erro}")
        return False

    except smtplib.SMTPAuthenticationError as erro:
        print(f"[ERRO] Falha na autenticação: {erro}")
        return False

    except smtplib.SMTPException as erro:
        print(f"[ERRO] Falha SMTP: {erro}")
        return False

    except Exception as erro:
        print(f"[ERRO] {type(erro).__name__}: {erro}")
        return False


def chamar_funcao(email, nome_arquivo, tipo_envio, assunto):

    # Enviar para todos os alunos
    if email is None:

        if not caminho_emails.is_file():
            print(f"[ERRO] Lista de e-mails não encontrada: {caminho_emails}")
            return False

        resultados = []

        with caminho_emails.open("r", encoding="utf-8") as arquivo:

            for destinatario in arquivo:

                destinatario = destinatario.strip()

                if not destinatario:
                    continue

                resposta = enviar_email(
                    destinatario,
                    nome_arquivo,
                    tipo_envio,
                    assunto
                )

                resultados.append(resposta)

        if not resultados:
            print("[ERRO] Nenhum destinatário encontrado.")
            return False

        enviados = resultados.count(True)
        total = len(resultados)

        print(f"[INFO] E-mails enviados: {enviados}/{total}")

        return all(resultados)

    # Enviar para um aluno específico
    else:

        return enviar_email(
            email,
            nome_arquivo,
            tipo_envio,
            assunto
        )


def enviar_resumo_pdf(nome_arquivo, data, email=None):

    arquivo = caminho_resumo_pdf / nome_arquivo

    if arquivo.is_file():

        return chamar_funcao(
            email,
            arquivo,
            "pdf",
            f"Resumo da aula {data}"
        )

    print(f"[ERRO] PDF não encontrado: {arquivo}")
    return False


def enviar_resumo(nome_arquivo, data, email=None):

    arquivo = caminho_resumo / nome_arquivo

    if arquivo.is_file():

        return chamar_funcao(
            email,
            arquivo,
            "octet-stream",
            f"Resumo da aula {data}"
        )

    print(f"[ERRO] Resumo não encontrado: {arquivo}")
    return False


def enviar_transcricao(nome_arquivo, data, email=None):

    arquivo = caminho_transcricoes / nome_arquivo

    if arquivo.is_file():

        return chamar_funcao(
            email,
            arquivo,
            "json",
            f"Transcrição da aula {data}"
        )

    print(f"[ERRO] Transcrição não encontrada: {arquivo}")
    return False