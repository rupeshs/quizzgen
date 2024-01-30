import os
from embedchain import App


os.environ["GOOGLE_API_KEY"] = "AIzaSyB_Wf8VWRPNMp6KTaR_0T0rxEmAEyObEkU"

app = App.from_config(config_path="config.yaml")

app.add(r"C:\Users\Rupesh\Downloads\test.pdf", data_type="pdf_file")

response = app.query(
    "create 2 quizz questions with 4 choices and correct answer about Adapter Pattern"
)
# response = app.query("create a list of topics")
if app.llm.config.stream:  # if stream is enabled, response is a generator
    for chunk in response:
        print(chunk)
else:
    print(response)
