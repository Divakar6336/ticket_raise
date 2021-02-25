Action server
New command window
# Environment
C:\Users\avinash.navlani\rasa_env\Scripts\activate
#cd into ega_chatbot  folder
Cd ega_chatbot
# start server
python -m rasa_sdk --actions actions
API Server
New command window
# Environment
C:\Users\avinash.navlani\rasa_env\Scripts\activate
#cd into ega_chatbot  folder
Cd ega_chatbot


#Run API server
python server_api.py
Main chatbot

cd ega_chatbot
C:\Users\avinash.navlani\rasa_env\Scripts\avtivate
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue
python app.py
