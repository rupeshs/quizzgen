import os
from embedchain import App
from argparse import ArgumentParser


app = App.from_config(config_path="config.yaml")

parser = ArgumentParser(description="QuizzGen")

parser.add_argument("--pdf_path", type=str, help="Path of pdf file", required=True)

parser.add_argument(
    "--topic",
    type=str,
    help="Name of the topic you want to generate questions",
    required=True,
)

parser.add_argument(
    "--number_of_questions",
    type=int,
    help="Number of questions to generate, default 1",
    default=1,
)
args = parser.parse_args()

app.add(args.pdf_path, data_type="pdf_file")
in_query = f"Create {args.number_of_questions} quizz questions with 4 choices(a,b,c,d) and answer about {args.topic}"
print(in_query)
response = app.query(in_query)

if app.llm.config.stream:  #
    for chunk in response:
        print(chunk)
else:
    print(response)
