from flask import Flask, render_template, request

app = Flask(__name__)


# Rendering starting page with infromation and start button
@app.route('/')
def start_page():
    return render_template('start.html')


# Rendering guess page then checking is PC guess user number
@app.route('/guess', methods=["GET", "POST"])
def guess_page():
    min_number = 0
    max_number = 1000
    guess = int((max_number - min_number) / 2) + min_number

    if request.method == "GET":
        return render_template('guess.html', min=min_number, max=max_number, guess=guess)
    else:
        user_answer = request.form['user_answer']
        min_number = int(request.form['min'])
        max_number = int(request.form['max'])
        guess = int(request.form['guess'])

        print(user_answer, min_number, max_number)

        if user_answer == 'you win':
            return f"I guessed you number!"
        else:
            if user_answer == 'to big':
                max_number = guess
            elif user_answer == 'to small':
                min_number = guess
            else:
                return f"Stop cheating!"

            guess = int((max_number - min_number) / 2) + min_number
            return render_template('guess.html', min=min_number, max=max_number, guess=guess)


if __name__ == '__main__':
    app.run(debug=True)
