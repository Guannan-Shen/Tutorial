# Notes by Guannan Shen using following references
## [Neural networks and deeplearning](http://neuralnetworksanddeeplearning.com/)
### Chapter 1
#### Perceptrons
A perceptron takes several binary inputs, x<sub>1</sub>, x<sub>2</sub>, …, and produces a single binary output. 
With the concept of weights, w<sub>1</sub>, w<sub>2</sub>, …, expressing the importance of the respective inputs. The output is 0 or 1, determined by the dot product of the input vector and the weight vector. Output equals 1 if the w dot x + b is greater than 0, b is the bias. **Perceptron is a method for weighting evidence to make decisions.** 
#### Sigmoid neuron
We want a small change in a weight or bias causes only a small change in ouput, thus we can delicately tune the model towards the manner we want. Since the output of perceptron jumps between 0 and 1, we need **sigmoid neuron**. In this context, the input is **continuous** between 0 and 1. The output is also **continuous** between 0 and 1. The output is *sigma(w dot x + b)*, based on the sigmoid function, f(z) = 1/(1 + e^-z). This function guarantees the output ranges from 0 to 1. In this case, the output is **1/(1 + exp(- w dot x - b))**, while z is the **w dot x + b**. The change of(delta) the output with respect to(wrt) w and b is related with the partial direvative wrt the delta b and delta w (w is the weight vector), actually, linear relationship. Similarly, the logit function, f(x) = ln( x / (1 -x)), has a restraint that the input ranges from 0 to 1, the x is the probability of given class in logistic regression scenario. The sigmoid function is the **activation function**. 
#### Gradient Descent Optimization

#### The architecture of neural networks
From left to right, the input layer (input neurons), hidden layer, output layer (output neurons). 
