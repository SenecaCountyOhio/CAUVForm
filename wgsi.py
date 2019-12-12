from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host='192.168.26.116',
        debug=False,
        port=5000,
        threaded=True,
    )
