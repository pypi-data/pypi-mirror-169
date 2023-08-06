from typing import Any, Dict

from lithopscloud.modules.gen2.endpoint import EndpointConfig
from lithopscloud.modules.utils import get_region_by_endpoint
from lithopscloud.modules.config_builder import ConfigBuilder


class LithopsEndpointConfig(EndpointConfig):

    def __init__(self, base_config: Dict[str, Any]) -> None:
        super().__init__(base_config)

        base_endpoint = self.base_config['ibm_vpc'].get(
            'endpoint') if self.base_config.setdefault('ibm_vpc', {}) else None
        try:
            # when endpoint was provided directly by user instead of selecting it
            # we just set it
            if base_endpoint:
                ConfigBuilder.ibm_vpc_client.set_service_url(base_endpoint + '/v1')
                self.ibm_vpc_client.set_service_url(base_endpoint + '/v1')
        
            self.defaults['region'] = get_region_by_endpoint(
                base_endpoint) if base_endpoint else None
        except Exception:
            pass

    def update_config(self, endpoint):
        self.base_config['ibm_vpc']['endpoint'] = endpoint
