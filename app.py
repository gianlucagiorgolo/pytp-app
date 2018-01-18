from flask import Flask, request, render_template
from waitress import serve

import parser
import tp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        sequent_input = request.form['sequent']
        try:
            sequent = parser.parse(sequent_input)
            if type(sequent) is tp.Sequent:
                proof_results = tp.prove(sequent)
            else:
                proof_results = tp.prove(tp.Sequent(sequent.hypotheses, sequent.theorem, sequent.unlimitedResources),
                                         sequent.terms)
            return render_template('template.html', proofs=proof_results.to_html())
        except Exception:
            return render_template('template.html',
                                   error='Oops something went wrong, maybe you made a mistake entering the sequent?')
    else:
        return render_template('template.html')


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, channel_timeout=120)
    # serve(app, host='127.0.0.1', port=4000, channel_timeout=120)
