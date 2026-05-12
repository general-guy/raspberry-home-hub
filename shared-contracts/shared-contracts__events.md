# EVENTS CONTRACTS
# Raspberry Home Hub Ecosystem

Versão: 0.1  
Status: Draft

---

# Objetivo

Este documento define:

- semântica dos eventos distribuídos
- estrutura dos payloads
- correlação causal
- regras de observabilidade
- contratos de eventos MQTT

Este documento NÃO define:

- tópicos MQTT
- arquitetura geral
- FSM física
- automações
- runtime interno

Referências:

- ARCHITECTURE.md
- shared-contracts__mqtt-topics.md
- esp32-node__fsm.md

---

# Filosofia dos Eventos

Eventos representam:

- fatos observáveis
- transições confirmadas
- ocorrências causais registradas

Eventos NÃO representam:

- intenções
- comandos
- suposições
- previsões de estado

---

# Características Obrigatórias

Todo evento deve ser:

- explícito
- rastreável
- timestamped
- semanticamente determinístico
- serializável
- observável

---

# Estrutura Base de Evento

Todos os eventos devem seguir:

```json
{
  "eventId": "evt-8f3a2b91",
  "eventType": "physical_state_transition",
  "nodeId": "pc-gamer",
  "timestamp": 1747000000,
  "version": 1
}
````

---

# Campos Obrigatórios

| Campo     | Descrição                |
| --------- | ------------------------ |
| eventId   | ID único do evento       |
| eventType | Tipo semântico do evento |
| nodeId    | Nó originador            |
| timestamp | Unix timestamp UTC       |
| version   | Versão do payload        |

---

# Convenções Gerais

## eventId

Deve ser:

* único
* imutável
* rastreável

Formato recomendado:

```text
evt-xxxxxxxx
```

---

## timestamp

Deve utilizar:

```text
Unix Epoch UTC
```

Exemplo:

```json
{
  "timestamp": 1747000000
}
```

---

## version

Versionamento do payload do evento.

Exemplo:

```json
{
  "version": 1
}
```

---

# Categorias de Eventos

## Physical Events

Eventos derivados da realidade física observada.

Exemplos:

* signal_transition
* physical_state_transition
* power_button_pressed

---

## Runtime Events

Eventos internos do runtime distribuído.

Exemplos:

* heartbeat
* node_online
* node_offline
* mqtt_connected

---

## Command Events

Eventos relacionados à execução física de intents.

Exemplos:

* command_accepted
* command_rejected
* command_execution_started
* command_execution_finished

---

## Observability Events

Eventos diagnósticos.

Exemplos:

* warning
* error
* timeout
* recovery

---

# Eventos Fundamentais

## heartbeat

Representa presença operacional do nó.

```json
{
  "eventId": "evt-001",
  "eventType": "heartbeat",
  "nodeId": "pc-gamer",
  "timestamp": 1747000000,
  "version": 1,
  "uptimeMs": 120000
}
```

---

## physical_state_transition

Representa mudança confirmada de estado físico.

```json
{
  "eventId": "evt-002",
  "eventType": "physical_state_transition",
  "nodeId": "pc-gamer",
  "timestamp": 1747000001,
  "version": 1,
  "from": "OFF",
  "to": "STARTING"
}
```

---

## signal_transition

Representa transição de sinal interpretado.

```json
{
  "eventId": "evt-003",
  "eventType": "signal_transition",
  "nodeId": "pc-gamer",
  "timestamp": 1747000002,
  "version": 1,
  "signal": "POWER_OK",
  "from": "INACTIVE",
  "to": "ACTIVE"
}
```

---

## command_accepted

Representa aceitação física de execução.

```json
{
  "eventId": "evt-004",
  "eventType": "command_accepted",
  "nodeId": "pc-gamer",
  "timestamp": 1747000003,
  "version": 1,
  "intentId": "intent-991",
  "command": "REQUEST_POWER_ON"
}
```

---

## command_rejected

Representa rejeição física de execução.

```json
{
  "eventId": "evt-005",
  "eventType": "command_rejected",
  "nodeId": "pc-gamer",
  "timestamp": 1747000004,
  "version": 1,
  "intentId": "intent-991",
  "reason": "COOLDOWN_ACTIVE"
}
```

---

## timeout

Representa timeout causal relevante.

```json
{
  "eventId": "evt-006",
  "eventType": "timeout",
  "nodeId": "pc-gamer",
  "timestamp": 1747000005,
  "version": 1,
  "timeoutType": "STARTING_TIMEOUT",
  "durationMs": 15000
}
```

---

# Correlação Causal

Eventos podem possuir:

| Campo         | Objetivo                      |
| ------------- | ----------------------------- |
| intentId      | Relacionar automações/intents |
| correlationId | Relacionar múltiplos eventos  |
| causationId   | Relacionar evento originador  |

---

# intentId

Usado quando um evento é consequência de uma intent distribuída.

Exemplo:

```json
{
  "intentId": "intent-991"
}
```

---

# correlationId

Usado para rastrear múltiplos eventos relacionados.

Exemplo:

```json
{
  "correlationId": "corr-441"
}
```

---

# causationId

Representa qual evento originou outro evento.

Exemplo:

```json
{
  "causationId": "evt-002"
}
```

---

# Imutabilidade

Eventos são:

* append-only
* imutáveis
* históricos

Eventos NÃO devem:

* ser editados
* ser sobrescritos
* ser reutilizados

---

# Garantias Semânticas

## Eventos NÃO implicam:

* intenção futura
* persistência permanente
* disponibilidade do nó
* sincronização global

---

## Eventos implicam:

* ocorrência observada
* registro causal
* fato distribuído

---

# Ordem dos Eventos

O sistema NÃO garante:

* ordenação global absoluta
* sincronização perfeita entre nós

Cada nó é responsável por:

* ordenação local
* monotonicidade temporal local

---

# Persistência

O Raspberry Hub pode:

* persistir eventos
* agregar timelines
* reconstruir estado derivado

Mas NÃO deve:

* alterar payloads históricos
* reescrever causalidade
* modificar eventos originados pelos nós

---

# Compatibilidade Futura

Os payloads devem ser:

* forward-compatible
* extensíveis
* tolerantes a campos adicionais

Consumidores devem:

* ignorar campos desconhecidos
* validar version
* evitar parsing rígido excessivo

---

# Convenções JSON

## Keys

Devem utilizar:

```text
camelCase
```

---

## Estados

Devem utilizar:

```text
UPPERCASE
```

---

## Event Types

Devem utilizar:

```text
snake_case
```

---

# Event Types Reservados

```text
heartbeat
signal_transition
physical_state_transition
command_accepted
command_rejected
command_execution_started
command_execution_finished
timeout
warning
error
recovery
node_online
node_offline
mqtt_connected
mqtt_disconnected
```

---

# Princípio Final

Eventos representam:

* realidade observada
* causalidade explícita
* fatos distribuídos

O ecossistema deve sempre reagir:

* a eventos confirmados
* e NÃO a suposições derivadas apenas da emissão de comandos.

```
```
