from flask import Flask
from flask import render_template,jsonify,request
import requests
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import re
from rasa_core.utils import EndpointConfig
# from gurunudi import AI,lang

core_endpoint_config = EndpointConfig(url="http://localhost:5055/webhook")

interpreter = RasaNLUInterpreter('./models/current/nlu')# nlu
agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint = core_endpoint_config) # core/dialogue

# ai=AI()
# core_endpoint_config = EndpointConfig(url="http://localhost:5055/webhook")

# model_path = get_model('./models/nlu')
# _, nlu_model = get_model_subdirectories(model_path)
# interpreter = RasaNLUInterpreter(nlu_model)
# agent = Agent.load('./models/core', interpreter=interpreter, action_endpoint = core_endpoint_config)


# interpreter = RasaNLUInterpreter('/home/avinash/Desktop/yash_office/banking_chatbot_v1/models/')# nlu
# agent = Agent.load('/home/avinash/Desktop/yash_office/banking_chatbot_v1/models/', interpreter=interpreter, action_endpoint = core_endpoint_config) # core/dialogue

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat',methods=["POST"])
def chat():
    try:
        match=None
        user_message = request.form["text"]
        print(user_message)
        # user_message=ai.autocorrect(user_message)
        # print(user_message)
        responses = agent.handle_text(user_message)      
        print(responses)
        return jsonify({"status":"success","response":responses[0]})

    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8075)

