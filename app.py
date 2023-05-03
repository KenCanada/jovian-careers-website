from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Job1',
  'location': 'location1',
  'salary': 'salary1'
}, {
  'id': 2,
  'title': 'Job2',
  'location': 'location2',
  'salary': 'salary2'
}, {
  'id': 3,
  'title': 'Job3',
  'location': 'location3',
  'salary': 'salary3'
}, {
  'id': 4,
  'title': 'Job4',
  'location': 'location4',
  'salary': 'salary4'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="CompanyMe")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
