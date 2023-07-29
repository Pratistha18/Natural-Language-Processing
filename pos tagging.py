# POS Tagging using Viterbi Algorithm

#HIDDEN MARKOV MODEL
import nltk
text= nltk.word_tokenize("I want to play guitar")
print(nltk.pos_tag(text))

def viterbi(obs, states, start_p, trans_p, emit_p):
    '''
    Viterbi Algorithm for Hidden Markov Models(HMM).
    ----------
    obs : Sequence of observations
    states : List of possible hidden states
    start_p : Initial probabilities of each hidden state
    trans_p : Transition probabilities between hidden states
    emit_p : Emission probabilities of observations given each hidden state
    -------
    '''
    
    # Initialize variables
    V = [{}]
    path = {}
    for s in states:
        V[0][s] = start_p[s] * emit_p[s][obs[0]]
        path[s] = [s]
        
    # Run Viterbi algorithm
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}
        for s in states:
            # Find most probable previous state and probability
            (prob, prev_state) = max((V[t-1][prev_s]*trans_p[prev_s][s]*emit_p[s][obs[t]],prev_s)
                                     for prev_s in states)
            V[t][s] = prob
            new_path[s] = path[prev_state] + [s]
        
        # Update path
        path = new_path
        
    # Find final state with highest probability
    (prob, state) = max((V[len(obs)-1][s], s)for s in states)
    
    # Return highest probability and path
    return(prob, path[state])

# Example HMM for parts-of-speech tagging
obs = ['I','want','to','play','guitar']
states = ['noun','verb','preposition']
start_p = {'noun':0.5, 'verb':0.2, 'preposition':0.3}
trans_p = {'noun':{'noun':0.1, 'verb':0.4, 'preposition':0.5},
           'verb':{'noun':0.5, 'verb':0.2, 'preposition':0.3},
           'preposition':{'noun':0.3, 'verb':0.6, 'preposition':0.1}}
emit_p = {'noun':{'I':0.4, 'want':0.1, 'to':0.3,'play':0.1,'guitar':0.1},
          'verb':{'I':0.0, 'want':0.7, 'to':0.1,'play':0.1,'guitar':0.1},
          'preposition':{'I':0.0, 'want':0.0, 'to':1.0,'play':0.0,'guitar':0.0}}

# Run Viterbi algorithm
prob, path = viterbi(obs, states, start_p, trans_p, emit_p)

# Print results
print("Most probable sequence of Parts-of-speech tags: ")
print(path)
print("Probability of the sequence: ", prob)
