# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lit']

package_data = \
{'': ['*']}

install_requires = \
['onnx2torch>=1.5.3,<2.0.0',
 'onnxruntime>=1.12.1,<2.0.0',
 'opencv-python>=4.4.0,<5.0.0,!=4.6.0.66',
 'pytorch-lantern>=0.12.1,<0.13.0',
 'transformers>=4.22.1,<5.0.0',
 'wget>=3.2,<4.0']

setup_kwargs = {
    'name': 'pytorch-zero-lit',
    'version': '0.2.3',
    'description': 'LiT: Zero-Shot Transfer with Locked-image text Tuning',
    'long_description': '# pytorch-zero-lit\n\nConverted official JAX models for [LiT: Zero-Shot Transfer with Locked-image text Tuning](https://arxiv.org/pdf/2111.07991v3.pdf)\nto pytorch.\n\n_JAX -> Tensorflow -> ONNX -> Pytorch._\n\n- Image encoder is loaded into pytorch and supports gradients\n- Text encoder is not loaded into pytorch and runs via ONNX on cpu\n\n## Install\n\n```bash\npoetry add pytorch-zero-lit\n```\n\nor\n\n```bash\npip install pytorch-zero-lit\n```\n\n## Usage\n\n```python\nfrom lit import LiT\n\nmodel = LiT()\n\nimages = TF.to_tensor(\n    Image.open("cat.png").convert("RGB").resize((224, 224))\n)[None]\ntexts = [\n    "a photo of a cat",\n    "a photo of a dog",\n    "a photo of a bird",\n    "a photo of a fish",\n]\n\nimage_encodings = model.encode_images(images)\ntext_encodings = model.encode_texts(texts)\n\ncosine_similarity = model.cosine_similarity(image_encodings, text_encodings)\n```\n',
    'author': 'Richard Löwenström',
    'author_email': 'samedii@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/samedii/pytorch-zero-lit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
