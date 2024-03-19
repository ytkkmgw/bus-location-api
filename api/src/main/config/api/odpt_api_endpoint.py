from config.api.odpt_api_key import ODPTApiKey
import urllib.parse


class OdptAPIEndpoint:
    def __init__(self, url: str, query: dict):
        self.url = url
        self.api_key = ODPTApiKey()
        self.query = query

    def create(self) -> str:
        return self.url + self._query_parameters()

    def _query_parameters(self) -> str:
        query_parameters = "?" + self._consumer_key()
        # query_parameters += "&odpt:operator="+urllib.parse.quote("odpt.Operator:SeibuBus")
        for key, value in self.query.items():
            query_parameters += "&" + key + "=" + urllib.parse.quote(value)

        return query_parameters

    def _consumer_key(self) -> str:
        return "acl:consumerKey=" + self.api_key.value
