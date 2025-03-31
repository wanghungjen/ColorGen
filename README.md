# Color Generator

## Motivation
Inspired by the recent wave of AI-generated art, I became curious about how colors get their names. Why does a shade called *Mountain Hideaway* evoke a sandy hue, while *Matrix* is a vivid green? These names seem to carry a certain semantic weight — suggesting that there's more to explore in color naming.

This led me to wonder whether deep learning could be used to capture some of the semantic patterns behind these naming conventions. Could a model learn to associate words with colors in a meaningful way? Building on that, can we use this information to associate colors with various terms or concepts? For example, what are the color representations of different programming languages? What does Python look like in color? What about C?

## References

This project is based on [this tutorial](https://fritz.ai/how-to-train-a-keras-model-to-generate-colors/). Some parts of the original code were outdated or deprecated, so I updated them to work with the latest version.


## Model Architecture
![](/images/model.png)

## Development + Learning Objectives

### Why One-Hot Encoding?

At first glance, it might seem sufficient to represent each character as a numeric ID for computational purposes. However, assigning numerical values like "a" = 2 and "e" = 4 can unintentionally introduce ordinal relationships — suggesting, for example, that 2 × "a" = "e", which makes no semantic sense. These misleading patterns could cause the model to learn the wrong relationships early on.

To avoid this, we use one-hot encoding. By representing each character as a vector where only one index is "hot" (set to 1) and the rest are 0, we ensure that each character is treated as a unique, independent category, with no implied hierarchy or magnitude between them.

### Why Use LSTMs?

Unlike traditional dense layers that process input all at once, LSTMs (Long Short-Term Memory networks) are designed to process data sequentially. This makes them especially well-suited for tasks where order matters — like interpreting sequences of characters.

Consider the words "earth" and "heart". Although they share the same letters, their meanings — and potentially their color representations — are completely different due to the order of the characters. LSTMs are able to preserve and learn from these sequential dependencies, allowing the model to distinguish between such cases effectively.

In short, LSTMs give the model a memory of past inputs, helping it make more context-aware predictions when handling character-based data.

## Examples
We attempted to predict the colors associated with Red, Green, Blue, Python, and C. The results are shown below:

| ![](/images/red.png) | ![](/images/green.png) | ![](/images/blue.png) | ![](/images/python.png) | ![](/images/c++.png) |
|:--------------------:|:--------------------:|:--------------------:|:--------------------:|:--------------------:|

## How to Run the Project
To install the required libraries:
```
pip3 install -r requirements.txt
```
To run the code:
```
python3 main.py
```
Feel free to experiment with different text inputs to see how the model responds!
