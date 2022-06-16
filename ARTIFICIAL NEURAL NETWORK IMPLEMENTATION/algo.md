ALGORITHM:
1. Getting the weighted sum of inputs of a particular unit using the h(x) function we defined earlier.
2. Plugging the value we get from step 1 into the activation function we have (f(a)=a in this example)
and using the activation value we get (i.e. the output of the activation function) as the input feature
for the connected nodes in the next layer.
3. If feeding forward happened using the following functions:
f(a) = a
4. Then feeding backward will happen through the partial derivatives of those functions. There is no
need to go through the working of arriving at these derivatives. All we need to know is that the above
functions will follow:
f'(a) = 1
J'(w) = Z . delta
5. Updating the weights.
