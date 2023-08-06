# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['azqueuetweeter']

package_data = \
{'': ['*']}

install_requires = \
['azure-storage-queue>=12.4.0,<13.0.0', 'tweepy>=4.10.1,<5.0.0']

setup_kwargs = {
    'name': 'azqueuetweeter',
    'version': '0.1.0',
    'description': 'Tweet from Azure Storage Queues',
    'long_description': '# AZImageTweeter\n\nSend images to Twitter using text from Azure Queue Storage\n\n## Usage instructions\n\n### Setup Azure authentication:\n\nFirst, as a general rule, you should not store credentials in your code;\na better option is to store them in environment variables and retrieve them\nwith `os.environ.get(\'ENV_NAME\')`.\n\nHere\'s what you\'ll need for Azure storage authentication:\n\n```\nfrom azqueuetweeter import storage\n\nsa = storage.Auth(connection_string="CONNECTION-STRING", queue_name="YOUR-QUEUE-NAME")\n```\n\nThe `connection_string` comes from [the Azure portal](https://learn.microsoft.com/en-us/azure/storage/queues/storage-python-how-to-use-queue-storage?tabs=python%2Cenvironment-variable-windows#copy-your-credentials-from-the-azure-portal).\nThe `queue_name` is whatever your named your queue. You can either create that programmatically\nusing the Azure client library, or more easily, using the [Azure Storage Explorer app](https://learn.microsoft.com/en-us/azure/vs-azure-tools-storage-manage-with-storage-explorer?tabs=macos).\n\n### Setup Twitter authentication:\n\nYou\'ll need a few more details for Twitter authentication:\n\n```\nfrom azqueuetweeter import twitter\n\nta = twitter.Auth(\n    consumer_key=\'CONSUMER-KEY\',\n    consumer_secret=\'CONSUMER-SECRET\',\n    access_token=\'ACCOUNT-ACCESS-TOKEN\',\n    access_token_secret=\'ACCOUNT-ACCESS-TOKEN-SECRET\')\n```\n\nThe `consumer_key` is also known as the API key and is provided to you in the Twitter developer portal. Similarly, the `consumer_secret` is also known as the API secret and is provided in the same place.\n\nThe `access_token` and `access_token_secret` credentials are for the Twitter account that will actually be the tweet author. If you\'re sending from the same account as the one that signed up for Twitter API access, then you can get those strings from the Twitter developer portal.If you\'re sending from a different account, you will need to do 3-legged OAuth to get that account\'s credentials.\n\nTo do 3-legged OAuth, first complete the _User authentication set up_ on the app settings page in the Twitter developer portal. Then use the `tweepy` package to programmatically go through the flow.\n\nFirst, get an authorization URL for your app:\n\n```\n>>> oauth1_user_handler = tweepy.OAuth1UserHandler(\n    "CONSUMER-KEY", "CONSUMER-SECRET",\n    callback="http://pamelafox.github.io"\n)\n>>> print(oauth1_user_handler.get_authorization_url())\nhttps://api.twitter.com/oauth/authorize?oauth_token=OAUTH-TOKEN\n```\n\nThen visit that URL using the desired account for tweeting,\nconfirm authorization of the app, and see the app redirect to a URL like:\n\nhttps://registeredwebsite.com/?oauth_token=OAUTH-TOKEN&oauth_verifier=OAUTH_VERIFIER\n\nPut the `OAUTH-VERIFIER` value into the next call:\n\n```\naccess_token, access_token_secret = oauth1_user_handler.get_access_token(\n    "OAUTH-VERIFIER"\n)\n```\n\nNow you have the `access_token` and `access_token_secret` needed for the `twitter.Auth` constructor above.\n\n### Construct a Queue Tweeter\n\nConstruct a `QueueTweeter` using the authentication objects:\n\n```\nfrom azqueuetweeter import QueueTweeter\nqt = QueueTweeter(storage_auth=sa, twitter_auth=ta)\n```\n\n### Queue up messages\n\nYou can add messages to the Queue either manually with the Azure Storage Explorer app or programmatically using the `QueueTweeter.queue_message` method.\n\nTo queue up a message with a simple string:\n\n```\nqt.queue_message(\'Hello world!\')\n```\n\nYou might also find it useful to queue up stringified JSON:\n\n```\nimport json\nqt.queue_message(json.dumps({"text": "when were f strings introduced?", "poll_options": ["3.6", "3.7", "3.8"], "poll_duration_minutes": 60*24}))\n```\n\nLater, you can transform your queued messages into tweet content, so you can store the information in the queue however works for you.\n\n### Send messages as tweets\n\nNow you can send tweets using the `QueueTweeter.send_next_message` method.\n\nIf the queued message contains exactly the text that you want tweeted, then you can call it with no arguments:\n\n```\nqt.send_next_message()\n```\n\nTo confirm the tweet contents first, you can specify `preview_mode=True` :\n\n```\nqt.send_next_message(preview_mode=True)\n```\n\nTo transform the queued message content first, specify a `message_transformer` function that returns back\na dict with the same arguments as tweepy\'s [create_tweet](https://docs.tweepy.org/en/stable/client.html#tweepy.Client.create_tweet) function. The most important argument is `"text"` but many other arguments are also possible.\n\nThis example adds a hashtag to the queued message string:\n\n```\nqt.send_next_message(message_transformer=lambda msg: {"text": msg + " #Python"})\n```\n\nThis example deserializes a serialized JSON string message:\n\n```\nimport json\n\nqt.queue_message(json.dumps({"text": "when were f strings introduced?", "poll_options": ["3.6", "3.7", "3.8"], "poll_duration_minutes": 60*24}))\nqt.send_next_message(message_transformer=lambda msg: json.loads(msg))\n```\n\nIt\'s also possible to upload an image to the tweet, as long as your Twitter account is approved for "elevated access".\nYour `message_transformer` must return the image bytes in a `"file"` key and provide a filename (with an extension)\nin the `"filename"` key..\n\n```\n\nimport io\nfrom PIL import Image\n\nimg = Image.open("Python_logo_icon.png")\nimg_bytes = io.BytesIO()\nimg.save(img_bytes, format="PNG")\nimg_bytes.seek(0)\n\nqt.queue_message("I want a stuffed Python logo!")\nqt.send_next_message(preview_mode=False, message_transformer=lambda msg: {"text": msg, "filename": "python.jpg", "file": img_bytes})\n```\n\n## Development guide\n\nStart a virtual environment:\n\n```\npython3 -m venv .venv\nsource .venv/bin/activate\n```\n\nInstall poetry:\n\n```\npython -m pip install poetry\n```\n\nInstall project dependencies:\n\n```\npoetry install\n```\n',
    'author': 'Jay Miller',
    'author_email': 'kjaymiller@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
