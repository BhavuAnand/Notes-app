from website import create_app

app = create_app()

if __name__ == '__main__':
    # Allow connections from any IP address and use port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
