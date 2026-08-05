# cancer-rnaseq-ml
Pan-cancer classification using ML/tree-based methods on expression data


## environment

conda env create -f environment.yml

## Register the kernal
    python -m ipykernel install \
    --user \
    --name cancer-ml \
    --display-name "Python (cancer-ml)"

## downloading data

curl -L -O "https://archive.ics.uci.edu/static/public/401/gene+expression+cancer+rna+seq.zip"
unzip gene+expression+cancer+rna+seq.zip
tar -xzf TCGA-PANCAN-HiSeq-801x20531.tar.gz