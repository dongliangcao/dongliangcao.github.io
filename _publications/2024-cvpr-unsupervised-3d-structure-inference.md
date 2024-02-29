---
title: "Unsupervised 3D Structure Inference from Category-Specific Image Collections"
collection: publications
permalink: /publication/2024-cvpr-unsupervised-3d-structure-inference
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-02-28
venue: 'Conference on Computer Vision and Pattern Recognition (CVPR)'
# paperurl: 'https://arxiv.org/pdf/2303.10971.pdf'
authors: 'Weikang Wang, <b>Dongliang Cao</b>, Florian Bernard'
teaser: /previews/weikang2024cvpr.png
# arxiv: 'https://arxiv.org/abs/2303.10971'
# code: 'https://github.com/dongliangcao/Self-Supervised-Multimodal-Shape-Matching'
# categories: [correspondence]
bibtex: true
---

{{ page.authors }}

<img class="pub_teaser" src="../images/previews/weikang2024cvpr.png" alt="Teaser Image" title="teaser" />

## Abstract

> Understanding 3D object structure from image collections of general object categories remains a long-standing challenge in computer vision. Due to the high relevance of image keypoints (e.g. for graph matching, controlling generative models, scene understanding, etc.), in this work we specifically focus on inferring 3D structure in terms of sparse keypoints. Existing 3D keypoint inference approaches rely on strong priors, such as spatio-temporal consistency, multi-view images of the same object, 3D shape priors (e.g. templates, skeleton), or supervisory signals e.g. in the form of 2D keypoint annotations. In contrast, we propose the first unsupervised 3D keypoint inference approach that can be trained for general object categories solely from an inhomogeneous image collection (containing different instances of objects from the same category). Our experiments show that our method not only improves upon unsupervised 2D keypoint inference, but more importantly, it also produces reasonable 3D structure for various object categories, both qualitatively and quantitatively.

## Resources

{% if page.paperurl %}<a href=" {{ page.paperurl }} ">[pdf]</a>{% endif %} {% if page.arxiv %}<a href=" {{ page.arxiv }} ">[arxiv]</a>{% endif %} {% if page.code %}<a href=" {{ page.code }} ">[github]</a>{% endif %} {% if page.pageurl %}<a href=" {{ page.pageurl }} ">[project page]</a>{% endif %} {% if page.video %}<a href=" {{ page.video }} ">[video]</a>{% endif %} {% if poster %}<a href=" {{ page.poster }} ">[poster]</a>{% endif %}


## Bibtex

    @InProceedings{Wang_2024_CVPR,
        author    = {Weikang Wang, Dongliang Cao, Florian Bernard},
        title     = {Unsupervised 3D Structure Inference from Category-Specific Image Collections},
        booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
        month     = {June},
        year      = {2024}
    }  
