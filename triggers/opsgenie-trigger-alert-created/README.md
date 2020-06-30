# opsgenie-trigger-alert-created

This [OpsGenie](https://www.atlassian.com/software/opsgenie) trigger fires when a new alert is created. 

## Data Emitted 

| Name | Data type | Description | 
|------|-----------|-------------|
| `id` | string | id of the alert | 
| `message` | string | alert message | 
| `description`  | string | alert description | 
| `team` | string |  team responding to alert |
| `priority` | string |  alert priority |

## Example Trigger

```
parameters:
  id: 
    default: ""
  message:
    default: ""
  team:
    default: ""
    
triggers:
- name: alert-created
  source:
    type: webhook
    image: relaysh/opsgenie-trigger-alert-created
  binding:
    parameters:
      id: !Data id
      message: !Data message
      team: !Data team
```

## Example Raw Data 

```
{
  "action": "Create",
  "alert": {
    "alertId": "7ec331d7-f5f3-4f78-a49c-2ad886df69fe-1593475564295",
    "message": "asdf",
    "tags": [],
    "tinyId": "8",
    "entity": "",
    "alias": "7ec331d7-f5f3-4f78-a49c-2ad886df69fe-1593475564295",
    "createdAt": 1593475564295,
    "updatedAt": 1593475564636000000,
    "username": "kenaz@puppet.com",
    "userId": "e760568d-4e19-413e-9ff9-2661f416edbb",
    "description": "",
    "team": "operations",
    "responders": [
      {
        "id": "6ee84e52-f33e-45d9-87ab-533fd69d5591",
        "type": "team",
        "name": "operations"
      }
    ],
    "teams": [
      "6ee84e52-f33e-45d9-87ab-533fd69d5591"
    ],
    "actions": [],
    "details": {},
    "priority": "P3",
    "source": "kenaz@puppet.com"
  },
  "source": {
    "name": "",
    "type": "web"
  },
  "integrationName": "operations_Webhook_2",
  "integrationId": "cab111af-f56b-4886-b20a-f947ea3163e2",
  "integrationType": "Webhook"
}
```
