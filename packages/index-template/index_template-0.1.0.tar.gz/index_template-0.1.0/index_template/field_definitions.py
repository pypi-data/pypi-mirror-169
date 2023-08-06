import json

## Reference:
## https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-data-types.html
## https://www.elastic.co/guide/en/elasticsearch/reference/current/array.html
## Multiple formats can be specified by separating them with || as a separator. Each format will be tried in turn until a matching format is found.

shared_fields = json.loads('''
{
   "doc_id":{
      "type":"keyword"
   },
   "crypto_ticker":{
      "type":"keyword"
   },
   "text":{
      "type":"text",
      "analyzer": "default",
      "fields": {
         "english_analyzed": {
            "type": "text",
            "analyzer": "english_customized"
         }
      }
   },
   "data_source":{
      "type": "keyword"
   },
   "engagement_count":{
      "type": "integer"
   },
   "created_at":{
      "type": "date",
      "format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
   },
   "updated_at":{
      "type": "date",
      "format": "epoch_second||yyyy-MM-dd"
   },
   "author_id":{
      "type": "keyword"
   },
   "url":{
      "type":"keyword"
   }
}
''')

podcast_fields = json.loads('''
{
   "podcast_created_at" : {
      "type" : "date",
      "format" : "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
   },
   "podcast_episode_guid" : {
      "type" : "keyword"
   },
   "podcast_episode_title" : {
      "type" : "text",
      "analyzer" : "default",
      "fields" : {
         "english_analyzed" : {
            "type" : "text",
            "analyzer" : "english_customized"
         }
      }
   },
   "podcast_episode_content_snippet":{
      "type" : "text",
      "analyzer" : "default",
      "fields" : {
         "english_analyzed" : {
            "type" : "text",
            "analyzer" : "english_customized"
         }
      }
   },
   "podcast_name" : {
      "type" : "keyword"
   },
   "podcast_episode_speaker" : {
      "type" : "keyword"
   },
   "podcast_episode" : {
      "type" : "integer"
   },
   "podcast_audio_type" : {
      "type" : "keyword"
   },
   "podcast_audio_length" : {
      "type" : "integer"
   },
   "podcast_audio_url" : {
      "type" : "keyword"
   },
   "podcast_transcript_url" : {
      "type" : "keyword"
   },
   "podcast_metadata_url" : {
      "type" : "keyword"
   },
   "podcast_episode_image_url" : {
      "type" : "keyword"
   },
   "podcast_episode_url" : {
      "type" : "keyword"
   },
   "podcast_transcript_raw" : {
      "type" : "text"
   },
   "podcast_transcript_detail": {
      "properties" : {
         "content" : {
            "type" : "text",
            "analyzer" : "default",
            "fields" : {
               "english_analyzed" : {
                  "type" : "text",
                  "analyzer" : "english_customized"
               }
            }
         },
         "end_time" : {
            "type" : "float"
         },
         "start_time" : {
            "type" : "float"
         },
         "speaker_label" : {
            "type" : "keyword"
         }
      }
   }
}
''')

