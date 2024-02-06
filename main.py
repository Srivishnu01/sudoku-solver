from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from SimpleEngine import Sudoku

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=["POST", "GET"])
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, world')  # Press Ctrl+F8 to toggle the breakpoint.


@app.route("/", methods=["GET"])
def load_home_page_simple():
    return send_file('home_page_simple.html')


@app.route("/solve-9-cross-9-sudoku", methods=["POST"])
def get_99_solved():
    s = Sudoku(request.json["game"])
    if (s.has_solution):
        response = {
            "success": True,
            "solution": s.arr,
            "message": "full solved"
        }
    else:
        response = {
            "success": False,
            "solution": None,
            "message": "Invalid input"
        }
    resp = jsonify(response)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
