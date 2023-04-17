import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    
    probability = {}
    ## if page has no links, then return equal probability for all pages
    if len(corpus[page]) == 0:
        return {page: 1/len(corpus) for page in corpus}
    ## if page has links, then return probability for each page
    initial_prob = (1-damping_factor) / len(corpus)
    probability = {page: initial_prob for page in corpus}
    for link in corpus[page]:
        probability[link] = initial_prob + (damping_factor)/len(corpus[page])
    return probability
        



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    ## create a dictionary to store the number of times each page is visited
    page_visited = {page: 0 for page in corpus}
    ## choose a random page to start
    page = random.choice(list(corpus.keys()))
    ## iterate n times
    for i in range(n):
        ## add 1 to the number of times the page is visited
        page_visited[page] += 1
        ## choose a random page based on the transition model
        page = random.choices(list(transition_model(corpus, page, damping_factor).keys()), list(transition_model(corpus, page, damping_factor).values()))[0]
    ## create a dictionary to store the probability of each page and calculate the probability of each page
    return {page : page_visited[page]/n for page in corpus}



def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    page_prob = {page: 1/len(corpus) for page in corpus}
    # page_prob = {}
    ## iterate until convergence
    while True:
        counter = 0
        for page in corpus:
            constant = (1-damping_factor)/len(corpus)
            function_prob = 0
            for other_page in corpus:
                if page in corpus[other_page]:
                    page_links = len(corpus[other_page])
                    function_prob = function_prob + page_prob[other_page] / page_links
            function_prob = damping_factor * function_prob
            constant += function_prob
            if abs(constant - page_prob[page]) < 0.001:
                counter+=1
            page_prob[page] = constant
        if counter == len(corpus):
            break
    return page_prob



if __name__ == "__main__":
    main()
