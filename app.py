from flask import Flask, render_template, request
from generate import *

app = Flask(__name__)

@app.route('/')
def view_home():
    """Home Page"""
    return render_template('main.html')

@app.route('/about')
def view_about():
    """About Page"""
    return render_template('about.html')

@app.route('/generate', methods=['POST'])
def view_pattern():
    """View Generated alankar on the Home Page"""
    if request.method == 'POST':
        num_notes = int(request.form['NumNotes'])
        num_bars = int(request.form['Length'])
        pattern = alankar_generator(num_notes, num_bars)
        result = {
            'pattern' : pattern
        }
    return render_template('main.html', result=result)
    # else : 
    #     return redirect('main_html')

if __name__ == "__main__":
    app.run(debug=True)


    