# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from jina_ai_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_EMBEDDINGS = "/v1/embeddings"
    V1_BULKEMBEDDINGS = "/v1/bulk-embeddings"
    V1_BULKEMBEDDINGS_JOB_ID = "/v1/bulk-embeddings/{job_id}"
    V1_BULKEMBEDDINGS_JOB_ID_DOWNLOADRESULT = "/v1/bulk-embeddings/{job_id}/download-result"
    V1_RERANK = "/v1/rerank"
    V1_MULTIEMBEDDINGS = "/v1/multi-embeddings"
    _ = "/"
