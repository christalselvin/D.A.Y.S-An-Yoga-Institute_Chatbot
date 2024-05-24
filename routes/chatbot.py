from flask import request, jsonify, Response, current_app as app
import re
import random

# Set the name of the bot
BOT_NAME = "jery"

R_EATING = f"I don't like eating anything because I'm a {BOT_NAME} obviously!"
R_ADVICE = f" Stay focused and constantly moving to make your dreams come true!"

# Define a dictionary to store predefined answers for specific questions
THINK_ANSWERS = {
    "what is the meaning of life?": "The meaning of life is a philosophical question concerning the significance of life or existence in general.",
    "what is the capital of France?": "The capital of France is Paris.",
    "how does the internet work?": "The internet is a global network of interconnected computers that communicate via standardized protocols.",
    # Add more question-answer pairs as needed
}


def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    message_certainty = 0

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    if required_words:
        if isinstance(required_words, list):  # Check if required_words is a list
            has_required_words = all(word in user_message for word in required_words)
        else:
            has_required_words = False
    else:
        has_required_words = True

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=None):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response(f'How can I help you, I\'m {BOT_NAME}!', ['hello', 'hi', 'hey'], single_response=True)
    response('Jerry', ['name'], single_response=True)
    response('Check My Career Page', ['job', 'assignment'], single_response=True)
    response('Email:selvin472001@gmail.com', ['contact'], single_response=True)
    response(f'I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Love you too!', ['i', 'love', 'you'], required_words=True)
    response('my name is jery', ['name'], single_response=True)
    response("I'm happy to chat with you too!", ['Bye','thank', 'thanks','bye', 'goodbye'], single_response=True)
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response('CHRISTAL', ['build','generate','design'], single_response=True)
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return unknown() if highest_prob_list[best_match] < 1 else best_match


@app.route('/bot', methods=['POST'])
def bot_response():
    user_input = request.json.get('message', '')
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())

    # Check if the user asked a predefined question
    if user_input.lower() in THINK_ANSWERS:
        return jsonify({'response': THINK_ANSWERS[user_input.lower()]})

    response = check_all_messages(split_message)
    return jsonify({'response': response})


def unknown():
    response = [
                "What does that mean?"][
        random.randrange(4)]
    return response
