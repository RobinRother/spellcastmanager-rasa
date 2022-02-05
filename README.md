# spellcastmanager-rasa
## description
This is a crude implementation of the spellcastmanager mycroft skill for in RASA.
Currently, just the help intent is implemented.

## usage
1. Install RASA like shown here: https://rasa.com/docs/rasa/installation/ 
2. Activate the virtual environment, if it is not already active by running this command in the console (without the ""): "source project_directory/venv/bin/activate" 
3. Train the model by running this command: "rasa train"
4. Start the action server with the "rasa run actions" command.
5. Start the chat bot, using the "rasa shell" command.
6. Everything is running now, Try asking for help with the spellcastmanager.
