# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xtsv_word']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xtsv-word',
    'version': '1.0.2',
    'description': 'A dataclass-like structure to make the handling of xtsv token attributes comfortable and transparent',
    'long_description': "# xtsv-word\n\n**This module provides a special dataclass-like structure to handle tokens in [xtsv](https://github.com/nytud/xtsv) format. It is meant to be used within `xtsv` modules to make the processing of token attributes (`xtsv` fields) more comfortable and transparent.**\n\nIt allows for each token to be represented by a `Word` object which is initialised simply by passing the token in its `xtsv` representation (i.e. a list of strings, one for each field in the input stream) to a `WordFactory` object. This factory object keeps track of the input and target fields of the `xtsv` module, and assigns the items of the list representing the token in `xtsv` to the respective `Word` object attributes which are identified by the name of the corresponding field (i.e. the `xtsv` column header).\n\nBoth the input and the target fields can be accessed as attributes of a `Word` object, i.e. they can be both retrieved and modified. (The usual use case is to only read input field attributes and to specify target field attributes. However, the `Word` object does not prevent a user from modifying input field values. This is discouraged but not ruled out by `xtsv`.) When the `xtsv` module is done processing a token, the `Word` object is simply converted into a list which contains the original input fields followed by the target fields, as expected by `xtsv`.\n\nDisclaimer: This is not an official extension of the [xtsv](https://github.com/nytud/xtsv) module.\n\n## Suggested usage\n\nInstall `xtsv-word` from `pip`:\n```\npython3 -m pip install xtsv-word\n```\n\nor build locally:\n```\nmake\n```\n\nFor example, assuming that the internal app object defined in the `xtsv` module `myXtsvModule` is called `InternalApp`, the input stream contains the fields `['form', 'wsafter']` and `myXtsvModule` has a single target field: `['syllables']`:\n\n1. **Create `WordFactory` object:**\n\n```\n# myXtsvModule.py\n\nfrom xtsv_word import WordFactory\n\nclass InternalApp:\n\t...\n\tdef prepare_fields(self, field_names):\n\t\tself.wf = WordFactory(field_names, self.target_fields)\n\t\t# self.target_fields is normally set in InternalApp.__init__()\n```\n\n2. **Use `Word` object:**\n\n```\nclass InternalApp:\n\t...\n\tdef process_sentence(self, sen, field_values):\n\t\treturn_sen = []\n\t\tfor tok in sen:\n\t\t\t# Get Word object from factory\n\t\t\tword = self.wf.get_word(tok)\n\n\t\t\t# process token by getting and setting its attributes, e.g.:\n\t\t\tword.syllables = split_syllables(word.form)\n\t\t\t...\n\t\t\t# alternatively access attributes as dict keys:\n\t\t\tword['syllables'] = '-'.join(word['syllables'])\n\n\t\t\t# convert Word object to list of fields for xtsv output stream\n\t\t\treturn_sen.append(list(word))\n\n\t\t...\n\t\treturn return_sen\n```\n\nSee docstrings for further details.\n",
    'author': 'Pethő Gergely',
    'author_email': 'pagstudium@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ril-lexknowrep/xtsv-word',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
