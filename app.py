from flask import Flask, render_template, request, redirect, url_for 
 
app = Flask(__name__) 
 
# Dummy function for recommendation logic def get_diet_recommendations(data): 
    # Replace with real logic     return { 
        "status": "Healthy", 
        "diet": [ 
            "Eat more fruits and vegetables", 
            "Reduce salt intake", 
            "Stay hydrated" 
        ] 
    } 
 
@app.route("/") def home():     return render_template("index.html") 
 
@app.route("/submit", methods=["POST"]) def submit():     user_data = { 
        "name": request.form["name"], 
        "age": request.form["age"], 
        "heart_rate": request.form["heart_rate"], 
        "blood_pressure": request.form["blood_pressure"], 
        "activity_level": request.form["activity"] 
    } 
    recommendations = get_diet_recommendations(user_data)     return render_template("result.html", name=user_data["name"], recommendations=recommendations) 
 
if __name__ == "__main__": 
    app.run(debug=True) 
