import typing_extensions

from jina_ai_python_sdk.paths import PathValues
from jina_ai_python_sdk.apis.paths.v1_embeddings import V1Embeddings
from jina_ai_python_sdk.apis.paths.v1_bulk_embeddings import V1BulkEmbeddings
from jina_ai_python_sdk.apis.paths.v1_bulk_embeddings_job_id import V1BulkEmbeddingsJobId
from jina_ai_python_sdk.apis.paths.v1_bulk_embeddings_job_id_download_result import V1BulkEmbeddingsJobIdDownloadResult
from jina_ai_python_sdk.apis.paths.v1_rerank import V1Rerank
from jina_ai_python_sdk.apis.paths.v1_multi_embeddings import V1MultiEmbeddings
from jina_ai_python_sdk.apis.paths.root import Root

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_EMBEDDINGS: V1Embeddings,
        PathValues.V1_BULKEMBEDDINGS: V1BulkEmbeddings,
        PathValues.V1_BULKEMBEDDINGS_JOB_ID: V1BulkEmbeddingsJobId,
        PathValues.V1_BULKEMBEDDINGS_JOB_ID_DOWNLOADRESULT: V1BulkEmbeddingsJobIdDownloadResult,
        PathValues.V1_RERANK: V1Rerank,
        PathValues.V1_MULTIEMBEDDINGS: V1MultiEmbeddings,
        PathValues._: Root,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_EMBEDDINGS: V1Embeddings,
        PathValues.V1_BULKEMBEDDINGS: V1BulkEmbeddings,
        PathValues.V1_BULKEMBEDDINGS_JOB_ID: V1BulkEmbeddingsJobId,
        PathValues.V1_BULKEMBEDDINGS_JOB_ID_DOWNLOADRESULT: V1BulkEmbeddingsJobIdDownloadResult,
        PathValues.V1_RERANK: V1Rerank,
        PathValues.V1_MULTIEMBEDDINGS: V1MultiEmbeddings,
        PathValues._: Root,
    }
)
