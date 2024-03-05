# PAC-MAN ASSIGNMENT #4
## Table of Contents
1. [The Purpose of the Project](#the-purpose-of-the-project)
2. [Value Iteration Algorithm](#value-iteration-algorithm)
3. [Q-Learning Algorithm](#q-learning-algorithm)
4. [Policies](#policies)
5. [Conclusions](#conclusions)
## The Purpose of the Project 
This project teaches us how to implement the value iteration agent, Q-learning agent and the Q-learning agent adapted for the game of Pac-Man. Focusing on the Markov distribution probability we mainly need to implement and adapt some of the mathematical formulas for our character to make the best decisions in a maze.
## Value Iteration Algorithm 
### Description 
The value iteration algorithm is one that helps us build an agent that is an offline planner, rather than learning from its mistakes or experience, the algorithm is considering already computed values and iterates over the whole set of states, gathering and estimating as many as the number of iterations allowed. For the formula of calculating the score of a state we need to take into account the probability of transitioning to the already computed states and multiply that by the next reward, the score of the next state, and of the reward, the score decided for transitioning into the chosen state. For computing the final score of the state based on two other methods: getQValue that calls the method computeQValueFromValues, used for computing the actual score and getAction that calls the method computeActionFromValues that chooses the best action to make out of all the possible actions based on their Q-values, using the method getQvalue too. 
### Python Code
```python
def runValueIteration(self):
    """
    Run the value iteration algorithm. Note that in standard value iteration,
    V_k+1(...) depends on V_k(...)'s.
    """
    # *** YOUR CODE HERE ***
    states = self.mdp.getStates()
    for i in range(self.iterations):
        q_values = util.Counter()
        for state in states:
            if self.mdp.isTerminal(state):
                continue
            q_values[state] = self.getQValue(state, self.getAction(state))
        for state in q_values.keys():
            self.values[state] = q_values[state]

def computeActionFromValues(self, state):
    """
    The policy is the best action in the given state according to the values
    currently stored in self.values. You may break ties any way you see fit.
    Note that if there are no legal actions, which is the case at the terminal state,
    you should return None.
    """
    # *** YOUR CODE HERE ***
    if self.mdp.isTerminal(state):
        return None
    actions = self.mdp.getPossibleActions(state)
    q_values = util.Counter()
    for action in actions:
        q_values[action] = self.getQValue(state, action)
    return q_values.argMax()

def computeQValueFromValues(self, state, action):
    """
    Compute the Q-value of action in state from the value function stored in self.values.
    """
    # *** YOUR CODE HERE ***
    result = 0
    for (nextState, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
        reward = self.mdp.getReward(state, action, nextState)
        next_reward = self.getValue(nextState)
        result += prob * (reward + next_reward * self.discount)
    return result
```
### Observation 
The algorithm as much from the map as the number of iteration set. The process of discovering of the Q-values of each tile is similar to traversing a tree from root, goal state, to its leaves, the possible beginning states. 
## Q-Learning Algorithm 
### Description 
Similar to Value Iteration Algorithm the Q-Learning algorithm uses the same principle of computing the Q-values of each state, but instead of having a pure theoretical usage such as the MDP, the values predefined in the Value Iteration Algorithm are computed from the experience of the algorithm on a given set of scenarios, by trial and error, much more practical and relatable to the real word. For our main update method we need to implement to other methods getValue which calls the computeValueFromQValues and the getQValue method. The getQValue returns the computed values if it was discovered otherwise it will return 0. The the computeValueFromQValues method returns the highest Q-value of a transition out of all the possible actions. For the formula implemented in update we need to get the Q-value of our transition and add that to the learning factor multiplied by the reward adding the next reward times the discount rate and subtract the past Q-value. 
### Python Code 
```python
def runValueIteration(self):
    """
    Run the value iteration algorithm. Note that in standard value iteration,
    V_k+1(...) depends on V_k(...)'s.
    """
    # *** YOUR CODE HERE ***
    states = self.mdp.getStates()
    for i in range(self.iterations):
        q_values = util.Counter()
        for state in states:
            if self.mdp.isTerminal(state):
                continue
            q_values[state] = self.getQValue(state, self.getAction(state))
        for state in q_values.keys():
            self.values[state] = q_values[state]

def computeActionFromValues(self, state):
    """
    The policy is the best action in the given state according to the values
    currently stored in self.values. You may break ties any way you see fit.
    Note that if there are no legal actions, which is the case at the terminal state,
    you should return None.
    """
    # *** YOUR CODE HERE ***
    if self.mdp.isTerminal(state):
        return None
    actions = self.mdp.getPossibleActions(state)
    q_values = util.Counter()
    for action in actions:
        q_values[action] = self.getQValue(state, action)
    return q_values.argMax()

def computeQValueFromValues(self, state, action):
    """
    Compute the Q-value of action in state from the value function stored in self.values.
    """
    # *** YOUR CODE HERE ***
    result = 0
    for (nextState, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
        reward = self.mdp.getReward(state, action, nextState)
        next_reward = self.getValue(nextState)
        result += prob * (reward + next_reward * self.discount)
    return result
```
### Observation 
As seen in other learning algorithms the Q-learning is highly influenced by the learning rate. If the alpha is too low the algorithm will find the solution but slower and will require extra steps, while if it is too high it will skip steps and go in the opposite direction of the expected behaviour. 
## Policies
### Description 
For this task you are supposed to create different strategies for the player depending on the scenario and the layout of the map. By varying the discount, how important is the next reward, noise, the chance for the character to make a wrong move, and the living reward, how important is for the character to stay alive, you can achieve same goals but on different layouts. a) Prefer the close exit (+1), risking the cliff (-10) b) Prefer the close exit (+1), but avoiding the cliff (-10) c) Prefer the distant exit (+10), risking the cliff (-10) d) Prefer the distant exit (+10), avoiding the cliff (-10) e) Avoid both exits and the cliff (so an episode should never terminate) 
### Python Code 
```python
def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

def question3a():
    answerDiscount = 0.3
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = 0.1
    answerNoise = 0.1
    answerLivingReward = 0.7
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = 0.9
    answerNoise = 0.5
    answerLivingReward = 1.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = 0.01
    answerNoise = 0.0
    answerLivingReward = 100
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'
' 
```
### Observation 
In almost all questions the noise should be the lowest parameter since in a normal environment is the one that goes against the algorithm, in most cases, even failing it.

