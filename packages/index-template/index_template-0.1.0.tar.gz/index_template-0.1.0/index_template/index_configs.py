from index_template.field_definitions import twitter_fields, discord_fields, podcast_fields, ticker_autocomplete_fields

class VerticalIndexConfig(object):
    def __init__(self, index_name, vertical_fields, number_of_replicas=1, number_of_shards=5):
        self.index_name = index_name
        self.uri = "search-devuswest2domai-x2rlx2ort7va-ob3ypm6swue7v5x5exiephrkmy.us-west-2.es.amazonaws.com"
        # self.uri = "search-betauswest2doma-kjm8byadxj3c-yksgdgqwjuproyejdvvcvgheui.us-west-2.es.amazonaws.com"
        self.username = "Kinesis-test1"
        self.password = "Kinesis-test1"
        self.vertical_fields = vertical_fields
        self.number_of_replicas = number_of_replicas
        self.number_of_shards = number_of_shards

twitter_index_config = VerticalIndexConfig(
    "twitter_alpha",
    twitter_fields)

discord_index_config = VerticalIndexConfig(
    "discord_alpha",
    discord_fields)

podcast_index_config = VerticalIndexConfig(
    "podcast_alpha",
    podcast_fields)

ticker_autocomplete_index_config = VerticalIndexConfig(
    "ticker_autocomplete_alpha_demo",
    ticker_autocomplete_fields)

index_config_lists = [
    twitter_index_config,
    discord_index_config,
    podcast_index_config,
    ticker_autocomplete_index_config
]
