# 📝 Python Task Manager

Um gerenciador de tarefas simples feito em Python, executado diretamente no terminal.

## 🚀 Funcionalidades

* ➕ Adicionar tarefas
* 📋 Listar tarefas
* ✅ Marcar tarefas como concluídas
* 💾 Salvamento automático em arquivo
* 📅 Suporte a datas nas tarefas

## 🛠️ Tecnologias

* Python 3
* InquirerPy (interface interativa no terminal)
* rich (melhoria visual no terminal)

## 📂 Estrutura do Projeto

```
Pyton/
├── setup.bat
├── repositorio/
│   ├── main.py
│   ├── utils.py
│   └── arquivo.txt
├── .venv/
├── requirements.txt
└── .gitignore
```

## ▶️ Como executar

### Método automatizado (em breve)

Será possível utilizar um script para automatizar a configuração do ambiente:

```
setup.bat
```

Esse script irá:

* Criar o ambiente virtual (`.venv`)
* Instalar todas as dependências automaticamente

⚠️ **Status:** ainda não disponível / em desenvolvimento

---

### Método manual (atual)

1. Criar o ambiente virtual:

```
python -m venv .venv
```

2. Ativar o ambiente:

```
.venv\Scripts\Activate.ps1
```

3. Instalar dependências:

```
pip install -r requirements.txt
```

4. Executar o projeto:

```
python repositorio\main.py
```

---

## ⚠️ Possíveis problemas

* **Erro de permissão no PowerShell**

  ```
  execução de scripts foi desabilitada
  ```

  Solução:

  ```
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

* **Biblioteca não encontrada**

  ```
  ModuleNotFoundError
  ```

  Solução: garantir que o `.venv` está ativo ou usar:

  ```
  .venv\Scripts\python -m pip install -r requirements.txt
  ```

* **Caminho com espaços**
  Pode causar erro no terminal
  Solução: usar aspas ao navegar entre pastas

---

## 📌 Objetivo

Projeto criado com foco em aprendizado de:

* lógica de programação
* manipulação de arquivos
* organização de código em Python
* uso de bibliotecas externas

---

Simples, direto e funcional.
