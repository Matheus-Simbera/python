from flask import Flask

app = Flask(__name__)


@app.route('/decorator') 
def hello():
    return ''' 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Decorator em Python</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f9f9f9;
                color: #333;
                margin: 20px;
            }
            h1, h2 {
                color: #2e7d32; /* Verde escuro */
            }
            p {
                color: #388e3c; /* Verde médio */
            }
            code {
                background-color: #e8f5e9;
                padding: 2px 4px;
                border-radius: 4px;
                color: #2e7d32;
                font-family: "Courier New", Courier, monospace;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>O que é um Decorator em Python?</h1>
            <p>Um <strong>decorator</strong> em Python é uma função especial que permite modificar ou estender o comportamento 
            de outra função ou método sem alterar diretamente o código dela. Ele é amplamente utilizado para adicionar 
            funcionalidades de forma elegante e reutilizável.</p>

            <h2>Para que ele serve?</h2>
            <p>Decorators são usados para adicionar lógica antes ou depois da execução de uma função. Eles ajudam a 
            reutilizar código, adicionar validações, logar informações, ou até mesmo modificar o comportamento de funções 
            de forma prática e organizada.</p>

            <h2>Como ele é utilizado no Flask?</h2>
            <p>No Flask, decorators são usados para associar rotas HTTP a funções que tratam essas rotas. Por exemplo, 
            o decorator <code>@app.route('/decorator')</code> associa a URL <code>/decorator</code> à função <code>hello</code>, 
            que será executada quando essa rota for acessada.</p>

            <h2>Exemplo no Flask:</h2>
            <p>Veja o exemplo abaixo:</p>
            <code>
                @app.route('/exemplo')<br>
                def exemplo():<br>
                &nbsp;&nbsp;&nbsp;&nbsp;return "Essa é uma rota de exemplo!"
            </code>
        </div>
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(debug=True)
