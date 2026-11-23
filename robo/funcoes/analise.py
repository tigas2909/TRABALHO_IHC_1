from ..comandos.modos import comandos
from ..comandos.comandos import (
    alterar_modo, 
    iniciar_aula,
    registrar_legenda,
    finalizar_aula,
    obter_aula_atual, 
    obter_modo_atual
)

modos = {
    # iniciar
    'iniciar_aula': True,
    'iniciar_tarefa': 'atividade',
    'iniciar_trabalho': 'trabalho',
    'iniciar_destaque': 'destaque',

    # finalizar
    'finalizar_tarefa': 'aula',
    'finalizar_trabalho': 'aula',
    'finalizar_destaque': 'aula',
    'finalizar_aula': None
}
def analisar(texto: str, inicio = None):
    txt = comandos(texto)
    if txt in modos:
        
        if txt == 'iniciar_aula':
            iniciar_aula(inicio['materia'], inicio['professor'])
        elif txt == 'finalizar_aula':
            finalizar_aula()
        else:
            alterar_modo(modos[txt])
    else:
        if obter_aula_atual() is not None:
            registrar_legenda(texto)
        else: 
            return None