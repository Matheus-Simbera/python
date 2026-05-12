from flask import Flask

app = Flask(__name__)

@app.route('/curriculo') 
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo - Matheus Fleming</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                background-color: #f9f9f9;
                color: #333;
                margin: 20px;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            h1, h2 {
                color: #2e7d32; /* Verde escuro */
            }
            p, li {
                color: #388e3c; /* Verde médio */
            }
            ul {
                padding-left: 20px;
            }
            .section {
                margin-bottom: 20px;
            }
            .contact-info {
                margin-bottom: 20px;
            }
            .contact-info p {
                margin: 5px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Matheus Fleming de Freitas Simbera</h1>
            <div class="contact-info">
                <p><strong>Brasileiro, Cursando 3º ano</strong></p>
                <p>Rua dos Bandolins, nº 215 (apt. 906), Conjunto Califórnia 1, Belo Horizonte</p>
                <p>Email: matheussimbera.x@gmail.com | Telefone: +55 (31) 9 9988-8409</p>
            </div>

            <div class="section">
                <h2>Formação Acadêmica</h2>
                <ul>
                    <li><strong>COTEMIG - COLÉGIO TÉCNICO</strong>
                        <ul>
                            <li>Ensino Médio integrado ao Curso Técnico em Programação/Informática</li>
                            <li>Previsão de Conclusão: 2024/2026</li>
                        </ul>
                    </li>
                    <li><strong>COLÉGIO SANTA MARIA MINAS</strong>
                        <ul>
                            <li>Belo Horizonte (Unidades Floresta e Coração Eucarístico)</li>
                            <li>Ensino Fundamental I e II</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="section">
                <h2>Experiência Profissional</h2>
                <ul>
                    <li><strong>Analista Administrativo</strong>
                        <ul>
                            <li>CLINICA MEDICA E PSICOLOGICA CHMED LTDA</li>
                            <li>Período: 2024/2025</li>
                        </ul>
                    </li>
                    <li><strong>Trabalho Voluntário</strong>
                        <ul>
                            <li>Monitor Code Club 2026</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="section">
                <h2>Habilidades e Competências</h2>
                <ul>
                    <li>Programação: Python, C#, HTML/CSS, JavaScript, MYSQL, PHP</li>
                    <li>Ferramentas: Ferramentas Google, Figma, Pacote Office</li>
                    <li>Conhecimentos: Hardware, Robótica (Básica), Manutenção e montagem de computadores</li>
                    <li>Soft Skills: Facilidade de Comunicação, Adaptabilidade, Trabalho em equipe, Facilidade de Aprendizado</li>
                </ul>
            </div>

            <div class="section">
                <h2>Objetivo</h2>
                <p>Estudante de Tecnologia em busca de oportunidades para aplicar e aprimorar meus conhecimentos. Tenho como objetivo crescer profissionalmente, contribuindo com dedicação, proatividade e minhas habilidades técnicas.</p>
            </div>

            <div class="section">
                <h2>Idiomas</h2>
                <ul>
                    <li>Português: Nativo</li>
                    <li>Inglês: Avançado</li>
                    <li>Espanhol: Médio</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)