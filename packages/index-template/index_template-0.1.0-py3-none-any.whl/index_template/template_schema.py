template_schema = '''
{
  "mappings": {
    "dynamic": "strict",
    "properties": ${fields}
  },
  "settings":{
    "analysis": {
      "filter": {
        "english_stop": {
          "type": "stop",
          "stopwords": "_english_"
        },
        "english_keywords": {
          "type": "keyword_marker",
          "keywords": []
        },
        "english_stemmer": {
          "type": "stemmer",
          "language": "english"
        },
        "english_possessive_stemmer": {
          "type": "stemmer",
          "language": "possessive_english"
        }
      },
      "analyzer": {
        "english_customized": {
          "tokenizer": "standard",
          "filter": [
            "english_possessive_stemmer",
            "lowercase",
            "english_stop",
            "english_keywords",
            "english_stemmer"
          ]
        }
      }
    },
    "index":{
      "number_of_replicas": ${number_of_replicas},
      "number_of_shards": ${number_of_shards},
      "mapping.ignore_malformed": false,
      "mapping.coerce": false
    }
  }
}
'''
