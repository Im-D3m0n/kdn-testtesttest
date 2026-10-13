from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():

    user_name = None

      if request.method == "POST":
        # Whatever the user types into the box gets saved here
        user_name = request.form.get("visitor_name") 

     return render_template("index.html", name=user_name)


if __name__ == "__main__":
    app.run(debug=True)