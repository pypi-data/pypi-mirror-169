import copy, json, requests
from requests.auth import HTTPBasicAuth
from string import Template
from .field_definitions import shared_fields
from .template_schema import template_schema
from .index_configs import twitter_index_config, discord_index_config

def get_fields_by_index(index_config):
  field_list = copy.deepcopy(shared_fields)
  for key in index_config.vertical_fields:
    assert not key in field_list
    field_list[key] = index_config.vertical_fields[key]
  return field_list

def build_template_json(index_config):
  field_list = get_fields_by_index(index_config)
  index_template = Template(template_schema)
  template_json = json.loads(index_template.substitute(
    fields=json.dumps(field_list),
    number_of_replicas=index_config.number_of_replicas,
    number_of_shards=index_config.number_of_shards,
  ))
  return template_json

def create_index(index_config):
  template_json = build_template_json(index_config)
  url = "https://" + index_config.uri + "/" + index_config.index_name
  response = requests.put(
    url,
    json=template_json,
    auth=HTTPBasicAuth(index_config.username, index_config.password),
  )
  return response.text