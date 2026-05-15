\# MQTT Topics

\# mqtt-topics.md



Versão: 1.0

Status: Active



\---



\# Namespace Oficial



Todos os tópicos seguem:



```text

rhh/<node-id>/<category>/<resource>



Exemplo:



rhh/pc-gamer/events/physical\_state\_transition

Categorias Oficiais

Categoria	Objetivo

intents	pedidos operacionais

events	fatos observáveis

state	snapshots materializados

telemetry	stream operacional

heartbeat	presença operacional

observability	logs e diagnósticos

Intents

Power On



Topic:



rhh/<node-id>/intents/request\_power\_on



QoS:



1



Retained:



false

Power Off



Topic:



rhh/<node-id>/intents/request\_power\_off



QoS:



1



Retained:



false

Events

Physical State Transition



Topic:



rhh/<node-id>/events/physical\_state\_transition



QoS:



1



Retained:



false

Signal Transition



Topic:



rhh/<node-id>/events/signal\_transition



QoS:



1



Retained:



false

State

Physical State



Topic:



rhh/<node-id>/state/physical\_state



QoS:



1



Retained:



true

Signals State



Topic:



rhh/<node-id>/state/signals



QoS:



1



Retained:



true

Heartbeat



Topic:



rhh/<node-id>/heartbeat



QoS:



1



Retained:



false

Observability

Logs



Topic:



rhh/<node-id>/observability/logs



QoS:



0



Retained:



false

Convenções

node-id



Formato:



lowercase-kebab-case



Exemplos:



pc-gamer

pc-server

network-rack

Regras

Intents



Representam:



tentativas operacionais



Nunca:



sucesso confirmado

Events



Representam:



fatos observáveis

State



Representa:



snapshot materializado atual

Retained Permitido



Somente:



state/\*

Retained Proibido



Nunca usar retained em:



intents/\*

events/\*

heartbeat

observability/\*



\---

