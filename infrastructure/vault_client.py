import os
import hvac


class VaultClient:
    """Simple wrapper around hvac Client for retrieving secrets."""

    def __init__(self):
        url = os.getenv("VAULT_ADDR")
        token = os.getenv("VAULT_TOKEN")
        if not url or not token:
            raise EnvironmentError("Vault configuration is missing")
        self.client = hvac.Client(url=url, token=token)

    def read_secret(self, path: str, key: str) -> str | None:
        """Read a specific key from a Vault KV v2 secret."""
        secret = self.client.secrets.kv.v2.read_secret_version(path=path)
        return secret["data"]["data"].get(key)
