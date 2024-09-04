from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse


from routes import etl_scord2

load_dotenv()

app = FastAPI(
  title="API Monitoreo",
  version="1.0",
  description="Monitoreo Actualizacion ETLs",
  contact={
    "name":"Daniel Calcina",
    "email": "danielnahuncalcinafuentes@gmail.com"
  },
  # swagger_ui_parameters={"filter: ''"}
)

app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_credentials = True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.get("/", include_in_schema=False)
def main():
  return RedirectResponse(url="/docs")

app.include_router(etl_scord2.route_etl, prefix='/api/etl_scord2')