import yaml

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from linkml.generators.pydanticgen import PydanticGenerator
from linkml.linter.linter import Linter
from linkml.linter.formatters import JsonFormatter
from fastapi.responses import FileResponse, Response
from linkml_runtime.linkml_model.meta import SchemaDefinition


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post(
    "/api/gen-pydantic/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml"},
            "required": True,
        },
    },
)
async def gen_pydantic(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")
    
    try:
        schema = SchemaDefinition(**data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

    generator = PydanticGenerator(schema=schema)
    pydantic_model = generator.serialize()
    
    with open('pydantic_model.py', 'w') as f:
        f.write(pydantic_model)

    return FileResponse('pydantic_model.py', media_type='application/octet-stream', filename='pydantic_model.py')

@app.post(
    "/api/validate-linkml/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml"},
            "required": True,
        },
    },
)
async def validate_linkml(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")

    with open('schema.yaml', 'w') as f:
        f.write(yaml.dump(data))
    
    problems =  Linter.validate_schema('schema.yaml')

    with open('report.json', 'w') as f:
        formatter = JsonFormatter(f)
        formatter.start_report()
        for problem in problems:
            formatter.handle_problem(problem)
        formatter.end_report()

        return FileResponse('report.json', media_type='application/json', filename='report.json')
