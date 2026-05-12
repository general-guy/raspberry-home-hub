\# Raspberry Hub Runtime

\# raspberry-hub\_\_runtime.md



Versão: 0.1  

Status: Draft



\---



\# Visão Geral



O Raspberry Home Hub representa o runtime central de orquestração distribuída do ecossistema.



O Hub NÃO substitui:



\- interpretação física

\- FSM local

\- controle elétrico embarcado



Essas responsabilidades continuam pertencendo aos nós ESP32.



O Hub atua como:



\- orchestrator

\- supervisor

\- agregador distribuído

\- runtime de automações

\- camada de persistência

\- camada de observabilidade global



\---



\# Objetivo do Runtime



O runtime do Raspberry Hub existe para:



\- agregar eventos distribuídos

\- persistir timelines causais

\- correlacionar estados

\- coordenar automações

\- expor APIs

\- supervisionar o ecossistema

\- centralizar observabilidade



O Hub NÃO existe para:



\- derivar física diretamente

\- interpretar GPIO

\- substituir FSM física

\- assumir sucesso de comandos

\- controlar hardware diretamente



\---



\# Filosofia Fundamental



\## Feedback-Driven



O Hub opera exclusivamente baseado em:



\- eventos observáveis

\- estados confirmados

\- feedback físico publicado pelos ESP32



O Hub NÃO deve assumir:



```text

Intent enviado

↓

Estado presumido

````



O modelo correto é:



```text id="d0w7rn"

Intent enviado

↓

ESP32 executa ação física

↓

Sinais físicos mudam

↓

FSM confirma estado

↓

Evento publicado

↓

Hub reage

```



\---



\# Responsabilidade do Hub



O Raspberry Hub é responsável por:



\* agregação distribuída

\* persistência de eventos

\* automações

\* APIs

\* telemetria global

\* observabilidade centralizada

\* supervisão distribuída

\* coordenação do ecossistema



\---



\# O Que o Hub NÃO Deve Fazer



O Hub NÃO deve:



\* interpretar sinais elétricos brutos

\* sobrescrever FSM física

\* assumir transições físicas

\* assumir sucesso de boot

\* atuar como driver de hardware

\* controlar GPIO diretamente dos PCs

\* inferir causalidade sem feedback explícito



\---



\# Estrutura Geral do Runtime



```text id="9mjlwm"

ESP32 Nodes

↓

MQTT Broker

↓

Node Registry

↓

Event Aggregation

↓

Persistence Layer

↓

Automation Engine

↓

API Layer

↓

UI / Integrations

```



\---



\# Camadas do Runtime



\## MQTT Integration Layer



Responsável por:



\* integração com broker MQTT

\* subscribe de eventos

\* publish de intents

\* roteamento distribuído

\* transporte de mensagens



A camada MQTT NÃO deve:



\* interpretar física

\* automatizar decisões

\* derivar estado físico



\---



\## Node Registry



Responsável por:



\* descoberta de nós

\* tracking de disponibilidade

\* capabilities

\* last\_seen

\* heartbeat tracking



O Registry mantém:



\* presença distribuída

\* lifecycle operacional dos nós



\---



\## Event Aggregation Layer



Responsável por:



\* agregação de eventos

\* correlação causal

\* timelines

\* reconstrução de estado

\* derivação de visão global



A camada de agregação NÃO substitui:



\* FSM física local



\---



\## Persistence Layer



Responsável por:



\* persistência de eventos

\* timelines históricas

\* snapshots de estado

\* logs estruturados

\* recovery operacional



\---



\## Automation Engine



Responsável por:



\* automações distribuídas

\* schedules

\* regras

\* correlação de eventos

\* intents automatizados



As automações devem reagir apenas a:



\* estados confirmados

\* eventos observáveis



\---



\## API Layer



Responsável por:



\* APIs REST

\* WebSocket

\* integração externa

\* dashboards

\* controle remoto



A API NÃO deve:



\* assumir causalidade física

\* substituir eventos reais



\---



\# Modelo de Operação



\## Runtime Event-Driven



O Hub opera como:



```text id="rjlwm1"

