import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

raiz_projeto = Path(__file__).resolve().parents[2]
load_dotenv(raiz_projeto / ".env")

pasta_arquivos = Path(__file__).resolve().parents[2] / "aruivos"
caminho_resumo_pdf = pasta_arquivos / "resumo_pdf"
caminho_resumo = pasta_arquivos / "resumo"
caminho_transcricoes = pasta_arquivos / "transcricoes"

def enviar_email(destinatario, arquivo, tipo_arquivo, assunto):
    try:
        remetente = os.getenv("REMETENTE")
        senha = os.getenv("SENHA")

        mensagem = EmailMessage()

        mensagem["From"] = remetente
        mensagem["To"] = destinatario
        mensagem["Subject"] = assunto

        mensagem.set_content("Segue o arquivo em anexo.")

        caminho = Path(arquivo)

        with open(caminho, "rb") as documento:
            mensagem.add_attachment(
                documento.read(),
                maintype="application",
                subtype=tipo_arquivo,
                filename=caminho.name
            )

        print("Conectando ao Gmail...")
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as servidor:
            print("Iniciando TLS...")
            servidor.starttls()

            print("Autenticando...")
            servidor.login(remetente, senha)

            print("Enviando mensagem...")
            servidor.send_message(mensagem)
            print("Mensagem aceita pelo servidor.")

            return True

    except FileNotFoundError as e:
        print(e)
        print(f"Arquivo não encontrado: {arquivo}")
        return False

    except smtplib.SMTPAuthenticationError as e:
        print(e)
        print("Erro de autenticação no e-mail.")
        return False

    except smtplib.SMTPException as erro:
        print(f"Erro SMTP: {erro}")
        return False
    except Exception as erro:
        print(f"Erro inesperado ({type(erro).__name__}): {erro}")
        return False

def chamar_funcao(Email, nome_arquivo, tipo_envio, resumo):
    print("chamou a funcao de chamar a funcao")
    if Email is None:
       with open(pasta_arquivos / "emails" / "emails.txt", "r", encoding="utf-8") as arquivo:
            for email in arquivo:
                email = email.strip()

                if email:
                    print("chegou na funcao de enviar")
                    resposta = enviar_email(email, nome_arquivo, tipo_envio, resumo)
                    return resposta
    else:
        print('chegou na funcao de enviar')
        resposta = enviar_email(Email, nome_arquivo, tipo_envio, resumo)
        return resposta

def enviar_resumo_pdf(nome_arquivo, data, email=None):
    print('iniciou a funcao reusmo_pdf')
    arquivo = caminho_resumo_pdf / nome_arquivo

    if arquivo.is_file():
        print('chamou a funcao de chamar_funcao')
        resposta = chamar_funcao(email, arquivo, "pdf", f"Resumo da aula {data}")
        return resposta
    else:
        print(f"PDF procurado em: {arquivo.resolve()}")
        print(f"Pasta de PDFs existe? {caminho_resumo_pdf.is_dir()}")
        return False


def enviar_resumo(nome_arquivo, data, email):
    print('chamou a funcao enviar_resumo')
    arquivo = caminho_resumo / nome_arquivo

    if arquivo.is_file():
        print('chamou a funcao de chamar_funcao')
        resposta = chamar_funcao(email, arquivo, "octet-stream", f"Resumo da aula {data}")
        return resposta
    else:
        print('arquivo n encontrando')
        return None


def enviar_transcricao(nome_arquivo, data, email):
    print('chamou a funcao de enviar_trancricao')
    arquivo = caminho_transcricoes / nome_arquivo

    if arquivo.is_file():
        print('chamou a funcao de chamar_funcao')
        resposta = chamar_funcao(email, arquivo, "json", f"Transcrição da aula {data}")
        return resposta
    else:
        print('arquivo n encontrado')
        return None