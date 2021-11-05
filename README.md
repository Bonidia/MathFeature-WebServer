![Python](https://img.shields.io/badge/python-v3.7-blue)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
![Status](https://img.shields.io/badge/status-up-brightgreen)

<h1 align="center">
  <img src="https://github.com/Bonidia/MathFeature/blob/master/img/MathFeature.png" alt="MathFeature" width="350">
</h1>

<h4 align="center">Feature Extraction Package for Biological Sequences Based on Mathematical Descriptors</h4>

<p align="center">
  <a href="https://github.com/Bonidia/MathFeature">Official MathFeature Repository</a> •
  <a href="https://bonidia.github.io/MathFeature/">Documentation</a> •
  <a href="#installing-dependencies-and-package">Installing</a> 
  <a href="#citation">Citation</a> 
</p>

<h1 align="center"></h1>

One of the main challenges in applying machine learning algorithms to biological sequence data is how to numerically represent a sequence in a numeric input vector. Feature extraction techniques capable of extracting numerical information from biological sequences have been reported in the literature. However, many of these techniques are not available in existing packages, such as mathematical descriptors. This paper presents a new package, MathFeature, which implements
mathematical descriptors able to extract relevant numerical information from biological sequences, i.e. DNA, RNA and proteins (prediction of structural features along the primary sequence of amino acids). MathFeature makes available 20 numerical feature extraction descriptors based on approaches found in the literature, e.g. multiple numeric mappings, genomic signal processing, chaos game theory, entropy and complex networks. MathFeature also allows the extraction of alternative features, complementing the existing packages. To ensure that our descriptors are robust and to assess their relevance, experimental results are presented in nine case studies. According to these results, the features extracted by MathFeature showed high performance (0.6350–0.9897, accuracy), both applying only mathematical descriptors, but also hybridization with well-known descriptors in the literature. Finally, through MathFeature, we overcame several studies in eight benchmark datasets, exemplifying the robustness and viability of the proposed package. MathFeature has advanced in the area by bringing descriptors not available in other packages, as well as allowing non-experts to use feature extraction techniques.

## Authors

* Robson Parmezan Bonidia, Douglas S. Domingues, Danilo Sipoli Sanches, and André Carlos Ponce de Leon Ferreira de Carvalho.

* **Correspondence:** rpbonidia@gmail.com or bonidia@usp.br


## Publication

See: https://www.biorxiv.org/content/10.1101/2020.12.19.423610v1


## Installing dependencies and package

Conda - Terminal

```sh
$ git clone https://github.com/Bonidia/MathFeature-WebServer.git MathFeature-WebServer

$ cd MathFeature-WebServer
```

**1 - Install Miniconda:** 

```sh

See documentation: https://docs.conda.io/en/latest/miniconda.html

$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

$ chmod +x Miniconda3-latest-Linux-x86_64.sh

$ ./Miniconda3-latest-Linux-x86_64.sh

$ export PATH=~/miniconda/bin:$PATH

```

**2 - Create environment:**

```sh

conda env create -f mathfeature-webserver.yml -n MathFeature-WebServer

```

**3 - Activate environment:**

```sh

conda activate MathFeature-WebServer

```

**4 - You can deactivate the environment, using:**

```sh

conda deactivate

```

## Citation

If you use this code in a scientific publication, we would appreciate citations to the following paper:

See: https://www.biorxiv.org/content/10.1101/2020.12.19.423610v1
