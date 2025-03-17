from langchain.chat_models import init_chat_model


class Repository:

    def __init__(self, model="gpt-4o-mini", model_provider="openai"):
        self.llm = init_chat_model(model, model_provider=model_provider)

    def get_llm(self):
        return self.llm
