from django.dispatch import receiver
from django.core import management
from django.conf import settings

from pretalx.schedule.signals import schedule_release
from pretalx.schedule.exporters import FrabJsonExporter

import requests
import json
import base64
from dotenv import load_dotenv
import os
import logging
from pathlib import Path

dotenv_path = Path(__file__).parent
load_dotenv()

logger = logging.getLogger('Swarm-plugin-logger')

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_EMAIL = os.getenv('GITHUB_EMAIL')

repo = 'datafund/web_devconagenda'
filename = 'democon.zip'
url="https://api.github.com/repos/{}/contents/{}".format(repo, filename)
token = 'Bearer {}'.format(GITHUB_TOKEN)
headers = {'Accept': 'application/vnd.github+json', 'Authorization': token}


def get_export_zip_path(event):
    export_path = settings.HTMLEXPORT_ROOT / event.slug
    return export_path.with_suffix(".zip")  


@receiver(schedule_release, dispatch_uid="swarm signal")
def on_schedule_release(sender, schedule, user, **kwargs):

    json_schedule = FrabJsonExporter(sender, schedule)
    rendered_schedule = json_schedule.render()
    #TODO post JSON to Swarm feeds

    management.call_command('export_schedule_html', sender,  '--zip',)

    zip_path = get_export_zip_path(sender)

    try:

        resp = requests.get(url, headers=headers)
        sha = json.loads(resp.text)['sha']

        with open(zip_path, 'rb') as f:
            file = f.read()

        encoded = base64.b64encode(file)
        data = {'message':'upload agenda zip','committer':{'name':GITHUB_USERNAME,'email':GITHUB_EMAIL},'content': encoded.decode(), 'sha': sha, 'branch': 'main'}
        response = requests.put(url, headers=headers, data = json.dumps(data))
        logger.info('Agenda succesfully exported to Swarm!')

    except Exception as e:
        logger.warning(str(e))    
