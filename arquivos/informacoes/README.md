# 🎓 Sistema de Legendagem e Resumo de Aulas

> Projeto acadêmico de Interação Humano-Computador (IHC), desenvolvido com foco em acessibilidade, reconhecimento de voz e inteligência artificial.

## 📖 Sobre o projeto

O projeto consiste no desenvolvimento de um sistema de acessibilidade capaz de acompanhar aulas por meio de **legendas em tempo real**, registrar as transcrições e gerar automaticamente **resumos em PDF**.

A proposta é facilitar o acompanhamento das explicações e permitir que os alunos consultem posteriormente os conteúdos apresentados.

O sistema utiliza reconhecimento de fala para transformar áudio em texto, inteligência artificial para revisar as transcrições e gerar resumos, além de uma interface para exibição das legendas.

Também contará com **armazenamento local**, preservando os arquivos gerados mesmo quando ocorrerem falhas de conexão ou de envio por e-mail.

---

## 🎯 Objetivos

### Objetivo principal

Desenvolver uma ferramenta que amplie a acessibilidade no ambiente educacional por meio de legendas em tempo real e materiais de apoio gerados automaticamente.

### Objetivos específicos

- Disponibilizar legendas durante as aulas.
- Reconhecer comandos de voz para controlar o sistema.
- Registrar as transcrições das aulas.
- Utilizar inteligência artificial para revisar o texto reconhecido.
- Gerar resumos organizados dos conteúdos apresentados.
- Converter os resumos em documentos PDF.
- Enviar os materiais aos alunos por e-mail.
- Armazenar localmente as transcrições, os resumos e os PDFs.
- Preservar documentos que não puderem ser enviados.
- Permitir a recuperação dos arquivos armazenados.

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| Reconhecimento de voz | Converte as falas do professor em texto. |
| Legendas em tempo real | Exibe o conteúdo reconhecido durante a aula. |
| Comandos de voz | Permite controlar o funcionamento do sistema. |
| Transcrição | Registra o conteúdo falado durante a aula. |
| Revisão textual | Utiliza IA para melhorar o texto transcrito. |
| Resumo automático | Organiza os principais conteúdos apresentados. |
| Geração de PDF | Produz um documento com o resumo da aula. |
| Envio por e-mail | Encaminha os documentos aos alunos. |
| Armazenamento local | Preserva os arquivos produzidos pelo sistema. |
| Tratamento de falhas | Mantém os documentos quando o envio não é concluído. |

> **Observação:** o projeto está em desenvolvimento. Algumas funcionalidades ainda estão em fase de implementação ou integração.

---

## ⚙️ Funcionamento do sistema

O funcionamento foi dividido em etapas para facilitar o desenvolvimento, os testes e a manutenção.

### 1. Inicialização

Ao iniciar, o sistema permanece aguardando um comando de voz.

O reconhecimento de comandos permite controlar o funcionamento sem depender exclusivamente de interações manuais.

### 2. Início da aula

Quando o comando `iniciar aula` é reconhecido:

1. O sistema inicia o registro da aula.
2. Um arquivo de transcrição é criado.
3. O caminho do arquivo é armazenado para utilização durante o processamento.
4. O reconhecimento contínuo de fala é iniciado.
5. As legendas começam a ser exibidas.

### 3. Reconhecimento e legendagem

Durante a aula, o Vosk realiza o reconhecimento de fala em português brasileiro.

O texto reconhecido é utilizado para:

- Exibir legendas.
- Registrar o conteúdo apresentado.
- Alimentar o processamento posterior da transcrição.

O sistema também utiliza um vocabulário de apoio com termos técnicos, especialmente relacionados à programação.

### 4. Revisão da transcrição

Periodicamente, os trechos reconhecidos são enviados a um modelo de inteligência artificial responsável pela revisão textual.

O objetivo é melhorar a legibilidade do conteúdo, corrigindo possíveis problemas de escrita sem alterar o significado das explicações.

O texto revisado é acrescentado ao registro da aula.

### 5. Finalização da aula

Quando o comando `finalizar aula` é reconhecido:

1. O registro da aula é encerrado.
2. A transcrição é preparada para o processamento.
3. O conteúdo é enviado ao Google Gemini.
4. A inteligência artificial gera um resumo.
5. O resumo é convertido em PDF.
6. Os arquivos são armazenados localmente.
7. O sistema realiza o envio do material por e-mail.

---

## 💾 Armazenamento local

O sistema contará com um mecanismo de armazenamento local para preservar as informações geradas durante as aulas.

