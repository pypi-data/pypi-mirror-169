# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['retracto']

package_data = \
{'': ['*']}

install_requires = \
['cohere>=2.4.2,<3.0.0',
 'google-api-python-client>=2.62.0,<3.0.0',
 'google-auth-oauthlib>=0.5.3,<0.6.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['retracto = retracto.app:app']}

setup_kwargs = {
    'name': 'retracto',
    'version': '1.0.2',
    'description': 'This app helps you as a youtube contnt creator to delete abusive and spam comments on a video in one shot.',
    'long_description': 'YouTube comment spam can take many forms. Major creators are often concerned about spam that impersonates them, promises viewers something good for messaging them, and then directs individuals off YouTube in some way to eventually scam them.Other spam comments can be less overtly malicious but still annoying or potentially harmful.YouTube does have many tools to combat spammy comments, and it removes a huge amount of them automatically.\n\n<b> Retracto </b> automatically identifies spam comments using Machine Learning and deletes them in a single command.\n\nThe package contains the following commands:\n- `retracto login`\n- `retracto comment <video_id>`\n\nYou have to start by logging into your google account by using `retracto login` and then use `retracto comment <video_id>` to strip down spam comments on your video.\n\n`<video_id>`: Go to your video on YouTube and copy the video id from the url(https://www.youtube.com/watch?v=<b><video_id></b>) and use it in the command.\n\n',
    'author': 'Amit Krishna A',
    'author_email': 'amit.ananthkumar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
