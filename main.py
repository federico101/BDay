from web import app 

site = app()

if __name__ == '__main__':
    site.run(debug=False, host="0,0,0,0")
