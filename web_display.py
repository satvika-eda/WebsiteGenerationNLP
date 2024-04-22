from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template that will be rendered by the Flask app

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Web Craft</title>
    <style>
        /* Flex container style */
        .flex-container {
            display: flex;
            flex-direction: row;
            align-items: start; /* Center items horizontally */
            justify-content: center; /* Center items vertically */
            height: 100%; /* Set the height of the container to viewport height */
            border-bottom: 1px solid #ccc;
            margin: 20px;
            padding: 20px;
        }
        /* Form container style */
        .form-container {
            margin-bottom: 20px;
        }
        /* Generated and Rendered HTML container style */
        .html-container {
            width: 50%;
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 20px;
            overflow-y: auto; /* Enable vertical scrolling if content exceeds container height */
        }
        .prompt-div {
            width: 40%;
            margin-right: 20px;
            border-right: 1px solid #ccc;
        }

        .generated-html {
            width: 60%;
            margin-left: 20px;
        }
        .rendered-html{
            border: 1px solid #ccc;
            padding: 10px;
            margin: 20px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
            overflow-y: auto; /* Enable vertical scrolling if content exceeds container height */
        }
    </style>
</head>
<body>
    <h1>Web Craft</h1>
    <div class='flex-container'>
        <div class='prompt-div'>
            <h2>Enter your prompt:</h2>
            <form action="/" method="post">
                <textarea name="prompt" rows="10" cols="50"></textarea><br>
                <input type="submit" value="Submit">
            </form>
        </div>
        <div class='generated-html'>
            
            <h2>Generated HTML:</h2>
            <pre style="white-space: pre-wrap;">{{ generated_html|escape }}</pre>
            
        </div>
    </div>
    <div>

        <h2>Rendered HTML:</h2>
        <div class='rendered-html'>{{ rendered_html|safe }}</div>
    </div>
</body>
</html>
"""

# Define the index route
@app.route('/', methods=['GET', 'POST'])
def index():
    generated_html = ''
    rendered_html = ''
    
    if request.method == 'POST':
        prompt = request.form['prompt']
        # here the model generated html will be placed by calling the model predict function from here and passing the prompt as an argument
        generated_html += '<!DOCTYPE html> <html> <head> <title>Zanzig.com Photo Hub - Photos From The Past</title> <style type="text/css"> body{ background-color: #F5F5FA; } .container{ max-width: 1200px; margin: 0 auto; padding: 20px; } .header{ text-align: center; margin-bottom: 20px; } .photo{ display: inline-block; width: 30%; margin-bottom: 20px; } img{ width: 100%; height: auto; } </style> </head> <body> <div class="container"> <div class="header"> <h1>Zanzig.com Photo Hub - Photos From The Past</h1> <p>Browse through our selection of classic photos from the past.</p> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?1" alt="Photo From The Past"> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?2" alt="Photo From The Past"> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?3" alt="Photo From The Past"> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?4" alt="Photo From The Past"> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?5" alt="Photo From The Past"> </div> <div class="photo"> <img src="https://source.unsplash.com/random/200x200?6" alt="Photo From The Past"> </div --> -->'
        
        # Render the HTML
        rendered_html = render_template_string(generated_html)
        
    return render_template_string(html_template, generated_html=generated_html, rendered_html=rendered_html)

if __name__ == '__main__':
    app.run(debug=True)
