import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from artifacts_api_client import AuthenticatedClient
from artifacts_api_client.api.my_characters import (
    action_gathering_my_name_action_gathering_post as api,  # noqa: F401
)

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImN5YW5zYWlyMDVAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6bnVsbH0.HlOn2RG7LJVS0UlZjSYdR_kKYpJQo0qDhpk00aa7gb0"
client = AuthenticatedClient("https://api.artifactsmmo.com/", TOKEN)
