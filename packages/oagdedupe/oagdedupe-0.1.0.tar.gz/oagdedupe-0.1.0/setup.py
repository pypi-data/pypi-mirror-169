# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oagdedupe',
 'oagdedupe.block',
 'oagdedupe.cluster',
 'oagdedupe.db',
 'oagdedupe.distance',
 'oagdedupe.fastapi',
 'oagdedupe.labelstudio',
 'oagdedupe.postgres']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.15.1,<14.0.0',
 'SQLAlchemy>=1.4.39,<2.0.0',
 'Sphinx>=5.1.1,<6.0.0,!=5.2.0.post0',
 'diagrams>=0.21.1,<0.22.0',
 'fastapi[all]>=0.79.0,<0.80.0',
 'flake8>=4.0.1,<5.0.0',
 'graphviz>=0.19.0,<0.20.0',
 'ipykernel>=6.13.0,<7.0.0',
 'jellyfish>=0.9.0,<0.10.0',
 'matplotlib>=3.5.1,<4.0.0',
 'modAL>=0.4.1,<0.5.0',
 'myst-parser>=0.18.0,<0.19.0',
 'nbconvert>=6.5.1,<7.0.0',
 'networkx>=2.8,<3.0',
 'numpy>=1.22.1,<2.0.0',
 'pandas>=1.4.2,<2.0.0',
 'pathos>=0.2.9,<0.3.0',
 'protobuf>=3.20.2,<4.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pytest>=7.1.2,<8.0.0',
 'ray>=1.13.0,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'sphinx-rtd-theme>=1.0.0,<2.0.0',
 'streamlit-aggrid>=0.2.3,<0.3.0',
 'streamlit>=1.11.1,<2.0.0',
 'tqdm>=4.58.0,<5.0.0']

extras_require = \
{'book': ['jupytext>=1.14.1,<2.0.0', 'autodocsumm>=0.2.9,<0.3.0']}

setup_kwargs = {
    'name': 'oagdedupe',
    'version': '0.1.0',
    'description': 'oagdedupe is a Python library for scalable entity resolution, using active learning to learn blocking configurations, generate comparison pairs, then clasify matches.',
    'long_description': '# oagdedupe  \n\noagdedupe is a Python library for scalable entity resolution, using active \nlearning to learn blocking configurations, generate comparison pairs, \nthen clasify matches. \n\n## page contents\n- [Documentation](#documentation)\n- [Installation](#installation)\n    - [label-studio](#label-studio)\n    - [postgres](#postgres)\n    - [project settings](#project-settings)\n- [dedupe](#dedupe-example)\n- [record-linkage](#record-linkage-example)\n    \n# Documentation<a name="#documentation"></a>\n\nYou can find the documentation of oagdedupe at https://deduper.readthedocs.io/en/latest/, \nwhere you can find the [api reference](https://deduper.readthedocs.io/en/latest/dedupe/api.html), \n[guide to methodology](https://deduper.readthedocs.io/en/latest/userguide/intro.html),\nand [examples](https://deduper.readthedocs.io/en/latest/examples/example_dedupe.html).\n\n# Installation<a name="#installation"></a>\n\n[tbd pip install instructions]\n\n## start label-studio<a name="#label-studio"></a>\n\nStart label-studio using docker command below, updating `[LS_PORT]` to the \nport on your host machine\n\n```\ndocker run -it -p [LS_PORT]:8080 -v `pwd`/cache/mydata:/label-studio/data \\\n\t--env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true \\\n\t--env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/files \\\n\t-v `pwd`/cache/myfiles:/label-studio/files \\\n\theartexlabs/label-studio:latest label-studio\n```\n\n## postgres<a name="#postgres"></a>\n\n[insert instructions here about initializing postgres]\n\nmost importantly, need to create functions (dedupe/postgres/funcs.py)\n\n## project settings<a name="#project-settings"></a>\n\nMake a `dedupe.settings.Settings` object. For example:\n```py\nfrom oagdedupe.settings import (\n    Settings,\n    SettingsOther,\n)\n\nsettings = Settings(\n    name="default",  # the name of the project, a unique identifier\n    folder="./.dedupe",  # path to folder where settings and data will be saved\n    other=SettingsOther(\n        n=5000, # active-learning samples per learning loop\n        k=3, # max_len of block conjunctions\n        cpus=20,  # parallelize distance computations\n        attributes=["givenname", "surname", "suburb", "postcode"],  # list of entity attribute names\n        path_database="postgresql+psycopg2://username:password@172.22.39.26:8000/db",  # where to save the sqlite database holding intermediate data\n        db_schema="dedupe",\n        path_model="./.dedupe/test_model",  # where to save the model\n        label_studio={\n            "port": 8089,  # label studio port\n            "api_key": "83e2bc3da92741aa41c272829558c596faefa745",  # label studio port\n            "description": "chansoo test project",  # label studio description of project\n        },\n        fast_api={"port": 8090},  # fast api port\n    ),\n)\nsettings.save()\n```\nTo get label studio api_key:\n   1. log in (can make up any user/pw).\n   2. Go to "Account & Settings" using icon on top-right\n   3. Get Access Token and copy/paste into settings at `settings.other.label_studio["api_key"]` \n\nSee [dedupe/settings.py](./dedupe/settings.py) for the full settings code.\n\n# dedupe<a name="#dedupe-example"></a>\n\nBelow is an example that dedupes `df` on attributes columns specified in settings.\n\n## train dedupe<a name="#train-dedupe"></a>\n\n```py\nimport glob\nimport pandas as pd\nfrom oagdedupe.api import Dedupe\n\nd = Dedupe(settings=settings)\nd.initialize(df=df, reset=True)\n\n# %%\n# pre-processes data and stores pre-processed data, comparisons, ID matrices in SQLite db\nd.fit_blocks()\n```\n\n# record-linkage<a name="#record-linkage-example"></a>\n\nBelow is an example that links `df` to `df2`, on attributes columns specified \nin settings (dataframes should share these columns).\n\n## train record-linkage<a name="#train-record-linkage"></a>\n```py\nimport glob\nimport pandas as pd\nfrom oagdedupe.api import RecordLinkage\n\nd = RecordLinkage(settings=settings)\nd.initialize(df=df, df2=df2, reset=True)\n\n# %%\n# pre-processes data and stores pre-processed data, comparisons, ID matrices in SQLite db\nd.fit_blocks()\n```\n\n# active learn<a name="#active-learn"></a>\n\nFor either dedupe or record-linkage, run:\n\n```sh\n   DEDUPER_NAME="<project name>";\n   DEDUPER_FOLDER="<project folder>";\n   python -m dedupe.fastapi.main\n```\n\nreplacing `<project name>` and `<project folder>` with your project settings (for the example above, `test` and `./.dedupe`).\n\nThen return to label-studio and start labelling. When the queue falls under 5 tasks, fastAPI will update the model with labelled samples then send more tasks to review.\n\n# predictions<a name="#predictions"></a>\n\nTo get predictions, simply run the `predict()` method.\n\nDedupe:\n```py\nd = Dedupe(settings=Settings(name="test", folder="./.dedupe"))\nd.predict()\n```\n\nRecord-linkage:\n```py\nd = RecordLinkage(settings=Settings(name="test", folder="./.dedupe"))\nd.predict()\n```',
    'author': 'Chansoo Song',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chansooligans/oagdedupe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
