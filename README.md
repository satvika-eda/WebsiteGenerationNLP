# WEBCRAFT - WHERE WORDS CREATE WEBPAGES

The Website Generation NLP project aims to simplify webpage creation using Natural Language Processing (NLP) and Web Development technologies. By leveraging NLP algorithms to interpret user input and organize content, the project facilitates the generation of aesthetically pleasing web layouts without requiring complex coding skills. This approach bridges the gap between technical and non-technical users, offering an intuitive interface for online content creation.

## Environment
To train the model, we have used a cluster with gpu type a100/80G and 12 CPUs.

## Files
1. data/Gettingdata.ipynb
    - This file will convert each URL into a prompt and its corresponding html code. It saves the data in json format.
      
2. src/code_llama.ipynb
    - This file has the code used for fine-tuning code_llama model with custom dataset as well as the evaluation steps for evaluating the model giving the user input.

3. src/falcon_training.ipynb
    - This file has the code used for fine-tuning falcon model with custom dataset as well as the evaluation steps for evaluating the model giving the user input.

4. src/llama_training.ipynb
    - This file has the code used for fine-tuning llama2 model with custom dataset as well as the evaluation steps for evaluating the model giving the user input.

5. src/gpt2_training.ipynb
    - This file has the code used for fine-tuning gpt2 model with custom dataset.

## Execution
1. Install the requirements stated in the requirements.txt or type the command in the terminal 
```pip install -r requirements.txt```
2. Execute each cell in the jupyter notebook based on the comments provided in the notebook to either train or to evaluate the model.


## Model
The fine-tuned code-llama model is saved in the models folder.

For more details, please refer project report.
