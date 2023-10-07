import os

from dynaconf import Dynaconf, Validator

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix='vm_cotacoes',
    preload=[os.path.join(HERE, 'default.toml')],
    settings_files=['settings.toml', '.secrets.toml'],
    environments=['development', 'production', 'testing'],
    env_switcher='vm_cotacoes_env',
    merge_enabled=True,
    load_dotenv=False
)

settings.validators.register(
    Validator('security.API_KEY', must_exist=True, is_type_of=str)
)
