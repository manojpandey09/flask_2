from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/manoj')
def manoj():
    return 'you are great, Manoj!'




# **********render_template**********

from flask import Flask, render_template


@app.route('/show')
def show_page():
    return render_template('show.html')



@app.route('/pandey')
def pandey_page():
    return render_template('pandey.html')





# **********request**********

from flask import Flask, request

@app.route('/ask')
def ask_name():
    name = request.args.get('name')
    return f"Hello {name}, data URL se aaya hai"




# **********redirect********

from flask import Flask, redirect



@app.route('/first')
def first_page():
    return redirect('/second')

@app.route('/second')
def second_page():
    return "Tum first se yahan bhej diye gaye ho"


# **********url_for**********
from flask import Flask, url_for



@app.route('/')
def home():
    link = url_for('profile')
    return f"Profile page ka address hai: {link}"

@app.route('/profile')
def profile():
    return "Ye profile page hai"








if __name__ == '__main__':
    app.run(debug=True)