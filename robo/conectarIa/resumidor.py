import os
import json
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

RAIZ = Path(__file__).resolve().parents[2]

PASTA_TRANSCRICOES = RAIZ / "arquivos" / "transcricoes"

PASTA_RESUMOS = RAIZ / "arquivos" / "resumo"

PASTA_PDF = RAIZ / "arquivos" / "resumo_pdf"

CONTEXTO = RAIZ / "arquivos" / "contexto_para_Ia" / "resumo_ordem.txt"

CHAVE = os.getenv("GEMINI_API_KEY")

MODELO = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")


def gerar_resumo(nome_arquivo: str) -> str:

    if not CHAVE:
        raise ValueError("Chave do Gemini não encontrada.")

    # Localizar a transcrição
    caminho = PASTA_TRANSCRICOES / Path(nome_arquivo).name

    # Ler o JSON da aula
    with caminho.open("r", encoding="utf-8") as arquivo:
        aula = json.load(arquivo)

    if not aula.get("legendas"):
        raise ValueError("A aula não possui legendas.")

    # Ler as instruções do Gemini
    contexto = CONTEXTO.read_text(encoding="utf-8")

    # Converter o dicionário para JSON em texto
    dados = json.dumps(aula, ensure_ascii=False)

    # Enviar os dados ao Gemini
    with genai.Client(api_key=CHAVE) as cliente:

        resposta = cliente.models.generate_content(
            model=MODELO,
            contents=dados,
            config=types.GenerateContentConfig(
                system_instruction=contexto,
                temperature=0.2
            )
        )

    # Verificar a resposta
    if not resposta.text:
        raise ValueError("O Gemini não retornou um resumo.")

    # Obter o texto gerado
    resumo = resposta.text.strip()

    return resumo