Essa funcionalidade tem como objetivo reduzir a dependência da conexão com a internet e evitar a perda de documentos em situações de falha no envio.

### Arquivos armazenados

Serão mantidos localmente:

- **Transcrições:** registros das falas reconhecidas durante as aulas.
- **Legendas:** conteúdo textual utilizado na exibição em tempo real.
- **Resumos:** textos organizados pela inteligência artificial.
- **PDFs:** documentos gerados ao finalizar as aulas.
- **Arquivos pendentes:** documentos que não puderam ser enviados aos destinatários.

### Tratamento de falhas

Caso ocorra uma falha de conexão ou de envio por e-mail:

1. O sistema preservará os arquivos disponíveis localmente.
2. Os documentos não enviados permanecerão armazenados.
3. Os arquivos poderão ser recuperados posteriormente.
4. O envio poderá ser realizado novamente quando o serviço estiver disponível.

Dessa forma, uma falha de comunicação não resultará automaticamente na perda dos materiais produzidos.

### Disponibilidade dos arquivos

Os documentos armazenados poderão ser utilizados para:

- Consulta posterior.
- Recuperação de transcrições.
- Acesso aos resumos.
- Reenvio de documentos.
- Verificação dos registros das aulas.

> **Importante:** o armazenamento local não substitui backups. Falhas físicas no dispositivo ainda podem comprometer os dados.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento do sistema |
| Vosk | Reconhecimento de fala |
| Google Gemini | Revisão textual e geração de resumos |
| FastAPI | Desenvolvimento da API |
| Uvicorn | Execução do servidor |
| WebSocket | Comunicação em tempo real |
| HTML | Estrutura da interface |
| CSS | Estilização da interface |
| JavaScript | Interatividade e atualização das legendas |
| JSON | Organização e troca de informações |
| PDF | Disponibilização dos resumos |

Outras bibliotecas poderão ser utilizadas conforme as necessidades de implementação.

---

## 📂 Estrutura do projeto

A organização do projeto separa os componentes responsáveis pelo reconhecimento de voz, processamento, integração com inteligência artificial e interface.

```text
trabalho_IHC/
│
├── robo/
│   ├── base.py
│   ├── comandos.py
│   ├── processamento/
│   ├── conectarIa/
│   ├── funcoes/
│   └── config/
│
├── view/
│
├── modelo/
│
├── aruivos/
│   ├── aulas/
│   ├── dicionario/
│   └── informacoes/
│
├── install.txt
│
└── README.md
```

> A estrutura apresentada poderá ser modificada durante o desenvolvimento.

---

## 📦 Instalação

### Pré-requisitos

- Python instalado.
- Pip.
- Microfone.
- Acesso à internet para utilização dos serviços externos.

### 1. Clonar o repositório

```bash
git clone https://github.com/tigas2909/trabalho_IHC.git
```

### 2. Acessar o diretório

```bash
cd trabalho_IHC
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

**Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

### 5. Instalar as dependências

```bash
pip install -r install.txt
```

### 6. Configurar as credenciais

Configure as variáveis de ambiente necessárias para os serviços de inteligência artificial e envio de e-mails.

As credenciais não devem ser publicadas no repositório.

---

## 🎙️ Comandos de voz

O sistema utiliza comandos para controlar o início e a finalização das atividades.

| Comando de voz | Identificador interno |
|---|---|
| iniciar aula | `iniciar_aula` |
| finalizar aula | `finalizar_aula` |
| iniciar tarefa | `iniciar_tarefa` |
| finalizar tarefa | `finalizar_tarefa` |
| iniciar trabalho | `iniciar_trabalho` |
| finalizar trabalho | `finalizar_trabalho` |
| aviso importante | `iniciar_importante` |
| aviso acabou | `finalizar_importante` |

### Identificação dos comandos

A identificação utiliza duas listas:

- `comando_voz`: contém as expressões reconhecidas.
- `comando`: contém os identificadores internos correspondentes.

A função responsável pela identificação procura a expressão recebida e retorna o identificador associado.

```python
def identificar_comando(texto):
    texto = " ".join(texto.lower().split())

    if texto in comando_voz:
        indice = comando_voz.index(texto)
        return comando[indice]

    return None
```

Essa abordagem permite adicionar novos comandos mantendo a correspondência entre as listas.

---

## 🧪 Testes

Os componentes estão sendo desenvolvidos e testados individualmente antes da integração completa.

### Teste de comandos

Para executar o teste de identificação de comandos:

```bash
python -m robo.base
```

Exemplo:

```text
Teste: iniciar aula
[iniciar_aula] funcionou

