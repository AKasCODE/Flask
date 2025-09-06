from flask import Flask,render_template,request, redirect, url_for, flash
#request -- for reading data

app=Flask(__name__)
app.secret_key="flash"

@app.route("/", methods=["POST","GET"])
def feedback():
    if request.method=="POST":              #Check if the form is submitted or not
        name=request.form.get("username")   #Reading input data
        message=request.form.get("message")
        if not name:
            flash("Name can not be empty!")     #send msg to flask memory.
            return redirect(url_for("feedback"))    #redirect to route name
        flash(f"Thanks {name}, for your feedback!!")
        return render_template("thankyou.html",user=name,message=message)
    return render_template("feedback.html")
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__=="__main__":
    app.run(debug=True)
