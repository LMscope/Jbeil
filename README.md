# Jbeil: Temporal Graph-Based Inductive Learning to Infer Lateral Movement in Evolving Enterprise Networks 

<github-button href="https://github.com/buttons/github-buttons/discussions" data-size="large" aria-label="Discuss buttons/github-buttons on GitHub">Discuss</github-button>
import GithubButton from 'vue-github-button'

(Accepted at IEEE Symposium on Security & Privacy 2024)
<hr>

## Description:
Jbeil is a data-driven framework to infer Lateral Movement (LM) attacks in evolving enterprise networks. Specifically, Jbeil takes as input time-stamped authentication events (benign events augmented with malicious ones) and output decision on LM activities within the network. The premise of this work is two folds: (i) lies in applying an encoder on a continuous-time evolving graph to produce for each time epoch the embedding of the visible graph nodes; and (ii) a decoder that leverage these embeddings to perform LM link prediction on unseen nodes using an inductive learning technique. 

## Graph map and graph features:
Check Graph Features Extraction directory.

## Authentication logs dataset:
Access the dataset from LANL here: https://csr.lanl.gov/data/

## Augmentation mechanism:
Access to Hopper tool: https://github.com/grantho/lateral-movement-simulator

Additional resources on the augmentation mechanism will be added soon...

## Detection mechanism:
Access to TGN tool: https://github.com/twitter-research/tgn

Additional resources on the detection mechanism will be added soon...
