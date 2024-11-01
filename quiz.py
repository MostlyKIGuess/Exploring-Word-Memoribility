import random
import re


report_text = """
# Background Literature and Gaps

## Animates are better remembered than inanimates: further evidence from word and picture stimuli

### Understanding

* The paper explores the "animacy effect," where animate entities (living things) are remembered better than inanimate objects. This aligns with the functionalist view of memory, suggesting memory prioritizes survival-relevant information.
* The authors conducted four experiments: free recall with words (incidental encoding), free recall with pictures, recognition with remember/know judgments (words), and sensory experience ratings.
* Experiments 1 and 2 replicated the animacy effect in French, using both words and pictures, extending previous findings in English.
* Experiment 3 showed the animacy effect in recognition tasks and demonstrated that the advantage stems from enhanced recollection (remember responses) rather than familiarity (know responses).
* Experiment 4 ruled out the possibility that the animacy effect is driven by richer sensory or perceptual features of animate items.

### Gaps

* While the experiments robustly demonstrate the animacy effect, the underlying proximate mechanisms remain unclear.  Is it purely attentional capture by animates, or are there inherent mnemonic differences in processing living vs. non-living things?
### Addressing Gaps with the Experiment 

*  Similar to Experiment 3 (word recognition). While not directly addressing animacy, the experiment could be adapted to include animate/inanimate word pairs. If animate pairs are better recalled despite the distraction, it would suggest an inherent mnemonic advantage beyond mere attentional capture. And I vividly remember recalling words like "Gaay"(cow in hindi) during the experiment because I still have that image I formed during the experiment.


## Exploring word memorability: How well do different word properties explain item free-recall probability?

### Understanding

* This paper investigates which word properties best predict free recall performance. It uses a large dataset (PEERS) of 1,638 words recalled by 147 participants, and a second dataset from Lau et al. (2018). (My analysis will be on this dataset itself :) ).
* Twenty lexical, semantic, and affective properties were examined.
* Semantic properties, particularly animacy (living things better recalled), usefulness (for survival), and size (larger things better recalled) showed the strongest relationship with recall probability. 
### Gaps

*  The PEERS word pool was not uniformly distributed across all dimensions (e.g., high in concreteness and prevalence), which limits the generalizability of findings for those properties. 

## Memorability: How what we see influences what we remember

### Understanding

* This paper reviews the concept of memorability, particularly for visual stimuli, as an intrinsic property measurable through memory performance (for e.g hit rate in recognition).
* It discusses the history of memorability research, starting with its connection to distinctiveness in face recognition studies.
* While distinctive faces are more memorable, distinctiveness alone doesn't fully explain memorability.Semantic features also play a role.
* Memorability is robust across different stimulus types (faces, scenes, words, abstract visualizations) and even transformations of the same stimulus.
*  Memorability effects are shown to be distinct from attention, cognitive control, and priming.
* Neuroimaging studies reveal that memorability processing involves ventral visual areas and memory-related regions like the perirhinal cortex and hippocampus, and it's distinct from subsequent memory effects.
* Memorable images have similar neural representations, while forgettable images are dissimilar.  This pattern is consistent across different tasks and brain regions.

### Gaps

* The paper primarily focuses on recognition memory.  More research is needed on how memorability influences recall, especially in tasks involving associations between items.
### Addressing Gaps with the Experiment

* My experiment addresses the gap regarding memorability in recall tasks involving associations. Analyzing the memorability of individual words within the pairs (as measured by consistent recall across participants) and relating it to recall success could reveal whether intrinsic word memorability influence retrieval.


## Memorability of Words in Arbitrary Verbal Associations Modulates Memory Retrieval in the Anterior Temporal Lobe

### Understanding

* This study investigates whether the memorability of words affects associative memory retrieval, using a paired-associate verbal learning task with both iEEG and online participants.
* Certain words were consistently better recalled across participants, indicating intrinsic memorability even with arbitrary cue words.
* A computational model based on semantic similarity predicted word memorability, suggesting that words semantically related to many other words are more easily retrieved.
*  Memorable words were recalled faster but also led to more intrusions (incorrect recalls of related words).
* iEEG recordings showed faster neural reinstatement (reactivation of encoding patterns) in the anterior temporal lobe (ATL) for memorable words during successful retrieval. This effect was observed in early retrieval periods and was specific to the ATL, not the posterior temporal lobe (PTL).

### Gaps

* The ATL's role in memorability could be general to associative processing or specific to semantic/verbal material. The PTL's potential sensitivity to visual associative memorability warrants investigation.
* Left and right ATL data were combined, potentially obscuring hemispheric specialization in memorability representation.

## Intrinsically memorable words have unique associations with their meanings

### Understanding

* This paper investigates word memorability, hypothesizing that memorable words uniquely identify a specific meaning.  
* Two large-scale recognition memory experiments were conducted (each with >600 participants and 2,222 words).
*  The experiments used a repeat detection task, similar to image memorability studies.
*  Results showed that words with fewer synonyms and meanings were more memorable, with the number of synonyms being a stronger predictor. ( this is also shown in my analysis )
* This supports an "ideal observer model" where memorability depends on a word's ability to unambiguously select a meaning.
*  The model, based on number of synonyms and meanings, explained >80% of explainable variance in memorability.
* Frequency, imageability, and familiarity also contributed to memorability.
### Gaps

* The study focuses on recognition, not recall.  How does this model of memorability apply to retrieval tasks requiring generating the word itself?

## Memorability: Reconceptualizing Memory as a Visual Attribute

### Understanding

* This chapter focuses on *visual memorability* – the intrinsic property of images that influences how likely they are to be remembered across individuals.
* Memorability is distinguished from the *process* of memory. It's a stable attribute, consistent across individuals despite varying experiences, and measurable through memory performance (hit rate, false alarm rate, etc.).
*  Memorability is consistent across different image types (faces, scenes, objects), tasks (recognition, incidental encoding), and time scales (milliseconds to days).
* Memorability is distinct from low-level visual features (color, edges), high-level features (aesthetics, emotionality), subjective memorability ratings, and attention.
### Gaps

- I don't see any gaps, although the mention of DNN to predict the memoribility of image is interesting and doesn't seem fully explained as they show in  https://brainbridgelab.uchicago.edu/resmem/ .  


## Memorable words are monogamous: The role of synonymy and homonymy in word recognition memory

### Understanding

*  Two large-scale recognition memory experiments were conducted, each with >600 participants and 2,222 words, using a repeat detection paradigm.
* The central hypothesis, based on rational analysis and Bayesian modeling, is that memorable words have a "monogamous" relationship with their meaning—few synonyms and few meanings.
*  Results confirmed this hypothesis: words with fewer synonyms and meanings were better recognized.
* The model based on these two factors explained a substantial portion of variance in memorability.
* Other factors, such as frequency, imageability, concreteness, and arousal, also contributed to memorability.
### Gaps

* While the "monogamous" model explained a good amount of variance, other factors might contribute to memorability particularly for stimuli other than words.
*  The experiments used isolated words. How does memorability operate in more naturalistic language contexts (sentences, discourse) where meaning is constructed from multiple words?

## Semantic determinants of memorability

### Understanding

* This paper investigates why some words are more memorable than others using machine learning models applied to word recognition and recall datasets.
* The authors compare their model's performance to previous psychological models and to human participants in memorability prediction tasks.
*  Their approach uses distributed semantic representations (Word2Vec embeddings) to capture semantic determinants of memorability in a data-driven manner.
* The model outperforms previous models and human participants in predicting both recognition and recall probabilities.
* The analysis identifies important semantic categories for memorability (e.g., "informal language", "death").
### Gaps

* The mechanisms by which semantic representations contribute to memorability isn't explained fully.  Is it related to distinctiveness within semantic space, network structure, or other properties of the representations?

## What makes an image memorable?

### Understanding

* This paper explores the predictability of image memorability – how likely an image is to be remembered after a single viewing.
* It introduces a dataset with memorability scores collected through a "memory game" on Amazon Mechanical Turk, where participants detect repeated images in a stream.
*  Simple image features (color, intensity statistics) and object statistics (number of objects, coverage) are weakly predictive of memorability.
*  Object and scene semantics are more predictive, with the best performance achieved by combining both.
*  "Memory maps" visualize the contribution of individual objects to an image's memorability.  People, interiors, and foreground objects tend to boost memorability, while exteriors and backgrounds decrease it.
*  Global image descriptors (GIST, SIFT, HOG, SSIM) can predict memorability without object labeling, with the best results obtained by combining all features.

### Gaps
* The dataset is limited to scene images.  How does memorability operate for other image types, such as faces, objects, or abstract art?

### Addressing Gaps with the Experiment

* While my experiment deals with words, the findings here about the importance of semantic information (object and scene categories) for visual memorability resonate with the idea that conceptual factors influence memory across modalities.  
* We could adapt my experiment to use images as stimuli and explore whether visual memorability (pre-rated using a similar method to this study) influences paired-associate learning. This would provide insights into how intrinsic image memorability interacts with associative processes.


## You Had Me at Hello: How Phrasing Affects Memorability

### Understanding

* This paper investigates how the phrasing of information influences its memorability.
*  They focus on movie quotes, using IMDb's "Memorable Quotes" and web occurrences as measures of memorability.
*  To control for context, they compare memorable quotes to non-memorable quotes spoken by the same character, of the same length, and at roughly the same point in the same movie.
*  A pilot study confirmed that human subjects could distinguish memorable from non-memorable quotes even for unseen movies.
* Memorable quotes are lexically distinctive (using less common words according to a Brown corpus language model) but syntactically common (using familiar part-of-speech patterns).
* Memorable quotes also exhibit greater *generality* – fewer 3rd person pronouns, more indefinite articles, less past tense verbs, and more present tense verbs – making them more portable to new contexts.

### Gaps

* The study relies on IMDb and web data, which may not perfectly reflect true memorability. How do these measures compare to memorability assessed in controlled memory experiments?


# Understanding as a Whole

The concept of memorability as explored in these papers represents a shift from focusing solely on memory processes to also considering the intrinsic properties of the stimuli that drive memory (Bainbridge, 2019; Bainbridge, 2022; Bainbridge et al., 2013; Isola et al., 2011; Tuckute et al., 2018). Memorability is the likelihood of a stimulus being remembered, regardless of individual differences in experience or cognitive abilities. This consistency across observers is a crucial finding, demonstrated across various stimulus types including images (Isola et al., 2011; [https://web.mit.edu/phillipi/www/publications/WhatMakesAnImageMemorable.pdf](https://www.google.com/url?sa=E&q=https%3A%2F%2Fweb.mit.edu%2Fphillipi%2Fwww%2Fpublications%2FWhatMakesAnImageMemorable.pdf)), faces (Bainbridge et al., 2013), and words (Madan, 2020; [https://link.springer.com/article/10.3758/s13423-020-01820-w](https://www.google.com/url?sa=E&q=https%3A%2F%2Flink.springer.com%2Farticle%2F10.3758%2Fs13423-020-01820-w); Tuckute et al., 2018; Mahowald et al.; [http://olivalab.mit.edu/Papers/Mahowald_etal.pdf](https://www.google.com/url?sa=E&q=http%3A%2F%2Folivalab.mit.edu%2FPapers%2FMahowald_etal.pdf)). This suggests that memorability is driven at least in part, by intrinsic stimulus attributes rather than solely by encoding or retrieval processes.


A key driver of memorability appears to be semantic information. For words like a "monogamous" relationship with meaning (few synonyms and few meanings) predicts higher recognition memory performance (Mahowald et al.; [http://olivalab.mit.edu/Papers/Mahowald_etal.pdf](https://www.google.com/url?sa=E&q=http%3A%2F%2Folivalab.mit.edu%2FPapers%2FMahowald_etal.pdf); Tuckute et al., 2018). Similarly, for images, object and scene semantics significantly influence memorability, with a combination of both providing the best predictions (Isola et al., 2011; [https://web.mit.edu/phillipi/www/publications/WhatMakesAnImageMemorable.pdf](https://www.google.com/url?sa=E&q=https%3A%2F%2Fweb.mit.edu%2Fphillipi%2Fwww%2Fpublications%2FWhatMakesAnImageMemorable.pdf)). This importance of semantic content resonates with findings in other memory research showing the influence of semantic relatedness on recall dynamics (Xie et al., 2020; [https://www.nature.com/articles/s41562-020-0901-2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41562-020-0901-2)). Furthermore, the stable and consistent effect of "animacy" on memory, where animate entities are consistently better remembered than inanimates suggests the evolutionarily driven prioritization of survival-relevant information (Bonin et al., 2014; [https://link.springer.com/article/10.3758/s13421-013-0368-8](https://www.google.com/url?sa=E&q=https%3A%2F%2Flink.springer.com%2Farticle%2F10.3758%2Fs13421-013-0368-8)).

Neuroimaging studies reveal that memorability involves distinct brain regions and processes. Ventral visual areas and memory-related regions within the MTL, including the perirhinal cortex, hippocampus, and ATL, show differential activity for memorable vs. forgettable stimuli (Bainbridge, 2017; Bainbridge et al., 2017; Bainbridge & Rissman, 2018; Xie et al., 2020; [https://www.nature.com/articles/s41562-020-0901-2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41562-020-0901-2)). Importantly, these neural patterns are distinguishable from those associated with subsequent memory effects, further supporting the idea of memorability as a distinct phenomenon (Bainbridge & Rissman, 2018). Beyond single-item processing, memorability also influences associative memory. Memorable words are retrieved faster in cued recall tasks, but also lead to more intrusions, suggesting an intricate relationship between memorability and the memory search process (Xie et al., 2020; [https://www.nature.com/articles/s41562-020-0901-2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41562-020-0901-2)).

Interestingly (well I believe this also has to do with the fact that it's not the first recall from the movies but a repetitive one giving more chance of recalling the quote) the phrasing of information also impacts memorability. Analysis of movie quotes reveals that memorable quotes tend to be lexically distinctive yet syntactically common, suggesting a combination of novel word choices built upon a familiar grammatical structure (Danescu-Niculescu-Mizil et al., 2012; [https://aclanthology.org/P12-1094/](https://www.google.com/url?sa=E&q=https%3A%2F%2Faclanthology.org%2FP12-1094%2F)). Moreover, the concept of "memorable language" characterized by features like generality and portability to new contexts may extend beyond specific domains like movie quotes (Danescu-Niculescu-Mizil et al., 2012; [https://aclanthology.org/P12-1094/](https://www.google.com/url?sa=E&q=https%3A%2F%2Faclanthology.org%2FP12-1094%2F)).

Finally, computational approaches, particularly DNNs, have demonstrated impressive performance in predicting and even manipulating image memorability (Khosla et al., 2015; Needell & Bainbridge, 2021; [https://osf.io/preprints/psyarxiv/ckv92/download](https://www.google.com/url?sa=E&q=https%3A%2F%2Fosf.io%2Fpreprints%2Fpsyarxiv%2Fckv92%2Fdownload)). These advances open new avenues for creating more memorable educational materials, designing effective user interfaces, and developing diagnostic tools for memory impairments. However this is ethically concerning for potential of manipulating memories (Bainbridge, 2022; [https://osf.io/preprints/psyarxiv/ckv92/download](https://www.google.com/url?sa=E&q=https%3A%2F%2Fosf.io%2Fpreprints%2Fpsyarxiv%2Fckv92%2Fdownload)).
## Gaps as a Whole

 Developing more comprehensive models that incorporate a wider range of factors influencing memory – including perceptual features, emotional valence, prior knowledge, and individual differences – is a crucial next step (Bainbridge, 2022; [https://osf.io/preprints/psyarxiv/ckv92/download](https://www.google.com/url?sa=E&q=https%3A%2F%2Fosf.io%2Fpreprints%2Fpsyarxiv%2Fckv92%2Fdownload); Isola et al., 2011; [https://web.mit.edu/phillipi/www/publications/WhatMakesAnImageMemorable.pdf](https://www.google.com/url?sa=E&q=https%3A%2F%2Fweb.mit.edu%2Fphillipi%2Fwww%2Fpublications%2FWhatMakesAnImageMemorable.pdf); Madan, 2020; [https://link.springer.com/article/10.3758/s13423-020-01820-w](https://www.google.com/url?sa=E&q=https%3A%2F%2Flink.springer.com%2Farticle%2F10.3758%2Fs13423-020-01820-w)). Further while correlations have been established between various features and memorability establishing causal relationships requires manipulating these features systematically and observing their effect on memory (e.g., manipulating semantic relatedness in paired-associate recall, varying the distinctiveness of lexical choices in sentences). We also need deeper understanding into the neural underpinnings of memorability. While specific brain regions have been implicated, the precise calculations performed by these regions and how they interact with other cognitive systems still remain to be fully understood (Bainbridge et al., 2017; Xie et al., 2020; [https://www.nature.com/articles/s41562-020-0901-2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41562-020-0901-2)). Finally, extending memorability research to incorporate a wider range of stimuli, tasks, and modalities is essential for developing a comprehensive theory of this intriguing phenomenon. Specifically, investigating the role of memorability in more naturalistic language processing (e.g., memory for stories, discourse comprehension) and exploring its potential connection to other cognitive abilities like fluid intelligence will be important future directions (Danescu-Niculescu-Mizil et al., 2012; [https://aclanthology.org/P12-1094/](https://www.google.com/url?sa=E&q=https%3A%2F%2Faclanthology.org%2FP12-1094%2F); Tuckute et al., 2018).


# Description of the Experiment I Participated In

The experiment I participated in involved the presentation of Hindi word pairs, followed by a simple arithmetic task, and then a cued recall test.  Specifically, we were shown a series of word pairs, one pair at a time, for a brief period. These pairs were unrelated semantically, meaning they did not have any pre-existing associative links.  After viewing all the pairs, we were given a short arithmetic task involving simple addition or subtraction problems. This task served as a distractor, preventing active rehearsal of the word pairs.  Finally, in the recall phase, we were presented with one word from each pair (the cue) and asked to recall the other word (the target).

# My Thoughts on the Cognitive Processes Involved


**Encoding:**  The initial presentation of word pairs engages encoding processes, where the words and their pairings are transformed into memory traces. The nature of these memory traces, whether they are primarily visual, auditory, or semantic, is an important question. Studies like "What makes an image memorable?" (Isola et al., 2011; https://web.mit.edu/phillipi/www/publications/WhatMakesAnImageMemorable.pdf) and "Memorable words are Monogamous" (Mahowald et al.; http://olivalab.mit.edu/Papers/Mahowald_etal.pdf) highlight the crucial role of semantic information in memorability for both images and words. In my experiment, since the word pairs were semantically unrelated, the encoding might rely more on other features like orthography, phonology, or visual imagery.  The use of Hindi words introduces a linguistic element relevant to studies like  "Exploring word memorability" (Madan, 2020; https://link.springer.com/article/10.3758/s13423-020-01820-w) and "Semantic determinants of memorability" (Aka et al., 2023; https://pubmed.ncbi.nlm.nih.gov/37442022/).


**Storage:** The intervening arithmetic task tests the storage of these memory traces. The distractor task engages working memory and cognitive control potentially interfering with the maintenance of the word pairs in memory. The duration and difficulty of the distractor task can affect the degree of interference, impacting the subsequent recall performance.

**Retrieval:** The cued recall phase starts retrieval processes.  Presenting one word from the pair serves as a cue triggering a search for the associated target word.  Studies like "Memorability of Words in Arbitrary Verbal Associations Modulates Memory Retrieval in the Anterior Temporal Lobe" (Xie et al., 2020; https://www.nature.com/articles/s41562-020-0901-2) have investigated the neural correlates of such retrieval processes, highlighting the role of the ATL in retrieving arbitrary verbal associations.  Since my experiment also uses arbitrary word pairs similar brain regions might be involved. Furthermore, studies investigating how "phrasing affects memorability" (Danescu-Niculescu-Mizil et al., 2012; https://aclanthology.org/P12-1094/) raise interesting questions about how the linguistic properties of cues might influence retrieval success.

**Distraction and Attention:**  The arithmetic task serves as a source of distraction engaging cognitive resources and potentially diverting attention away from the word pairs.  This manipulation allows us to explore the impact of distraction on memory, similar to how studies like "Memorability: How what we see influences what we remember" (Bainbridge, http://wilmabainbridge.com/sharepapers/plm-2019.pdf) examined the resilience of memorability effects to attentional manipulations and other cognitive tasks.

**Connection to the broader literature:** The experiment can be seen as a bridge between the study of single-item memorability (e.g.,  "Animates are better remembered than inanimates"; Bonin et al., 2014; https://link.springer.com/article/10.3758/s13421-013-0368-8; "Intrinsically memorable words have unique associations with their meanings"; Tuckute et al., 2018; https://osf.io/preprints/psyarxiv/p6kv9) and the memorability of more complex stimuli and events. By using word *pairs*, the experiment introduces a basic level of association, providing a controlled environment to study how intrinsic word memorability might influence associative learning and retrieval.  Further, manipulating factors like semantic relatedness within the word pairs introducing different types of distractor tasks and varying the retention interval could provide valuable insights into the dynamics of memorability in more complex settings.

# Analysis of the Dataset

## Interpretation of the Madan (2020) Dataset

For this analysis, I chose the dataset provided by Madan (2020; [https://link.springer.com/article/10.3758/s13423-020-01820-w](https://link.springer.com/article/10.3758/s13423-020-01820-w)),  "Exploring word memorability: How well do different word properties explain item free-recall probability?".  This study focuses on free recall, which provides valuable insights into the intrinsic memorability of words and allows for the investigation of a wide range of word properties relevant to my broader research interests.  The data and associated word property norms are openly accessible ([https://osf.io/spqjz/](https://osf.io/spqjz/)), ensuring transparency and reproducibility.


**Dataset Details:** The dataset includes free recall data from 147 participants across 20 experimental sessions. A total of 1,638 words were presented, and recall probabilities were calculated for each word based on the rate at which they were freely recalled across participants. The dataset also includes norms for 20 lexical, semantic, and affective word properties, including:

* **Lexical:** Number of letters, number of syllables, word frequency, orthographic neighborhood size, etc.
* **Semantic:** Animacy, concreteness, imageability, number of semantic features, etc.
* **Affective:** Arousal,Valence, Dominance.


**Memorability Calculation:** Memorability is operationalized as the probability of free recall for each word. This metric reflects the likelihood of a word being retrieved from memory without the aid of specific cues, thus emphasizing the inherent memorability of the word itself.


## My Analysis

### Data Summary and Initial Exploration

The  first thing I did in my analysis was summarizing and examining the data structure. 

![Data Info](Pasted%20image%2020241031175311.png)

### Frequency Binning of WFlog

The variable representing word frequency, `WFlog`, was divided into three bins (low, medium, and high) using quantiles. This allowed for a structured investigation of the impact of frequency on recall probability (`pRecall`).

### Distributions of Key Variables

Histograms and kernel density estimate (KDE) plots were generated to visualize the distributions of key variables, including `pRecall`, `Concreteness`, and `Arousal`.

1. **Recall Probability Distribution:**  

![distributionofrecallprob](distributionofrecallprob.png)

   The histogram and KDE plot of `pRecall` shows an approximately normal distribution, which is expected and it's tilted towards > 0.6 giving most words were recallable.

2. **Concreteness Distribution:** 
   
   ![freqvsconcreteness](freqvsconcreteness.png)

   The histogram of `Concreteness` illustrates that ratings are right-skewed and that a large portion of the words are high in Concreteness which gives us info about how most words were recallable as we saw on the previous studies.

3. **Arousal Distribution:** 

![freqvsarousal](freqvsarousal%201.png)


   The histogram and KDE plot of `Arousal`  reveals a distribution that appears approximately normal. It peaks between 4.5 to 5. Which doesn't give much info to us.

### Box and Violin Plots by Frequency Bins


1. **Box Plot of Recall Probability by Frequency Bin:** 

![recallprobvsfreqbin](recallprobvsfreqbin.png)


2. **Violin Plot of Recall Probability by Frequency Bin:** 

![recallprobvsfreqbinviolin](recallprobvsfreqbinviolin.png)


It can be observed the medium frequency bins have some low outliers, indicating these medium frequency words have a lower recall probability.
The denser regions of the violin indicate higher probability densities. Violin plot provides a clearer understanding of the probability density and the central tendency. 

### Scatter Plots and Pairwise Relationships

A pairwise scatterplot matrix was generated using `seaborn.pairplot` to explore connections between `pRecall`, `nLet`, `WFlog`, `Animacy`, `Concreteness`, `Valence` and `Arousal`.  


![PairWise Scatterplot](corelation.png)



This visualization reveals potential correlations and non-linear relationships between pairs of variables. For eg the scatterplot of `pRecall` vs. `nLet` shows a potential negative trend which tells us that shorter words might be more memorable. The diagonal of the matrix displays [KDE plots](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) for the distribution of each individual variable, complementing the histograms shown earlier.

### Correlation Analysis 

![correlationmatrix](correlationmatrix.png)


Spearman's rank correlation coefficients were calculated to quantify the relationships between recall probability and word properties. This matrix summarizes the strength and direction of associations between variables. For eg, `pRecall` shows a moderate positive correlation with `Concreteness` and a strong negative correlation with `nLet` which means negative relationship between recall probability and word length.


## Conclusion: What I Learned

* **Operationalizing Memorability:**  The Madan (2020) study provides a nice approach using free recall probability but other operationalizations exist and the choice of metric can influence the interpretation of results. 
* **Complexity of Word Memorability:**  Word memorability is not determined by a single factor but is influenced by a complex interaction of lexical ,semantic and affective properties.  Analyzing the range of variables in Madan's (2020) dataset highlighted this complexity and allowed me to understand which properties are most strongly related to memorability in a free recall context but lack of Hindi dataset did restrict a proper exploration of cross-cultural differences in memorability.
* **Statistical Modeling and Interpretation:** Statistical modeling such as linear regression can be used for investigating the relationship between word properties and memorability. In the case of Madan's data, I tried to replicate the reported correlation between word length and memorability but did not find a significant impact of language frequency itself.  It would be nice to include individual factors like native language, cultural background, and cognitive abilities as mentioned in other papers, which is impossible due to the limitation of the current dataset. 
* **The role of open science:** Openly available data and code like those provided by Madan are important for enhancing transparency, reproducibility, and collaboration in memory research.  This open approach facilitates observation, extension of analyses, and testing of new hypotheses, accelerating scientific progress.


"""

