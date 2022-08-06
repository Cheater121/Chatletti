from jsonschema import validate


schema = {
	"type": "object",
	"minProperties": 4,
	"maxProperties": 4,
	"properties": {
		"Username": {
			"type": "string",
			"minLength": 1
			},
		"Timestamp": {
			"type": "string",
			"format": "date-time"
			},
		"Messagetext": {
			"type": "string",
			"minLength": 1
			},
		"Recipient": {
			"type": "string",
			"minLength": 1
			}
		}, 
	"required": ["Username", "Timestamp", "Messagetext", "Recipient"]
	}


def msg_validator(msg):
	try:
		validate(msg, schema)
		return True
	except:
		return False
