
# An extended example: Tic-Tac-Toe
The following questions can be found on
Chapter I : The problem, part 1.4 : An extended example: Tic-Tac-Toe



## Exercise 1.1 Self Play

Suppose, instead of playing against a fixed oppoennt, the reinforcement learning algorithm
described above played against itself. What do you think would happen in this case?
Would it learn a different way of playing?

- The algorithm would still search and converge as to win each time it can, it would just do so much
slower because when playing a human, it's confronted directly to the big strategies, but when playing
against itself, the learning at first would be random.
- I don't think it would learn a different way of playing since Tic-Tac_toe is quite limited in its strategies. In more complex games however, it could find new ways and strategies to achieve maximal rewards.



## Exercise 1.2 Symmetries

Many tic-tac-toe positions appear different but are really the same because of symmetries. How might we amend the reinforcement learning algorithm described above to take advantage of this? In what ways would this improve it? Now think again. Suppose the opponent did not take advantage of symmetries. In that case, should we? Is it true, then, that symmetrically equivalent positions should necessarily have the same value?

- One way to amend the RL algorithm would be at the *temporal-difference learning steps*. We would not only update V(s) but we would take every state symmetrical to s and update it's value too.
- This would accelerate the learning considerably because instead of being confronted to the same state 4 different times, it would only need to confront it once.
- Taking advantage of symmetries I believe, would considerably make the algorithm more efficient, and the learning faster. But it would take more time to code it.
