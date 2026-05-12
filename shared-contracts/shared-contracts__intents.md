\# INTENTS CONTRACTS

\# Raspberry Home Hub Ecosystem



Versão: 0.1  

Status: Draft



\---



\# Objetivo



Este documento define:



\- semântica das intents distribuídas

\- estrutura dos payloads

\- regras de execução

\- contratos de intenção distribuída

\- causalidade entre intents e eventos



Este documento NÃO define:



\- tópicos MQTT

\- FSM física

\- automações internas

\- implementação de hardware

\- arquitetura geral



Referências:



\- ARCHITECTURE.md

\- shared-contracts\_\_mqtt-topics.md

\- shared-contracts\_\_events.md

\- esp32-node\_\_fsm.md

\- raspberry-hub\_\_runtime.md



\---



\# Filosofia das Intents



Intents representam:



\- pedidos distribuídos

\- intenções operacionais

\- solicitações de ação

\- desejos de mudança de comportamento



Intents NÃO representam:



\- sucesso confirmado

\- execução garantida

\- transição física confirmada

\- mudança de estado concluída



\---



\# Separação Fundamental



\## Intent



Representa:



```text

"algo deve ser tentado"

````



\---



\## Command Execution



Representa:



```text

"o nó decidiu executar fisicamente"

```



\---



\## Event



Representa:



```text

"algo foi fisicamente observado"

```



\---



\# Fluxo Correto



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

Evento confirmado

↓

Hub reage

```



\---



\# Fluxo Incorreto



```text

Intent

↓

Estado presumido

↓

Automação executa imediatamente

```



\---



\# Características Obrigatórias



Toda intent deve ser:



\* explícita

\* rastreável

\* serializável

\* idempotente quando possível

\* semanticamente clara

\* desacoplada de implementação física



\---



\# Estrutura Base de Intent



```json

{

&#x20; "intentId": "intent-991",

&#x20; "intentType": "REQUEST\_POWER\_ON",

&#x20; "targetNode": "pc-gamer",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

```



\---



\# Campos Obrigatórios



| Campo      | Descrição                |

| ---------- | ------------------------ |

| intentId   | ID único da intent       |

| intentType | Tipo semântico da intent |

| targetNode | Nó alvo                  |

| timestamp  | Unix timestamp UTC       |

| version    | Versão do payload        |



\---



\# Convenções Gerais



\## intentId



Deve ser:



\* único

\* imutável

\* rastreável



Formato recomendado:



```text

intent-xxxxxxxx

```



\---



\## timestamp



Deve utilizar:



```text

Unix Epoch UTC

```



\---



\## version



Versionamento do payload.



Exemplo:



```json

{

&#x20; "version": 1

}

```



\---



\# Intents Fundamentais



\## REQUEST\_POWER\_ON



Solicita tentativa de energização.



```json

{

&#x20; "intentId": "intent-001",

&#x20; "intentType": "REQUEST\_POWER\_ON",

&#x20; "targetNode": "pc-gamer",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

```



\---



\## REQUEST\_POWER\_OFF



Solicita tentativa de desligamento.



```json

{

&#x20; "intentId": "intent-002",

&#x20; "intentType": "REQUEST\_POWER\_OFF",

&#x20; "targetNode": "pc-gamer",

&#x20; "timestamp": 1747000001,

&#x20; "version": 1

}

```



\---



\## REQUEST\_RESTART



Solicita tentativa de reboot.



```json

{

&#x20; "intentId": "intent-003",

&#x20; "intentType": "REQUEST\_RESTART",

&#x20; "targetNode": "pc-gamer",

&#x20; "timestamp": 1747000002,

&#x20; "version": 1

}

```



\---



\## REQUEST\_FORCE\_POWER\_OFF



Solicita desligamento forçado.



```json

{

&#x20; "intentId": "intent-004",

&#x20; "intentType": "REQUEST\_FORCE\_POWER\_OFF",

&#x20; "targetNode": "pc-gamer",

&#x20; "timestamp": 1747000003,

&#x20; "version": 1

}

```



\---



\# Responsabilidade do ESP32



O nó ESP32 é responsável por:



