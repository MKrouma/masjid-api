import os
from api import create_app
from waitress import serve
from dotenv import load_dotenv
# from api.cores.extens import db
# from api.models.users import User, Role

# load env
load_dotenv(override=True)
mode = os.getenv('FLASK_ENV')
print(f"Running in {mode} mode...")

# app
app = create_app(config_name=mode)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    serve(app, host='0.0.0.0', port=port)
