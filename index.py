from flask import Flask
from api.controllers.GptController import GptController
from api.services.GptService import GptService

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

gpt_controller = GptController(GptService)

@app.route("/create-recipe", methods=["POST"])
def create_recipe():
    """Endpoint that receives this body {"ingredients": "frango, tomate, cebola, milho, batata, curry, leite de coco"}
    and returns a recipe with the provided ingredients"""
    return gpt_controller.create_recipe()

@app.route("/summary", methods=["POST"])
def create_summary():
    """Endpoint that receives this body {"text": "História do titanic"} and return a summary"""
    return gpt_controller.create_summary()

@app.route("/translator", methods=["POST"])
def translator():
    """Endpoint that receives this body {"source_language": "português", "target_language": "inglês", "text": "Olá mundo!"}
    and returns the translation"""
    return gpt_controller.translator()

@app.route("/writing-assistant", methods=["POST"])
def writing_assistant():
    """Endpoint that receives this body {"text": "Blog post sobre os benefícios da vitamina D"}
    and returns the text"""
    return gpt_controller.writing_assistant()

if __name__ == "__main__":
    app.run()
