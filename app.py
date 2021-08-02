from flask import Flask, render_template
app = Flask(__name__)
playlists  =  [ 
    {  'title' :  'Cat Videos' ,  'description' :  'Cats agissant bizarrement'  }, 
    {  'title' :  '80  Music' ,  'description' :  'Don  « arrête pas de croire ! »'  } 
]

@app.route('/')
def index():
    """Return homepage."""
    #return 'Hello, world!'
    return render_template('home.html', msg='Flask is Cool!!')

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)