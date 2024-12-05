import re
import json
from urllib.parse import urlparse, parse_qs

class CurlToMakeConverter:
    def __init__(self):
        self.template = {
            "subflows": [{
                "flow": [{
                    "id": 8,
                    "module": "http:ActionSendData",
                    "version": 3,
                    "parameters": {
                        "handleErrors": False,
                        "useNewZLibDeCompress": True
                    },
                    "mapper": {
                        "method": "get",
                        "headers": [],
                        "qs": [],
                        "bodyType": "raw",
                        "parseResponse": True,
                        "serializeUrl": False,
                        "authUser": "",
                        "authPass": "",
                        "timeout": "",
                        "shareCookies": False,
                        "rejectUnauthorized": True,
                        "followRedirect": True,
                        "useQuerystring": False,
                        "gzip": True,
                        "useMtls": False,
                        "followAllRedirects": False,
                        "contentType": "application/json",
                        "data": ""
                    },
                    "metadata": {
                        "designer": {
                            "x": 210,
                            "y": 265,
                            "name": "http_request"
                        }
                    }
                }]
            }],
            "metadata": {
                "version": 1
            }
        }

    def parse_curl(self, curl_command):
        # Извлекаем URL
        url_match = re.search(r"'(https?://[^']+)'", curl_command)
        if url_match:
            url = url_match.group(1)
            parsed_url = urlparse(url)
            self.template["subflows"][0]["flow"][0]["mapper"]["url"] = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
            
            # Обрабатываем query параметры
            query_params = parse_qs(parsed_url.query)
            for key, value in query_params.items():
                self.template["subflows"][0]["flow"][0]["mapper"]["qs"].append({
                    "name": key,
                    "value": value[0]
                })

        # Извлекаем метод
        method_match = re.search(r"--request (\w+)", curl_command)
        if method_match:
            self.template["subflows"][0]["flow"][0]["mapper"]["method"] = method_match.group(1).lower()

        # Извлекаем заголовки
        headers = re.finditer(r"--header '([^:]+):\s*([^']+)'", curl_command)
        for header in headers:
            self.template["subflows"][0]["flow"][0]["mapper"]["headers"].append({
                "name": header.group(1).lower(),
                "value": header.group(2).strip()
            })

        return self.template

    def to_json(self):
        return json.dumps(self.template, indent=2)

# Пример использования
def convert_curl_to_make(curl_command):
    converter = CurlToMakeConverter()
    converter.parse_curl(curl_command)
    return converter.to_json()

# Тестовый пример
if __name__ == "__main__":
    curl_command = """curl --location --request GET 'https://api.scrapecreators.com/v1/youtube/video?videoId=RF6bXufgoCw' \\
    --header 'accept: application/json' \\
    --header 'x-api-key: oEXk---ao4Lp1'"""
    
    result = convert_curl_to_make(curl_command)
    print(result)
