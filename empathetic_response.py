import os
import torch
import numpy as np

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

device = 'cpu'
if torch.cuda.is_available():
    device = 'cuda'

softmax = torch.nn.Softmax(dim=1)

class DM_Response:
    def __init__(self, model_number, models_folder):

        self.model_name = "KETI-AIR/long-ke-t5-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

        # load model of fine-tuning
        model_path = os.path.join(models_folder, f"{model_number}.pt")
        self.model.load_state_dict(torch.load(model_path))
        self.model = self.model.to(device)
        print(f"model {model_number} loaded!")

        self.response_only = ""

    def response(self, dm_input):
        print(dm_input)
        response = self.get_response(dm_input)
        return response

    def detach_stg(self, output_text):
        splits = output_text.split()
        self.response_only = ' '.join(splits[2:]) # to return only uttr (not stg and emotion)


    def get_response(self, dm_input):
        input_txt = [dm_input]

        self.model.eval()

        inputs = self.tokenizer(input_txt, padding=True, truncation='longest_first', return_tensors='pt')
        input_ids = inputs.input_ids.to(device)

        text = self.model.generate(input_ids, max_length=50, num_beams=4, repetition_penalty=2.0)
        output_text = self.tokenizer.decode(text[0], skip_special_tokens=True)

        return output_text



