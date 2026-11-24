# 🎓 Sistema de Legendagem e Resumo de Aulas

> Projeto acadêmico de **Interação Humano-Computador (IHC)** voltado à acessibilidade educacional, à transcrição de aulas e à produção automática de materiais de apoio com inteligência artificial.

**Status:** 🚧 Em desenvolvimento

O fluxo de transcrição estruturada, geração de resumos com inteligência artificial e produção de PDFs já foi implementado e testado. A integração das legendas em tempo real com a interface web permanece em desenvolvimento.

---

## 📖 Sobre o projeto

O **Sistema de Legendagem e Resumo de Aulas** é uma solução de acessibilidade desenvolvida para facilitar o acompanhamento das explicações em ambientes educacionais.

O projeto busca atender especialmente estudantes com deficiência auditiva ou que necessitam de recursos visuais e materiais escritos para acompanhar e revisar os conteúdos apresentados durante as aulas.

A solução combina:

- Reconhecimento de fala em português brasileiro.
- Identificação de comandos e gerenciamento dos modos da aula.
- Registro estruturado das transcrições.
- Processamento de informações com inteligência artificial.
- Geração automática de resumos.
- Criação de documentos TXT e PDF.
- Distribuição de materiais por e-mail.
- Armazenamento local dos documentos.

A proposta também contempla uma interface web que permitirá acompanhar as legendas em tempo real utilizando **FastAPI e WebSocket**.

---

## 🎯 Objetivos

### Objetivo principal

Desenvolver uma ferramenta que amplie a acessibilidade no ambiente educacional por meio de legendas em tempo real e materiais de apoio gerados automaticamente.

### Objetivos específicos

- Disponibilizar legendas para acompanhamento das aulas.
- Registrar transcrições estruturadas.
- Identificar momentos importantes das explicações.
- Distinguir conteúdos gerais, destaques, trabalhos e atividades.
- Utilizar inteligência artificial para organizar os conteúdos.
- Gerar resumos sem fornecer respostas prontas às atividades.
- Produzir documentos TXT e PDF.
- Distribuir materiais por e-mail.
- Preservar os arquivos mesmo diante de falhas no processamento ou envio.
- Permitir a recuperação dos documentos armazenados.

---

## 🚀 Funcionalidades

| Funcionalidade | Situação |
|---|---|
| Identificação de comandos | ✅ Implementado e testado por texto |
| Gerenciamento dos modos da aula | ✅ Implementado |
| Registro de aulas em JSON | ✅ Implementado e testado |
| Integração com Google Gemini | ✅ Implementado e testado |
| Geração automática de resumos | ✅ Implementado e testado |
| Salvamento de resumos em TXT | ✅ Implementado |
| Geração de PDF com ReportLab | ✅ Implementado e testado |
| Formatação de títulos, listas e negritos | ✅ Implementado |
| Armazenamento local | ✅ Implementado |
| Funções de envio por e-mail | ✅ Implementadas |
| Integração automática do envio | 🟡 Em validação |
| Reconhecimento contínuo de voz com Vosk | 🚧 Em desenvolvimento |
| Revisão periódica das legendas com IA | 🚧 Planejado |
| Legendas em tempo real pela web | 🚧 Em desenvolvimento |
| Reenvio automático de documentos pendentes | 📋 Planejado |

> **Observação:** o projeto ainda não está concluído. Os testes realizados validaram principalmente o processamento de transcrições estruturadas e a geração automática de documentos.

---

## ⚙️ Funcionamento do sistema

O sistema foi dividido em módulos independentes, facilitando o desenvolvimento, os testes e a manutenção.

### 1. Inicialização

O sistema aguarda um comando para iniciar a aula.

Durante os testes atuais, os comandos podem ser digitados, permitindo verificar a lógica sem depender do reconhecimento de voz.

### 2. Início da aula

Ao reconhecer o comando `iniciar aula`, o sistema:

1. Inicia uma nova sessão.
2. Registra as informações da disciplina e do professor.
3. Cria uma estrutura para armazenar a transcrição.
4. Ativa o modo de aula.
5. Permite o registro das informações recebidas.

### 3. Gerenciamento dos modos

O sistema diferencia as informações registradas durante a aula.

| Modo | Finalidade |
|---|---|
| Aula | Registrar as explicações e o conteúdo geral |
| Destaque | Identificar informações que merecem maior importância no resumo |
| Trabalho | Registrar requisitos e orientações de trabalhos |
| Tarefa/atividade | Registrar os enunciados e as instruções das atividades |