event-driven orchestrator

```



E NÃO como:



```text id="jlwmr2"

imperative hardware controller

```



\---



\# Fluxo Operacional



\## Fluxo Correto



```text id="jlwmr3"

Intent

↓

ESP32 executa fisicamente

↓

FSM física confirma

↓

Evento MQTT

↓

Hub agrega

↓

Automação reage

```



\---



\## Fluxo Incorreto



```text id="jlwmr4"

Intent

↓

Hub assume sucesso

↓

Estado derivado artificialmente

```



\---



\# Node Registry



\## Objetivo



O Node Registry mantém:



\* presença distribuída

\* disponibilidade dos nós

\* capabilities

\* rastreamento operacional



\---



\# Estado dos Nós



\## ONLINE



Nó saudável e publicando heartbeats.



\---



\## STALE



Heartbeat atrasado.



Nó potencialmente degradado.



\---



\## OFFLINE



Nó indisponível.



Sem comunicação válida.



\---



\## DEGRADED



Nó operacionalmente instável.



Exemplo:



\* heartbeat irregular

\* eventos inconsistentes

\* falhas parciais



\---



\# Heartbeats



Cada nó ESP32 deve publicar:



\* disponibilidade

\* heartbeat periódico

\* timestamp operacional



O Hub utiliza isso para:



\* detectar presença

\* detectar falhas

\* monitorar saúde operacional



\---



\# Ownership de Estado



\## ESP32 é owner de:



\* sinais físicos

\* debounce

\* interpretação temporal

\* FSM física

\* execução física

\* derivação de estado físico



\---



\## Raspberry Hub é owner de:



\* agregação distribuída

\* persistência

\* automações

\* telemetria global

\* APIs

\* observabilidade centralizada



\---



\# Persistência



O runtime deve persistir:



\* eventos

\* timelines

\* snapshots

\* logs estruturados

\* histórico operacional



\---



\# Logs Estruturados



O Hub deve priorizar logs estruturados.



Evitar:



```text

PC ligou

```



Preferir:



```json id="jlwmr5"

{

&#x20; "event": "physical\_state\_transition",

&#x20; "node": "pc-gamer",

&#x20; "from": "STARTING",

&#x20; "to": "RUNNING",

&#x20; "timestamp": 123456789

}

```



\---



\# Recovery Operacional



O Hub deve conseguir:



\* reiniciar

\* reconstruir estado

\* reprocessar timelines

\* recuperar contexto distribuído



Sem depender de:



\* memória transitória

\* estado implícito

\* inferência temporal não persistida



\---



\# Independência Operacional



O ecossistema deve continuar seguro mesmo se:



\* o Raspberry falhar

\* MQTT cair

\* APIs ficarem indisponíveis



Os ESP32 devem continuar:



\* interpretando física

\* executando FSM local

\* protegendo hardware

\* operando autonomamente



\---



\# Estratégia de Deployment



\## Desenvolvimento



Executado principalmente em:



\* Windows

\* VSCode

\* Git



\---



\## Runtime Operacional



Executado em:



\* Raspberry Pi Zero 2 W



O Raspberry atua como:



\* runtime operacional

\* deployment target

\* infraestrutura persistente



\---



\# Estratégia de Evolução



O runtime deve preservar:



\* simplicidade

\* causalidade explícita

\* observabilidade distribuída

\* desacoplamento entre runtimes

\* determinismo operacional



Evitar:



\* automações cegas

\* inferência implícita

\* acoplamento oculto

\* lógica distribuída ambígua

\* event buses redundantes

\* overengineering prematuro



\---



\# Objetivo Final



O Raspberry Hub existe para transformar eventos físicos distribuídos em:



\* observabilidade global

\* automações rastreáveis

\* coordenação distribuída

\* persistência causal

\* integração externa



Sem comprometer:



\* autonomia física dos ESP32

\* causalidade explícita

\* robustez do ecossistema

\* separação arquitetural

\* confiabilidade operacional



```

```



