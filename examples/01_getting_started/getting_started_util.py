from vectara.factory import Factory
from vectara.managers import CreateCorpusRequest
from pathlib import Path
from vectara.types import StructuredDocument
from typing import List, Dict
from vectara.utils import LabHelper
from vectara import Vectara
import re
import logging

class GettingStartedUtil:

    def __init__(self):
        logging.basicConfig(format='%(asctime)s:%(name)-35s %(levelname)s:%(message)s', level=logging.INFO,
                            datefmt='%H:%M:%S %z')
        self.logger = logging.getLogger(self.__class__.__name__)

    def _check_initialized(self, client: Vectara):
        if not client.lab_helper:
            raise Exception("Client not initialized correctly")

    def setup_01(self, client: Vectara) -> str:
        self.logger.info("Setting up Lab 01")
        self._check_initialized(client)
        request = CreateCorpusRequest(name="Getting Started - Query API", key="01-getting-started-query-api")
        response = client.lab_helper.create_lab_corpus(request)  # type: ignore
        if not isinstance(response.key, str):
            raise Exception(f"Unexpected response type for key: {response.key}")

        self.logger.info(f"Our corpus key is [{response.key}]")

        path = Path("resources/shakespeare/taming_shrew.txt")
        with open(path, "r", encoding="utf-8") as f:
            play_text = f.read()

        doc_request = StructuredDocument.parse_obj({
            "id": "my-doc",
            "type": "structured",
            "title": "Taming of the Shrew",
            "description": "The Shakespeare play, 'the Taming of the Shrew'",
            "sections": [
                {
                    "text": play_text  # One big section which will be automatically chunked.
                }
            ]
        })

        client.documents.create(response.key, request=doc_request)

        self.logger.info("Lab setup for 01 complete")
        return response.key

    def setup_02(self, client: Vectara) -> str:
        self.logger.info("Setting up Lab 02")
        self._check_initialized(client)  # type: ignore
        request = CreateCorpusRequest(name="Getting Started - Index API", key="02-getting-started-index-api")
        response = client.lab_helper.create_lab_corpus(request)  # type: ignore

        self.logger.info(f"Our corpus key is [{response.key}]")
        self.logger.info("Lab setup for 02 complete")
        return response.key  # type: ignore

    def lab_02_chunk_play(self, play_path: Path) -> List[Dict]:

        scene = {"name": "", "scene_texts": []}
        act = {"name": "Overview", "scenes": [scene]}
        acts = [act]

        break_marker = re.compile(r'^=+$')

        ignored_break_markers = [
            "Characters in the Play"
        ]

        scene_prefix = "Scene"

        last = ""
        self.logger.info(f"Loading {play_path}")
        with open(play_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f):
                stripped_line = line.strip()

                if idx > 0:
                    if break_marker.match(stripped_line):
                        if last in ignored_break_markers:
                            continue
                        if last.startswith(scene_prefix):
                            self.logger.info(f"\tFound scene: {last}")
                            # Put the last scene into the act (if not empty)
                            scene = {"name": last, "scene_texts": []}
                            act["scenes"].append(scene)  # type: ignore
                        else:
                            self.logger.info(f"Found act: {last}")
                            # New Act.
                            act = {"name": last, "scenes": []}
                            acts.append(act)
                    else:
                        scene["scene_texts"].append(last)   # type: ignore
                last = stripped_line

        return acts

    def lab_03_setup(self, client) -> str:

        self.logger.info("Setting up Lab 03")
        self._check_initialized(client)

        request = CreateCorpusRequest(name="Getting Started - Upload API", key="03-getting-started-upload-api")
        response = client.lab_helper.create_lab_corpus(request)  # type: ignore
        corpus_key = response.key
        self.logger.info(f"Our corpus key is [{corpus_key}]")

        self.logger.info("Lab setup for 02 complete")
        return corpus_key



