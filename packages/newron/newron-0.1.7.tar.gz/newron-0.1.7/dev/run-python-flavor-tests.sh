#!/usr/bin/env bash
set -x

export MLFLOW_HOME=$(pwd)

# TODO: Run tests for h2o, shap, and paddle in the cross-version-tests workflow
pytest \
  tests/tensorflow \
