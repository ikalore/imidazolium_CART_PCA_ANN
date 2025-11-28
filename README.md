# Repository for: ln(MIC) Prediction of Bis-Imidazolium Chlorides Using PCA–MLP Models

This repository contains the datasets and preprocessing scripts associated with the manuscript:

_[Insert full manuscript title here]_.

## Contents of the repository

### 📁 `data/`
- `descriptors_full_5270.csv`  
  Full Dragon descriptor matrix (N = 5270 molecular descriptors) used as the starting point for the analysis.

- `descriptors_filtered_54.csv`  
  Final reduced set of 54 descriptors obtained as the overlap between pathogen-specific CART analyses for *S. aureus* and *C. albicans*.  
  These descriptors were used as input for PCA.

### 📁 `preprocessing/`
Python scripts used for:
- descriptor filtering and preparation,
- preprocessing and standardisation,
- preparing PCA input matrices.

Scripts included:
- `preprocessing_pipeline.py`
- `pca_preparation.py`
- `requirements.txt`

### 📁 `models/`
Neural network models (PCA–MLP) were created and trained in **Statistica**.  
A note is provided for clarity:
- `NOTE_models_created_in_STATISTICA.txt`

### 📁 `docs/`
Optional workflow diagrams and supplementary materials.

## Reproducibility
- Datasets are provided in `.csv` format.
- All preprocessing steps performed in Python are described in the manuscript and included as scripts in this repository.
- PCA and MLP modelling were conducted in Statistica, as stated in the manuscript.

If you use this repository, please cite the associated publication.
