import chevron
from requests import JSONDecodeError
from urllib.parse import urljoin
from .authenticate import Authenticate
from .attachments import parse_attachment_output


class Runner(Authenticate):

    def run(self, inputs=None, input_schema=None):
        self._update_headers(inputs)
        response = self.session.request(
            method=self.get_method(input_schema['meta']),
            url=urljoin(self.url, self.get_endpoint(inputs, input_schema['meta'])),
            **self.get_kwargs(inputs)
        )
        resp = self.parse_response(response, input_schema)
        return resp

    def _update_headers(self, inputs=None):
        self.session.headers.update(
            inputs.get('headers', {})
        )

    @staticmethod
    def get_method(self, input_meta=None):
        return input_meta['method']

    @staticmethod
    def get_endpoint(self, inputs=None, input_meta=None):
        # Mustache if available if not returns string as is.
        return chevron.render(input_meta['endpoint'], inputs.get('path_parameters', {}))

    def get_kwargs(self, inputs):
        # todo can we handle files automatically.
        self.params.update(inputs.get('parameters', {}))
        return {
            'params': self.params,
            'data': inputs.get('data_body'),
            'json': inputs.get('json_body'),
            'files': inputs.get('files')
        }

    def parse_response(self, response, input_schema):
        output = {
            'status_code': response.status_code,
            'response_headers': dict(response.headers),
            'reason': response.reason
        }
        file = parse_attachment_output(response, input_schema)
        if file:
            output['file'] = file

        try:
            output['json_body'] = response.json()
        except JSONDecodeError:
            if 'file' not in output:
                # Avoids the duplication of the file content in response_text
                output['response_text'] = response.text
        return output
