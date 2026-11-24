import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


def corrigir_texto(texto: str) -> str:
    chave = os.getenv("GEMINI_API_KEY")

    if not chave:
        raise ValueError("Chave do Gemini não encontrada.")

    with genai.Client(api_key=chave) as cliente:
        resposta = cliente.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=f"""
Corrija a transcrição abaixo.

Regras:
- Corrija erros ortográficos.
- Adicione pontuação.
- Preserve termos técnicos.
- Não resuma.
- Não acrescente informações.
- Retorne somente o texto corrigido.

Transcrição:
{texto}
"""
        )

    if not resposta.text:
        raise ValueError("O Gemini não retornou texto.")

    return resposta.text.strip()