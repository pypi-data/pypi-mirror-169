from .client import Client as _Client

_global_client: _Client = _Client(verbose=True)

get_devices = _global_client.get_devices
upload_model = _global_client.upload_model
get_models = _global_client.get_models
get_model = _global_client.get_model
submit_profile_job = _global_client.submit_profile_job
get_jobs = _global_client.get_jobs
get_job = _global_client.get_job
set_verbose = _global_client.set_verbose
upload_dataset = _global_client.upload_dataset
get_datasets = _global_client.get_datasets

__all__ = [
    "get_devices",
    "upload_model",
    "get_model",
    "get_models",
    "submit_profile_job",
    "get_job",
    "get_jobs",
    "set_verbose",
    "upload_dataset",
    "get_datasets",
]
