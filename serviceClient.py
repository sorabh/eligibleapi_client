import urllib
import urllib2
import json
from serviceListResponse import serviceListResponse


class serviceClient:

##### for one client usually resource URL and key remain same ,only request get changes. so I kept url and key as its property and and other parameters changes as for diffrent request.
    def __init__(self,res_url,api_key):
        self.resource_url=res_url
        self.api_key =api_key
    def get_responce(self,service_type_code,payer_name, payer_id ,service_provider_first_name,service_provider_last_name,service_provider_npi,subscriber_id,subscriber_first_name,subscriber_last_name,subscriber_dob):
	
	self.Dict={"service_type_code":service_type_code,"api_key":self.api_key,"payer_name":payer_name,"payer_id":payer_id,"service_provider_first_name":service_provider_first_name,"service_provider_last_name":service_provider_last_name,"service_provider_npi":service_provider_npi,"subscriber_id":subscriber_id,"subscriber_first_name":subscriber_first_name,"subscriber_last_name":subscriber_last_name,"subscriber_dob":subscriber_dob}


	Arg=urllib.urlencode(self.Dict)
	self.request=self.resource_url+"?"+Arg


	pointer=urllib2.urlopen(self.request)
        data=pointer.read()
        data_json=json.loads(data)
	return serviceListResponse(data_json)



