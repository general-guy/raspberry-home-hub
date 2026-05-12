````md
# ARCHITECTURE
# Raspberry Home Hub Ecosystem

Versão: 0.2  
Status: Draft

---

# Visão Geral

O Raspberry Home Hub é um ecossistema distribuído de automação e supervisão doméstica baseado em:

- ESP32
- Raspberry Pi
- MQTT
- observabilidade orientada por eventos
- interpretação física determinística

A arquitetura foi projetada para:

- preservar causalidade explícita
- evitar inferência implícita de estado
- separar física de orquestração
- manter observabilidade distribuída
- garantir autonomia operacional dos nós físicos

---

# Arquitetura Geral

```text
[ APIs / UI / Automations ]
↓
Raspberry Home Hub
↓
MQTT Broker
↓
ESP32 Nodes
↓
Physical Hardware Layer
````

---

# Filosofia Arquitetural

## Feedback-Driven

O ecossistema opera baseado em:

* feedback físico observável
* eventos confirmados
* transições verificáveis

E NÃO apenas em:

* emissão de comandos
* requests externos
* estados presumidos

---

## Command ≠ Success

Comandos representam:

```text
tentativas operacionais
```

E NÃO:

```text
confirmação física
```

Toda confirmação deve ocorrer através de:

* sinais físicos
* FSM local
* eventos observáveis
* telemetria válida

---

## Event-Driven Architecture

Automações devem reagir a:

* eventos confirmados
* estados materializados
* transições observáveis

E NÃO a:

* intents isoladas
* RPC implícito
* estados presumidos

---

## Physical-State Authority

A autoridade sobre estado físico pertence ao ESP32 responsável pelo hardware.

O Raspberry Hub:

* supervisiona
* agrega
* automatiza
* correlaciona

Mas NÃO deve:

* inferir física sem feedback
* sobrescrever FSM local
* assumir sucesso de transições

---

# Modelo Conceitual

## Intent

Representa:

```text
"algo deve ser tentado"
```

Intents NÃO representam:

* sucesso confirmado
* execução garantida
* mudança física concluída

---

## Event

Representa:

```text
"algo observável aconteceu"
```

Eventos representam:

* fatos históricos
* causalidade registrada
* transições confirmadas

---

## State

Representa:

```text
"visão materializada atual"
```

State é derivado de:

* FSM
* eventos
* timelines
* agregação distribuída

---

## Telemetry

Representa:

```text
stream operacional contínuo
```

Telemetry NÃO representa:

* causalidade semântica
* transições confirmadas
* eventos históricos

---

# Fluxo Operacional Correto

```text
Intent
↓
ESP32 valida execução
↓
Command Layer executa
↓
Sinais físicos mudam
↓
FSM deriva estado
↓
Evento publicado
↓
Hub agrega
↓
Automações reagem
```

---

# Fluxo Incorreto

```text
Intent enviada
↓
Estado presumido
↓
Automação executa imediatamente
```

---

# Separação de Responsabilidades

# ESP32 Nodes

Os ESP32 representam:

* runtime físico embarcado
* autoridade local de hardware
* interpretação temporal determinística

Responsáveis por:

* GPIO
* aquisição de sinais físicos
* debounce
* interpretação temporal
* FSM física local
* execução física de comandos
* observabilidade local

Os ESP32:

* derivam realidade física
* executam hardware
* operam autonomamente

Mesmo sem:

* Raspberry Hub
* MQTT
* Wi-Fi
* internet

---

# Raspberry Home Hub

O Raspberry Hub representa:

* orchestrator distribuído
* agregador de estado
* supervisor operacional
* runtime de automações

Responsável por:

* automações
* persistência
* agregação distribuída
* APIs
* observabilidade global
* telemetria centralizada
* coordenação do ecossistema

O Hub NÃO deve:

* interpretar GPIO diretamente
* substituir FSM local
* inferir causalidade sem eventos
* assumir sucesso de boot
* atuar como driver físico

---

# Runtime do Hub

## MQTT Integration Layer

Responsável por:

* subscribe de eventos
* publish de intents
* roteamento distribuído
* integração com broker MQTT

MQTT é utilizado como:

```text
event transport layer
```

E NÃO como:

```text
remote procedure call system
```

---

## Event Aggregation Layer

Responsável por:

* agregação de eventos
* timelines causais
* reconstrução de estado
* visão global do ecossistema

---

## Persistence Layer

Responsável por:

* persistência de eventos
* snapshots
* logs estruturados
* recovery operacional

---

## Automation Engine

Responsável por:

* automações distribuídas
* schedules
* regras operacionais
* intents automatizadas

As automações devem reagir apenas a:

* eventos confirmados
* estados válidos
* causalidade observável

---

## API Layer

Responsável por:

* APIs REST
* WebSocket
* dashboards
* integrações externas

A API NÃO deve:

* assumir causalidade física
* substituir eventos reais
* inferir estado sem feedback

---

# Node Registry

O Registry representa:

* presença operacional
* disponibilidade distribuída
* lifecycle dos nós
* metadata operacional

O Registry NÃO representa:

* realidade física
* estado elétrico
* confirmação física

---

# Estados do Registry

## ONLINE

Heartbeat saudável e comunicação operacional.

---

## STALE

Heartbeat atrasado e presença incerta.

---

## OFFLINE

Nó indisponível ou sem comunicação válida.

---

## DEGRADED

Comportamento operacional inconsistente.

Exemplos:

* reconnects excessivos
* heartbeat irregular
* latência excessiva

---

# Heartbeats

Heartbeats existem para:

* confirmar presença operacional
* detectar falhas
* atualizar lifecycle do nó

Heartbeat NÃO implica:

* FSM RUNNING
* hardware saudável
* sucesso de intents

---

# Ownership de Estado

## ESP32 é owner de:

* sinais físicos
* debounce
* interpretação temporal
* FSM física
* execução física
* derivação de estado físico

---

## Raspberry Hub é owner de:

* automações
* persistência
* agregação distribuída
* observabilidade global
* APIs
* telemetria centralizada

---

# Modelo MQTT

## Namespace Oficial

Todos os tópicos seguem:

```text
rhh/<node-id>/<category>/<resource>
```

---

# Categorias MQTT

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

# Estrutura dos Topics

## Intents

```text
rhh/<node-id>/intents/<intent_type>
```

Exemplos:

```text
rhh/pc-gamer/intents/request_power_on
rhh/pc-gamer/intents/request_power_off
```

---

## Events

```text
rhh/<node-id>/events/<event_type>
```

Exemplos:

```text
rhh/pc-gamer/events/physical_state_transition
rhh/pc-gamer/events/signal_transition
```

---

## State

```text
rhh/<node-id>/state/<state_type>
```

Exemplos:

```text
rhh/pc-gamer/state/physical_state
rhh/pc-gamer/state/signals
```

---

## Telemetry

```text
rhh/<node-id>/telemetry/<metric>
```

Exemplos:

```text
rhh/pc-gamer/telemetry/temperature
rhh/pc-gamer/telemetry/uptime
```

---

## Heartbeat

```text
rhh/<node-id>/heartbeat
```

---

# Estratégia de Retained Messages

## DEVEM ser retained

```text
state/*
registry/*
```

Pois representam:

* snapshot atual
* materialização de estado
* recovery rápido

---

## NÃO DEVEM ser retained

```text
events/*
intents/*
heartbeat
observability/*
```

Para evitar:

* replay artificial
* causalidade falsa
* reexecução acidental

---

# Estratégia de QoS

## QoS 0

Usar para:

* telemetria de alta frequência
* métricas não críticas

---

## QoS 1

Usar para:

* intents
* eventos importantes
* state
* heartbeat

---

## QoS 2

Evitar inicialmente.

Motivos:

* overhead
* complexidade operacional
* benefício limitado

---

# Eventos

Eventos representam:

* fatos observáveis
* transições confirmadas
* causalidade explícita

Eventos NÃO representam:

* intenção futura
* previsão de estado
* sucesso presumido

---

# Estrutura Base de Evento

```json
{
  "eventId": "evt-001",
  "eventType": "physical_state_transition",
  "nodeId": "pc-gamer",
  "timestamp": 1747000000,
  "version": 1
}
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

# Intents

Intents representam:

* pedidos distribuídos
* solicitações operacionais
* intenções de ação

Intents NÃO representam:

* sucesso
* execução garantida
* transição física confirmada

---

# Estrutura Base de Intent

```json
{
  "intentId": "intent-001",
  "intentType": "REQUEST_POWER_ON",
  "targetNode": "pc-gamer",
  "timestamp": 1747000000,
  "version": 1
}
```

---

# Intent Types Reservadas

```text
REQUEST_POWER_ON
REQUEST_POWER_OFF
REQUEST_RESTART
REQUEST_FORCE_POWER_OFF
REQUEST_STATUS_REFRESH
REQUEST_HEARTBEAT
```

---

# Correlação Causal

Eventos e intents podem utilizar:

| Campo         | Objetivo                      |
| ------------- | ----------------------------- |
| intentId      | relacionamento causal         |
| correlationId | rastreamento distribuído      |
| causationId   | encadeamento causal explícito |

---

# Convenções Gerais

## Node IDs

Devem:

* ser únicos
* ser persistentes
* usar lowercase-kebab-case

Exemplos:

```text
pc-gamer
pc-server
network-rack
ups-main
```

---

## Estados

Estados devem utilizar:

```text
UPPERCASE
```

Exemplos:

```text
OFF
STARTING
RUNNING
ERROR
```

---

## Event Types

Devem utilizar:

```text
snake_case
```

---

## JSON Keys

Devem utilizar:

```text
camelCase
```

---

# Logs Estruturados

Evitar:

```text
PC ligou
```

Preferir:

```json
{
  "event": "physical_state_transition",
  "node": "pc-gamer",
  "from": "STARTING",
  "to": "RUNNING",
  "timestamp": 1747000000
}
```

---

# Persistência

O Hub deve conseguir:

* persistir eventos
* reconstruir estado
* recuperar timelines
* restaurar contexto distribuído

Sem depender de:

* memória transitória
* estado implícito
* inferência não persistida

---

# Compatibilidade Futura

Payloads e tópicos devem ser:

* extensíveis
* forward-compatible
* semanticamente estáveis

Consumidores devem:

* ignorar campos desconhecidos
* validar version
* evitar parsing rígido excessivo

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

Sem semântica clara.

---

# Estratégia Operacional

## Desenvolvimento

Executado principalmente em:

* Windows
* VSCode
* Git
* PlatformIO

---

## Runtime Operacional

Executado em:

* Raspberry Pi Zero 2 W

O Raspberry atua como:

* runtime operacional
* deployment target
* infraestrutura persistente

E NÃO como:

* ambiente principal de desenvolvimento
* source of truth do projeto

---

# Estrutura do Repositório

```text
raspberry-home-hub/

├── esp32-node/
├── raspberry-hub/
├── shared-contracts/
├── docs/
└── scripts/
```

---

# Convenção para Arquivos Flat

Como "Fontes do Projeto" utiliza estrutura flat, os arquivos devem preservar contexto estrutural usando:

```text
modulo__arquivo.ext
```

Exemplos:

```text
esp32-node__fsm.md
raspberry-hub__runtime.md
shared-contracts__events.md
```

---

# Estratégia de Evolução

O sistema deve preservar:

* simplicidade
* causalidade explícita
* observabilidade distribuída
* desacoplamento entre runtimes
* determinismo operacional

Evitar:

* automações cegas
* inferência implícita
* acoplamento oculto
* lógica distribuída ambígua
* event buses redundantes
* overengineering prematuro

---

# Princípio Final

O ecossistema deve operar baseado em:

* realidade física observável
* feedback explícito
* transições confirmadas
* causalidade rastreável

Toda automação deve reagir:

* a eventos confirmados
* a estados válidos
* e nunca apenas à emissão de intents.

```
```
