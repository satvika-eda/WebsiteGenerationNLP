WEBCRAFT


This repository contains code for training a pre trained Code-Llama model to generate HTML code from natural language prompts. The model is fine-tuned on a custom dataset containing pairs of prompts and corresponding HTML outputs.

Installation
To install the required dependencies, run:

pip install -r requirements.txt


This will install the necessary Python packages, including PyTorch, Transformers, tqdm, NumPy, pandas, accelerate, peft, trl and bitsandbytes.

Usage:

Training: To train the model, run the train.py script with the appropriate arguments. Make sure to specify the path to your dataset and any other relevant parameters.

Inference: Once the model is trained, you can generate HTML code from prompts using the generate.py script. Provide a prompt as input, and the model will output the corresponding HTML code.

Evaluation: Use the evaluate.py script to evaluate the model's performance on a test dataset. This script computes metrics such as accuracy, F1 score, and area under the ROC curve.

Directory Structure

data/: Contains the dataset used for training and evaluation.
models/: Saved model checkpoints.
src/: Source code for training, inference, and evaluation.
requirements.txt: List of required Python packages.


Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests through GitHub.

License
