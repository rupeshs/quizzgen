import os
from argparse import ArgumentParser
from rag import add_file, generate_questions, is_streaming_response
from stream import stream_to_console

os.environ["EC_TELEMETRY"] = "false"


parser = ArgumentParser(description="QuizzGen")
parser.add_argument("--file", type=str, help="File path PDF/Text", required=True)
parser.add_argument(
    "--topic",
    type=str,
    help="Name of the topic you want to generate questions",
)
parser.add_argument(
    "--max_questions",
    type=int,
    help="Maximum number of questions to generate in single pass,default 5",
    default=5,
)

args = parser.parse_args()

add_file(args.file)


def print_message(response: str):
    if is_streaming_response():
        stream_to_console(response)
    else:
        print(response)


while True:
    print()
    topic = input(">> ")

    if topic == "exit":
        break
    if topic == "":
        continue

    for index in range(args.max_questions):
        question_count = args.max_questions - index
        response = generate_questions(question_count, topic)
        if "Sorry" in response:
            print_message(f"Failed generate {question_count} questions about {topic}!")
            print()
            continue
        else:
            print_message(response)
            break
