#!/usr/bin/env bash

# Copyright 2016 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

##########################################################################

# INSTRUCTIONS:
#
# This script sets up a development dependencies for running Oppia.
# Run the script from the oppia root folder:
#
#   bash scripts/install_prerequisites.sh
#
# Note that the root folder MUST be named 'oppia'.

sudo apt-get -y update

# Install Java 8
apt-get -y install software-properties-common
wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
sudo add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
sudo apt-get update && sudo apt-get -y install adoptopenjdk-8-hotspot-jre
java -version

sudo apt-get -y install curl
sudo apt-get -y install git
sudo apt-get -y install python-setuptools
sudo apt-get -y install python-dev
sudo apt-get -y install python-pip
sudo apt-get -y install unzip
sudo apt-get -y install python-yaml
# This is only done to address an
#     "ImportError: No module named functools_lru_cache"
# error. See the Troubleshooting page for details:
#    https://github.com/oppia/oppia/wiki/Troubleshooting
sudo apt-get -y install python-matplotlib
sudo pip install --upgrade pip
