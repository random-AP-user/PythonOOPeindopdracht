from jinja2 import Template

def buildWebsite(data):
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Table</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="reset.css">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        {% for group in data %}
        <div>
            <h2>{{ group.name }} (Seats: {{ group.seats }})</h2>
            <table>
                <tr>
                    <th>Kandidaten</th>
                    <th>ranglijst + votes</th>
                    <th>Stemmen</th>
                    <th>zetels</th>
                </tr>
                {% for candidate in group.chosencandidates %}
                    <tr>
                        <td>{{ candidate.candidate }}</td>
                        <td>{{ candidate.totalRank }}</td>
                        <td>{{ candidate.votes }}</td>
                        <td>{{ candidate.seats }}</td>
                    </tr>
                {% endfor %}
            </table>
        </div>
        {% endfor %}
    </body>
    </html>
    """

    jinja_template = Template(template)
    rendered_html = jinja_template.render(data=data)

    with open("./index.html", "w") as f:
        f.write(rendered_html)
