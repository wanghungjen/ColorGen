# Color Generator

## Motivation
Inspired by the recent wave of AI-generated art, I became curious about how colors get their names. Why does a shade called *Mountain Hideaway* evoke a sandy hue, while *Matrix* is a vivid green? These names seem to carry a certain semantic weight — suggesting that there's more to explore in color naming.

This led me to wonder whether deep learning could be used to capture some of the semantic patterns behind these naming conventions. Could a model learn to associate words with colors in a meaningful way? Building on that, can we use this information to associate colors with various terms or concepts? For example, what are the color representations of different programming languages? What does Python *look* like in color? What about C?

## Development

## Model Architecture
![](/images/model.png)

## Example
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

## References

This project is based on [this tutorial](https://fritz.ai/how-to-train-a-keras-model-to-generate-colors/). Some parts of the original code were outdated or deprecated, so I updated them to work with the latest version.
