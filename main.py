from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-sarif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
          <form method="post" action="/">
              <label for="rotation_amount"><b>Rotate by:</b>
              <input type="text" id="rotation_amount" name="rot" value="0" />
              </label>
              <textarea name="text">{0}</textarea>
              <input type="submit" value="Submit Query" />
        </body>
    </html>
    """

@app.route("/", methods=['POST'])    
def encrypt():
    user_text = request.form['text']
    rotation_amount = int(request.form['rot'])
    rotated_text = rotate_string(user_text, rotation_amount)

    return form.format(rotated_text)
    

@app.route("/")
def index():
    return form.format('')

app.run()