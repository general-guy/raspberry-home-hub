# NODE REGISTRY
# Raspberry Home Hub Ecosystem

Versão: 0.1  
Status: Draft

---

# Objetivo

O Node Registry é responsável por:

- rastrear presença distribuída
- monitorar disponibilidade operacional
- manter lifecycle dos nós
- armazenar capabilities
- manter metadata operacional
- detectar degradação de conectividade
- fornecer visão global do ecossistema

O Registry NÃO é responsável por:

- derivação de estado físico
- FSM local
- automações
- interpretação elétrica
- execução física de comandos

Referências:

- ARCHITECTURE.md
- raspberry-hub__runtime.md
- shared-contracts__events.md
- shared-contracts__intents.md

---

# Filosofia do Registry

O Registry representa:

- presença operacional
- conectividade distribuída
- estado de comunicação
- metadata dos nós

O Registry NÃO representa:

- realidade física do hardware
- estado elétrico
- estado da FSM física
- confirmação de execução física

---

# Separação Fundamental

## Registry State

Representa:

```text
"o nó está operacionalmente acessível"
````

---

## Physical State

Representa:

```text id="6j4q8l"
"o hardware realmente está em determinado estado físico"
```

---

# Fluxo Correto

```text id="vq0p2f"
ESP32 publica heartbeat
↓
Registry atualiza presença
↓
Hub atualiza lifecycle operacional
↓
Automações podem reagir
```

---

# Fluxo Incorreto

```text id="7kl7wr"
Node ONLINE
↓
Hardware presumido como RUNNING
```

---

# Responsabilidade do Registry

O Registry é responsável por:

* node discovery
* lifecycle tracking
* availability tracking
* heartbeat monitoring
* capabilities registry
* metadata operacional
* observabilidade distribuída

---

# Estrutura Base de Registro

```json id="w6a0ez"
{
  "nodeId": "pc-gamer",
  "status": "ONLINE",
  "lastSeen": 1747000000,
  "capabilities": [
    "power-control",
    "telemetry"
  ],
  "version": 1
}
```

---

# Campos Obrigatórios

| Campo    | Descrição                 |
| -------- | ------------------------- |
| nodeId   | Identificador único do nó |
| status   | Estado operacional do nó  |
| lastSeen | Último heartbeat válido   |
| version  | Versão do registro        |

---

# Node IDs

Os IDs devem:

* ser únicos
* ser persistentes
* usar lowercase kebab-case

Exemplos:

```text id="0ckow4"
pc-gamer
pc-server
network-rack
ups-main
```

---

# Estados do Registry

## ONLINE

Representa:

* heartbeat saudável
* comunicação operacional
* presença confirmada

Critérios típicos:

```text id="c7j7b8"
heartbeat dentro da janela válida
```

---

## STALE

Representa:

* heartbeat atrasado
* comunicação potencialmente degradada
* presença incerta

Critérios típicos:

```text id="e7s9y1"
heartbeat atrasado além do limite saudável
```

---

## OFFLINE

Representa:

* ausência de comunicação
* timeout operacional
* nó indisponível

Critérios típicos:

```text id="2xw4gl"
nenhum heartbeat recebido
```

---

## DEGRADED

Representa:

* comportamento operacional inconsistente
* conectividade instável
* falhas parciais

Exemplos:

* reconnects excessivos
* heartbeat irregular
* eventos inconsistentes
* latência excessiva

---

# Heartbeats

## Objetivo

Heartbeats existem para:

* confirmar presença operacional
* medir disponibilidade
* detectar falhas
* atualizar lifecycle do nó

---

# Estrutura Recomendada

```json id="g6v4gc"
{
  "eventType": "heartbeat",
  "nodeId": "pc-gamer",
  "timestamp": 1747000000,
  "uptimeMs": 120000,
  "version": 1
}
```

---

# Regras de Heartbeat

Heartbeats devem ser:

* periódicos
* leves
* determinísticos
* independentes de automações

---

# O heartbeat NÃO implica:

* FSM RUNNING
* hardware saudável
* sucesso de intents
* estado físico específico

---

# Timeout Operacional

## Objetivo

Detectar:

* perda de conectividade
* falha do nó
* degradação operacional

---

# Exemplo Conceitual

```text id="4hwbri"
Heartbeat recebido
↓
Tempo excedido
↓
STALE
↓
Timeout prolongado
↓
OFFLINE
```

---

# Capabilities

Capabilities representam:

* funcionalidades disponíveis
* features suportadas
* recursos expostos pelo nó

---

# Exemplos

```json id="j3b1xo"
{
  "capabilities": [
    "power-control",
    "telemetry",
    "temperature-monitoring"
  ]
}
```

---

# Capabilities NÃO representam:

* estado operacional
* autorização
* disponibilidade física
* estado da FSM

---

# Metadata Operacional

O Registry pode manter:

* firmwareVersion
* protocolVersion
* ipAddress
* lastSeen
* uptime
* reconnectCount

---

# Exemplo Completo

```json id="y1fdw8"
{
  "nodeId": "pc-gamer",
  "status": "ONLINE",
  "lastSeen": 1747000000,
  "firmwareVersion": "1.0.0",
  "protocolVersion": 1,
  "uptimeMs": 120000,
  "reconnectCount": 2,
  "capabilities": [
    "power-control",
    "telemetry"
  ],
  "version": 1
}
```

---

# Descoberta de Nós

## Modelo Recomendado

A descoberta deve ocorrer através de:

* heartbeat
* retained topics
* eventos operacionais
* registro dinâmico

---

# O Registry NÃO deve:

* depender de configuração manual rígida
* assumir presença permanente
* assumir disponibilidade infinita

---

# Persistência

O Hub pode persistir:

* metadata dos nós
* histórico operacional
* availability timelines
* reconnect history

---

# O Hub NÃO deve persistir:

* estado físico presumido
* causalidade inferida
* estados artificiais

---

# Relação com a FSM Física

A FSM física continua pertencendo ao ESP32.

O Registry apenas acompanha:

* disponibilidade operacional
* presença distribuída
* conectividade

---

# Relação com Eventos

O Registry reage principalmente a:

* heartbeat
* node_online
* node_offline
* mqtt_connected
* mqtt_disconnected

---

# Relação com Intents

O Registry NÃO confirma:

* sucesso de intents
* execução física
* transições da FSM

O Registry apenas informa:

```text id="ef4h5i"
"o nó aparentemente está acessível"
```

---

# Garantias Arquiteturais

O Registry garante:

* visão distribuída do ecossistema
* rastreamento operacional
* monitoramento de presença
* observabilidade de conectividade

---

# O Registry NÃO garante:

* realidade física
* sincronização global perfeita
* causalidade elétrica
* execução de hardware

---

# Compatibilidade Futura

Os registros devem ser:

* extensíveis
* forward-compatible
* tolerantes a novos campos

Consumidores devem:

* ignorar campos desconhecidos
* validar version
* evitar parsing rígido excessivo

---

# Convenções JSON

## Keys

Devem utilizar:

```text id="8u7l0m"
camelCase
```

---

## Estados

Devem utilizar:

```text id="z7s0g9"
UPPERCASE
```

---

# Lifecycle Operacional

```text id="3h0vmv"
UNKNOWN
↓
ONLINE
↓
STALE
↓
OFFLINE
```

Estados podem retornar para:

```text id="3l8m0a"
ONLINE
```

caso heartbeats válidos sejam restaurados.

---

# Princípio Final

O Node Registry existe para fornecer:

* presença distribuída
* disponibilidade operacional
* observabilidade de conectividade
* visão global do ecossistema

Sem comprometer:

* autonomia física dos ESP32
* causalidade explícita
* ownership da FSM local
* separação entre conectividade e realidade física.

```
```
