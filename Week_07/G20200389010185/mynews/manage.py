from app import app
from flask import Flask
from flask_script import Manager

manager = Manager(app)

# @manager.command
# def dev():
#     from livereload import Server
#     live_server = Server(app.wsgi_app)
#     live_server.watch("**/*.*")
#     live_server.serve(open_url=True)

if __name__ == "__main__":
    app.run()
