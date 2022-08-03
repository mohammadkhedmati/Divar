from datetime import datetime

import pytz

def sample_responses(user_input):

    input_text = str(user_input).lower()

    if input_text in ["تهران", "tehran"]:

        return input_text

        if input_text == ["توقف", "stop"]:
            return "stop"

        if input_text in ["date", "date?"]:

            date = datetime.now()

            return date.strftime('%d – %B – %Y')

        if input_text in ["bye", "ttyl", "good bye"]:

            return "It was nice chatting with you. Bye!"

    return "Sorry,I didn't understand you"

