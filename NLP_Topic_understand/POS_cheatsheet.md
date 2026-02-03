# POS Tagging Cheat Sheet

Part-of-Speech (POS) tagging assigns grammatical labels to words in a sentence.
This cheat sheet follows the **Penn Treebank POS Tags**, widely used in NLP.

---

## POS Tag Table

| POS Tag | Full Form / Meaning | Example | Notes / Usage |
|------|-------------------|--------|--------------|
| CC | Coordinating conjunction | and, but, or | Connects words or phrases |
| CD | Cardinal number | 1, 20, 2025 | Numbers and quantities |
| DT | Determiner | the, a, an | Modifies nouns |
| EX | Existential there | there | e.g., "There is a cat" |
| FW | Foreign word | bonjour, amigo | Non-English words |
| IN | Preposition / Subordinating conjunction | in, on, at, because | Links nouns or clauses |
| JJ | Adjective | good, large | Describes nouns |
| JJR | Adjective, comparative | bigger, faster | Comparative adjectives |
| JJS | Adjective, superlative | biggest, fastest | Superlative adjectives |
| LS | List item marker | 1., a., i. | Ordered lists |
| MD | Modal verb | can, should, will | Possibility, necessity |
| NN | Noun, singular | cat, car | Single entity |
| NNS | Noun, plural | cats, cars | Multiple entities |
| NNP | Proper noun, singular | John, London | Specific names |
| NNPS | Proper noun, plural | Beatles | Names of groups |
| PDT | Predeterminer | all, both | Comes before determiners |
| POS | Possessive ending | ’s | Ownership (John’s book) |
| PRP | Personal pronoun | I, he, she | Refers to people/things |
| PRP$ | Possessive pronoun | my, his, her | Shows ownership |
| RB | Adverb | quickly, very | Modifies verb/adjective |
| RBR | Adverb, comparative | faster, better | Comparative adverbs |
| RBS | Adverb, superlative | fastest, best | Superlative adverbs |
| RP | Particle | up, off | Phrasal verbs (pick up) |
| SYM | Symbol | %, $, & | Special symbols |
| TO | Infinitive marker | to run, to eat | Marks infinitives |
| UH | Interjection | wow!, oh! | Express emotion |
| VB | Verb, base form | go, eat | Base verb |
| VBD | Verb, past tense | went, ate | Past action |
| VBG | Verb, gerund/present participle | going, eating | Continuous form |
| VBN | Verb, past participle | gone, eaten | Perfect tense |
| VBP | Verb, present (not 3rd person singular) | go, eat | Present tense |
| VBZ | Verb, present (3rd person singular) | goes, eats | He/She/It form |
| WDT | Wh-determiner | which, that | Questions/relative clauses |
| WP | Wh-pronoun | who, what | Question pronouns |
| WP$ | Possessive wh-pronoun | whose | Ownership questions |
| WRB | Wh-adverb | when, where, why | Question adverbs |

---

## Example Sentence

**Sentence:**  
> *"Virat Kohli plays cricket in India."*

**POS Tags:**  
- Virat/NNP  
- Kohli/NNP  
- plays/VBZ  
- cricket/NN  
- in/IN  
- India/NNP  

---

## Why POS Tagging is Important
- Helps understand sentence structure  
- Used in NER, Chunking, Parsing  
- Improves NLP model accuracy  

---

## Tools for POS Tagging
- NLTK
- spaCy
- Stanford NLP
- HuggingFace Transformers
