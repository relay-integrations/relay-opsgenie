from nebula_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

import logging

relay = Interface()
app = Quart('alert-created')

logging.getLogger().setLevel(logging.INFO)


@app.route('/', methods=['POST'])
async def handler():
    
    payload = await request.get_json(force=True)
    if payload['action'] != 'Create':
        return {'message': 'not the event you are looking for'}, 400, {}


    alert = payload['alert']

    relay.events.emit({
        'id': alert['alertId'],
        'message': alert['message'],
        'description': alert['description'],
        'team': alert['team'],
        'priority': alert['priority']
    })

    return {'message': 'success'}, 202, {}


if __name__ == '__main__':
    WebhookServer(app).serve_forever()