twitter_fields = json.loads('''
{
   "twitter_tweet_id":{
      "type":"keyword"
   },
   "twitter_tweet_conversation_id":{
      "type":"keyword"
   },
   "twitter_tweet_author_id" : {
      "type" : "keyword"
   },
   "twitter_tweet_created_at" : {
      "type" : "date",
      "format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
   },
   "twitter_tweet_author_detail" : {
      "properties" : {
         "twitter_user_created_at" : {
            "type" : "date",
            "format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
         },
         "twitter_user_description" : {
            "type":"text",
            "analyzer": "default",
            "fields": {
               "english_analyzed": {
                  "type": "text",
                  "analyzer": "english_customized"
               }
            }
         },
         "twitter_user_followers_count" : {
            "type" : "integer"
         },
         "twitter_user_following_count" : {
            "type" : "integer"
         },
         "twitter_user_id" : {
            "type" : "keyword"
         },
         "twitter_user_listed_count" : {
            "type" : "integer"
         },
         "twitter_user_name" : {
            "type" : "keyword"
         },
         "twitter_user_pinned_tweet_id" : {
            "type" : "keyword"
         },
         "twitter_user_profile_image_url" : {
            "type" : "keyword"
         },
         "twitter_user_protected" : {
            "type" : "boolean"
         },
         "twitter_user_tweet_count" : {
            "type" : "integer"
         },
         "twitter_user_username" : {
            "type" : "keyword"
         },
         "twitter_user_verified" : {
            "type" : "boolean"
         }
      }
   },
   "twitter_tweet_is_conversation_head":{
      "type":"boolean"
   },
   "twitter_tweet_retweet_count":{
      "type":"integer"
   },
   "twitter_tweet_reply_count":{
      "type":"integer"
   },
   "twitter_tweet_like_count":{
      "type":"integer"
   },
   "twitter_tweet_quote_count":{
      "type":"integer"
   },
   "twitter_tweet_in_reply_to_user_id":{
      "type":"keyword"
   },
   "twitter_tweet_reference_types":{
      "type":"keyword"
   },
   "twitter_tweet_replied_to_tweet_ids":{
      "type":"keyword"
   },
   "twitter_tweet_retweeted_to_tweet_ids":{
      "type":"keyword"
   },
   "twitter_tweet_quoted_to_tweet_ids":{
      "type":"keyword"
   },
   "twitter_tweet_has_no_reference" : {
      "type" : "boolean"
   },
   "twitter_tweet_is_reply" : {
      "type" : "boolean"
   },
   "twitter_tweet_is_retweet" : {
      "type" : "boolean"
   },
   "twitter_tweet_is_quote" : {
      "type" : "boolean"
   },
   "twitter_tweet_lang" : {
      "type" : "keyword"
   },
   "twitter_tweet_text" : {
      "type" : "text"
   },
   "twitter_referenced_tweets_detail" : {
      "properties" : {
         "twitter_referenced_tweet_detail": {
            "properties" : {
               "twitter_tweet_id":{
                  "type":"keyword"
               },
               "twitter_tweet_conversation_id":{
                  "type":"keyword"
               },
               "twitter_tweet_author_id" : {
                  "type" : "keyword"
               },
               "twitter_tweet_created_at" : {
                  "type" : "date",
                  "format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
               },
               "twitter_tweet_author_detail" : {
                  "properties" : {
                     "twitter_user_created_at" : {
                        "type" : "date",
                        "format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
                     },
                     "twitter_user_description" : {
                        "type":"text",
                        "analyzer": "default",
                        "fields": {
                           "english_analyzed": {
                              "type": "text",
                              "analyzer": "english_customized"
                           }
                        }
                     },
                     "twitter_user_followers_count" : {
                        "type" : "integer"
                     },
                     "twitter_user_following_count" : {
                        "type" : "integer"
                     },
                     "twitter_user_id" : {
                        "type" : "keyword"
                     },
                     "twitter_user_listed_count" : {
                        "type" : "integer"
                     },
                     "twitter_user_name" : {
                        "type" : "keyword"
                     },
                     "twitter_user_pinned_tweet_id" : {
                        "type" : "keyword"
                     },
                     "twitter_user_profile_image_url" : {
                        "type" : "keyword"
                     },
                     "twitter_user_protected" : {
                        "type" : "boolean"
                     },
                     "twitter_user_tweet_count" : {
                        "type" : "integer"
                     },
                     "twitter_user_username" : {
                        "type" : "keyword"
                     },
                     "twitter_user_verified" : {
                        "type" : "boolean"
                     }
                  }
               },
               "twitter_tweet_is_conversation_head":{
                  "type":"boolean"
               },
               "twitter_tweet_retweet_count":{
                  "type":"integer"
               },
               "twitter_tweet_reply_count":{
                  "type":"integer"
               },
               "twitter_tweet_like_count":{
                  "type":"integer"
               },
               "twitter_tweet_quote_count":{
                  "type":"integer"
               },
               "twitter_tweet_in_reply_to_user_id":{
                  "type":"keyword"
               },
               "twitter_tweet_reference_types":{
                  "type":"keyword"
               },
               "twitter_tweet_replied_to_tweet_ids":{
                  "type":"keyword"
               },
               "twitter_tweet_retweeted_to_tweet_ids":{
                  "type":"keyword"
               },
               "twitter_tweet_quoted_to_tweet_ids":{
                  "type":"keyword"
               },
               "twitter_tweet_has_no_reference" : {
                  "type" : "boolean"
               },
               "twitter_tweet_is_reply" : {
                  "type" : "boolean"
               },
               "twitter_tweet_is_retweet" : {
                  "type" : "boolean"
               },
               "twitter_tweet_is_quote" : {
                  "type" : "boolean"
               },
               "twitter_tweet_lang" : {
                  "type" : "keyword"
               },
               "twitter_tweet_text" : {
                  "type" : "text"
               }
            }
         },
         "twitter_referenced_tweet_id": {
            "type" : "keyword"
         },
         "twitter_referenced_tweet_type": {
            "type" : "keyword"
         }
      }
   }
}
''')

