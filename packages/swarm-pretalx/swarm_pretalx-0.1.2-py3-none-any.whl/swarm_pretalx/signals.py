import base64
import json
import logging
import os
from pathlib import Path

import requests
from django.conf import settings
from django.core import management
from django.dispatch import receiver
from dotenv import load_dotenv
from pretalx.schedule.exporters import FrabJsonExporter
from pretalx.schedule.signals import schedule_release

dotenv_path = Path(__file__).parent

logger = logging.getLogger("Swarm-plugin-logger")

try:
    load_dotenv()
except Exception as e:
    logger.warning(
        "Problems loading .env file. Please check the structure and location of the file! See README for more."
    )

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_EMAIL = os.getenv("GITHUB_EMAIL")

feeds_url = "https://gateway.fairdatasociety.org/proxy/bzz"
feeds_headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/octet-stream",
    "swarm-postage-batch-id": "36b7efd913ca4cf880b8eeac5093fa27b0825906c600685b6abdd6566e6cfe8f",
    "user-agent": "bee-js",
}

repo = "datafund/web_devconagenda"
filename = "democon.zip"
url = "https://api.github.com/repos/{}/contents/{}".format(repo, filename)
token = "Bearer {}".format(GITHUB_TOKEN)
headers = {"Accept": "application/vnd.github+json", "Authorization": token}


def get_export_zip_path(event):
    export_path = settings.HTMLEXPORT_ROOT / event.slug
    return export_path.with_suffix(".zip")


@receiver(schedule_release, dispatch_uid="swarm signal")
def on_schedule_release(sender, schedule, user, **kwargs):

    agenda = FrabJsonExporter(sender, schedule)
    agenda_json = agenda.render()
    resp1 = requests.post(
        feeds_url, json={"agenda_json": agenda_json}, headers=feeds_headers
    )
    logger.info(resp1.text)

    # management.call_command(
    #     "export_schedule_html",
    #     sender,
    #     "--zip",
    # )

    zip_path = get_export_zip_path(sender)

    try:

        resp2 = requests.get(url, headers=headers)
        sha = json.loads(resp2.text)["sha"]

        with open(zip_path, "rb") as f:
            file = f.read()

        encoded = base64.b64encode(file)
        data = {
            "message": "upload agenda zip",
            "committer": {"name": GITHUB_USERNAME, "email": GITHUB_EMAIL},
            "content": encoded.decode(),
            "sha": sha,
            "branch": "main",
        }
        resp3 = requests.put(url, headers=headers, data=json.dumps(data))
        logger.info("Agenda succesfully exported to Swarm!")

    except Exception as e:
        logger.warning(str(e))
