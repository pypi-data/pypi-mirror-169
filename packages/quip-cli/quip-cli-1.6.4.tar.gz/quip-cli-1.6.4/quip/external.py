import requests
import logging
import sys
import json


class SonarQube():
    def __init__(self, base_url, credentials, ssl_verify=False) -> None:
        self.log = logging
        logging.basicConfig(level="DEBUG", format=' %(asctime)s - %(levelname)s - %(message)s')

        self.base_url = base_url.rstrip(" /") # clean end of the url
        self.credentials = credentials
        self.ssl_verify = ssl_verify


    def create_project(self, name, quality_gate="CS UAC and Community QG"):
        # echo -e "INFO:Create sonarqube project:${PROJECT} "
        # curl  --request   GET -k --fail -u squ_39bb405492e9cacc02b9c84f4eae90d3d66b5807: "https://sonarqube.stonebranch.com/api/projects?project=${PROJECT}&name=${PROJECT}"
        # echo $?

        # echo -e "INFO:Assign Quality gate"
        # curl --request   POST -k --fail -u aakeykey: "https://sonarqube.stonebranch.com/api/qualitygates/select?gateName=CS%20UAC%20and%20Community%20QG&projectKey=${PROJECT}"
        # echo $?
        try:
            response = self.post(resource="/projects/create", query=[f"project={name}", f"name={name}"])
        except Exception as e:
            self.log.error(f"Failed with reason : {e}")
        if not response.ok:
            #_json = json.loads(response.text)
            self.log.error(f"Response: {response.text}")
            return False

        try:
            response = self.post(resource="/qualitygates/select", query=[f"gateName={quality_gate}", f"projectKey={name}"])
        except Exception as e:
            self.log.error(f"Failed with reason : {e}")
        if not response.ok:
            #_json = json.loads(response.text)
            self.log.error(f"Response: {response.text}")
            return False
        
        return True


    def post(self, resource, query="", json_data=None):
        return self.call("POST", resource, query, json_data)

    def put(self, resource, query="", json_data=None):
        return self.call("PUT", resource, query, json_data)

    def get(self, resource, query=""):
        return self.call("GET", resource, query, json_data=None)

    def delete(self, resource, query="", json_data=None):
        return self.call("DELETE", resource, query, json_data)

    def call(self, method, resource, query, json_data):
        self.log.debug("rest_call start")
        headers = {"content-type": "application/json", "Accept": "application/json"}
        if len(query) > 0:
            query = "?" + "&".join(query)
        uri = f"{self.base_url}/api{resource}{query}"
        self.log.info(f"URL = {uri}")
        try:
            if method == "GET":
                response = requests.get(uri,
                                        headers=headers,
                                        auth=self.credentials,
                                        verify=self.ssl_verify)
            elif method == "POST":
                response = requests.post(uri,
                                        headers=headers,
                                        json=json_data,
                                        auth=self.credentials,
                                        verify=self.ssl_verify)
            elif method == "DELETE":
                response = requests.delete(uri,
                                        headers=headers,
                                        json=json_data,
                                        auth=self.credentials,
                                        verify=self.ssl_verify)
            elif method == "PUT":
                response = requests.put(uri,
                                        headers=headers,
                                        json=json_data,
                                        auth=self.credentials,
                                        verify=self.ssl_verify)
            else:
                self.log.error(f"Unknown method {method}")
                raise
        except Exception as unknown_exception:
            self.log.error(f"Error Calling{self.base_url} API {sys.exc_info()}")
            raise

        return response