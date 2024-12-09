from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "secret-key-for-flask"

# Ruta de inicio
@app.route("/")
def home():
    return render_template("index.html")

# Configuración para la carpeta de carga de archivos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#  Asegurarse de que la carpeta "uploads" exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
#  Rutas para visitantes
@app.route("/visitante", methods=["GET", "POST"])
def visitante():
    if request.method == "POST":
        poliza = request.files.get("poliza")
        clausula = request.files.get("clausula")
        fecha_visita = request.form.get("fecha")
        alturas = request.form.get("alturas") == "on"

#  Guardar archivos PDF si se subieron
        if poliza:
            poliza.save(f"uploads/{poliza.filename}")
        if clausula:
            clausula.save(f"uploads/{clausula.filename}")

        flash("Información del visitante registrada correctamente.")
        return redirect(url_for("home"))

    return render_template("visitante.html")

# Rutas para trabajadores
@app.route("/trabajador", methods=["GET", "POST"])
def trabajador():
    if request.method == "POST":
        checklist = {
            "iluminacion": request.form.get("iluminacion"),
            "orden": request.form.get("orden"),
            "derrames": request.form.get("derrames")
        }
        condiciones_inseguras = request.form.get("condiciones_inseguras")
        actos_inseguros = request.form.get("actos_inseguros")
        observaciones = request.form.get("observaciones")
        
        # Procesar la información
        flash("Información del trabajador registrada correctamente.")
        return redirect(url_for("home"))
    
    return render_template("trabajador.html")

# Correr la aplicación
if __name__ == "__main__":
    app.run(debug=True)
