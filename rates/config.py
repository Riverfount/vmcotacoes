from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix='VM_COTACOES',
    settings_files=[
        'core/configs/settings.toml', 'core/configs/.secrets.toml'
    ],
    environments=True,
)

settings.validators.register(
    Validator('security.API_KEY', must_exist=True, is_type_of=str)
)
