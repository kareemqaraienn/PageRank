# PageRank 
The PageRank algorithm is used to determine the relative importance of web pages in a given corpus. The algorithm was developed by Google co-founder Larry Page and is used in Google's web search engine. The algorithm assigns a score to each page in the corpus based on the importance of the pages that link to it.

## Usage
To run the pagerank algorithm on a corpus of HTML pages, execute the following command in the terminal:<br><br>
`python pagerank.py corpus_directory`<br><br>
The corpus_directory argument should be the path to a directory containing the HTML pages to be analyzed.

The output of the script will include two sets of results:<br>

1) PageRank Results from Sampling (n = 10000)
2) PageRank Results from Iteration

Each set of results will display the PageRank score for each page in the corpus.

## Implementation
The PageRank algorithm is implemented using two functions: sample_pagerank and iterate_pagerank.

The sample_pagerank function calculates the PageRank scores by randomly sampling pages from the corpus and using a transition model to determine the probability of transitioning from one page to another. This process is repeated n times, and the final PageRank scores are calculated based on the number of times each page is visited during the sampling process.

The iterate_pagerank function calculates the PageRank scores by iteratively updating the scores until they converge. The algorithm starts with an initial score of 1/N for each page, where N is the total number of pages in the corpus. The scores are then updated using a recursive formula based on the scores of the pages that link to each page in the corpus. This process is repeated until the scores converge.

The algorithm uses a damping factor of 0.85, which represents the probability that a user will continue browsing the web by clicking on a link, as opposed to typing in a new URL.

## Dependencies
The implementation requires the following dependencies:

- os
- random
- re
- sys

## References
For more information on the PageRank algorithm, see the following resources:

- Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web. Technical report, Stanford InfoLab.
- Langville, A. N., & Meyer, C. D. (2012). Google's PageRank and beyond: The science of search engine rankings. Princeton University Press.

## Acknowledgement
- The corpusN folders were created by CS50 as part of their course material.
- All relevant functions in pagerank.py were implemented solely by myself as part of my course.
