from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/')
def users():
  names = ['Craig', 'Thomas', 'Lee', 'Jamie', 'Syl']
  return render_template('collections.html', names=names)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
