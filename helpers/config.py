import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class ConfigSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # игнорировать лишние переменные
    )

    AUTH: str = Field(default="", description="Токен для авторизации в API")
    LOG_PATH: str = Field(
        default="logs",
        description="Путь для сохранения логов",
    )
    LOG_LEVEL: str = Field(
        default="DEBUG",
        description="Уровень логирования (DEBUG, INFO, WARNING, ERROR)",
    )


IN_DOCKER = os.getenv("IN_DOCKER", "").lower() in ("1", "true", "yes")
env_path = Path(".env")

if not IN_DOCKER and not env_path.exists():
    if not env_path.exists():
        with open(env_path, "w", encoding="utf-8") as f:
            for field_name, field_info in ConfigSettings.model_fields.items():
                desc = field_info.description or ""
                default = field_info.get_default()
                if isinstance(default, bool):
                    default = "true" if default else "false"
                else:
                    default = str(default)

                f.write(f"# {desc}\n")
                f.write(f"{field_name}={default}\n\n")

        raise RuntimeError(
            "Файл .env не найден и был создан со шаблоном.\n"
            "Отредактируйте параметры перед запуском:\n"
            f"- Файл: {env_path.absolute()}"
        )

# Создание экземпляра конфигурации
config = ConfigSettings()
