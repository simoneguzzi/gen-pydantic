import yaml

from fastapi import FastAPI, Request, HTTPException
from linkml.generators.pydanticgen import PydanticGenerator
from linkml_runtime.linkml_model.meta import SchemaDefinition


app = FastAPI()


@app.post(
    "/gen-pydantic/",
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
    generator = PydanticGenerator(schema=SchemaDefinition(**data))
    pydantic_model = generator.serialize()
    return pydantic_model
