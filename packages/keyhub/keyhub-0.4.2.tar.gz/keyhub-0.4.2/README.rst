# keyhub-python-sdk

SDK for KeyHub written in Python

Python client for the Topicus KeyHub Vault API, supported under python 3 (only tested with 3.6).

Basic usage:

```python
    import keyhub

    keyhub_client = keyhub.client(uri='<your KeyHub uri>', client_id='<KeyHub application id>', client_secret='<KeyHub application secret>')
    keyhub_vault = keyhub.vault(authentication=keyhub_client_auth)

    print(keyhub_client.info())

    keyhub_client.get_group('<group uuid>')

    keyhub_client.get_vault_records('<group uuid>')

    keyhub_client.get_vault_record('<group uuid>', '<vault record uuid>')

    keyhub_client.get_account_record(account_uuid='<useraccount uuid>')

    keyhub_client.get_account_record(account_username='<useraccount username>')

    payload = {
        'items': [
            {
            "$type": "vault.VaultRecord",
            'additionalObjects': {
                'secret': {
                    '$type': 'vault.VaultRecordSecrets',
                    'password': 'super-secure-password123',
                    "comment": "This is an example record, nothing special"
                }
            },
            'name': 'KeyHub example record', 
            'username': 'my-username', 
            'color': 'PINK_LAVENDER', # PINK_LAVENDER, RED, ANDROID_GREEN, DARK, NONE, BLUE, SAGE, ARTICHOKE, CRIMSON_RED, GREEN, MIDDLE_YELLOW
            'url': 'https://topicus-keyhub.com',
            'endDate': '2023-05-25',
            'warningPeriod': 'ONE_MONTH' # AT_EXPIRATION, TWO_WEEKS, ONE_MONTH, TWO_MONTHS, THREE_MONTHS, SIX_MONTHS, NEVER
            }
        ]
    }
    post_vault_record = keyhub_vault.post_vault_record(group_uuid=settings['vault_uuid'], payload=payload)
```

> This repository is a cherry pick from the original authors repo: https://github.com/topicusonderwijs/keyhub-sdk and modified to fit some more specific needs
