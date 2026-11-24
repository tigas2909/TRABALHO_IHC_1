import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet


RAIZ = Path(__file__).resolve().parents[2]

PASTA_PDF = RAIZ / "arquivos" / "resumo_pdf"


def formatar_texto(texto: str) -> str:
    texto = escape(texto)

    texto = re.sub(
        r"\*\*(.*?)\*\*",
        r"<b>\1</b>",
        texto
    )

    return texto


def gerar_pdf(resumo: str, nome_arquivo: str) -> Path:

    nome = Path(nome_arquivo).stem

    caminho = PASTA_PDF / f"{nome}.pdf"

    PASTA_PDF.mkdir(parents=True, exist_ok=True)

    documento = SimpleDocTemplate(
        str(caminho),
        pagesize=A4
    )

    estilos = getSampleStyleSheet()

    elementos = []

    elementos.append(
        Paragraph("Resumo da Aula", estilos["Title"])
    )

    elementos.append(Spacer(1, 20))

    for linha in resumo.splitlines():

        linha = linha.strip()

        if not linha:
            elementos.append(Spacer(1, 8))
            continue

        if linha.startswith("### "):
            elementos.append(
                Paragraph(
                    formatar_texto(linha[4:]),
                    estilos["Heading2"]
                )
            )

        elif linha.startswith("## "):
            elementos.append(
                Paragraph(
                    formatar_texto(linha[3:]),
                    estilos["Heading1"]
                )
            )

        elif linha.startswith("# "):
            elementos.append(
                Paragraph(
                    formatar_texto(linha[2:]),
                    estilos["Title"]
                )
            )

        elif linha.startswith(("* ", "- ")):
            elementos.append(
                Paragraph(
                    "• " + formatar_texto(linha[2:]),
                    estilos["Normal"]
                )
            )

        else:
            elementos.append(
                Paragraph(
                    formatar_texto(linha),
                    estilos["Normal"]
                )
            )

        elementos.append(Spacer(1, 6))

    documento.build(elementos)

    return caminho