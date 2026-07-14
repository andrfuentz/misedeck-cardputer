# Mise_Deck

**Um mise en place de bolso e caixa de ferramentas culinÃ¡ria para o M5Stack Cardputer.**

O Mise_Deck transforma o M5Stack Cardputer em um mise en place de bolso para escalar receitas, gerenciar ingredientes, usar timer, compartilhar receitas offline e acessar um portal local pelo navegador.

> *"nÃ³s somos os mÃºsicos e somos os sonhadores de sonhos"*

O Mise_Deck foi idealizado por **AndrÃ© Fuentes** / **@anfuentz** e vibecodeado com **Codex**.

## Status

Release pÃºblica atual: **v1.5.0**

Builds em inglÃªs e portuguÃªs brasileiro estÃ£o disponÃ­veis.

## O que ele faz

- Salva receitas no microSD
- Organiza receitas por categoria e favoritas
- Suporta receitas simples e compostas
- Recalcula receitas proporcionalmente pelo peso total
- Permite criar, duplicar, editar e apagar receitas no Cardputer
- Permite mover o cursor durante ediÃ§Ã£o de textos e nÃºmeros
- Inclui modo rÃ¡pido para cÃ¡lculos proporcionais
- Inclui timer, conversor, tela de bateria e controle de som/volume
- Conecta ao Wi-Fi pelo prÃ³prio Cardputer
- Cria um portal local em `misedeck.local` ou pelo IP do aparelho
- Tem interface responsiva para celular
- Permite editar, salvar e baixar arquivos TXT de receita pelo navegador
- Compartilha receitas offline por QR Code

## Hardware

Pensado para:

- M5Stack Cardputer
- M5Stack Cardputer ADV / Cardputer-Adv

O projeto usa o target ESP32-S3 / StampS3 usado pelo Cardputer.

## Controles

Controles principais:

- `;` â€” cima
- `.` â€” baixo
- `,` â€” esquerda / anterior
- `/` â€” direita / prÃ³ximo
- `OK` / `Enter` â€” confirmar
- `` ` `` / `Esc` â€” voltar / cancelar
- `Del` â€” apagar caractere
- `Tab` â€” favoritar/desfavoritar receita

Durante ediÃ§Ã£o de texto ou nÃºmero:

- `,` â€” mover cursor para esquerda
- `/` â€” mover cursor para direita
- `Del` â€” apagar antes do cursor

## Portal local

Depois de conectar o Cardputer ao Wi-Fi:

1. Abra `http://misedeck.local` no navegador, ou use o IP mostrado no Cardputer.
2. Navegue pelas receitas por categoria ou pela aba Todas.
3. Abra uma receita para visualizar, recalcular proporÃ§Ã£o, editar TXT, salvar ou baixar.

O portal roda direto no Cardputer dentro da rede local. Ele nÃ£o Ã© um serviÃ§o de nuvem e nÃ£o precisa de conta.

## Formato TXT das receitas

Formato simples e legÃ­vel:

```txt
FOCACCIA DO ANDRE
CATEGORIA: MASSAS
FAVORITA: SIM
TOTAL: 700.3

[INGREDIENTES]

AGUA|293.0|g
ACUCAR|8.0|g
AZEITE|20.0|g
FARINHA DE TRIGO|366.0|g
FERMENTO|3.3|g
SAL|10.0|g
```

Receitas compostas usam blocos `[PREPARO]`.

## Compartilhamento offline

O Mise_Deck gera um QR Code para compartilhamento offline:

```text
Receita > AÃ§Ãµes > Compartilhar
```

O QR nÃ£o precisa da rede Wi-Fi da casa. Ele ajuda o celular a conectar diretamente no modo de compartilhamento do Cardputer e abrir uma pÃ¡gina local da receita com opÃ§Ãµes de copiar e baixar.

## CompilaÃ§Ã£o

Recomendado: PlatformIO.

```bash
pio run
pio run -t upload
```

Validado com:

- PlatformIO
- M5Cardputer `1.1.1`
- M5Unified `0.2.17`
- M5GFX `0.2.24`
- Arduino framework para ESP32

Veja [docs/INSTALL.md](docs/INSTALL.md) para instruÃ§Ãµes de gravaÃ§Ã£o.

## BinÃ¡rios da release

- InglÃªs: `releases/v1.5.0/Mise_Deck_Cardputer_v1.5.0_EN.bin`
- PortuguÃªs/Brasil: `releases/v1.5.0/Mise_Deck_Cardputer_v1.5.0_PT-BR.bin`

## DocumentaÃ§Ã£o

- [InstalaÃ§Ã£o](docs/INSTALL.md)
- [Funcionalidades](docs/FEATURES.md)
- [Portal](docs/PORTAL.md)
- [Roadmap](docs/ROADMAP.md)
- [Checklist de release](docs/RELEASE_CHECKLIST.md)
- [README em inglÃªs](README.md)

## LicenÃ§a

Mise_Deck Ã© distribuÃ­do sob a [licenÃ§a MIT](LICENSE).


