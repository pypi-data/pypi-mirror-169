# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['perceiver',
 'perceiver.data',
 'perceiver.data.image',
 'perceiver.data.text',
 'perceiver.model',
 'perceiver.model.core',
 'perceiver.model.image',
 'perceiver.model.text',
 'perceiver.scripts',
 'perceiver.scripts.image',
 'perceiver.scripts.text',
 'perceiver.scripts.utils']

package_data = \
{'': ['*']}

install_requires = \
['einops>=0.4.0,<0.5.0',
 'fairscale>=0.4.0,<0.5.0',
 'fsspec[s3]==2022.5.0',
 'jsonargparse[signatures]>=4.12.0,<4.13.0',
 'pytorch-lightning>=1.7.0,<1.8.0',
 'torch-optimizer>=0.3.0,<0.4.0',
 'torch>=1.12.0,<1.13.0',
 'torchmetrics>=0.9.0,<0.10.0']

extras_require = \
{'image': ['datasets>=2.4.0,<2.5.0', 'torchvision>=0.13.0,<0.14.0'],
 'text': ['datasets>=2.4.0,<2.5.0',
          'tokenizers>=0.12.0,<0.13.0',
          'transformers>=4.21.0,<4.22.0']}

setup_kwargs = {
    'name': 'perceiver-io',
    'version': '0.6.0',
    'description': 'Perceiver IO',
    'long_description': '# Perceiver, Perceiver IO and Perceiver AR\n\nThis repository is a PyTorch and PyTorch Lightning implementation of\n\n<table>\n  <tr>\n    <td>\n       <b>Perceiver</b>: General Perception with Iterative Attention\n       (<a href="https://arxiv.org/abs/2103.03206">paper</a>,\n        <a href="https://www.youtube.com/watch?v=P_xeshTnPZg">video</a>)\n    </td>\n    <td><img src="docs/images/small-perceiver.png" alt="Perceiver"/></td>\n  </tr>\n  <tr>\n    <td>\n      <b>Perceiver IO</b>: A General Architecture for Structured Inputs & Outputs\n      (<a href="https://arxiv.org/abs/2107.14795">paper</a>,\n       <a href="https://www.deepmind.com/blog/building-architectures-that-can-handle-the-worlds-data">blog post</a>)\n    </td>\n    <td><img src="docs/images/small-perceiver-io.png" alt="Perceiver IO"/></td>\n  </tr>\n  <tr>\n    <td>\n      General-purpose, long-context autoregressive modeling with <b>Perceiver AR</b>\n      (<a href="https://arxiv.org/abs/2202.07765">paper</a>,\n       <a href="https://www.deepmind.com/blog/perceiver-ar-general-purpose-long-context-autoregressive-generation">blog post</a>)\n    </td>\n    <td><img src="docs/images/small-perceiver-ar.png" alt="Perceiver AR"/></td>\n  </tr>\n</table>\n\nThe codebase is modular and designed for easy extension to new tasks and datasets. The integration with\n[PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/) supports model training at scale. The command\nline interface is implemented with the [Lightning CLI](https://pytorch-lightning.readthedocs.io/en/stable/cli/lightning_cli.html).\n\n[Pretrained models](docs/pretrained-models.md) can be imported from the 🤗 Hub. Datasets used for model training\nare 🤗 [Datasets](https://huggingface.co/docs/datasets) wrapped into PyTorch Lightning data modules. For NLP tasks,\nthis library also supports 🤗 [fast tokenizers](https://huggingface.co/docs/transformers/fast_tokenizers) and the\n🤗 Perceiver UTF-8 bytes tokenizer.\n\n## Installation\n\n### Via pip\n\n```shell\npip install perceiver-io[image,text]\n```\n\n### From sources\n\nInstallation from sources requires a [Miniconda](https://docs.conda.io/en/latest/miniconda.html) and a\n[Poetry](https://python-poetry.org/docs/#installation) (1.2.0 or higher) installation.\n\n```shell\nconda env create -f environment.yml\nconda activate perceiver-io\npoetry install --all-extras\n```\n\n### Docker image\n\n```shell\ndocker pull ghcr.io/krasserm/perceiver-io:latest\n```\n\nSee [Docker image](docs/docker-image.md) for details.\n\n## Documentation\n\n- [Pretrained models](docs/pretrained-models.md)\n- [Model construction](docs/model-construction.md)\n- [Building blocks](docs/building-blocks.md)\n- [Training examples](docs/training-examples.md)\n- [Inference examples](notebooks/inference_examples.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/krasserm/perceiver-io/blob/main/notebooks/inference_examples.ipynb)\n\n## Getting started\n\nHere\'s a minimal example for autoregressive language modeling with Perceiver AR. A small language model (30.7M parameters)\nis trained on the WikiText-103-raw dataset and then used to generate text from a prompt. Input text is tokenized into\nraw UTF-8 bytes, the model also predicts the raw UTF-8 bytes of generated text. More details about Perceiver AR and\nPerceiver IO model construction, training and inference are covered in the [documentation](#documentation).\n\n### Training\n\nThe command line interface is implemented with [Lightning CLI](https://pytorch-lightning.readthedocs.io/en/stable/cli/lightning_cli.html).\nModel training can be started with:\n\n```shell\npython -m perceiver.scripts.text.clm fit \\\n  --model.num_latents=512 \\\n  --model.num_channels=512 \\\n  --model.num_self_attention_layers=8 \\\n  --model.cross_attention_dropout=0.5 \\\n  --data=WikiTextDataModule \\\n  --data.tokenizer=deepmind/language-perceiver \\\n  --data.max_seq_len=4096 \\\n  --data.batch_size=16 \\\n  --data.task=clm \\\n  --optimizer=Adam \\\n  --optimizer.lr=2e-4 \\\n  --trainer.max_steps=5000 \\\n  --trainer.accelerator=gpu \\\n  --trainer.devices=1 \\\n  --trainer.accumulate_grad_batches=4\n```\n\nYou can also do this programmatically with the PyTorch Lightning `Trainer`:\n\n```python\nfrom torch.optim import Adam\n\nfrom perceiver.data.text.wikitext import WikiTextDataModule, Task\nfrom perceiver.model.text.clm import LitCausalLanguageModel, CausalLanguageModelConfig\n\nimport pytorch_lightning as pl\n\n\n# Lightning WikiText data module\ndata = WikiTextDataModule(\n    tokenizer="deepmind/language-perceiver",\n    max_seq_len=4096,\n    batch_size=16,\n    task=Task.clm,\n)\n\n# Language model configuration object\nmodel_config = CausalLanguageModelConfig(\n    vocab_size=data.vocab_size,\n    max_seq_len=data.max_seq_len,\n    num_latents=512,\n    num_channels=512,\n    num_self_attention_layers=8,\n    cross_attention_dropout=0.5,\n)\n\ndef configure_optimizers(self):\n    return Adam(self.parameters(), lr=2e-4)\n\n# Associate optimizer factory with Lightning module (not predefined there)\nsetattr(LitCausalLanguageModel, "configure_optimizers", configure_optimizers),\n\n# Lightning module of language model (a Perceiver AR)\nlit_model = LitCausalLanguageModel.create(model_config)\n\n# Instantiate Lightning Trainer\ntrainer = pl.Trainer(accelerator="gpu", devices=1, max_steps=5000, accumulate_grad_batches=4)\n\n# Train model (will also preprocess dataset if used for the first time)\ntrainer.fit(lit_model, datamodule=data)\n```\n\nIf you instead want to use plain PyTorch (without PyTorch Lightning, except for data sources):\n\n```python\nfrom perceiver.model.text.clm import CausalLanguageModel\n\nimport torch.nn.functional as F\nfrom torch.optim import Adam\n\ndata = ...\ndata.prepare_data()\ndata.setup()\n\nmodel_config = ...\n\n# Plain PyTorch module of language model\nmodel = CausalLanguageModel(config=model_config)\nmodel.train()\n\noptim = Adam(model.parameters(), lr=2e-4)\n\n# Simplified training loop compared to previous examples\n# (no gradient accumulation, epochs instead of max_steps, ...)\nfor epoch in range(4):\n    for labels_ids, input_ids, _ in data.train_dataloader():\n        logits = model(input_ids)\n        loss = F.cross_entropy(logits.permute(0, 2, 1), labels_ids[:, -model_config.num_latents:])\n        loss.backward()\n        optim.step()\n        optim.zero_grad()\n```\n\n### Inference\n\n```python\nfrom perceiver.model.text.clm import LitCausalLanguageModel\n\ndata = ...\n\n# Load Lightning module from training checkpoint\nlit_model = LitCausalLanguageModel.load_from_checkpoint("/path/to/checkpoint")\n\n# Obtain trained plain PyTorch model\nmodel = lit_model.model.eval()\n\n# Get text preprocessor from data module\npreproc = data.text_preprocessor()\n\n# Tokenize a sample prompt\nprompt, _ = preproc.preprocess("A man was reading a book on a sunny day until he sudden")\n\n# Generate tokens from prompt via top-k sampling where k = f(vocab_size, threshold)\ngenerated = model.generate(num=512, prompt=prompt[None, ...], threshold=0.9)[0]\n\n# Decode generated tokens\ngenerated_text = data.tokenizer.decode(generated)\n```\n\nYou can also run text generation interactively in the [Colab notebook](https://colab.research.google.com/github/krasserm/perceiver-io/blob/main/notebooks/inference_examples.ipynb).\n\n## Other implementations\n\n- [Perceiver](https://paperswithcode.com/paper/perceiver-general-perception-with-iterative#code)\n- [Perceiver IO](https://paperswithcode.com/paper/perceiver-io-a-general-architecture-for#code)\n- [Perceiver AR](https://paperswithcode.com/paper/general-purpose-long-context-autoregressive#code)\n',
    'author': 'Martin Krasser',
    'author_email': 'krasserm@googlemail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/krasserm/perceiver-io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
