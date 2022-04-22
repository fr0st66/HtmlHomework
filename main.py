
from turtle import title
from myWeb import create_app
from myWeb.models import Recipe

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

