## Empathetic Dialogue Model - verbal
#### - To generate an AI agent response based on verbal information in the conversation


----------------------------------

## Empathetic Response Generation

The model is built on KE-T5, a pre-trained language model, and fine-tuned using AI-HUB's empathy conversation dataset, KETI conversation dataset, and more.

The model and usage information is as follows.


#### How to use

1) Run the command below to download the model parameters (weights)
```bash
    python get_weight.py
```

1) Run the command below to generate a empathetic response
```bash
    python agent.py
```


#### Pretrained Language Model
- KE-T5 base
(https://github.com/AIRC-KETI/ke-t5)



#### Etc
- The model training parameters (weight values) are saved to the directory below after downloading.

    (./model/ke_t5_dm/best.pt)
