from flask import Flask, render_template, json, request
app = Flask(__name__)

@app.route("/")
def main ():
    return render_template ('index.html')

@app.route('/calc')
def calcSum ():
    # receive values and validate them
    num1 = 0
    num2 = 0
    try:
        num1 = int (request.args.get ("number1", ''))
        num2 = int (request.args.get ("number2", ''))
    except:
        return "Error, you didn't input valid numbers";
     
    res = request.args.get ("result", '')
    if res != "":
        try:
            res = int (res)
            answer = str (str (num1 + num2) + " != " + str (res))
            return answer
        except:
            return str (int (num1 + num2))
    else:
        return str (int (num1 + num2))

if __name__ == "__main__":
    app.run ()