discord_fields = json.loads('''
{
	"discord_author_detail": {
		"properties": {
			"discord_user_avatar_url": {
				"type": "keyword"
			},
			"discord_user_color": {
				"type": "keyword"
			},
			"discord_user_discriminator": {
				"type": "keyword"
			},
			"discord_user_id": {
				"type": "keyword"
			},
			"discord_user_is_bot": {
				"type": "boolean"
			},
			"discord_user_name": {
				"type": "keyword"
			},
			"discord_user_nickname": {
				"type": "keyword"
			},
			"discord_user_official": {
				"type": "boolean"
			},
			"discord_user_roles": {
				"properties": {
					"discord_role_color": {
						"type": "keyword"
					},
					"discord_role_id": {
						"type": "keyword"
					},
					"discord_role_name": {
						"type": "keyword"
					},
					"discord_role_position": {
						"type": "keyword"
					}
				}
			}
		}
	},
	"discord_channel_category_id": {
		"type": "keyword"
	},
	"discord_channel_category_name": {
		"type": "keyword"
	},
	"discord_channel_id": {
		"type": "keyword"
	},
	"discord_channel_name": {
		"type": "keyword"
	},
	"discord_mentions_detail": {
		"properties": {
			"discord_user_avatar_url": {
				"type": "keyword"
			},
			"discord_user_color": {
				"type": "keyword"
			},
			"discord_user_discriminator": {
				"type": "keyword"
			},
			"discord_user_id": {
				"type": "keyword"
			},
			"discord_user_is_bot": {
				"type": "boolean"
			},
			"discord_user_name": {
				"type": "keyword"
			},
			"discord_user_nickname": {
				"type": "keyword"
			},
			"discord_user_official": {
				"type": "boolean"
			},
			"discord_user_roles": {
				"properties": {
					"discord_role_color": {
						"type": "keyword"
					},
					"discord_role_id": {
						"type": "keyword"
					},
					"discord_role_name": {
						"type": "keyword"
					},
					"discord_role_position": {
						"type": "keyword"
					}
				}
			}
		}
	},
	"discord_message_attachments_count": {
		"type": "integer"
	},
	"discord_message_content": {
		"type": "keyword"
	},
	"discord_message_created_at": {
		"type": "date",
		"format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
	},
	"discord_message_edited_at": {
		"type": "date",
		"format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
	},
	"discord_message_embeds_count": {
		"type": "integer"
	},
	"discord_message_id": {
		"type": "keyword"
	},
	"discord_message_mentions_count": {
		"type": "integer"
	},
	"discord_message_pinned": {
		"type": "boolean"
	},
	"discord_message_reaction_count": {
		"type": "integer"
	},
	"discord_message_stickers_count": {
		"type": "integer"
	},
	"discord_message_type": {
		"type": "keyword"
	},
	"discord_message_url": {
		"type": "keyword"
	},
	"discord_reference_message_id": {
		"type": "keyword"
	},
	"discord_reference_message_url": {
		"type": "keyword"
	},
	"discord_referenced_message_detail": {
		"properties": {
			"discord_author_detail": {
				"properties": {
					"discord_user_avatar_url": {
						"type": "keyword"
					},
					"discord_user_color": {
						"type": "keyword"
					},
					"discord_user_discriminator": {
						"type": "keyword"
					},
					"discord_user_id": {
						"type": "keyword"
					},
					"discord_user_is_bot": {
						"type": "boolean"
					},
					"discord_user_name": {
						"type": "keyword"
					},
					"discord_user_nickname": {
						"type": "keyword"
					},
					"discord_user_official": {
						"type": "boolean"
					},
					"discord_user_roles": {
						"properties": {
							"discord_role_color": {
								"type": "keyword"
							},
							"discord_role_id": {
								"type": "keyword"
							},
							"discord_role_name": {
								"type": "keyword"
							},
							"discord_role_position": {
								"type": "keyword"
							}
						}
					}
				}
			},
			"discord_mentions_detail": {
				"properties": {
					"discord_user_avatar_url": {
						"type": "keyword"
					},
					"discord_user_color": {
						"type": "keyword"
					},
					"discord_user_discriminator": {
						"type": "keyword"
					},
					"discord_user_id": {
						"type": "keyword"
					},
					"discord_user_is_bot ": {
						"type": "boolean"
					},
					"discord_user_name": {
						"type": "keyword"
					},
					"discord_user_nickname": {
						"type": "keyword"
					},
					"discord_user_official": {
						"type": "boolean"
					},
					"discord_user_roles": {
						"properties": {
							"discord_role_color": {
								"type": "keyword"
							},
							"discord_role_id": {
								"type": "keyword"
							},
							"discord_role_name": {
								"type": "keyword"
							},
							"discord_role_position": {
								"type": "keyword"
							}
						}
					}
				}
			},
			"discord_message_attachments_count": {
				"type": "integer"
			},
			"discord_message_content": {
				"type": "text"
			},
			"discord_message_created_at": {
				"type": "date",
				"format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
			},
			"discord_message_edited_at": {
				"type": "date",
				"format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'||yyyy-MM-dd'T'HH:mm:ss.SSSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SSZZZZZ||yyyy-MM-dd'T'HH:mm:ss.SZZZZZ||yyyy-MM-dd'T'HH:mm:ssZZZZZ||yyyy-MM-dd||epoch_second"
			},
			"discord_message_embeds_count": {
				"type": "integer"
			},
			"discord_message_id": {
				"type": "keyword"
			},
			"discord_message_mentions_count": {
				"type": "integer"
			},
			"discord_message_pinned": {
				"type": "boolean"
			},
			"discord_message_reaction_count": {
				"type": "integer"
			},
			"discord_message_stickers_count": {
				"type": "integer"
			},
			"discord_message_type": {
				"type": "keyword"
			},
			"discord_message_url": {
				"type": "keyword"
			},
			"discord_reference_message_id": {
				"type": "keyword"
			},
			"discord_reference_message_url": {
				"type": "keyword"
			}
		}
	},
	"discord_server_id": {
		"type": "keyword"
	},
	"discord_server_name": {
		"type": "keyword"
	}
}
''')

ticker_autocomplete_fields = json.loads('''
{
   "ticker_id":{
      "type":"integer"
   },
   "ticker":{
      "type":"search_as_you_type"
   },
   "fullname":{
      "type":"search_as_you_type"
   },
   "type":{
      "type":"keyword"
   },
   "logo":{
      "type":"keyword"
   }
}
''')