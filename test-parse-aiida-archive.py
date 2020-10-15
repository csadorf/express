import json
from express import ExPrESS

kwargs = {
    "path": "./tests/fixtures/aiida/test-001/structures.zip",
}

express_ = ExPrESS("aiida-archive", **kwargs)
print json.dumps(express_.property("material", is_final_structure=True), indent=4)
