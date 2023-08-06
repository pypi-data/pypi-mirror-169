from email.mime import base
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_platform_services import IamIdentityV1
from lithopscloud.modules.config_builder import ConfigBuilder, update_decorator
from typing import Any, Dict
from lithopscloud.modules.utils import color_msg, Color, password_dialog, verify_iam_api_key 
from inquirer import errors


class ApiKeyConfig(ConfigBuilder):

    def __init__(self, base_config: Dict[str, Any]) -> None:
        super().__init__(base_config)
        self.defaults['api_key'] = self.base_config['ibm']['iam_api_key'] if self.base_config.setdefault('ibm', {}) \
            else None

    @update_decorator
    def run(self, api_key=None, compute_iam_endpoint=None, cos_iam_api_key=None) -> Dict[str, Any]:
        # first validate cos_iam_api_key if exists as it uses default iam endpoint
        if cos_iam_api_key:            
            verify_iam_api_key(None, cos_iam_api_key, iam_endpoint=ConfigBuilder.compute_iam_endpoint)
            
        ConfigBuilder.compute_iam_endpoint = compute_iam_endpoint
        
        if not api_key:
            default = self.defaults.get('api_key')
            api_key = password_dialog("Please provide " + color_msg("IBM API KEY", color=Color.CYAN),
                                  default=default,
                                  validate=verify_iam_api_key)['answer']

        ConfigBuilder.iam_api_key = api_key
        if not cos_iam_api_key:
            ConfigBuilder.cos_iam_api_key = api_key
        
        return api_key, compute_iam_endpoint, cos_iam_api_key

    def update_config(self, iam_api_key, compute_iam_endpoint=None, cos_iam_api_key=None) -> Dict[str, Any]:
        self.base_config['ibm'] = {'iam_api_key': iam_api_key}
        
        if compute_iam_endpoint:
            self.base_config['ibm']['iam_endpoint'] = compute_iam_endpoint
        if cos_iam_api_key:
            self.base_config['ibm_cos'] = {'iam_api_key': cos_iam_api_key}
            
        return self.base_config
    
    def verify(self, base_config):
        cos_iam_api_key = base_config['ibm_cos'].get('iam_api_key')
        api_key = base_config['ibm']['iam_api_key']
        
        if cos_iam_api_key:
            verify_iam_api_key(None, base_config['ibm_cos']['iam_api_key'], iam_endpoint=ConfigBuilder.compute_iam_endpoint)
        else:
            ConfigBuilder.cos_iam_api_key = api_key
            
        ConfigBuilder.compute_iam_endpoint = self.base_config['ibm'].get('iam_endpoint')
        
        verify_iam_api_key(None, api_key, iam_endpoint=ConfigBuilder.compute_iam_endpoint)
        ConfigBuilder.iam_api_key = api_key
            
        return base_config

