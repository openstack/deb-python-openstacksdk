# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from openstack.cluster import cluster_service
from openstack.cluster.v1 import cluster as _cluster
from openstack import resource


class Receiver(resource.Resource):
    resource_key = 'receiver'
    resources_key = 'receivers'
    base_path = '/receivers'
    service = cluster_service.ClusterService()

    # Capabilities
    allow_list = True
    allow_retrieve = True
    allow_create = True
    allow_delete = True

    # Properties
    #: The name of the receiver.
    name = resource.prop('name')
    #: The type of the receiver.
    type = resource.prop('type')
    #: The ID of the user who created the receiver, thus the owner of it.
    user = resource.prop('user')
    #: The ID of the project this receiver belongs to.
    project = resource.prop('project')
    #: The domain ID of the receiver.
    domain = resource.prop('domain')
    #: The ID of the targeted cluster.
    cluster = resource.prop('cluster_id', type=_cluster.Cluster)
    #: The name of the targeted action.
    action = resource.prop('action')
    #: Timestamp of when the receiver was created.
    created_at = resource.prop('created_at')
    #: Timestamp of when the receiver was last updated.
    updated_at = resource.prop('updated_at')
    #: The credential of the impersonated user.
    actor = resource.prop('actor', type=dict)
    #: A dictionary containing key-value pairs that are provided to the
    #: targeted action.
    params = resource.prop('params', type=dict)
    #: The information about the channel through which you can trigger the
    #: receiver hence the associated action.
    channel = resource.prop('channel', type=dict)
