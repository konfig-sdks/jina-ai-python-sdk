<div align="center">

[![Visit Jina ai](./header.png)](https://jina.ai)

# Jina ai<a id="jina-ai"></a>

This is the UniversalAPI to access all the Jina embedding models


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`jinaai.bulk_embeddings.download_result_post`](#jinaaibulk_embeddingsdownload_result_post)
  * [`jinaai.bulk_embeddings.get_job`](#jinaaibulk_embeddingsget_job)
  * [`jinaai.bulk_embeddings.upload_file_and_get_embeddings`](#jinaaibulk_embeddingsupload_file_and_get_embeddings)
  * [`jinaai.embeddings.create_representation`](#jinaaiembeddingscreate_representation)
  * [`jinaai.health.check_status`](#jinaaihealthcheck_status)
  * [`jinaai.multi_embeddings.generate_embeddings`](#jinaaimulti_embeddingsgenerate_embeddings)
  * [`jinaai.rerank.pair_ranking`](#jinaairerankpair_ranking)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Jina%20AI&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from jina_ai_python_sdk import JinaAi, ApiException

jinaai = JinaAi()

try:
    # Download Result
    download_result_post_response = jinaai.bulk_embeddings.download_result_post(
        job_id="job_id_example",
    )
    print(download_result_post_response)
except ApiException as e:
    print("Exception when calling BulkEmbeddingsApi.download_result_post: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from jina_ai_python_sdk import JinaAi, ApiException

jinaai = JinaAi()


async def main():
    try:
        # Download Result
        download_result_post_response = (
            await jinaai.bulk_embeddings.adownload_result_post(
                job_id="job_id_example",
            )
        )
        print(download_result_post_response)
    except ApiException as e:
        print("Exception when calling BulkEmbeddingsApi.download_result_post: %s\n" % e)
        pprint(e.body)
        if e.status == 422:
            pprint(e.body["detail"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from jina_ai_python_sdk import JinaAi, ApiException

jinaai = JinaAi()

try:
    # Download Result
    download_result_post_response = jinaai.bulk_embeddings.raw.download_result_post(
        job_id="job_id_example",
    )
    pprint(download_result_post_response.body)
    pprint(download_result_post_response.body["id"])
    pprint(download_result_post_response.body["download_url"])
    pprint(download_result_post_response.headers)
    pprint(download_result_post_response.status)
    pprint(download_result_post_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BulkEmbeddingsApi.download_result_post: %s\n" % e)
    pprint(e.body)
    if e.status == 422:
        pprint(e.body["detail"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `jinaai.bulk_embeddings.download_result_post`<a id="jinaaibulk_embeddingsdownload_result_post"></a>

Download Result

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_result_post_response = jinaai.bulk_embeddings.download_result_post(
    job_id="job_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DownloadResultResponse`](./jina_ai_python_sdk/pydantic/download_result_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bulk-embeddings/{job_id}/download-result` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.bulk_embeddings.get_job`<a id="jinaaibulk_embeddingsget_job"></a>

Retrieve Job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_response = jinaai.bulk_embeddings.get_job(
    job_id="job_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BulkEmbeddingJobResponse`](./jina_ai_python_sdk/pydantic/bulk_embedding_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bulk-embeddings/{job_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.bulk_embeddings.upload_file_and_get_embeddings`<a id="jinaaibulk_embeddingsupload_file_and_get_embeddings"></a>

Upload a file and get embeddings for each row

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_file_and_get_embeddings_response = (
    jinaai.bulk_embeddings.upload_file_and_get_embeddings(
        file=open("/path/to/file", "rb"),
        model="string_example",
        email="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

##### model: `str`<a id="model-str"></a>

##### email: `str`<a id="email-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BodyStartBulkEmbeddingV1BulkEmbeddingsPost`](./jina_ai_python_sdk/type/body_start_bulk_embedding_v1_bulk_embeddings_post.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BulkEmbeddingJobResponse`](./jina_ai_python_sdk/pydantic/bulk_embedding_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/bulk-embeddings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.embeddings.create_representation`<a id="jinaaiembeddingscreate_representation"></a>

Create embedding representations of the given input texts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_representation_response = jinaai.embeddings.create_representation(
    body={
        "model": "jina-embeddings-v2-base-en",
        "input": ["string_example"],
        "encoding_format": "float",
    },
    model="clip",
    input=[
        {
            "id": "c801ec96945569130923f081d9dd5e8e",
        }
    ],
    encoding_format="float",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: `str`<a id="model-str"></a>

The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 

##### input: Union[List[`ImageDoc`], `ImageDoc`]<a id="input-unionlistimagedoc-imagedoc"></a>


List of images to embed

##### encoding_format: `str`<a id="encoding_format-str"></a>

The format in which you want the embeddings to be returned.Possible value are `float` and `base64`. Defaults to `float`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmbeddingsCreateRepresentationRequest`](./jina_ai_python_sdk/type/embeddings_create_representation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ModelEmbeddingOutput`](./jina_ai_python_sdk/pydantic/model_embedding_output.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/embeddings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.health.check_status`<a id="jinaaihealthcheck_status"></a>

Get the health of this Gateway service.
.. # noqa: DAR201

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
check_status_response = jinaai.health.check_status()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.multi_embeddings.generate_embeddings`<a id="jinaaimulti_embeddingsgenerate_embeddings"></a>

Create embedding representations of the given input texts.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_embeddings_response = jinaai.multi_embeddings.generate_embeddings(
    model="jina-colbert-v1-en",
    input=["string_example"],
    input_type="document",
    encoding_format="float",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: `str`<a id="model-str"></a>

The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 

##### input: Union[`List[str]`, `str`, List[`ApiSchemasEmbeddingTextDoc`], `ApiSchemasEmbeddingTextDoc`]<a id="input-unionliststr-str-listapischemasembeddingtextdoc-apischemasembeddingtextdoc"></a>


List of texts to embed

##### input_type: `str`<a id="input_type-str"></a>

Type of the embedding to compute, query or document

##### encoding_format: `str`<a id="encoding_format-str"></a>

The format in which you want the embeddings to be returned.Possible value are `float` and `base64`. Defaults to `float`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApiSchemasMultiEmbeddingsTextEmbeddingInput`](./jina_ai_python_sdk/type/api_schemas_multi_embeddings_text_embedding_input.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ColbertModelEmbeddingsOutput`](./jina_ai_python_sdk/pydantic/colbert_model_embeddings_output.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/multi-embeddings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `jinaai.rerank.pair_ranking`<a id="jinaairerankpair_ranking"></a>

Rank pairs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pair_ranking_response = jinaai.rerank.pair_ranking(
    model="jina-reranker-v1-base-en",
    query="string_example",
    documents=["string_example"],
    top_n=1,
    return_documents=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### model: `str`<a id="model-str"></a>

The identifier of the model.  Available models and corresponding param size and dimension: - `jina-embedding-t-en-v1`, 14m, 312 - `jina-embedding-s-en-v1`, 35m, 512 (default) - `jina-embedding-b-en-v1`, 110m, 768 - `jina-embedding-l-en-v1`, 330, 1024  For more information, please checkout our [technical blog](https://arxiv.org/abs/2307.11224). 

##### query: Union[`str`, `ApiSchemasRankTextDoc`]<a id="query-unionstr-apischemasranktextdoc"></a>


The search query

##### documents: Union[`List[str]`, List[`ApiSchemasRankTextDoc`]]<a id="documents-unionliststr-listapischemasranktextdoc"></a>


A list of text documents or strings to rerank. If a document is provided the text fields is required and all other fields will be preserved in the response.

##### top_n: `int`<a id="top_n-int"></a>

The number of most relevant documents or indices to return, defaults to the length of `documents`

##### return_documents: `bool`<a id="return_documents-bool"></a>

If false, returns results without the doc text - the api will return a list of {index, relevance score} where index is inferred from the list passed into the request. If true, returns results with the doc text passed in - the api will return an ordered list of {index, text, relevance score} where index + text refers to the list passed into the request. Defaults to true

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TextRankInput`](./jina_ai_python_sdk/type/text_rank_input.py)
#### 🔄 Return<a id="🔄-return"></a>

[`RankingOutput`](./jina_ai_python_sdk/pydantic/ranking_output.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/rerank` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
