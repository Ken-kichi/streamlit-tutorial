from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def get_key_container():
    KVUri = f"https://graph0614.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    print(f"Retrieving your secret from KV_NAME.")

    AZURE_ENDPOINT = client.get_secret("AZURE-ENDPOINT")
    AZURE_KEY = client.get_secret("AZURE-KEY")

    return AZURE_ENDPOINT.value, AZURE_KEY.value
