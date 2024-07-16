from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

digimons_list = [
    {"name": "Agumon", "level": "Child", "type": "Reptile", "description": "A brave and adventurous Digimon.", "image_url": "https://wikimon.net/images/thumb/7/72/Agumon.jpg/640px-Agumon.jpg"},
    {"name": "Gabumon", "level": "Child", "type": "Reptile", "description": "A Digimon that wears a fur pelt.", "image_url": "https://wikimon.net/images/7/71/Gabumon.jpg"},
]

@app.route('/')  #the defaut method is GET
def home():
    return render_template('home.html', digimons = digimons_list)

@app.route('/add', methods =['GET', 'POST'])
def add_digimon():
    if request.method == 'POST':
        #handle the form submission
        name_from_form = request.form.get('name')
        level_from_form = request.form.get('level')
        type_from_form = request.form.get('type')
        description_from_form = request.form.get('description')
        image_url_from_form = request.form.get('image_url')
            #put the data from the form to our list
        digimons_list.append({"name": name_from_form, "level":level_from_form, "type": type_from_form, "description": description_from_form, "image_url": image_url_from_form})
        return redirect(url_for('home'))
   #handle the display
    return render_template('add_digimon.html')

if __name__ == '__main__':
    app.run()