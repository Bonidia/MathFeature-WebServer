![Python](https://img.shields.io/badge/python-v3.7-blue)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![Status](https://img.shields.io/badge/status-up-brightgreen)

<h1 align="center">
  <img src="img/MathFeature.png" alt="MathFeature" width="350">
</h1>

<h4 align="center">Feature Extraction Package for Biological Sequences Based on Mathematical Descriptors</h4>

<p align="center">
  <a href="https://bonidia.github.io/MathFeature/">Documentation</a> •
  <a href="#installing-dependencies-and-package">Installing</a> •
  <a href="#list-of-descriptors">Descriptors</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#citation">Citation</a> 
</p>

<h1 align="center"></h1>

One of the main challenges in the application of Machine Learning (ML) algorithms to biological sequence data is how to numerically represent a sequence in a numeric input vector. Feature extraction techniques capable of extracting numerical information from biological sequences have been reported in the literature. However, many of these techniques are not available in existing packages, such as mathematical descriptors. This paper presents a new package, MathFeature, which implements mathematical descriptors able to extract relevant numerical information from biological sequences, i.e., DNA, RNA, and Proteins (prediction of structural features along the primary sequence of amino acids). MathFeature makes available 20 numerical feature extraction descriptors based on approaches found in the literature, e.g., multiple numeric mappings, genomic signal processing, chaos game theory, entropy, and complex networks. MathFeature also allows the extraction of alternative features, complementing the existing packages. To ensure that our descriptors are robust and to assess their relevance, experimental results are presented in nine case studies. According to these results, the features extracted by MathFeature shown high performance (0.6350-0.9897, accuracy), both applying only mathematical descriptors, but also hybridization with well-known descriptors in the literature. Finally, through MathFeature, we overcome several studies in eight benchmark datasets, exemplifying the robustness and viability of the proposed package. MathFeature advances in the area by bringing descriptors not available in other packages, as well as allowing non-experts to use feature extraction techniques.

## Authors

* Robson Parmezan Bonidia, Douglas S. Domingues, Danilo Sipoli Sanches, and André Carlos Ponce de Leon Ferreira de Carvalho.

* **Correspondence:** rpbonidia@gmail.com or bonidia@usp.br


## Publication

See: https://www.biorxiv.org/content/10.1101/2020.12.19.423610v1


## Installing dependencies and package

MathFeature can be run on the console, but we also provide a GUI-based platform.

## Docker Image - Terminal - MathFeature v1.0

It is important to note that we consider that the Docker is installed.

Docker commands - Examples

1 - https://www.docker.com/sites/default/files/d8/2019-09/docker-cheat-sheet.pdf

2 - https://dockerlabs.collabnix.com/docker/cheatsheet/

3 - https://github.com/wsargent/docker-cheat-sheet

```sh
$ docker pull bio21061993/mathfeature:latest

$ docker run -it --name mathfeature-terminal bio21061993/mathfeature bash

$ cd MathFeature/

$ conda activate mathfeature-terminal

$ Run the desired scripts - See Documentation
```

## List of Descriptors

Descriptors calculated by MathFeature for DNA, RNA, and Protein sequences: [Click here.](https://github.com/Bonidia/MathFeature/blob/gh-pages/descriptors.md)

## How to use

We proposed an open-source Python package called MathFeature, that implements feature extraction approaches using mathematical features, including 20 descriptors organized into five categories. To our best knowledge, MathFeature is the first package that computes biological sequence features based on various mathematical descriptors. In this section, 5 feature extraction groups are available: **(1)** numerical mapping techniques, **(2)** numerical mapping techniques with Fourier transform, **(3)** techniques with game chaos, **(4)** techniques with Entropy, **(5)** techniques with complex networks. Moreover, we provide some additional scripts for feature extraction and preprocessing.

See our [documentation](https://bonidia.github.io/MathFeature).

## Citation

If you use this code in a scientific publication, we would appreciate citations to the following paper:

See: https://www.biorxiv.org/content/10.1101/2020.12.19.423610v1
