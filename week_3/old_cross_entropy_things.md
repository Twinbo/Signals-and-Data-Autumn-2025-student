
### Exercise 2.2:

*Assume you have a prediction from a neural network, with 3 probabilities denoting the
certainty. You also have a one-hot encoded vector which is 0 everywhere but in the place
which corresponds to the correct class.*

**1. How should the prediction probabilities look if you wanted to maximize cross-entropy?**

$\dots$

**2. How about if you wanted to minimize it?**

$\dots$

**3. Do you see any potential issues with a neural network using this loss?** (*Hint: Check out [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) p. 4: NLL*)

$\dots$


## **Exercise 2.3:

*This is a bit of a long one, so itemized for your convenience:*
- *Say you have a set of images, each with a given class. We denote a single as 𝑋𝑖,
and its class as the random variable 𝐶𝑖*
- *That the class of the i’th image is a given class (𝑘 for example) can then be given
by the probability 𝑝(𝐶𝑖 = 𝑘|𝑋𝑖) = 𝑝(𝐶𝑖,𝑋𝑖)*
𝑃 (𝐶𝑖) . This holds for every possible class up to
the max number of classes 𝐾.
- *In other words, the conditional distribution of classes for each image follows a cat-
egorical distribution; 𝑝(𝐶𝑖 = 𝑘|𝑋) ∼ 𝐶𝑎𝑡(𝐾)*

**1. What would it take to minimize uncertainty when choosing 𝐶𝑖 based on 𝑋𝑖?
HINT: Some tasks are hard because you must put in work. Some are hard because you
must understand the task enough. This task is the latter kind.**

$\dots$


**2. What would it take to maximize uncertainty when choosing 𝐶𝑖 based on 𝑋𝑖?**

$\dots$

**3. Can you think of (google/gpt) any measure of uncertainty/chaos/unpredictability in
random variables that would be fitting for exactly this question?**

$\dots$

**4. Given that you find this measure (let us just denote it 𝐻), how would you minimize
𝐻(𝐶|𝑋). So minimize the measure of uncertainty of choosing a class 𝐶 based on an
image 𝑋.**

$\dots$

**5. Describe in your own words what the relation is between uncertainty and information
in a system or a random variable**

$\dots$

**6. Mathematically describe this same relation**

$\dots$

**7. Thinking once more of information given uncertainty and our example. Given the
distribtion of a random variable denoting the classes 𝑃 (𝐶) and the class probabilities for
the i’th image with conditional density 𝑃 (𝐶|𝑋𝑖). How would you write the information
gained by this image?**

$\dots$

**8. What is the maximum conditional entropy H(X|Y) if we have marginal entropy H(X)**

$\dots$
