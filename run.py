from app import create_app

flask_appp = create_app()

if __name__ == '__main__':
  flask_appp.run(host='0.0.0.0', debug=True)