# Extract words using regular expressions 
words = re.findall(r'\b\w+\b', report_text.lower()) 


# --- Word Selection & MCQ Generation ---

# Manually curated lists (adapt these based on YOUR judgment of memorability from the report)
extremely_recallable = ["memorability", "recall", "probability", "words", "analysis", "dataset",
                       "semantic", "properties", "frequency", "length", "concreteness", "arousal",
                       "valence", "animacy", "usefulness", "correlation", "regression", "model",
                       "distribution", "visualization", "figures", "participants", "sessions",
                       "lexical", "affective", "statistical", "relationship", "variables", "findings",
                       "hypothesis", "effects", "cognitive", "neural", "brain", "regions", "encoding",
                       "retrieval", "attention", "dnn", "models", "interaction", "predict", "key",
                       "explored", "suggests", "observed", "influence", "significant", "plot", "matrix",
                      "properties"]

mildly_recallable = ["information", "experiments", "conducted", "properties", "examined", "bins", "violin", "box", "plot",
                     "scatterplot", "correlation", "matrix", "regression", "model", "interaction", "effect", "bands", "multifaceted", "nature","judgments", "output","patterns", "density", "comparisons","output", "indicates", "levels", "jointly", "influence",
                    "cross", "linguistic", "compared", "datasets", "available", "accessible", "transparency", "reproducibility",
                    "comprises", "sessions", "calculated","normed", "encompassing", "features", "dimensions", "operationalized", "metric", "retrievability", "exploratory",
                    "visualizations", "characteristics", "histograms", "density", "estimates", "correlations", "coefficient"]

