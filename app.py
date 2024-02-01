import os
from argparse import ArgumentParser
from rag import add_pdf, generate_questions, is_streaming_response
from stream import stream_to_console

os.environ["EC_TELEMETRY"] = "false"


parser = ArgumentParser(description="QuizzGen")
parser.add_argument("--pdf", type=str, help="PDF file path", required=True)
parser.add_argument(
    "--topic",
    type=str,
    help="Name of the topic you want to generate questions",
)
args = parser.parse_args()

add_pdf(args.pdf)


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

    for x in range(5):
        i = 5 - x
        response = generate_questions(i, topic)
        if "Sorry" in response:
            print_message(f"Failed generate {i} questions about {topic}!")
            print()
            continue
        else:
            print_message(response)
            break
