from llms.AIModel import AIModel
from config_manage.manager import ConfigManager
from charset_normalizer import from_path

class MuLi:
    def __init__(self):
        with open("core/prompts/MuLi.txt", "r", encoding=from_path("core/prompts/MuLi.txt").best().encoding) as f:
            spmp = f.read()

        config = ConfigManager("config.json5")
        self.ai_model = AIModel(
            api_key=config.get("model_config.ai_model.api_key"),
            base_url=config.get("model_config.ai_model.api_base_url"),
            model_name=config.get("model_config.ai_model.model_name"),
            provider_type=config.get("model_config.ai_model.provider_type"),
            system_prompt=spmp,
            tools=None
        )