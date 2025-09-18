FROM python:3.11-slim
WORKDIR /app
COPY financial-rag-system/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY financial-rag-system /app/financial-rag-system
WORKDIR /app/financial-rag-system
CMD ['uvicorn','src.financial_rag.interfaces.api.fastapi_app:app','--host','0.0.0.0','--port','8000']
