import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="samplefuncapp", auth_level=func.AuthLevel.FUNCTION)
def samplefuncapp(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. Now using Azure Key Vault to access secrets to deployed to Azure Function App", status_code=200)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )