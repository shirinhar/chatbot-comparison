
# Dissertation
The repo looks at the code necessary to run the Rasa, DeepPavlov and DialogFlow chatbots used in the paper  "An Empirical Study of the Usability of Chatbot Systems". The repo also contains the notebook used to analyse the data gathered from the user study. 

## File Layout

 - conversion
	 - Files used to convert the DSCT2 dataset into the necessary frameowork strcture
 - database 
	 - Restaurant database used by DSTC2
	 - Both files reflect the same data but are in two different formats
 - deeppavlov-bot
 - dialogflow-bot
	 - API code
 - ngrok
	 - Necessary files used to run Rasa and DeepPavlov bots simultaniously
 - rasa-bot
	 - Converted files used to train the rasa model
	 - Rasa model
 - survey-analysis
	 - Data gathered from the survey
	 - Jupyter Notebook used to analyse the data

## Run DialogFlow
Runs online and does not need any commands to run.
## Run DeepPavlov
Before running the DeepPavlov server make sure to use python Python 3.7.5 and not higher as Rasa v2.0 cannot run on a newer version of Python.


The code below shows how the bot was run using the SSL key and certificate used. The documentation used to host the bot on the Microsoft Web App Bot can be found at http://docs.deeppavlov.ai/en/master/integrations/ms_bot.html

    python -m deeppavlov msbot config.json -i 789a812b-16ff-494f-9d17-2b9a91d3988d -s 8da~W.i6MW9NL6TL9v0hh8nZ-qZe~uko9- --key server.key --cert server.crt -d -p 5005
   
   DeepPavlov connects the action server to the bot automatically and does not need to be run separately. 
## Run Rasa
Before running the Rasa server, all the environment variables must be correctly set. Make sure to use python Python 3.7.10 and not higher as Rasa v2.0 cannot run on a newer version of Python.

To run the Rasa bot, the Rasa messaging server and action server need to be running. Running the messaging server can be done using the following command: 

    rasa run -p 5002
The actions server can be run by running the following command in a new terminal window. 

    rasa run actions

## Ngrok
In order to run both the Rasa and DeepPavlov bot simultaneously the Ngrok config needed to be modified. The modified config can be found in the ngrok folder of the repository. To get Ngrok to open all the specified ports the following command must be run in ngrok the folder. 

    ./ngrok start --all

