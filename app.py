import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message, send_text_message_AI

load_dotenv()


machine = TocMachine(
    states=["user", "adapt", "care","dog","cat","dog_fat","dog_sick","dog_vaccine","dog_parasite","cat_fat","cat_sick","cat_vaccine","cat_parasite","dog_heart","dog_infectious","dog_cancer","dog_kidney",
            "dog_too_fat","dog_median","dog_too_thin","cat_tooth","cat_liver","cat_diabete","cat_kidney","cat_too_fat","cat_median","cat_too_thin","abandon","commercial"],
    transitions=[
        {"trigger": "advance", "source": ["user", "adapt", "care","dog","cat","dog_fat","dog_sick","dog_vaccine","dog_parasite","cat_fat","cat_sick","cat_vaccine","cat_parasite","dog_heart","dog_infectious","dog_cancer","dog_kidney",
            "dog_too_fat","dog_median","dog_too_thin","cat_tooth","cat_liver","cat_diabete","cat_kidney","cat_too_fat","cat_median","cat_too_thin","abandon","commercial"],
         "dest": "user","conditions": "is_going_to_user",},
        {
            "trigger": "advance",
            "source": "adapt",
            "dest": "commercial",
            "conditions": "is_going_to_commercial",
        },
        {
            "trigger": "advance",
            "source": "adapt",
            "dest": "abandon",
            "conditions": "is_going_to_abandon",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "adapt",
            "conditions": "is_going_to_adapt",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "care",
            "conditions": "is_going_to_care",
        },
        {
            "trigger": "advance",
            "source": "care",
            "dest": "dog",
            "conditions": "is_going_to_dog",
        },
        {
            "trigger": "advance",
            "source": "care",
            "dest": "cat",
            "conditions": "is_going_to_cat",
        },
        {
            "trigger": "advance",
            "source": "dog",
            "dest": "dog_fat",
            "conditions": "is_going_to_dog_fat",
        },
        {
            "trigger": "advance",
            "source": "dog",
            "dest": "dog_sick",
            "conditions": "is_going_to_dog_sick",
        },
        {
            "trigger": "advance",
            "source": "dog",
            "dest": "dog_vaccine",
            "conditions": "is_going_to_dog_vaccine",
        },
        {
            "trigger": "advance",
            "source": "dog",
            "dest": "dog_parasite",
            "conditions": "is_going_to_dog_parasite",
        },
        {
            "trigger": "advance",
            "source": "cat",
            "dest": "cat_fat",
            "conditions": "is_going_to_cat_fat",
        },
        {
            "trigger": "advance",
            "source": "cat",
            "dest": "cat_sick",
            "conditions": "is_going_to_cat_sick",
        },
        {
            "trigger": "advance",
            "source": "cat",
            "dest": "cat_vaccine",
            "conditions": "is_going_to_cat_vaccine",
        },
        {
            "trigger": "advance",
            "source": "cat",
            "dest": "cat_parasite",
            "conditions": "is_going_to_cat_parasite",
        },
        {
            "trigger": "advance",
            "source": "dog_fat",
            "dest": "dog_too_fat",
            "conditions": "is_going_to_dog_too_fat",
        },
        {
            "trigger": "advance",
            "source": "dog_fat",
            "dest": "dog_too_thin",
            "conditions": "is_going_to_dog_too_thin",
        },
        {
            "trigger": "advance",
            "source": "dog_fat",
            "dest": "dog_median",
            "conditions": "is_going_to_dog_median",
        },
        {
            "trigger": "advance",
            "source": "dog_sick",
            "dest": "dog_heart",
            "conditions": "is_going_to_dog_heart",
        },
        {
            "trigger": "advance",
            "source": "dog_sick",
            "dest": "dog_infectious",
            "conditions": "is_going_to_dog_infectious",
        },
        {
            "trigger": "advance",
            "source": "dog_sick",
            "dest": "dog_cancer",
            "conditions": "is_going_to_dog_diabete",
        },
        {
            "trigger": "advance",
            "source": "dog_sick",
            "dest": "dog_kidney",
            "conditions": "is_going_to_dog_kidney",
        },
        {
            "trigger": "advance",
            "source": "cat_fat",
            "dest": "cat_too_fat",
            "conditions": "is_going_to_cat_too_fat",
        },
        {
            "trigger": "advance",
            "source": "cat_fat",
            "dest": "cat_too_thin",
            "conditions": "is_going_to_cat_too_thin",
        },
        {
            "trigger": "advance",
            "source": "cat_fat",
            "dest": "cat_median",
            "conditions": "is_going_to_cat_median",
        },
        {
            "trigger": "advance",
            "source": "cat_sick",
            "dest": "cat_tooth",
            "conditions": "is_going_to_cat_tooth",
        },
        {
            "trigger": "advance",
            "source": "cat_sick",
            "dest": "cat_liver",
            "conditions": "is_going_to_cat_liver",
        },
        {
            "trigger": "advance",
            "source": "cat_sick",
            "dest": "cat_cancer",
            "conditions": "is_going_to_cat_cancer",
        },
        {
            "trigger": "advance",
            "source": "cat_sick",
            "dest": "cat_kidney",
            "conditions": "is_going_to_cat_kidney",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if event.message.text.lower() == 'fsm':
                url='https://imgur.com/aispSB6.jpg'
                send_image_message(event.reply_token,url)
            else :
                send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
