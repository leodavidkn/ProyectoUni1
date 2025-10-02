from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Proyecto DevOps</title>
        <style>
            body {
                background: linear-gradient(to right, #1c92d2, #f2fcfe);
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
                color: #333;
            }
            .card {
                background-color: #ffffffbb;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                display: inline-block;
                max-width: 600px;
            }
            h1 {
                font-size: 32px;
                color: #1c92d2;
            }
            h2 {
                font-size: 24px;
                margin-top: 20px;
                color: #444;
            }
            p {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Automatización de Infraestructura Digital II</h1>
            <h2>Proyecto</h2>
            <p><strong>Alumno:</strong> Leonardo David Salazar Mora</p>
            <p><strong>Profesor:</strong> Froylan Alonso Pérez Alanís</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)