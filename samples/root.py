# Usage snippet provided for createDataset
import leonardoaisdk
from leonardoaisdk.models import operations, shared

s = leonardoaisdk.LeonardoAiSDK(
    bearer_auth="",
)

req = operations.CreateDatasetRequestBody(
    name='string',
)

res = s.dataset.create_dataset(req)

if res.create_dataset_200_application_json_object is not None:
    # handle response
    pass