---
title: "Unsupervised Learning of Robust Spectral Shape Matching"
collection: publications
permalink: /publication/2023-siggraph-unsupervised-learning-of-robust-spectral-shape-matching
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2023-04-19
venue: 'ACM Transactions on Graphics (ToG)'
paperurl: 'https://arxiv.org/pdf/2304.14419.pdf'
authors: '<b>Dongliang Cao</b>, Paul Roetzer, Florian Bernard'
teaser: /previews/cao23sig.jpg
arxiv: 'https://arxiv.org/abs/2304.14419'
code: 'https://github.com/dongliangcao/unsupervised-learning-of-robust-spectral-shape-matching'
pageurl: 'https://dongliangcao.github.io/urssm/'
categories: [correspondence]
bibtex: true
---

{{ page.authors }}

<img class="pub_teaser" src="../images/previews/cao23sig.jpg" alt="Teaser Image" title="teaser" />

## Abstract

> We propose a novel learning-based approach for robust 3D shape matching. Our method builds upon deep functional maps and can be trained in a fully unsupervised manner. Previous deep functional map methods mainly focus on predicting optimised functional maps alone, and then rely on off-the-shelf post-processing to obtain accurate point-wise maps during inference. However, this two-stage procedure for obtaining point-wise maps often yields sub-optimal performance. In contrast, building upon recent insights about the relation between functional maps and point-wise maps, we propose a novel unsupervised loss to couple the functional maps and point-wise maps, and thereby directly obtain point-wise maps without any post-processing. Our approach obtains accurate correspondences not only for near-isometric shapes, but also for more challenging non-isometric shapes and partial shapes, as well as shapes with different discretisation or topological noise. Using a total of nine diverse datasets, we extensively evaluate the performance and demonstrate that our method substantially outperforms previous stateof-the-art methods, even compared to recent supervised methods.

## Resources

{% if page.paperurl %}<a href=" {{ page.paperurl }} ">[pdf]</a>{% endif %} {% if page.arxiv %}<a href=" {{ page.arxiv }} ">[arxiv]</a>{% endif %} {% if page.code %}<a href=" {{ page.code }} ">[github]</a>{% endif %} {% if page.pageurl %}<a href=" {{ page.pageurl }} ">[project page]</a>{% endif %} {% if page.video %}<a href=" {{ page.video }} ">[video]</a>{% endif %} {% if poster %}<a href=" {{ page.poster }} ">[poster]</a>{% endif %}


## Bibtex

    @article{cao2023unsupervised,
      title={Unsupervised Learning of Robust Spectral Shape Matching}, 
      author={Dongliang Cao and Paul Roetzer and Florian Bernard},
      journal = {ACM Transactions on Graphics (TOG)},
      year = {2023},
      publisher = {ACM New York, NY, USA},
      doi = {10.1145/3592107},
      url = {https://doi.org/10.1145/3592107}
    }