Teste: aviso importante
[iniciar_importante] funcionou

Teste: aviso acabou
[finalizar_importante] funcionou

Teste: finalizar aula
[finalizar_aula] funcionou

Teste: sair
Saindo...
```

O teste por texto permite verificar a lógica dos comandos independentemente do reconhecimento de voz.

Isso facilita a identificação de erros durante o desenvolvimento.

---

## ♿ Acessibilidade

O projeto foi desenvolvido com foco na ampliação do acesso ao conteúdo educacional.

As legendas em tempo real oferecem uma alternativa visual para acompanhar as explicações do professor.

Os resumos permitem consultar posteriormente os principais assuntos apresentados durante a aula.

### Benefícios esperados

- Maior acessibilidade ao conteúdo falado.
- Apoio ao acompanhamento das aulas.
- Disponibilização de registros escritos.
- Possibilidade de revisão posterior.
- Redução da dependência de anotações manuais.
- Acesso aos documentos armazenados localmente.

O sistema é uma ferramenta complementar de acessibilidade e não substitui automaticamente outros recursos necessários aos alunos.

---

## 🔒 Privacidade e proteção de dados

O projeto trabalha com informações produzidas durante atividades educacionais.

Por isso, deverão ser considerados cuidados relacionados à privacidade e à proteção dos dados.

Entre eles:

- Controle de acesso aos arquivos.
- Proteção das credenciais dos serviços externos.
- Armazenamento adequado das transcrições.
- Definição de critérios para retenção e exclusão dos documentos.
- Utilização dos registros apenas para as finalidades previstas.
- Observância da Lei Geral de Proteção de Dados Pessoais (LGPD).

O armazenamento local deverá ser acompanhado de medidas de proteção para evitar acessos não autorizados.

---

## 📌 Status do desenvolvimento

🚧 **Projeto em desenvolvimento.**

O desenvolvimento está sendo realizado por componentes, permitindo testar cada funcionalidade antes da integração.

### Etapas do projeto

- [x] Definição da proposta.
- [x] Planejamento do funcionamento.
- [x] Estruturação inicial dos módulos.
- [x] Implementação inicial da identificação de comandos.
- [ ] Integração completa dos comandos com o reconhecimento de voz.
- [ ] Captura e transcrição contínua das aulas.
- [ ] Integração completa das legendas com a interface.
- [ ] Revisão periódica das transcrições com IA.
- [ ] Geração automática dos resumos.
- [ ] Integração completa da geração de PDFs.
- [X] Envio automático dos documentos por e-mail.
- [X] Armazenamento local de todos os arquivos.
- [ ] Tratamento de falhas de envio.
- [ ] Testes de integração.
- [ ] Validação do sistema completo.

---

## 🔮 Melhorias futuras

Entre as possibilidades de evolução do projeto estão:

- Implementação de uma fila de documentos pendentes.
- Reenvio automático após o restabelecimento da conexão.
- Interface para consultar aulas anteriores.
- Pesquisa em transcrições armazenadas.
- Gerenciamento de arquivos e documentos.
- Melhorias no reconhecimento de termos técnicos.
- Otimização do processamento para dispositivos de baixo consumo.

Essas funcionalidades representam possibilidades de evolução e não fazem parte necessariamente da versão inicial.

---

## 🏫 Contexto acadêmico

**Instituição:** Instituto Federal do Paraná (IFPR)

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

**Disciplina:** Interação Humano-Computador (IHC)

**Tipo:** Projeto acadêmico de acessibilidade

---

## 👨‍💻 Desenvolvimento

**Desenvolvedor:** Tiago Siqueira

**GitHub:** [tigas2909](https://github.com/tigas2909)

**Repositório:** [trabalho_IHC](https://github.com/tigas2909/trabalho_IHC)

---

## 📄 Considerações finais

O projeto busca demonstrar como diferentes tecnologias podem ser integradas para desenvolver soluções de acessibilidade no ambiente educacional.

A combinação de reconhecimento de fala, legendas em tempo real, inteligência artificial, geração de documentos e armazenamento local permite construir uma ferramenta voltada ao acompanhamento e à revisão de conteúdos acadêmicos.

O objetivo final é oferecer uma solução funcional, acessível e capaz de preservar as informações produzidas durante as aulas, inclusive diante de falhas de comunicação.

**A tecnologia deve ampliar o acesso ao conhecimento.**