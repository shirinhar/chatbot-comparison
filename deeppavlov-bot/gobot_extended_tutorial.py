# -*- coding: utf-8 -*-
"""gobot_extended_tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12nFyXpEm4Yr1wlXo_8i6M_kpM8Ws6U_V

### You can also run the notebook in [COLAB](https://colab.research.google.com/github/deepmipt/DeepPavlov/blob/master/examples/gobot_extended_tutorial.ipynb).

# Goal-oriented bot in DeepPavlov

This tutorial describes how to build a goal/task-oriented dialogue system with DeepPavlov framework. It covers the following steps:

0. [Data preparation](#0.-Data-Preparation)
1. [Build Database of items](#1.-Build-Database-of-items)
2. [Build Slot Filler](#2.-Build-Slot-Filler)
3. [Build and Train a Bot](#3.-Build-and-Train-a-Bot)
4. [Interact with bot](#4.-Interact-with-Bot)

An example of the final model served as a telegram bot:

![gobot_example.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_example.png?raw=1)
"""

# !pip install deeppavlov
# !python -m deeppavlov install gobot_simple_dstc2

"""## 0. Data Preparation

In this tutorial we build a chatbot for restaurant booking. To train our chatbot we use [Dialogue State Tracking Challenge 2 (DSTC-2)](http://camdial.org/~mh521/dstc/) dataset. DSTC-2 provides dialogues of a human talking to a booking system labelled with slots and dialogue actions. These labels will be used for training a dialogue policy network.

First of all let's take a quick look at the data for the task.
"""

from deeppavlov.dataset_readers.dstc2_reader import SimpleDSTC2DatasetReader

data = SimpleDSTC2DatasetReader().read('my_data')

# !ls my_data

"""The training/validation/test data are stored in json files (`simple-dstc2-trn.json`, `simple-dstc2-val.json` and `simple-dstc2-tst.json`):"""

# !head -n 101 my_data/simple-dstc2-trn.json

"""To iterate over batches of preprocessed DSTC-2 we need to import `DatasetIterator`."""

from deeppavlov.dataset_iterators.dialog_iterator import DialogDatasetIterator

iterator = DialogDatasetIterator(data)

"""You can now iterate over batches of preprocessed DSTC-2 dialogs:"""

from pprint import pprint

for dialog in iterator.gen_batches(batch_size=1, data_type='train'):
    turns_x, turns_y = dialog
    
    print("User utterances:\n----------------\n")
    pprint(turns_x[0], indent=4)
    print("\nSystem responses:\n-----------------\n")
    pprint(turns_y[0], indent=4)
    
    break

"""In real-life annotation of data is expensive. To make our tutorial closer to production use-cases we take  only 50 dialogues for training."""

# !cp my_data/simple-dstc2-trn.json my_data/simple-dstc2-trn.full.json

import json

NUM_TRAIN = 50

with open('my_data/simple-dstc2-trn.full.json', 'rt') as fin:
    data = json.load(fin)
with open('my_data/simple-dstc2-trn.json', 'wt') as fout:
    json.dump(data[:NUM_TRAIN], fout, indent=2)
print(f"Train set is reduced to {NUM_TRAIN} dialogues (out of {len(data)}).")

"""## 1. Build Database of items

### Building database of restaurants

To assist with restaurant booking the chatbot should have access to a `database` of restaurants. The `database` contains task-specific information such as type of food, price range, location, etc.

    >> database([{'pricerange': 'cheap', 'area': 'south'}])
    
    Out[1]: 
        [[{'name': 'the lucky star',
           'food': 'chinese',
           'pricerange': 'cheap',
           'area': 'south',
           'addr': 'cambridge leisure park clifton way cherry hinton',
           'phone': '01223 244277',
           'postcode': 'c.b 1, 7 d.y'},
          {'name': 'nandos',
           'food': 'portuguese',
           'pricerange': 'cheap',
           'area': 'south',
           'addr': 'cambridge leisure park clifton way',
           'phone': '01223 327908',
           'postcode': 'c.b 1, 7 d.y'}]]

&nbsp;
![gobot_database.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_database.png?raw=1)
&nbsp;

The chatbot should be trained to make api calls. For this, training dataset contains a `"db_result"` dictionary key. It annotates turns where system performs an api call to the database of items. Rusulting value is stored in `"db_result"`.
"""

