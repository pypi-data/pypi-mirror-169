# Generative Language Models for Paragraph-Level Question Generation: A Unified Benchmark and Evaluation

<p align="center">
  <img src="https://github.com/asahi417/lm-question-generation/blob/master/assets/qg_diagram.png" width="500">
</p>

This is the official repository of the paper
"Generative Language Models for Paragraph-Level Question Generation:
A Unified Benchmark and Evaluation, EMNLP 2022 main conference".
This repository includes following contents:
- ***QG-Bench***, the first ever multilingual/multidomain QG benchmark.
- ***Multilingual/multidomain QG models*** fine-tuned on QG-Bench.
- A python library ***`lmqg`*** developed to fine-tune/evaluate QG model.
- ***AutoQG***, a web application hosting QG models where user can test the model output interactively. 

### Table of Contents  
1. **[QG-Bench: multilingual & multidomain QG datasets (+ fine-tuned models)](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md)**
2. **[LMQG: python library to fine-tune/evaluate QG model](#lmqg-language-model-for-question-generation)**
3. **[AutoQG: web application hosting multilingual QG models](#autoqg)**
4. **[RestAPI: run model prediction via restAPI](#rest-api-with-huggingface-inference-api)**
5. **[Reproduce Analysis of the Paper](#reproduce-analysis)**

Please cite following paper if you use any resource:
```
@inproceedings{ushio-etal-2022-generative,
    title = "{G}enerative {L}anguage {M}odels for {P}aragraph-{L}evel {Q}uestion {G}eneration: {A} {U}nified {B}enchmark and {E}valuation",
    author = "Ushio, Asahi  and
        Alva-Manchego, Fernando  and
        Camacho-Collados, Jose",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, U.A.E.",
    publisher = "Association for Computational Linguistics",
}
```

## LMQG: Language Model for Question Generation 🚀
The `lmqg` is a python library to fine-tune seq2seq language models ([T5](https://arxiv.org/pdf/1910.10683.pdf), [BART](https://arxiv.org/pdf/1910.13461.pdf)) 
on the question generation task and provide an API to host the model prediction via [huggingface](https://huggingface.co/).
Let's install `lmqg` via pip first.
```shell
pip install lmqg
```

### Model Evaluation
The evaluation tool reports `BLEU4`, `ROUGE-L`, `METEOR`, `BERTScore`, and `MoverScore` following [QG-Bench](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md).

```shell
lmqg-eval -m ckpt/test/epoch_10/ -e ckpt/test/epoch_10/eval
```
Check `lmqg-eval -h` to display all the options.


### Model Training
<p align="center">
  <img src="https://github.com/asahi417/lm-question-generation/blob/master/assets/grid_search.png" width="500">
</p>

To fine-tune QG model, we employ a two-stage hyper-parameter optimization, described as above diagram.
Following command is to run the fine-tuning with parameter optimization.
```shell
lmqg-train-search -c "tmp_ckpt" -d "lmqg/qg_squad" -m "t5-small" -b 64 --epoch-partial 5 -e 15 --language "en" --n-max-config 1 \
  -g 2 4 \
  --lr 1e-04 5e-04 1e-03 \
  --label-smoothing 0 0.15
```
Check `lmqg-train-search -h` to display all the options.

Fine-tuning models in python follows below.  
```python
from lmqg import GridSearcher
trainer = GridSearcher(
    checkpoint_dir='tmp_ckpt', dataset_path='lmqg/qg_squad', model='t5-small', epoch=15, epoch_partial=5, batch=64, n_max_config=5,
    gradient_accumulation_steps=[2, 4], lr=[1e-04, 5e-04, 1e-03], label_smoothing=[0, 0.15])
trainer.run()
```


## AutoQG

<p align="center">
  <img src="https://github.com/asahi417/lm-question-generation/blob/master/assets/autoqg.gif" width="500">
</p>

***AutoQG ([https://autoqg.net](https://autoqg.net/))*** is a free web application hosting our QG models.
The QG models are listed at the [QG-Bench page](https://github.com/asahi417/lm-question-generation/blob/master/QG_BENCH.md).

## Rest API with huggingface inference API
<p align="center">
  <img src="https://github.com/asahi417/lm-question-generation/blob/master/assets/api.png" width="500">
</p>

We provide a rest API which hosts the model inference through huggingface inference API. You need huggingface API token to run your own API and install dependencies as below.
```shell
pip install lmqg[api]
```
Swagger UI is available at [`http://127.0.0.1:8080/docs`](http://127.0.0.1:8080/docs), when you run the app locally (replace the address by your server address).

- Build/Run Local (command line):
```shell
export API_TOKEN={Your Huggingface API Token}
uvicorn app:app --reload --port 8088
uvicorn app:app --host 0.0.0.0 --port 8088
```

- Build/Run Local (docker):
```shell
docker build -t lmqg/app:latest . --build-arg api_token={Your Huggingface API Token}
docker run -p 8080:8080 lmqg/app:latest
```


## Reproduce Analysis
- [Model Fine-tuning/Evaluation](https://github.com/asahi417/lm-question-generation/tree/master/misc/qg_model_training)
- [QA based Evaluation](https://github.com/asahi417/lm-question-generation/tree/master/misc/qa_based_evaluation)
- [NQG model baseline](https://github.com/asahi417/lm-question-generation/tree/master/misc/nqg_baseline)