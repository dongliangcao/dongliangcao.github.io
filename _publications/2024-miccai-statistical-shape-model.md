---
title: "A Universal and Flexible Framework for Unsupervised Statistical Shape Model Learning"
collection: publications
permalink: /publication/2024-miccai-statistical-shape-model
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-05-29
venue: 'Medical Image Computing and Computer Assisted Intervention (MICCAI)'
# paperurl: 'https://arxiv.org/pdf/2402.18920.pdf'
authors: 'Nafie El Amrani, <b>Dongliang Cao</b>, Florian Bernard'
teaser: /previews/dongliang2024miccai.png
# arxiv: 'https://arxiv.org/abs/2402.18920'
# code: 'https://github.com/dongliangcao/Self-Supervised-Multimodal-Shape-Matching'
categories: [correspondence]
bibtex: true
---

{{ page.authors }}

<img class="pub_teaser" src="../images/previews/dongliang2024miccai.png" alt="Teaser Image" title="teaser" />

## Abstract

> We introduce a novel unsupervised deep learning framework for constructing statistical shape models (SSMs). Although unsupervised learning-based 3D shape matching methods have made a major leap forward in recent years, the correspondence quality of existing methods does not meet the demanding requirements necessary for the construction of SSMs of complex anatomical structures. We address this shortcoming by proposing a novel deformation coherency loss to effectively enforce smooth and high-quality correspondences during neural network training. We demonstrate that our framework outperforms existing methods in creating high-quality SSMs by conducting extensive experiments on five challenging datasets with varying anatomical complexities. Our proposed method sets the new state of the art in unsupervised SSM learning, offering a universal solution that is both flexible and reliable.
## Resources

{% if page.paperurl %}<a href=" {{ page.paperurl }} ">[pdf]</a>{% endif %} {% if page.arxiv %}<a href=" {{ page.arxiv }} ">[arxiv]</a>{% endif %} {% if page.code %}<a href=" {{ page.code }} ">[github]</a>{% endif %} {% if page.pageurl %}<a href=" {{ page.pageurl }} ">[project page]</a>{% endif %} {% if page.video %}<a href=" {{ page.video }} ">[video]</a>{% endif %} {% if poster %}<a href=" {{ page.poster }} ">[poster]</a>{% endif %}


<!-- ## Bibtex

    @InProceedings{Cao_2024_CVPR,
        author    = {Dongliang Cao, Marvin Eisenberger, Nafie El Amrani, Daniel Cremers, Florian Bernard},
        title     = {Spectral Meets Spatial: Harmonising 3D Shape Matching and Interpolation},
        booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
        month     = {June},
        year      = {2024}
    }   -->
