import os
EMBED_MODEL = os.getenv('EMBED_MODEL','intfloat/multilingual-e5-base')
VECTOR_DB = os.getenv('VECTOR_DB','faiss')
METADATA_DB = os.getenv('METADATA_DB','sqlite')
PDF_DIR = os.getenv('PDF_DIR','data/raw/samples')
