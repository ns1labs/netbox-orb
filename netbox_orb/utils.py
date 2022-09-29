import logging
from typing import DefaultDict
import requests
import json
from django.conf import settings

logger = logging.getLogger("netbox.plugins.netbox_orb")
CONFIG = settings.PLUGINS_CONFIG["netbox_orb"]
HOST = CONFIG["host"]
TOKEN = CONFIG["token"]
HEADERS = {
    "content-type": "application/json",
    "Authorization": "Bearer {}".format(TOKEN)
}

def update_orb_agent(model):
    payload = {
        "name": model.name,
        "orb_tags": {
            "source": "netbox"
        },
    }

    if model.device:
        payload["orb_tags"]['device_id'] = str(model.device.id)
        payload["orb_tags"]['device_name'] = str(model.device.name)
        if model.device.site:
            payload["orb_tags"]['site_id'] = str(model.device.site.id)
            payload["orb_tags"]['site_name'] = str(model.device.site.name)
        if model.device.cluster:
            payload["orb_tags"]['cluster_id'] = str(model.device.cluster.id)
            payload["orb_tags"]['cluster_name'] = str(model.device.cluster.name)

    if model.vm:
        payload["orb_tags"]['vm_id'] = str(model.vm.id)
        payload["orb_tags"]['vm_name'] = str(model.vm.name)
        if model.vm.device: 
            payload["orb_tags"]['device_id'] = str(model.vm.device.id)
            payload["orb_tags"]['device_name'] = str(model.vm.device.name)
        if model.vm.site:
            payload["orb_tags"]['site_id'] = str(model.vm.site.id)
            payload["orb_tags"]['site_name'] = str(model.vm.site.name)
        if model.vm.cluster:
            payload["orb_tags"]['cluster_id'] = str(model.vm.cluster.id)
            payload["orb_tags"]['cluster_name'] = str(model.vm.cluster.name)

    for tag in model.extra_tags:
        key, value = tag.split(":")
        payload["orb_tags"][key] = value

    url = "https://{host}/api/v1/agents/{orb_id}".format(host=HOST, orb_id=model.orb_id)

    print(payload)
    r = requests.put(
        url,
        headers=HEADERS,
        data=json.dumps(payload),
    )
    print(r.text)
    print("update_orb_agent: {}".format(r.status_code))

def upsert_agent_group(model):
    payload = {
        "name": model.name,
        "tags": {
            "source": "netbox"
        },
    }

    if model.description:
        payload["description"] = model.description

    if model.site:
        payload["tags"]['site_id'] = str(model.site.id)

    if model.device:
        payload["tags"]['device_id'] = str(model.device.id)
    
    if model.vm:
        payload["tags"]['vm_id'] = str(model.vm.id)
    
    for tag in model.extra_tags:
        key, value = tag.split(":")
        payload["tags"][key] = value

    if model.orb_id:
        url = "https://{host}/api/v1/agent_groups/{orb_id}".format(host=HOST, orb_id=model.orb_id)
        r = requests.put(
            url,
            headers=HEADERS,
            data=json.dumps(payload),
        )
    else:
        url = "https://{host}/api/v1/agent_groups".format(host=HOST)
        r = requests.post(
            url,
            headers=HEADERS,
            data=json.dumps(payload),
        )

    if r.status_code // 100 == 2:
        return r.json()

def delete_agent_group(model):
    url = "https://{host}/api/v1/agent_groups/{orb_id}".format(host=HOST, orb_id=model.orb_id)
    r = requests.delete(
        url,
        headers=HEADERS,
    )
