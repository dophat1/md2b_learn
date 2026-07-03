## Overview

Vector embedding is transforming sentences into vector so the machine can read it.

Simplest vector embedding is transform all the words appeared into a dictionary. The sentence then be transformed into a list of numbers, starting with full 0. Each time the word in the sentence appears, the index number of that word will be added by 1, else just stays 0. Loops until the end, you will get a vector embedded. 

Compare similarities between sentences = compare the cosine similarities between vectors. Because the cosine only cares about the direction, not the magnitude. The sentences will be broken down into many dimensions. 

The cosine is -1 < cos < 1 with -1 is opposite meaning, 0 is orthogonal -> no related, 1 is the same meaning. 

Pretrained model is model has been trained previously by others, so you can just get the number to inference it for your result. The pretrained model has difference form than what we said before. Its more complicated and filled with probability of meeting that specific criteria for the word in the sentence. For example, "man" will be high in chance for being a human, and low in chance of "object", so it will be modelled as [0.9, 0.1] (where 0.9 is % of man being a human, 0.1 is % of man being an object)
