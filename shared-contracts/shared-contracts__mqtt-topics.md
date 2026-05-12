# MQTT TOPICS CONTRACTS
# Raspberry Home Hub Ecosystem

Versão: 0.2
Status: Draft

---

# Objetivo

Este documento define:

- namespace MQTT oficial do ecossistema
- semântica dos tópicos
- organização hierárquica
- convenções de publish/subscribe
- regras de retenção
- QoS recomendado
- separação entre intents, eventos, estado e telemetria
- contratos de interoperabilidade distribuída

Este documento NÃO define:

- payloads específicos
- FSM física
- automações
- arquitetura interna do runtime
- implementação do broker

Referências:

- ARCHITECTURE.md
- shared-contracts__events.md
- shared-contracts__intents.md
- esp32-node__fsm.md
- raspberry-hub__runtime.md
- raspberry-hub__node-registry.md

---

# Filosofia Arquitetural

A arquitetura MQTT foi projetada para preservar:

- causalidade explícita
- observabilidade distribuída
- separação entre intenção e realidade física
- desacoplamento entre runtimes
- autonomia física dos ESP32

O sistema evita:

- inferência implícita de estado
- RPC disfarçado via MQTT
- acoplamento oculto
- ambiguidades semânticas
- automações baseadas apenas em comandos emitidos

---

# Princípio Fundamental

MQTT é utilizado como:

