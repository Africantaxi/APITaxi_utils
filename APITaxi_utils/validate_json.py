#coding: utf-8
from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError
from flask_restplus import abort
from werkzeug.utils import cached_property
from ..api import api

class ValidatorMixin(object):
    @cached_property
    def validator(self):
        return Draft4Validator(self.schema, resolver=api.resolver)

    def validate(self, data):
        try:
            self.validator.validate(data)
        except ValidationError as e:
            if e.validator == 'maxItems':
                abort(413, message="Maximum size of {} is {}".format(e.relative_path[-1],
                    e.validator_value))
            elif e.validator == 'enum':
                abort(400,
                  message='Invalid {}, {}'.format(e.relative_path[-1], e.message))
            abort(400, message=e.message)
