\# Events Contract

\# events.md



Versão: 1.0

Status: Active



\---



\# Estrutura Base



```json

{

&#x20; "eventId": "uuid",

&#x20; "eventType": "physical\_state\_transition",

&#x20; "nodeId": "pc-gamer",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

Campos Obrigatórios

Campo	Tipo

eventId	string

eventType	string

nodeId	string

timestamp	number

version	number

Event Types

physical\_state\_transition

signal\_transition

command\_accepted

command\_rejected

command\_execution\_started

command\_execution\_finished

timeout

warning

error

recovery

heartbeat

mqtt\_connected

mqtt\_disconnected

Physical State Transition



Topic:



rhh/<node-id>/events/physical\_state\_transition



Payload:



{

&#x20; "eventId": "uuid",

&#x20; "eventType": "physical\_state\_transition",

&#x20; "nodeId": "pc-gamer",

&#x20; "from": "OFF",

&#x20; "to": "STARTING",

&#x20; "timestamp": 1747000000,

&#x20; "intentId": "uuid",

&#x20; "version": 1

}

Signal Transition



Topic:



rhh/<node-id>/events/signal\_transition



Payload:



{

&#x20; "eventId": "uuid",

&#x20; "eventType": "signal\_transition",

&#x20; "nodeId": "pc-gamer",

&#x20; "signal": "POWER\_OK",

&#x20; "from": false,

&#x20; "to": true,

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

Command Accepted



Topic:



rhh/<node-id>/events/command\_accepted



Payload:



{

&#x20; "eventId": "uuid",

&#x20; "eventType": "command\_accepted",

&#x20; "nodeId": "pc-gamer",

&#x20; "intentId": "uuid",

&#x20; "command": "REQUEST\_POWER\_ON",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

Command Rejected



Topic:



rhh/<node-id>/events/command\_rejected



Payload:



{

&#x20; "eventId": "uuid",

&#x20; "eventType": "command\_rejected",

&#x20; "nodeId": "pc-gamer",

&#x20; "intentId": "uuid",

&#x20; "reason": "INVALID\_STATE",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

Timeout



Topic:



rhh/<node-id>/events/timeout



Payload:



{

&#x20; "eventId": "uuid",

&#x20; "eventType": "timeout",

&#x20; "nodeId": "pc-gamer",

&#x20; "context": "STARTING\_TIMEOUT",

&#x20; "timestamp": 1747000000,

&#x20; "version": 1

}

Regras

Eventos representam

fatos históricos observáveis

Eventos nunca representam

intenções futuras

Eventos devem ser imutáveis



Após publicados:



nunca devem ser alterados

Estados Oficiais

OFF

STARTING

RUNNING

ERROR

Convenções

eventType



Formato:



snake\_case

JSON Keys



Formato:



camelCase



\---

