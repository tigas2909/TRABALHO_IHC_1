import json
from datetime import datetime
from pathlib import Path

PASTA_AULAS = Path(__file__).resolve().parents[2] / "arquivos" / "transcricoes"

def criar_aula(materia: str, professor: str, inicio: datetime) -> dict:
    return {
        "id": inicio.isoformat(timespec="microseconds"),
        "materia": materia,
        "professor": professor,
        "legendas": [],
        "ativo": True,
    }


def salvar_legenda(aula: dict, texto: str, modo: str) -> None:
    if not aula["ativo"]:
        raise ValueError("A aula já foi finalizada.")

    legendas = aula["legendas"]

    legendas.append({
        "id": len(legendas),
        "modo": modo,
        "legenda": texto,
    })


def caminho_aula(aula: dict) -> Path:
    inicio = datetime.fromisoformat(aula["id"])

    return PASTA_AULAS / f"aula_{inicio:%Y-%m-%d_%H-%M-%S-%f}.json"


def salvar_progresso(aula: dict) -> Path:
    PASTA_AULAS.mkdir(parents=True, exist_ok=True)

    caminho = caminho_aula(aula)
    temporario = caminho.with_suffix(".tmp")

    with temporario.open("w", encoding="utf-8") as arquivo:
        json.dump(aula, arquivo, ensure_ascii=False, indent=4)

    temporario.replace(caminho)

    return caminho


def salvar_aula(aula: dict) -> Path:
    if not aula["ativo"]:
        raise ValueError("A aula já foi finalizada.")

    aula["ativo"] = False

    return salvar_progresso(aula)


def recuperar_aula(caminho: Path) -> dict:
    with caminho.open("r", encoding="utf-8") as arquivo:
        aula = json.load(arquivo)

    return aula