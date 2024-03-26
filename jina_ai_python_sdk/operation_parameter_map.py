operation_parameter_map = {
    '/v1/bulk-embeddings/{job_id}/download-result-POST': {
        'parameters': [
            {
                'name': 'job_id'
            },
        ]
    },
    '/v1/bulk-embeddings/{job_id}-GET': {
        'parameters': [
            {
                'name': 'job_id'
            },
        ]
    },
    '/v1/bulk-embeddings-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'model'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/v1/embeddings-POST': {
        'parameters': [
            {
                'name': 'model'
            },
            {
                'name': 'input'
            },
            {
                'name': 'encoding_format'
            },
        ]
    },
    '/-GET': {
        'parameters': [
        ]
    },
    '/v1/multi-embeddings-POST': {
        'parameters': [
            {
                'name': 'model'
            },
            {
                'name': 'input'
            },
            {
                'name': 'input_type'
            },
            {
                'name': 'encoding_format'
            },
        ]
    },
    '/v1/rerank-POST': {
        'parameters': [
            {
                'name': 'model'
            },
            {
                'name': 'query'
            },
            {
                'name': 'documents'
            },
            {
                'name': 'top_n'
            },
            {
                'name': 'return_documents'
            },
        ]
    },
};