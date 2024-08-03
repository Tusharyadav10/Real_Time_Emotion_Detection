import eel
import db_controller
import Emotion_Recognizer

eel.init("web")

# os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode='edge', host='localhost', block=True)