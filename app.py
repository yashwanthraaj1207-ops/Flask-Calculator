from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calculate(expression):
    try:
        stack = []
        num = 0
        sign = '+'

        for i in range(len(expression)):
            ch = expression[i]

            # build number
            if ch.isdigit():
                num = num * 10 + int(ch)

            # process when operator or last character
            if ch in "+-*/" or i == len(expression) - 1:

                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    if num == 0:
                        return "Error"
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)

                sign = ch
                num = 0

        return sum(stack)

    except:
        return "Error"


@app.route('/calculate', methods=['POST'])
def calc_api():
    data = request.get_json()

    if not data or 'expression' not in data:
        return jsonify({'result': 'Error'})

    expression = data.get('expression', '').replace(" ", "")

    if expression == "":
        return jsonify({'result': 'Error'})

    result = calculate(expression)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)