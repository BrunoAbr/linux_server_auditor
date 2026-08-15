# 🔐 Linux Server Auditor

Ferramenta em Python para realizar auditorias automatizadas em servidores Linux.

O projeto tem como objetivo coletar informações do sistema, analisar configurações e identificar possíveis problemas de infraestrutura e segurança.

## 🚧 Status

**Em desenvolvimento.**

Atualmente, o projeto possui módulos para:

### 🖥️ System Audit
- Hostname
- Sistema operacional
- Versão do sistema
- Kernel
- Uso de CPU
- Uso de memória
- Uso de disco
- Uptime

### ⚙️ Process Audit
- Processos em execução
- Processos com maior consumo de CPU
- Processos com maior consumo de memória

### 👤 User Audit
- Usuários regulares
- Usuários do sistema
- Usuários com UID 0
- Usuários administrativos
- Usuários com acesso ao shell
- Verificações básicas de segurança

### 🔧 Service Audit
- Serviços ativos
- Serviços com falha
- Serviços habilitados
- Verificações básicas de serviços

Novas funcionalidades e verificações de segurança serão adicionadas durante o desenvolvimento.

## 🛠️ Tecnologias

- Python
- Linux
- psutil
- systemctl

## 📁 Estrutura

```text
linux_server_auditor/
├── auditor/
│   ├── __init__.py
│   ├── system.py
│   ├── processes.py
│   ├── users.py
│   └── services.py
│
├── presentation/
│   ├── __init__.py
│   └── terminal.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── .gitignore
```