Essa separação permite que a inteligência artificial compreenda melhor a importância e a finalidade de cada informação.

### 4. Transcrição

As informações recebidas são armazenadas em arquivos JSON.

O sistema utiliza uma estrutura organizada para registrar o conteúdo das aulas, permitindo seu processamento posterior.

A integração completa com o reconhecimento contínuo de áudio está em desenvolvimento.

### 5. Processamento com inteligência artificial

Ao finalizar a aula, a transcrição é enviada ao **Google Gemini**.

O modelo recebe instruções específicas para:

- Produzir uma visão geral da aula.
- Destacar as informações mais importantes.
- Organizar os trabalhos.
- Organizar as atividades.
- Preservar os requisitos apresentados pelo professor.
- Oferecer orientações de como começar as atividades.
- Evitar fornecer respostas prontas.
- Não inventar informações que não estejam presentes na transcrição.

As instruções utilizadas ficam armazenadas em:

`arquivos/contexto_para_Ia/resumo_ordem.txt`

### 6. Geração de documentos

Após receber o resumo, o sistema produz automaticamente dois arquivos:

**TXT:** contém o resumo textual gerado pela inteligência artificial.

**PDF:** apresenta o conteúdo organizado em um documento com títulos, listas e formatação de texto.

A geração dos PDFs utiliza a biblioteca **ReportLab**.

### 7. Envio por e-mail

O módulo de envio utiliza SMTP para encaminhar os documentos.

O sistema permite:

- Enviar um documento para um destinatário específico.
- Enviar documentos para os destinatários cadastrados.
- Anexar arquivos PDF, TXT ou JSON.
- Identificar falhas durante o envio.

As funções de envio já foram implementadas. A validação completa da integração automática está entre as próximas etapas.

---

## 🔄 Fluxo do sistema

```text
          RECONHECIMENTO DE FALA
             (em integração)
                     |
                     v
          IDENTIFICAÇÃO DE COMANDOS
                     |
                     v
             INÍCIO DA AULA
                     |
                     v
          GERENCIAMENTO DOS MODOS
                     |
          +----------+----------+
          |          |          |
          v          v          v
        AULA      DESTAQUE   ATIVIDADE
                     |
                     v
              TRANSCRIÇÃO
                     |
                     v
                 JSON
                     |
                     v
             FINALIZAR AULA
                     |
                     v
              GOOGLE GEMINI
                     |
                     v
                 RESUMO
                     |
              +------+------+
              |             |
              v             v
             TXT           PDF
                            |
                            v
                     ENVIO POR E-MAIL
                       (em validação)
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Desenvolvimento da lógica do sistema |
| Vosk | Reconhecimento de fala |
| Google Gemini | Geração de resumos com IA |
| google-genai | Integração com a API do Gemini |
| ReportLab | Geração de PDFs |
| FastAPI | Desenvolvimento da API |
| Uvicorn | Execução do servidor |
| WebSocket | Comunicação em tempo real |
| HTML | Estrutura da interface |
| CSS | Estilização da interface |
| JavaScript | Interatividade e atualização das legendas |
| JSON | Armazenamento estruturado das transcrições |
| SMTP / smtplib | Envio de documentos por e-mail |
| python-dotenv | Carregamento de variáveis de ambiente |

---

## 📂 Estrutura do projeto

A organização separa os componentes responsáveis pelos comandos, processamento, integração com inteligência artificial e geração de documentos.

```text
trabalho_IHC/
│
├── arquivos/
│   ├── contexto_para_Ia/
│   │   └── resumo_ordem.txt
│   │
│   ├── dicionario/
│   │
│   ├── emails/
│   │   └── emails.txt
│   │
│   ├── informacoes/
│   │
│   ├── resumo/
│   │
│   ├── resumo_pdf/
│   │
│   └── transcricoes/
│
├── robo/
│   ├── base.py
│   │
│   ├── comandos/
│   │
│   ├── conectarIa/
│   │   ├── refinador.py
│   │   └── resumidor.py
│   │
│   └── funcoes/
│       ├── email.py
│       ├── pdf.py
│       ├── salvarAula.py
│       └── salvar_resumo.py
│
├── install.txt
├── .gitignore
└── README.md
```

**Observação:** essa estrutura apresenta os principais módulos e poderá ser modificada durante o desenvolvimento.

Os diretórios que armazenam e-mails, transcrições e documentos gerados devem permanecer fora do versionamento público.

---

## 📦 Instalação

### Pré-requisitos

- Python instalado.
- Pip.
- Microfone para os testes de reconhecimento de áudio.
- Acesso à internet para utilização da API do Gemini e envio de e-mails.

### 1. Clonar o repositório

```bash
git clone https://github.com/tigas2909/TRABALHO_IHC_1.git
```

### 2. Acessar o diretório

```bash
cd TRABALHO_IHC_1
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

**Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
python -m pip install -r install.txt
```

### 6. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Exemplo:

```dotenv
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=nome_de_um_modelo_disponivel_na_sua_conta

REMETENTE=seu_email@gmail.com
SENHA=sua_senha_de_app
```

O modelo Gemini configurado deve estar disponível para a chave utilizada.

Para o Gmail, utilize um método de autenticação compatível, como uma senha de aplicativo quando disponível.

**Nunca publique suas credenciais no GitHub.**

---

## 🎙️ Comandos do sistema

Os comandos permitem controlar o funcionamento da aula.

| Comando | Finalidade |
|---|---|
| `iniciar aula` | Iniciar o registro da aula |
| `finalizar aula` | Encerrar a aula e iniciar a geração do resumo |
| `iniciar tarefa` | Iniciar o registro de uma tarefa |
| `finalizar tarefa` | Encerrar o registro da tarefa |
| `iniciar trabalho` | Iniciar o registro de um trabalho |
| `finalizar trabalho` | Encerrar o registro do trabalho |
| `iniciar destaque` | Iniciar o registro de uma informação importante |
| `finalizar destaque` | Encerrar o destaque |

Durante o desenvolvimento, a entrada textual é utilizada para validar a interpretação desses comandos.

Posteriormente, a mesma lógica poderá ser integrada ao reconhecimento de voz.

---

## 🧪 Testes

O projeto está sendo desenvolvido de forma modular.

Isso permite testar os componentes individualmente antes da integração completa.

### Testar a entrada textual

Execute:

```bash
python -m robo.base
```

A interface permite verificar o funcionamento dos comandos e dos modos da aula.

### Testar o fluxo completo

Quando o arquivo de teste automatizado estiver disponível na versão local:

```bash
python -m teste_automatico
```

Esse teste permite simular:

1. Início de uma aula.
2. Registro de explicações.
3. Registro de destaques.
4. Registro de trabalhos.
5. Registro de atividades.
6. Finalização da aula.
7. Geração do resumo pelo Gemini.
8. Salvamento do TXT.
9. Geração do PDF.

**Atenção:** testes completos podem consumir tokens da API do Gemini e, caso o envio esteja ativado, encaminhar e-mails reais.

### Resultado obtido

O sistema já conseguiu executar o processamento de uma aula simulada e gerar os documentos correspondentes.

Exemplo de organização do resumo:

```text
Resumo da Aula

Aula: Programação Orientada a Objetos
Professor: Tiago

Visão Geral
Conceitos de classes, objetos, atributos e métodos.

Destaques da aula
- Herança e reutilização de código.

Trabalhos
- Enunciado do trabalho.
- Requisitos apresentados.
- Orientações de como começar.

Atividades
- Enunciado da atividade.
- Orientações de como começar.
```

O conteúdo acima é ilustrativo. Os documentos reais dependem das informações registradas e do processamento realizado pelo modelo.

---

## 💾 Armazenamento local

O sistema utiliza armazenamento local para preservar os documentos produzidos durante as aulas.

### Arquivos armazenados

| Diretório | Conteúdo |
|---|---|
| `arquivos/transcricoes/` | Transcrições em JSON |
| `arquivos/resumo/` | Resumos em TXT |
| `arquivos/resumo_pdf/` | Documentos PDF |
| `arquivos/contexto_para_Ia/` | Instruções utilizadas pelo Gemini |
| `arquivos/dicionario/` | Vocabulário de apoio |

### Preservação dos arquivos

O registro da aula é salvo antes da geração do resumo.

Dessa forma, se ocorrer uma falha na comunicação com o Gemini ou na geração dos documentos, a transcrição poderá continuar disponível localmente.

Os arquivos TXT e PDF também permanecem armazenados caso o envio por e-mail falhe.

A implementação de mecanismos automáticos de recuperação e reenvio está prevista para etapas futuras.

---

## ♿ Acessibilidade

A acessibilidade é o principal objetivo do projeto.

As legendas em tempo real buscam oferecer uma alternativa visual para acompanhar as explicações do professor.

Os resumos permitem revisar posteriormente os conteúdos apresentados.

### Benefícios esperados

- Ampliação do acesso às explicações orais.
- Apoio a estudantes com deficiência auditiva.
- Disponibilização de materiais escritos.
- Redução da dependência de anotações manuais.
- Identificação de informações importantes.
- Organização de atividades e trabalhos.
- Possibilidade de revisão posterior.
- Maior autonomia no acompanhamento dos conteúdos.

O sistema foi pensado como uma ferramenta complementar de acessibilidade e não como substituto universal de outros recursos necessários aos estudantes.

---

## 🔒 Privacidade e proteção de dados

O projeto poderá processar informações produzidas durante atividades educacionais, incluindo falas, nomes e endereços de e-mail.

Por isso, devem ser observados cuidados relacionados à **Lei Geral de Proteção de Dados Pessoais (LGPD)**.

Entre as medidas importantes estão:

- Obter as autorizações necessárias para captação de áudio.
- Restringir o acesso às transcrições e documentos.
- Proteger as credenciais de serviços externos.
- Evitar a publicação de informações pessoais.
- Definir critérios de armazenamento e exclusão.
- Informar sobre o processamento de transcrições por serviços externos.
- Utilizar os dados apenas para as finalidades previstas.

### Arquivos que não devem ser publicados

```gitignore
.env
.venv/
__pycache__/
*.pyc

