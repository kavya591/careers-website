from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Benguluru, India',
    'salary': 'Rs. 10,00,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000',
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Hyderabad, India',
    'salary': 'Rs. 16,00,000',
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name='Career')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  