```text
event transport layer
````

E NÃO como:

```text
remote procedure call system
```

---

# Modelo Conceitual

## Intent

Representa:

```text
"algo deve ser tentado"
```

---

## Event

Representa:

```text
"algo observável aconteceu"
```

---

## State

Representa:

```text
"visão materializada atual"
```

---

## Telemetry

Representa:

```text
"stream operacional contínuo"
```

---

# Namespace Oficial

Todos os tópicos seguem:

```text
rhh/<node-id>/<category>/<resource>
```

Onde:

| Segmento | Objetivo                        |
| -------- | ------------------------------- |
| rhh      | namespace global do ecossistema |
| node-id  | identificador do nó             |
| category | categoria semântica             |
| resource | recurso específico              |

---

# Convenções Gerais

## Node IDs

Devem:

* ser únicos
* ser persistentes
* usar lowercase kebab-case

Exemplos:

```text
pc-gamer
pc-server
network-rack
ups-main
```

---

## Categorias

Categorias devem utilizar:

```text
lowercase-kebab-case
```

---

## Recursos

Resources devem utilizar:

```text
snake_case
```

---

# Categorias MQTT Oficiais

| Categoria     | Objetivo                 |
| ------------- | ------------------------ |
| intents       | pedidos distribuídos     |
| events        | fatos observáveis        |
| state         | snapshots materializados |
| telemetry     | stream operacional       |
| heartbeat     | presença operacional     |
| registry      | metadata operacional     |
| observability | logs e diagnósticos      |
| system        | eventos internos         |
| capabilities  | features do nó           |

---

# Estrutura de Topics

## Intents

Publicação de intents distribuídas.

Formato:

```text
rhh/<node-id>/intents/<intent_type>
```

Exemplos:

```text
rhh/pc-gamer/intents/request_power_on
rhh/pc-gamer/intents/request_power_off
rhh/pc-server/intents/request_restart
```

---

## Events

Publicação de eventos observáveis.

Formato:

```text
rhh/<node-id>/events/<event_type>
```

Exemplos:

```text
rhh/pc-gamer/events/physical_state_transition
rhh/pc-gamer/events/signal_transition
rhh/pc-gamer/events/command_accepted
rhh/pc-gamer/events/timeout
```

---

## State

Snapshots materializados do estado atual.

Formato:

```text
rhh/<node-id>/state/<state_type>
```

Exemplos:

```text
rhh/pc-gamer/state/physical_state
rhh/pc-gamer/state/runtime_state
rhh/pc-gamer/state/signals
```

---

## Telemetry

Streams contínuos de dados operacionais.

Formato:

```text
rhh/<node-id>/telemetry/<metric>
```

Exemplos:

```text
rhh/pc-gamer/telemetry/temperature
rhh/pc-gamer/telemetry/uptime
rhh/pc-gamer/telemetry/wifi_rssi
```

---

## Heartbeat

Presença operacional.

Formato:

```text
rhh/<node-id>/heartbeat
```

Exemplos:

```text
rhh/pc-gamer/heartbeat
rhh/network-rack/heartbeat
```

---

## Registry

Metadata operacional agregada.

Formato:

```text
rhh/<node-id>/registry/<resource>
```

Exemplos:

```text
rhh/pc-gamer/registry/status
rhh/pc-gamer/registry/capabilities
```

---

## Observability

Eventos diagnósticos e logs estruturados.

Formato:

```text
rhh/<node-id>/observability/<event>
```

Exemplos:

```text
rhh/pc-gamer/observability/error
rhh/pc-gamer/observability/warning
rhh/pc-gamer/observability/recovery
```

---

# Ownership dos Topics

## ESP32 Publica

Os ESP32 devem publicar:

* events
* state
* telemetry
* heartbeat
* observability

---

## ESP32 Consome

Os ESP32 devem consumir:

* intents

---

## Raspberry Hub Publica

O Hub pode publicar:

* intents
* automações derivadas
* agregações distribuídas
* registry
* system

---

## Raspberry Hub Consome

O Hub deve consumir:

* events
* telemetry
* state
* heartbeat
* observability

---

# Separação Semântica Obrigatória

## Events NÃO são State

Eventos representam:

```text
fatos históricos
```

State representa:

```text
visão atual materializada
```

---

## Intents NÃO são Events

Intents representam:

```text
pedidos
```

Events representam:

```text
confirmações observáveis
```

---

## Telemetry NÃO é Event

Telemetry representa:

```text
stream contínuo operacional
```

E NÃO causalidade semântica.

---

# Estratégia de Retained Messages

## Regra Fundamental

Retained messages devem representar:

```text
estado materializado atual
```

E NÃO:

```text
histórico causal
```

---

# Topics que DEVEM ser Retained

## State

```text
rhh/<node-id>/state/*
```

Motivo:

* snapshot atual
* recovery rápido
* sincronização imediata

---

## Registry

```text
rhh/<node-id>/registry/*
```

Motivo:

* metadata operacional
* capabilities
* lifecycle atual

---

# Topics que NÃO DEVEM ser Retained

## Events

```text
rhh/<node-id>/events/*
```

Eventos são históricos e append-only.

Retained causaria:

* replay artificial
* falsa causalidade
* automações incorretas

---

## Intents

```text
rhh/<node-id>/intents/*
```

Evita:

* reexecução acidental
* duplicidade operacional
* efeitos perigosos após reconnect

---

## Heartbeat

```text
rhh/<node-id>/heartbeat
```

Heartbeat retained cria:

* presença falsa
* lifecycle inconsistente

---

## Observability

```text
rhh/<node-id>/observability/*
```

Logs NÃO representam estado atual.

---

# Estratégia de QoS

## QoS 0

Usar para:

* telemetry de alta frequência
* métricas não críticas

Exemplos:

```text
telemetry/temperature
telemetry/wifi_rssi
```

---

## QoS 1

Usar para:

* intents
* state
* heartbeat
* eventos importantes

Exemplos:

```text
events/physical_state_transition
intents/request_power_on
heartbeat
```

---

## QoS 2

Evitar inicialmente.

Motivos:

* complexidade operacional
* overhead
* benefício limitado no cenário atual

---

# Snapshot Philosophy

## Objetivo

State topics existem para:

* recovery operacional
* sincronização rápida
* materialização de estado atual
* bootstrap de novos consumidores

---

# Exemplo de Snapshot

Topic:

```text
rhh/pc-gamer/state/physical_state
```

Payload:

```json
{
  "state": "RUNNING",
  "since": 1747000000,
  "version": 1
}
```

---

# Eventos Continuam Sendo Source of Truth

State snapshots são derivados de:

* eventos
* FSM
* timelines

Snapshots NÃO substituem:

* causalidade histórica
* eventos originais

---

# Wildcards Recomendados

## Todos os eventos

```text
rhh/+/events/#
```

---

## Todos os heartbeats

```text
rhh/+/heartbeat
```

---

## Todos os estados físicos

```text
rhh/+/state/physical_state
```

---

## Toda telemetria

```text
rhh/+/telemetry/#
```

---

# Tópicos Reservados

## Sistema

```text
rhh/system/*
```

Uso reservado para:

* manutenção global
* eventos internos do hub
* operações administrativas

---

## Broadcast

```text
rhh/broadcast/*
```

Uso opcional e altamente restrito.

Evitar:

* causalidade ambígua
* fanout excessivo
* acoplamento implícito

---

# Ordem e Temporalidade

MQTT NÃO garante:

* ordenação global
* causalidade distribuída perfeita
* sincronização absoluta

Cada nó deve manter:

* monotonicidade local
* timestamps explícitos
* causalidade rastreável

---

# Segurança Semântica

## Commands ≠ Success

Publicar:

```text
request_power_on
```

NÃO implica:

```text
RUNNING
```

A confirmação correta ocorre através de:

```text
events/physical_state_transition
```

---

# Compatibilidade Futura

O namespace deve ser:

* extensível
* forward-compatible
* semanticamente estável

Consumidores devem:

* ignorar tópicos desconhecidos
* tolerar novos resources
* evitar parsing rígido excessivo

---

# Convenções de Evolução

Evitar:

* breaking changes em topics existentes
* renomeação frequente
* overload semântico
* múltiplos significados para o mesmo tópico

Preferir:

* novos resources
* novas categorias
* versionamento explícito

---

# Anti-Patterns Proibidos

## RPC via MQTT

Evitar:

```text
request
↓
reply
↓
estado presumido
```

---

## Estado Inferido por Intent

Evitar:

```text
intent publicada
↓
dashboard assume RUNNING
```

---

## Topics Ambíguos

Evitar:

```text
status
data
message
event
```

Sem contexto semântico claro.

---

# Estratégia Operacional

## ESP32

Permanece:

* autoridade física
* owner da FSM
* responsável por causalidade elétrica

---

## Raspberry Hub

Permanece:

* orchestrator distribuído
* agregador
* runtime de automações
* camada de persistência

---

# Princípio Final

O namespace MQTT existe para transportar:

* intents explícitas
* eventos observáveis
* snapshots materializados
* telemetria operacional

Sem comprometer:

* causalidade rastreável
* autonomia física dos ESP32
* separação arquitetural
* determinismo observável
* robustez distribuída

O ecossistema deve sempre reagir:

* a eventos confirmados
* a estados materializados válidos
* e nunca apenas à emissão de intents.

```
```
