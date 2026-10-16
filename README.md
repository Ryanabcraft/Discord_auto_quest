# 🎯 Discord Auto Quest

Feito por **Ryanab** e **DeepSeek V4.1 Flash**

Bot open source para automatizar missões (quests) do Discord.

## Aviso
- Uso por sua conta e risco.
- Automação com token de usuário pode violar os Termos do Discord.
- Não compartilhe seu token.

## Configuração

Preencha o arquivo `.env` na pasta do projeto. O `BOT_TOKEN` é o token do bot;
`OWNER_ID` é seu ID do Discord. Os demais campos podem ficar nos valores padrão.

O `.env` é ignorado pelo Git para manter seus tokens privados.

### DATA_KEY (recomendado)

Gere uma chave e cole no `DATA_KEY` do `.env`:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Com a chave definida, os tokens das contas em `data/` são salvos criptografados.
Sem ela, o bot avisa no startup e salva em texto puro.

⚠️ A pasta `data/` (tokens das contas) também é ignorada pelo Git. Não publique
o `.env` nem arquivos compactados da pasta sem conferir o conteúdo.

## Rodar

```bash
pip install -r requirements.txt
python autoquest.py
```

## Comandos (dono)
- `!painel orbs` — painel
- `!setup qn` — token do notify
- `!quest notify` — ativa notify no canal

## Painel
Login · Quests · Tutorial · Config · Sair
