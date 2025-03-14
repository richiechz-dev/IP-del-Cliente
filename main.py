from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

lista = ["Huevo", "Pollo", "Arroz", "Lechuga"]

@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response( redirect("/show_information_adress"))
    response.set_cookie("user_ip_information", user_ip_information)
    return response

@app.route("/show_information_adress")
def show():
    user_ip = request.cookies.get("user_ip_information")
    context = {
        "user_ip":user_ip,
        "lista":lista
    }
    return render_template("ip_template.html", **context)

app.run(host='0.0.0.0', port=81, debug=True)