from enum import Enum


class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "FILE_VALIDATED_SUCCESS"
    FILE_TYPE_NOT_SUPPORTED = "FILE_TYPE_NOT_SUPPORTED"
    FILE_SIZE_EXCEEDED = "FILE_SIZE_EXCEEDED"
    FILE_UPLOAD_SUCCESS = "FILE_UPLOAD_SUCCESS"
    FILE_UPLOAD_FAIL = "FILE_UPLOAD_FAIL"
    PROCESSING_SUCCESS = "processing_success"
    PROCESSING_FAIL = "processing_failed"
    NO_FILES_ERROR = "not_found_files"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    PROJECT_NOT_FOUND = "project_not_found"
    INSERT_INTO_VECTOR_DB_ERROR = "insert_into_vector_db_error"
    INSERT_INTO_VECTOR_DB_SUCCESS = "insert_into_vector_db_success"
    VECTORDB_COLLECTION_RETRIEVED = "vectordb_collection_retrieved"
    VECTORDB_SEARCH_ERROR = "vectordb_search_error"
    VECTORDB_SEARCH_SUCCESS = "vectordb_search_success"
    RAG_ANSWER_ERROR = "rag_answer_error"
    RAG_ANSWER_SUCCESS = "rag_answer_success"