## Conclusions
In conclusion, this documentation has provided a comprehensive overview of implementing various algorithms within the Pac-Man project framework, focusing on Value Iteration and Q-Learning approaches. Through the detailed descriptions, Python code examples, and observations provided, we aimed to illustrate the principles behind these algorithms and their practical applications within a game environment that simulates real-world decision-making scenarios. We explored how the Value Iteration Algorithm assists in creating an effective offline planning agent and how the Q-Learning Algorithm enables a character to learn from its environment dynamically, thereby making informed decisions based on past experiences. Additionally, we delved into policy strategies, showing how altering parameters can lead to different behaviors and outcomes, emphasizing the importance of understanding the underlying mechanics to achieve desired results. The observations highlighted in each section shed light on the algorithms' performance and behavior, offering valuable insights into their strengths and limitations. This reinforces the idea that there is no one-size-fits-all solution in AI and that successful implementation often requires careful consideration, experimentation, and adaptation to specific contexts. By working through these examples and analyses, readers should gain a solid foundation in reinforcement learning principles and how they can be applied to not just gaming scenarios but a broad range of real-world problems. It is our hope that this documentation serves as a useful guide for students, enthusiasts, and professionals alike, providing the tools and understanding necessary to embark on their own AI projects and research. Finally, we encourage readers to experiment with the code, tweak the parameters, and explore different strategies beyond what is covered here. AI and machine learning are dynamic and expansive fields, and continuous learning and experimentation are key to staying at the forefront of technology and innovation.
