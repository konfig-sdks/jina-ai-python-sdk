import typing_extensions

from jina_ai_python_sdk.apis.tags import TagValues
from jina_ai_python_sdk.apis.tags.bulk_embeddings_api import BulkEmbeddingsApi
from jina_ai_python_sdk.apis.tags.embeddings_api import EmbeddingsApi
from jina_ai_python_sdk.apis.tags.rerank_api import RerankApi
from jina_ai_python_sdk.apis.tags.multi_embeddings_api import MultiEmbeddingsApi
from jina_ai_python_sdk.apis.tags.health_api import HealthApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BULKEMBEDDINGS: BulkEmbeddingsApi,
        TagValues.EMBEDDINGS: EmbeddingsApi,
        TagValues.RERANK: RerankApi,
        TagValues.MULTIEMBEDDINGS: MultiEmbeddingsApi,
        TagValues.HEALTH: HealthApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BULKEMBEDDINGS: BulkEmbeddingsApi,
        TagValues.EMBEDDINGS: EmbeddingsApi,
        TagValues.RERANK: RerankApi,
        TagValues.MULTIEMBEDDINGS: MultiEmbeddingsApi,
        TagValues.HEALTH: HealthApi,
    }
)
