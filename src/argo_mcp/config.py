from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with types and defaults, can be
    overriden by environment variables"""

    argo_base_url: str = ""
    argo_namespace: str = "argo"
    oidc_issuer: str = ""
    oidc_audience: str = ""
    roles_claim: str = "roles"

    otel_exporter_endpoint: str = ""
    gated_templates: str = ""
    approval_timeout_seconds: int = 300
    approval_webhook_url: str = ""

    # Use the .env file to populate these settings.
    model_config = SettingsConfigDict(env_file=".env")
