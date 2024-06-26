#  Copyright 2024 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""BigTable connection"""
from typing import List, Optional

from google.cloud.storage import Client

from metadata.generated.schema.entity.automations.workflow import (
    Workflow as AutomationWorkflow,
)
from metadata.generated.schema.entity.services.connections.storage.gcsConnection import (
    GcsConnection,
)
from metadata.generated.schema.security.credentials.gcpValues import (
    GcpCredentialsValues,
    SingleProjectId,
)
from metadata.ingestion.connections.test_connections import (
    SourceConnectionException,
    test_connection_steps,
)
from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.ingestion.source.storage.gcs import MultiProjectClient
from metadata.utils.credentials import set_google_credentials
from metadata.utils.logger import ingestion_logger

logger = ingestion_logger()


def get_connection(connection: GcsConnection):
    set_google_credentials(connection.credentials)
    project_ids = None
    if isinstance(connection.credentials.gcpConfig, GcpCredentialsValues):
        project_ids = (
            [connection.credentials.gcpConfig.projectId.__root__]
            if isinstance(connection.credentials.gcpConfig.projectId, SingleProjectId)
            else connection.credentials.gcpConfig.projectId.__root__
        )
    return MultiProjectClient(client_class=Client, project_ids=project_ids)



class Tester:

    def __init__(self, client: MultiProjectClient):
        self.client = client
        self.project_id = None
        self.instance = None
        self.buckets = None

    def test_buckets(connection: GCSConnection, client: GCSObjectStoreClient):
        if connection.bucketNames:
            for bucket_name in connection.bucketNames:
                client.client.list_objects(Bucket=bucket_name)
            return
        client.g.list_buckets()

    # def list_instances(self):
    #     self.project_id = list(self.client.clients.keys())[0]
    #     instances = list(self.client.list_instances(project_id=self.project_id))
    #     self.instance = get_nested_index(instances, [0, 0])

    def list_buckets(self):
        if not self.instance:
            raise SourceConnectionException(
                f"No instances found in project {self.project_id}"
            )
        buckets = list(self.instance.list_buckets())
        self.buckets = buckets[0]

    # def get_row(self):
    #     if not self.table:
    #         raise SourceConnectionException(
    #             f"No tables found in project {self.instance.project_id} and instance {self.instance.instance_id}"
    #         )
    #     self.table.read_rows(limit=1)


def test_connection(
    metadata: OpenMetadata,
    client: MultiProjectClient,
    service_connection: GcsConnection,
    automation_workflow: Optional[AutomationWorkflow] = None,
) -> None:
    """
    Test connection. This can be executed either as part
    of a metadata workflow or during an Automation Workflow
    """
    tester = Tester(client)

    test_fn = {
        "GetInstances": tester.list_instances,
        "GetTables": tester.list_tables,
        "GetRows": tester.get_row,
    }

    test_connection_steps(
        metadata=metadata,
        test_fn=test_fn,
        service_type=service_connection.type.value,
        automation_workflow=automation_workflow,
    )
