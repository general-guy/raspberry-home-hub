````md
# ESP32 Physical State Machine
# esp32-node__fsm.md

Versão: 0.2  
Status: Draft

---

# Visão Geral

A Physical State Machine (FSM) do ESP32 é responsável por derivar o estado físico real do hardware monitorado.

A FSM opera exclusivamente através de:

- sinais físicos observados
- interpretação temporal estabilizada
- feedback elétrico confirmado

A FSM representa a autoridade local sobre a realidade física do nó.

Referências:

- ARCHITECTURE.md

---

# Objetivo

A FSM existe para:

- derivar estado físico confiável
- validar transições físicas
- manter causalidade explícita
- proteger contra estados presumidos
- fornecer observabilidade física determinística

---

# Escopo da FSM

A FSM é responsável por:

- derivação de estado físico
- rastreamento temporal
- validação de transições
- detecção de timeout
- observabilidade local

A FSM NÃO é responsável por:

- automações distribuídas
- persistência global
- APIs
- MQTT
- dashboards
- orquestração externa

---

# Fluxo Operacional

```text
GPIO
↓
IO Layer
↓
Interpretation Layer
↓
FSM Física
↓
Estado Derivado
↓
Eventos
````

---

# Dependências

## Interpretation Layer

Responsável por:

* debounce temporal
* estabilidade lógica
* tracking temporal
* interpretação dos sinais físicos

A FSM opera apenas sobre sinais já estabilizados.

---

# Sinais Utilizados

## POWER_OK

Indica:

* confirmação lógica de power state
* feedback físico da motherboard

---

## SENSE_12V

Indica:

* presença de alimentação principal
* atividade elétrica do sistema

---

## SYS_FAN_PWM

Atualmente não utilizado pela FSM.

Reservado para:

* telemetria futura
* inferência operacional
* análise térmica

---

# Estados da FSM

## OFF

Representa sistema fisicamente desligado.

Características:

* POWER_OK inativo
* SENSE_12V inativo

---

## STARTING

Representa sistema em transição de boot.

Características:

* atividade física parcial
* sinais ainda não estabilizados
* boot não confirmado

---

## RUNNING

Representa sistema operacionalmente ativo.

Características:

* POWER_OK ativo
* SENSE_12V ativo
* atividade estabilizada

---

# Diagrama de Estados

```text
OFF
 │
 ▼
STARTING
 │
 ▼
RUNNING
```

Transições reversas:

```text
RUNNING → STARTING
RUNNING → OFF
STARTING → OFF
```

---

# Transições

## OFF → STARTING

Ocorre quando sinais físicos indicam início de energização.

Exemplos:

* POWER_OK ativou
* SENSE_12V ativou

---

## STARTING → RUNNING

Ocorre quando:

* sinais físicos estabilizam
* boot é confirmado fisicamente

Condições típicas:

* POWER_OK ativo
* SENSE_12V ativo
* estabilidade temporal válida

---

## RUNNING → STARTING

Ocorre quando:

* sinais tornam-se instáveis
* shutdown ou reboot foi detectado

---

## RUNNING → OFF

Ocorre quando:

* atividade física desaparece completamente

Condições típicas:

* POWER_OK inativo
* SENSE_12V inativo

---

## STARTING → OFF

Ocorre quando:

* boot falha
* timeout é atingido
* atividade desaparece antes da estabilização

---

# Timeout de Inicialização

## STARTING Timeout

Objetivo:

* impedir estados intermediários indefinidos
* evitar FSM presa em STARTING

Valor atual:

```text
15 segundos
```

Comportamento:

```text
STARTING
↓
Timeout atingido
↓
OFF
```

---

# Temporalidade

Cada estado mantém:

* timestamp de entrada
* duração acumulada
* tempo desde última transição

---

# Tracking de Estado

A FSM mantém:

* estado atual
* estado anterior
* timestamp da transição
* duração do estado atual

---

# Observabilidade

A FSM expõe:

* estado atual
* transições
* duração do estado
* timeout events
* causalidade temporal

---

# Integração Externa

A FSM permanece:

* determinística
* desacoplada de rede
* independente de automações
* independente do Hub

Publicações MQTT e integrações externas devem ocorrer através de camadas externas de integração.

---

# Garantias da FSM

A FSM garante:

* causalidade explícita
* autonomia física local
* determinismo observável
* independência de rede
* separação entre física e orquestração

---

# Objetivo Final

A FSM existe para garantir que o ecossistema distribuído opere baseado em:

* sinais físicos observáveis
* transições confirmadas
* feedback explícito
* causalidade rastreável

E nunca baseado apenas em:

* comandos emitidos
* requests externos
* estados presumidos
* inferência implícita de sucesso

```
```