hard_to_recall = [ "operationalizations", "quantiles", "kernel", "tapers", "pairwise", "lmplot", "conjunctions", "interdisciplinary", "orthographic", "phonological", "epiphenomenon",
                 "monogamous", "operationalized"]

unknown_words = ["jazz", "rhythm", "blizzard", "galaxy", "oxygen", "equation", "algorithm", "quantum",
                 "microphone", "strawberry"]  # These aren't in the report





all_word_sets = [extremely_recallable, mildly_recallable, hard_to_recall, unknown_words , words]
all_words = set()

for word_set in all_word_sets:
    all_words.update(word_set)


# --- MCQ Quiz (structured by category, improved distractor logic) ---

num_questions_per_category = 5
score = 0

categories = {
    "Extremely Recallable": extremely_recallable,
    "Mildly Recallable": mildly_recallable,
    "Hard to Recall": hard_to_recall,
    "Unknown": unknown_words
}

print("\nWelcome to the Word Recall Challenge!\n")
print("This quiz tests your memory and understanding of the report's key concepts.\n")

for category_name, word_list in categories.items():
    print(f"\n--- {category_name} Words ---\n")  

    for i in range(num_questions_per_category):
        correct_word = random.choice(word_list)

        other_categories = [words for cat, words in categories.items() if cat != category_name]
        distractors = [random.choice(random.choice(other_categories)) for _ in range(2)]


        options = distractors + [correct_word]
        random.shuffle(options)


        print(f"Question {i+1}: Which word is MOST closely related to the concept of '{category_name}' words?")
        for j, option in enumerate(options):
            print(f"{j+1}. {option.title()}")

        answer = input("Your answer (1-3): ")
        if options[int(answer)-1] == correct_word:
            score +=1
            print("correct")
        else:
            print(f"incorrect. The answer was: {correct_word.title()}.")



print("\n--- Quiz Results ---")
print(f"Your final score: {score}/{num_questions_per_category * len(categories)}")


print("\nKey takeaway:  Memorability varies based on word properties and our engagement with the text.")
print("Reflect on how the different word categories relate to the analysis and findings discussed in the report.")