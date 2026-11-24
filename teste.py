import time

from robo.funcoes.analise import analisar
from robo.comandos.comandos import obter_modo_atual


def testar_aula():
    print("=== INICIANDO TESTE AUTOMÁTICO ===")

    comandos = [
        "Hoje vamos estudar programação orientada a objetos.",
        "Uma classe possui atributos e métodos.",
        "Um objeto é uma instância de uma classe.",
        "iniciar destaque",
        "Herança permite reutilizar características de outras classes.",
        "finalizar destaque",
        "iniciar tarefa",
        "Criem uma classe Pessoa com nome e idade.",
        "A atividade deverá ser entregue amanhã.",
        "finalizar tarefa",
        "iniciar trabalho",
        "Desenvolvam um sistema de cadastro de alunos.",
        "O trabalho deverá ser entregue em PDF.",
        "finalizar trabalho",
    ]

    try:
        print("\n[1] Iniciando aula...")

        resultado = analisar(
            "iniciar aula",
            {
                "materia": "Programação Orientada a Objetos",
                "professor": "Tiago"
            }
        )

        if resultado is False:
            raise RuntimeError("Não foi possível iniciar a aula.")

        print(f"[OK] Modo atual: {obter_modo_atual()}")

        print("\n[2] Simulando transcrição...")

        for texto in comandos:
            print(f"[{obter_modo_atual()}] {texto}")

            resultado = analisar(texto)

            if resultado is False:
                raise RuntimeError(
                    f"Falha ao processar: {texto}"
                )

            time.sleep(0.2)

        print("\n[3] Finalizando aula...")
        print("[INFO] Gerando resumo com Gemini e PDF...")

        resultado = analisar("finalizar aula")

        if resultado is False:
            raise RuntimeError("Falha ao finalizar a aula.")

        print("\n[OK] Fluxo de finalização executado.")
        print(f"[MODO FINAL] {obter_modo_atual()}")

        print("\n=== TESTE ENCERRADO ===")

    except Exception as erro:
        print(f"\n[ERRO] {type(erro).__name__}: {erro}")


if __name__ == "__main__":
    testar_aula()