# Intents Contract
# intents.md

Versão: 1.0
Status: Active

---

# Estrutura Base

```json
{
  "intentId": "uuid",
  "intentType": "REQUEST_POWER_ON",
  "targetNode": "pc-gamer",
  "timestamp": 1747000000,
  "source": "raspberry-hub",
  "version": 1
}
Campos Obrigatórios
Campo	Tipo
intentId	string
intentType	string
targetNode	string
timestamp	number
source	string
version	number
Intent Types
REQUEST_POWER_ON
REQUEST_POWER_OFF
REQUEST_RESTART
REQUEST_FORCE_POWER_OFF
REQUEST_STATUS_REFRESH
REQUEST_HEARTBEAT
REQUEST_POWER_ON

Topic:

rhh/<node-id>/intents/request_power_on

Payload:

{
  "intentId": "uuid",
  "intentType": "REQUEST_POWER_ON",
  "targetNode": "pc-gamer",
  "timestamp": 1747000000,
  "source": "raspberry-hub",
  "version": 1
}
REQUEST_POWER_OFF

Topic:

rhh/<node-id>/intents/request_power_off

Payload:

{
  "intentId": "uuid",
  "intentType": "REQUEST_POWER_OFF",
  "targetNode": "pc-gamer",
  "timestamp": 1747000000,
  "source": "raspberry-hub",
  "version": 1
}
REQUEST_RESTART

Topic:

rhh/<node-id>/intents/request_restart

Payload:

{
  "intentId": "uuid",
  "intentType": "REQUEST_RESTART",
  "targetNode": "pc-gamer",
  "timestamp": 1747000000,
  "source": "raspberry-hub",
  "version": 1
}
Regras
Intents representam
tentativas operacionais
Intents nunca representam
sucesso confirmado
Fluxo Correto
Intent
↓
Execução física
↓
FSM detecta
↓
Evento publicado
Fluxo Proibido
Intent publicada
↓
Estado presumido
Convenções
intentType

Formato:

UPPERCASE_SNAKE_CASE
JSON Keys

Formato:

camelCase