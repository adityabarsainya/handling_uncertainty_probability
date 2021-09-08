# Abstract

This research aims at portraying the capabilities of probabilistic approaches in
handling uncertainty that form an integral part of designing learning agents in
Artificial Intelligence. The project deals with uncertainty using knowledge base
i.e. MySQL database, concepts of probability and updating the KB with the data
the agent encounters. The theoretic aspect of the project is adopted from the
book by Russell and the language used is Python. The domain is fixed to food
ordering where the customer places orders or any other relevant queries and the
agent (program) responds with the best possible unambiguous interpretation.

The implementation is done by eliminating stop words, the POS (parts of speech)
tagging taken, and, if wrong, corrected by the agent based on its calculated
probability in the KB. In case of words with different forms in different
contexts, the agent decides to choose the one with the larger relative
probability and fixes that form of the word for that sentence. Neural networks
seem to do a better job as they do not involve strong assumptions but
comparative results of the incorrect interpretation and corrected version is
displayed in the form of a parse tree and is used to show uncertainty handling.