arquivos/emails/
arquivos/transcricoes/
arquivos/resumo/
arquivos/resumo_pdf/
```

O `.gitignore` impede o rastreamento de novos arquivos correspondentes às regras, mas não remove automaticamente arquivos que já foram adicionados ao histórico do Git.

---

## 📌 Status do desenvolvimento

🚧 **Projeto em desenvolvimento.**

O desenvolvimento está sendo realizado por módulos, permitindo validar cada componente antes da integração final.

### Etapas concluídas

- [x] Definição da proposta.
- [x] Planejamento da arquitetura inicial.
- [x] Estruturação dos módulos.
- [x] Implementação da identificação de comandos por texto.
- [x] Gerenciamento dos modos da aula.
- [x] Registro de transcrições em JSON.
- [x] Integração com a API do Google Gemini.
- [x] Geração automática dos resumos.
- [x] Salvamento dos arquivos TXT.
- [x] Geração de PDFs com ReportLab.
- [x] Formatação básica dos PDFs.
- [x] Implementação das funções de envio por e-mail.
- [x] Armazenamento local das transcrições e dos documentos.

### Em desenvolvimento

- [ ] Validação completa do envio automático de e-mails.
- [ ] Integração do reconhecimento contínuo de voz.
- [ ] Comunicação em tempo real com WebSocket.
- [ ] Exibição das legendas na interface web.
- [ ] Revisão periódica das legendas com inteligência artificial.
- [ ] Otimização do processamento para dispositivos de baixo consumo.
- [ ] Testes de integração em ambiente real.
- [ ] Validação completa da solução.

---

## 🔮 Melhorias futuras

Entre as possibilidades de evolução estão:

- Implementação de uma fila de documentos pendentes.
- Reenvio automático de arquivos após falhas de conexão.
- Interface para consulta de aulas anteriores.
- Pesquisa em transcrições.
- Gerenciamento de arquivos e documentos.
- Melhorias no reconhecimento de termos técnicos.
- Otimização para TV Box e dispositivos de baixo consumo.
- Melhorias na apresentação visual das legendas.
- Ampliação dos recursos de acessibilidade.

Essas funcionalidades poderão ser incorporadas conforme a evolução do projeto.

---

## 🏫 Contexto acadêmico

**Instituição:** Instituto Federal do Paraná (IFPR)

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

**Disciplina:** Interação Humano-Computador (IHC)

**Área:** Acessibilidade e tecnologia educacional

**Tipo:** Projeto acadêmico

---

## 👨‍💻 Desenvolvimento

**Desenvolvedores:** Tiago Siqueira e Breno

**GitHub:** [tigas2909](https://github.com/tigas2909)

**Repositório:** [TRABALHO_IHC_1](https://github.com/tigas2909/TRABALHO_IHC_1)

---

## 📄 Considerações finais

O projeto demonstra como diferentes tecnologias podem ser integradas para desenvolver soluções voltadas à acessibilidade educacional.

A combinação de reconhecimento de fala, processamento de informações, inteligência artificial, geração de documentos e comunicação em tempo real busca facilitar o acompanhamento das aulas e ampliar o acesso ao conhecimento.

O objetivo final é disponibilizar uma ferramenta funcional, acessível e capaz de preservar os conteúdos apresentados durante as atividades educacionais.

**A tecnologia deve ampliar o acesso ao conhecimento.**
