#!/bin/bash -eu

export REMOTE_STATE_NAME=shared-app-infra
exec ci/deploy-tf

