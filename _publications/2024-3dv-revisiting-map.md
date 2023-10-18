---
title: "Revisiting Map Relations for Unsupervised Non-Rigid Shape Matching"
collection: publications
permalink: /publication/2024-3dv-revisiting-map
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2023-10-16
venue: 'International Conference on 3D Vision (3DV)'
paperurl: 'https://arxiv.org/pdf/2310.11420.pdf'
authors: '<b>Dongliang Cao</b>, Paul Roetzer, Florian Bernard'
teaser: /previews/cao_3dv_24.png
arxiv: 'https://arxiv.org/abs/2310.11420'
categories: [correspondence]
bibtex: true
---

{{ page.authors }}

<img class="pub_teaser" src="../images/previews/cao_3dv_24.png" alt="Teaser Image" title="teaser" />

## Abstract

> We propose a novel unsupervised learning approach for non-rigid 3D shape matching. Our approach improves upon recent state-of-the art deep functional map methods and can be applied to a broad range of different challenging scenarios. Previous deep functional map methods mainly focus on feature extraction and aim exclusively at obtaining more expressive features for functional map computation. However, the importance of the functional map computation itself is often neglected and the relationship between the functional map and point-wise map is underexplored. In this paper, we systematically investigate the coupling relationship between the functional map from the functional map solver and the point-wise map based on feature similarity. To this end, we propose a self-adaptive functional map solver to adjust the functional map regularisation for different shape matching scenarios, together with a vertex-wise contrastive loss to obtain more discriminative features. Using different challenging datasets (including non-isometry, topological noise and partiality), we demonstrate that our method substantially outperforms previous state-of-the-art methods.

## Resources

{% if page.paperurl %}<a href=" {{ page.paperurl }} ">[pdf]</a>{% endif %} {% if page.arxiv %}<a href=" {{ page.arxiv }} ">[arxiv]</a>{% endif %} {% if page.code %}<a href=" {{ page.code }} ">[github]</a>{% endif %} {% if page.pageurl %}<a href=" {{ page.pageurl }} ">[project page]</a>{% endif %} {% if page.video %}<a href=" {{ page.video }} ">[video]</a>{% endif %} {% if poster %}<a href=" {{ page.poster }} ">[poster]</a>{% endif %}


## Bibtex

    @InProceedings{cao2023revisiting,
        title={Revisiting Map Relations for Unsupervised Non-Rigid Shape Matching}, 
        author={Dongliang Cao and Paul Roetzer and Florian Bernard},
        year={2024},
        booktitle={International Conference on 3D Vision (3DV)},
    } 
