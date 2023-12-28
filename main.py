

if __name__ == '__main__':

    import uvicorn
    from config.config import SERVER_PORT
    uvicorn.run(app='api.app:app',
                reload=True,
                host='127.0.0.1',
                port=SERVER_PORT,
                workers=1)