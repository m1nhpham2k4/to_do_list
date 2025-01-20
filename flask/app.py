from todolist import create_app
from os import name 

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
