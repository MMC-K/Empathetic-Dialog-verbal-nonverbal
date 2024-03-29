## Empathetic Dialogue Model - verbal & non-verbal
#### - To generate an AI agent non-verbal response based on a verbal response in the conversation


----------------------------------

## Empathetic Response Generation

The model is built on long-KE-T5, a pre-trained language model, and fine-tuned using KETI conversation dataset.

The model will be updated occasionally.

The model and usage information is as follows.


#### How to use

1) Run the command below to download the model parameters (weights)
```bash
    python get_weight.py
```

1) Run the command below to generate an empathetic response
```bash
    python agent.py
```


#### Pretrained Language Model
- long-KE-T5
(https://github.com/AIRC-KETI/long-ke-t5)



#### Etc
- The model training parameters (weight values) are saved to the directory below after downloading.

    (./model/ke_t5_dm/best.pt)
