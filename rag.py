from embedchain import App
from typing import Any

app = App.from_config(config_path="config.yaml")


def add_file(filepath: str):
    app.add(filepath)


def generate_questions(
    num_questions: int,
    topic: str,
) -> Any:
    in_query = f"""Create {num_questions} quiz questions with 4 choices(a,b,c,d) and answer about {topic},avoid markup format,if you dont know reply Sorry,I don't know"""
    print(in_query)
    response = app.query(in_query)
    return response


def is_streaming_response() -> bool:
    return app.llm.config.stream
