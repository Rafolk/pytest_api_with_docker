import pytest
import json
import os
import io


@pytest.fixture(scope='session')
def auth_data():
    script_dir = os.path.dirname(__file__)
    with io.open(os.path.join(script_dir, "auth_data.json"), encoding="utf-8") as json_file:
        return json.load(json_file)