# !head -n 78 my_data/simple-dstc2-trn.json | tail +51

"""Set `primary_keys` to a list of slot names that have unique values for different items (common SQL term). For the case of DSTC-2, the primary slot is a restaurant name."""

from deeppavlov.core.data.sqlite_database import Sqlite3Database

database = Sqlite3Database(primary_keys=["name"],
                           save_path="my_bot/db.sqlite")

"""
Let's find all `"db_result"` api call results and add them to our database of restaurants:"""

db_results = []

for dialog in iterator.gen_batches(batch_size=1, data_type='all'):
    turns_x, turns_y = dialog
    db_results.extend(x['db_result'] for x in turns_x[0] if x.get('db_result'))


print(f"Adding {len(db_results)} items.")
print(db_results)
if db_results:
    database.fit(db_results)

"""### Interacting with database

We can now play with the database and make requests to it:
"""

database([{'pricerange': 'cheap', 'area': 'south'}])

# !ls my_bot

"""## 2. Build Slot Filler

`Slot Filler` is a component that finds slot values in user input:

    >> slot_filler(['I would like some chineese food'])
    
    Out[1]: [{'food': 'chinese'}]

&nbsp;
![gobot_slotfiller.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_slotfiller.png?raw=1)
&nbsp;

To implement a `Slot Filler` you need to provide
    
 - **slot types**,
 - all possible **slot values**,
 - also, it is good to have examples of mentions for every value of each slot.
 
In this tutorial, a schema for `slot types` and `slot values` should be defined in `slot_vals.json` with the following format:

    {
        'food': {
            'chinese': ['chinese', 'chineese', 'chines'],
            'french': ['french', 'freench'],
            'dontcare': ['any food', 'any type of food']
        }
    }
                

Let's use a simple non-trainable slot filler that relies on Levenshtein distance.
"""

from deeppavlov.download import download_decompress

download_decompress(url='http://files.deeppavlov.ai/deeppavlov_data/dstc_slot_vals.tar.gz',
                    download_path='my_bot/slotfill')

# !ls my_bot/slotfill

"""Print some `slot types` and `slot values`."""

# !head -n 10 my_bot/slotfill/dstc_slot_vals.json

"""Check performance of our slot filler on DSTC-2 dataset."""

from deeppavlov import configs
from deeppavlov.core.common.file import read_json

slotfill_config = read_json(configs.ner.slotfill_simple_dstc2_raw)

"""We take [original DSTC2 slot-filling config](https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/ner/slotfill_dstc2_raw.json) from DeepPavlov and change variables determining data paths:"""

slotfill_config['metadata']['variables']['DATA_PATH'] = 'my_data'
slotfill_config['metadata']['variables']['SLOT_VALS_PATH'] = 'my_bot/slotfill/dstc_slot_vals.json'

"""Run evaluation."""

from deeppavlov import evaluate_model

slotfill = evaluate_model(slotfill_config);

"""We've got slot accuracy of **93% on valid** set and **95% on test** set.

Building `Slot Filler` model from DeepPavlov config.
"""

from deeppavlov import build_model

slotfill = build_model(slotfill_config)

"""Testing the model."""

slotfill(['i want cheap chinee food'])

"""Saving slotfill config file to disk (we will require it's path later)."""

import json

json.dump(slotfill_config, open('my_bot/slotfill_config.json', 'wt'))

# !ls my_bot

"""## 3. Build and Train a Bot

### Dialogue policy and response templates

A policy module of the bot decides what action should be taken in the current dialogue state. The policy in our bot is implemented as a recurrent neural network (recurrency over user utterances) followed by a dense layer with softmax function on top. The network classifies user input into one of predefined system actions. Examples of possible actions are to say hello, to request user's location or to make api call to a database.

![gobot_policy.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_policy.png?raw=1)

All actions available for the system should be listed in a `simple-dstc2-templates.txt` file. Also, every action should be associated with a template string of the corresponding system response.

![gobot_templates.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_templates.png?raw=1)

Templates for responses should be in the format `<act>TAB<template>`, where `<act>` is a dialogue action and `<template>` is the corresponding response. The response text might contain slot type names, where every `#slot_type` will be filled with the slot value from the current dialogue state.
"""

