import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # игнорировать лишние переменные
    )
    LOG_LEVEL: str = Field(
        default="INFO",
        description="Уровень логирования",
    )

    LOG_PATH: str = Field(
        default="logs/",
        description="Папка для хранения логов",
    )

    URL: str = Field(
        default="https://api.artifactsmmo.com",
        description="URL для API",
    )

    TOKEN: str = Field(
        default="",
        description="Персональный токен",
    )

    LAMBERJACK_NAME: str = Field(
        default="",
        description="Имя персонажа, который будет дровосеком",
    )
    MINER_NAME: str = Field(
        default="",
        description="Имя персонажа, который будет шахтером",
    )
    FISHERMAN_NAME: str = Field(
        default="",
        description="Имя персонажа, который будет рыбаком",
    )

    GARDENER_NAME: str = Field(
        default="",
        description="Имя персонажа, который будет садовником",
    )

    BLACKSMITH_NAME: str = Field(
        default="",
        description="Имя персонажа, который будет кузнецом",
    )
    POLLING_INTERVAL: float = Field(
        default=0.5,
        description="Интервал между опросами sheduler",
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

config = ConfigSettings()