\* validar execução física

\* rejeitar intents inválidas

\* proteger hardware

\* aplicar cooldowns

\* validar causalidade local

\* executar hardware fisicamente



\---



\# O ESP32 PODE rejeitar intents



Exemplos:



\* cooldown ativo

\* estado incompatível

\* hardware indisponível

\* FSM inconsistente

\* proteção operacional



\---



\# Exemplo de Rejeição



```json

{

&#x20; "eventType": "command\_rejected",

&#x20; "intentId": "intent-001",

&#x20; "reason": "COOLDOWN\_ACTIVE"

}

```



\---



\# Intents NÃO Implicam



Intents NÃO implicam:



\* sucesso

\* execução

\* mudança de estado

\* confirmação física

\* disponibilidade do nó



\---



\# Confirmação Correta



A confirmação correta ocorre através de:



\* eventos físicos

\* signal\_transition

\* physical\_state\_transition

\* heartbeat

\* telemetria observável



E NÃO através de:



```text

Intent ACK

```



\---



\# Relação Entre Intent e Evento



Uma intent pode gerar:



\* zero eventos

\* um evento

\* múltiplos eventos



Exemplo:



```text

REQUEST\_POWER\_ON

↓

command\_accepted

↓

signal\_transition

↓

physical\_state\_transition

↓

heartbeat

```



\---



\# Idempotência



Intents devem ser idempotentes quando possível.



Exemplo:



```text

REQUEST\_POWER\_ON

```



quando o sistema já está:



```text

RUNNING

```



não deve causar:



\* loops

\* toggles

\* reboot involuntário



\---



\# Timeout Semântico



O Hub NÃO deve assumir sucesso imediato.



O Hub deve aguardar:



\* eventos físicos

\* timeout operacional

\* confirmação da FSM



\---



\# Correlação Causal



Intents devem ser correlacionáveis com:



\* command\_accepted

\* command\_rejected

\* physical\_state\_transition

\* timeout

\* observability events



\---



\# Campos de Correlação



| Campo         | Objetivo              |

| ------------- | --------------------- |

| intentId      | Relacionamento causal |

| correlationId | Fluxos distribuídos   |

| causationId   | Encadeamento causal   |



\---



\# Imutabilidade



Intents são:



\* imutáveis

\* históricas

\* append-only



Intents NÃO devem:



\* ser editadas

\* ser sobrescritas

\* ser reutilizadas



\---



\# Compatibilidade Futura



Payloads devem ser:



\* forward-compatible

\* extensíveis

\* tolerantes a novos campos



Consumidores devem:



\* ignorar campos desconhecidos

\* validar version

\* evitar parsing rígido excessivo



\---



\# Convenções JSON



\## Keys



Devem utilizar:



```text

camelCase

```



\---



\## Intent Types



Devem utilizar:



```text

UPPERCASE

```



\---



\# Intent Types Reservadas



```text

REQUEST\_POWER\_ON

REQUEST\_POWER\_OFF

REQUEST\_RESTART

REQUEST\_FORCE\_POWER\_OFF

REQUEST\_STATUS\_REFRESH

REQUEST\_HEARTBEAT

```



\---



\# Garantias Arquiteturais



O sistema garante:



\* separação entre intenção e realidade física

\* causalidade explícita

\* autonomia física do ESP32

\* observabilidade distribuída

\* desacoplamento entre runtimes



\---



\# O Que o Hub NÃO Deve Fazer



O Raspberry Hub NÃO deve:



\* assumir sucesso baseado em intent

\* derivar estado sem feedback físico

\* sobrescrever FSM local

\* inferir causalidade sem eventos



\---



\# O Que o ESP32 NÃO Deve Fazer



O ESP32 NÃO deve:



\* assumir automações globais

\* assumir estado distribuído completo

\* persistir estado global

\* inferir intenção futura



\---



\# Princípio Final



Intents representam apenas:



\* pedidos distribuídos

\* intenções operacionais

\* solicitações de ação



A realidade do ecossistema continua sendo derivada exclusivamente através de:



\* sinais físicos

\* FSM local

\* eventos observáveis

\* feedback causal explícito.



```

```



