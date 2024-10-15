# Pydantic

## Run locally

1. Install requirements:

   ```shell
   pip install -r requirements.txt
   ```

2. If you plan on using the openapi features, set the required environment
   variables:

   ```shell
   export OPENAI_API_KEY=sk-proj-0123456789ABCDEF
   export OPENAI_THREAD_ID=thread_0123456789ABCDEF
   export OPENAI_ASSISTANT_ID=asst_0123456789ABCDEF
   ```

3. Run the application:

   ```shell
   fastapi dev main.py
   ```
