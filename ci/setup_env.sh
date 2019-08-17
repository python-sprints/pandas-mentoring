#!/bin/bash -e

MINICONDA_DIR="$HOME/miniconda3"


if [ -d "$MINICONDA_DIR" ]; then
    echo "rm -rf "$MINICONDA_DIR""
    rm -rf "$MINICONDA_DIR"
fi

echo "Install Miniconda"
UNAME_OS=$(uname)

if [[ "$UNAME_OS" == 'Linux' ]]; then
    if [[ "$BITS32" == "yes" ]]; then
        CONDA_OS="Linux-x86"
    else
        CONDA_OS="Linux-x86_64"
    fi
fi

wget -q "https://repo.continuum.io/miniconda/Miniconda3-latest-$CONDA_OS.sh" -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b

export PATH=$MINICONDA_DIR/bin:$PATH


echo "conda env create -q --file=${ENV_FILE}"
time conda env create -q --file="${ENV_FILE}"

echo "activate pandas-docs"
source activate pandas-docs

