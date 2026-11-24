from pathlib import Path

PASTA_RESUMOS = (
    Path(__file__).resolve().parents[2]
    / "arquivos"
    / "resumo"
)

def salvar_resumo(nome_arquivo: str, resumo: str):
    nome = Path(nome_arquivo).stem
    caminho = PASTA_RESUMOS / f"{nome}.txt"

    PASTA_RESUMOS.mkdir(parents=True, exist_ok=True)

    caminho.write_text(resumo, encoding="utf-8")

    return caminho