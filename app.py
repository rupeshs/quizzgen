import os
from embedchain import App


os.environ["GOOGLE_API_KEY"] = "AIzaSyB_Wf8VWRPNMp6KTaR_0T0rxEmAEyObEkU"

app = App.from_config(config_path="config.yaml")

app.add("https://www.forbes.com/profile/elon-musk")

response = app.query("create 3 quizz questions with 4 choices and correct answer")
if app.llm.config.stream:  # if stream is enabled, response is a generator
    for chunk in response:
        print(chunk)
else:
    print(response)