# !head -n 10 my_data/simple-dstc2-templates.txt

"""In essense, the dialogue policy module solves classification task, where a set of classes is defined in `simple-dstc2-templates.txt`. So, to train the dialogue policy network you need action label for each system's turn in training dialogues. The DSTC-2 provides `"act"` dictionary key that contains action associated with current response. Here is an example of training data for the policy network."""

# !head -n 24 my_data/simple-dstc2-trn.json

"""Now we configure a full data processing pipline for the restaurant bot.

As a starting point, let's take a [simple DSTC2 bot config](https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/go_bot/gobot_simple_dstc2.json) ([more configs](https://github.com/deepmipt/DeepPavlov/blob/master/deeppavlov/configs/go_bot) are available) from DeepPavlov and, then change sections responsible for:
- embeddings, 
- database,
- slot filler,
- templates,
- data and model load/save paths.

Loading bot:
"""

from deeppavlov import configs
from deeppavlov.core.common.file import read_json

gobot_config = read_json(configs.go_bot.gobot_simple_dstc2)

"""Set default bag-of-words embedder:"""

gobot_config['chainer']['pipe'][-1]['embedder'] = None

"""Configure bot to use our database:"""

gobot_config['chainer']['pipe'][-1]['database'] = {
    'class_name': 'sqlite_database',
    'primary_keys': ["name"],
    'save_path': 'my_bot/db.sqlite'
}

"""Configure bot to use levenshtein distance based slot filler:"""

gobot_config['chainer']['pipe'][-1]['slot_filler']['config_path'] = 'my_bot/slotfill_config.json'

"""To maintain values of slots of the whole conversation, we first detect slot values mentioned in the latest utterance and then apply `tracker` module which updates current global slot values, so called dialogue state:"""

gobot_config['chainer']['pipe'][-1]['tracker']['slot_names'] = ['pricerange', 'this', 'area', 'food']

"""Configure bot to use templates:"""

gobot_config['chainer']['pipe'][-1]['nlg_manager']['template_type'] = 'DefaultTemplate'
gobot_config['chainer']['pipe'][-1]['nlg_manager']['template_path'] = 'my_data/simple-dstc2-templates.txt'

"""Specify train/valid/test data path and path to save the final bot model:"""

gobot_config['metadata']['variables']['DATA_PATH'] = 'my_data'
gobot_config['metadata']['variables']['MODEL_PATH'] = 'my_bot'

"""The whole dialogue system pipeline looks like this:

![gobot_pipeline.png](https://github.com/deepmipt/DeepPavlov/blob/master/examples/img/gobot_pipeline.png?raw=1)

### Training policy network
"""

from deeppavlov import train_model

gobot_config['train']['batch_size'] = 8 # batch size
gobot_config['train']['max_batches'] = 250 # maximum number of training batches
gobot_config['train']['log_on_k_batches'] = 20
gobot_config['train']['val_every_n_batches'] = 40 # evaluate on full 'valid' split each n batches
gobot_config['train']['log_every_n_batches'] = 40 # evaluate on 20 batches of 'train' split every n batches

train_model(gobot_config);

"""Training on 50 dialogues takes from 5 to 20 minutes depending on gpu/cpu hardware. Training on 1000 dialogues takes 10-30 mins.

See DeepPavlov [config doc page](http://docs.deeppavlov.ai/en/master/intro/configuration.html) for advanced configuration of the training process.

### Evaluation of training

Calculating **accuracy** of trained bot: whether predicted system responses match true responses (full string match).
"""

from deeppavlov import evaluate_model

evaluate_model(gobot_config);

"""With settings of `max_batches=250`, valid accuracy `= 0.5` and test accuracy is `~ 0.5`.

## 4. Interact with Bot
"""

from deeppavlov import build_model

bot = build_model(gobot_config)

bot(['hi, i want to eat, can you suggest a place to go?'])

bot(['i want cheap food'])

bot(['chinese food'])

bot(['thanks, give me their address'])

bot(['i want their phone number too'])

bot(['bye'])

bot.reset()

bot(['hi, is there any cheap restaurant?'])

"""You can also train a Simple bot following [gobot_tutorial.ipynb](https://github.com/deepmipt/DeepPavlov/blob/master/examples/gobot_tutorial.ipynb)"""

