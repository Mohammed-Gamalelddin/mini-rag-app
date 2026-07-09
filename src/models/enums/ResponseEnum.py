from enum import Enum


class ResponseSignal(Enum):
    FILE_VALIDATION_SUCCESS = "file_validation_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDS = "file size exceeds"
    FILE_UPLOAD_SUCCESS = "file uploaded success"
    FILE_UPLOAD_FAILED = "file upload failed"
