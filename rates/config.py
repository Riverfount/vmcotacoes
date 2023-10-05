from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix='VM_COTACOES',
    settings_files=[
        'core/configs/settings.toml', 'core/configs/.secrets.toml'
    ],
    environments=True,
)
