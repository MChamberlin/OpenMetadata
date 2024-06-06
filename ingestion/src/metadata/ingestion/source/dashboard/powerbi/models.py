#  Copyright 2023 Collate
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""
PowerBI Models
"""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class Tile(BaseModel):
    """
    PowerBI Tile/Chart Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles-in-group#tile
    """

    id: str
    title: Optional[str] = None
    subTitle: Optional[str] = None
    embedUrl: Optional[str] = None
    datasetId: Optional[str] = None
    reportId: Optional[str] = None


class PowerBIDashboard(BaseModel):
    """
    PowerBI PowerBIDashboard Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards-in-group#dashboard
    """

    id: str
    displayName: str
    webUrl: Optional[str] = None
    embedUrl: Optional[str] = None
    tiles: Optional[List[Tile]] = []


class PowerBIReport(BaseModel):
    """
    PowerBI PowerBIReport Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-report#report
    """

    id: str
    name: str
    datasetId: Optional[str] = None


class DashboardsResponse(BaseModel):
    """
    PowerBI DashboardsResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-dashboards-in-group
    """

    odata_context: str = Field(alias="@odata.context")
    value: List[PowerBIDashboard]


class ReportsResponse(BaseModel):
    """
    PowerBI ReportsResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports-in-group
    """

    odata_context: str = Field(alias="@odata.context")
    value: List[PowerBIReport]


class TilesResponse(BaseModel):
    """
    PowerBI TilesResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/dashboards/get-tiles-in-group
    """

    odata_context: str = Field(alias="@odata.context")
    value: List[Tile]


class PowerBiColumns(BaseModel):
    """
    PowerBI Column Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables-in-group#column
    """

    name: str
    dataType: Optional[str] = None
    columnType: Optional[str] = None


class PowerBiTable(BaseModel):
    """
    PowerBI Table Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables-in-group#table
    """

    name: str
    columns: Optional[List[PowerBiColumns]] = None
    description: Optional[str] = None


class TablesResponse(BaseModel):
    """
    PowerBI TablesResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/push-datasets/datasets-get-tables-in-group
    """

    odata_context: str = Field(alias="@odata.context")
    value: List[PowerBiTable]


class Dataset(BaseModel):
    """
    PowerBI Dataset Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasets-in-group#dataset
    """

    id: str
    name: str
    tables: Optional[List[PowerBiTable]] = []
    description: Optional[str] = None


class DatasetResponse(BaseModel):
    """
    PowerBI DatasetResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/datasets/get-datasets-in-group
    """

    odata_context: str = Field(alias="@odata.context")
    value: List[Dataset]


class Group(BaseModel):
    """
    PowerBI Group Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups#group
    """

    id: str
    name: Optional[str] = None
    type: Optional[str] = None
    state: Optional[str] = None
    dashboards: Optional[List[PowerBIDashboard]] = []
    reports: Optional[List[PowerBIReport]] = []
    datasets: Optional[List[Dataset]] = []


class GroupsResponse(BaseModel):
    """
    PowerBI GroupsResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups
    """

    odata_context: str = Field(alias="@odata.context")
    odata_count: int = Field(alias="@odata.count")
    value: List[Group]


class WorkSpaceScanResponse(BaseModel):
    """
    PowerBI WorkSpaceScanResponse Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-status
    """

    id: str
    createdDateTime: datetime
    status: Optional[str] = None


class Workspaces(BaseModel):
    """
    PowerBI Workspaces Model
    Definition: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/workspace-info-get-scan-result
    """

    workspaces: List[Group]


class PowerBiToken(BaseModel):
    """
    PowerBI Token Model
    """

    expires_in: Optional[int] = None
    access_token: Optional[str] = None


class RemoteArtifacts(BaseModel):
    """
    PowerBI RemoteArtifacts Model
    """

    DatasetId: str
    ReportId: str


class ConnectionFile(BaseModel):
    """
    PowerBi Connection File Model
    """

    RemoteArtifacts: Annotated[
        Optional[List[RemoteArtifacts]], Field(None, description="Remote Artifacts")
    ]


class DataModelSchema(BaseModel):
    """
    PowerBi Data Model Schema Model
    """

    tables: Optional[List[PowerBiTable]] = None
    connectionFile: Optional[ConnectionFile] = None
