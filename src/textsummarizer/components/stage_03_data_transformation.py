from textsummarizer.entities import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_from_disk
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_tokens(self, example_batch):

        input_encodings = self.tokenizer(example_batch['dialogue'], truncation=True, max_length=1024)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], truncation=True, max_length=128)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert_data(self):
        data_samsum = load_from_disk(self.config.data_path)
        data_samsum_temp = data_samsum.map(self.convert_examples_to_tokens, batched=True)
        data_samsum_temp.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
