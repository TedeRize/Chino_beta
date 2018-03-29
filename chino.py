# coding: UTF-8

import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = os.environ.get("token")

def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'ja'  # optional, default value equal 'en'

    print("文字を入力してください")

    input_word = sys.stdin.readline()

    request.session_id = '<SESSION ID, UNIQUE FOR EACH USER>'

    request.query =  input_word

    response = request.getresponse()

    print (response.read())

if __name__ == '__main__':
    main()