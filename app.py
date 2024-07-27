from flask import Flask, render_template, request

app = Flask(__name__)

def power_set(s):
    result = [[]]
    for elem in s:
        result.extend([x + [elem] for x in result])
    # Sort each subset and then sort the entire list of subsets
    result = sorted([sorted(subset) for subset in result], key=lambda x: (len(x), x))
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input_set']
        input_set = user_input.split(',') if user_input else []
        input_set = [item.strip() for item in input_set]
        result = power_set(input_set)
        return render_template('index.html', result=result, input_set=user_input)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
