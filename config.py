class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}


COMPLETIONS_MODEL = "text-davinci-003"
EMBEDDINGS_MODEL = "text-embedding-ada-002"
CHAT_MODEL = 'gpt-3.5-turbo'
TEXT_EMBEDDING_CHUNK_SIZE=300
VECTOR_FIELD_NAME='content_vector'

PREFIX = "skolodoc"
INDEX_NAME = "skolo-index"


