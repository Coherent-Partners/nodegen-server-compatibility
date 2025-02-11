###############################
# RUNNER COMPILER COMPATIBILITY
###############################

import configparser
import json
from mdutils.mdutils import MdUtils
import os
import pandas as pd

# import the configuration
config = configparser.ConfigParser()
config.read("nodegen-server-compatibility.ini")

#############################
# Read the compatibility data
#############################

# read the runner compiler history
runner_versions_pd = pd.read_csv(os.path.join(os.environ.get(config["paths"]["root"]),config["paths"]["runner_versions"]))
# for each version of the runner note the latest Neuron that was released
runner_versions_pd = runner_versions_pd.sort_values(by="date", ascending=False).drop_duplicates("runner_version", keep="first").reset_index(drop=True)
# filter for only the published versions of the runner
runner_versions_published_pd = pd.read_csv(os.path.join(os.environ.get(config["paths"]["root"]),config["paths"]["runner_versions_published"]))
runner_versions_pd = runner_versions_pd.merge(runner_versions_published_pd, how="inner", on="runner_version")

# read the runner feature version requirements
# features_pd = pd.read_csv("nodegen-server Features (Testing).csv").sort_values(by="feature")
features_pd = pd.read_csv(os.path.join(os.environ.get(config["paths"]["root"]),config["paths"]["features"])).sort_values(by="feature")

##########################
# JSON for machine reading
##########################

# create dictionary for runner_versions
runner_versions_compiler_versions = runner_versions_pd.loc[:, "runner_version"].tolist()
runner_versions_data = runner_versions_pd.drop("runner_version", axis=1).to_dict("index")
runner_versions = {}
for i in range(len(runner_versions_pd)):
    runner_versions[runner_versions_compiler_versions[i]] = runner_versions_data.pop(i)

# create dictionary for features if any have been specified
if len(features_pd) > 0:
    features_feature = features_pd.loc[:, "feature"].tolist()
    features_data = features_pd.drop("feature", axis=1).to_dict("index")
    features = {}
    for i in range(len(features_pd)):
        features[features_feature[i]] = features_data.pop(i)
    # Combine the dictionaries together and output a JSON file
    json.dump({"features": features, "runner_versions": runner_versions}, open("nodegen-server-compatibility.json", "w"), separators=(',', ':'))
# Only output the runner_versions to JSON file
else:
    json.dump({"runner_versions": runner_versions}, open("nodegen-server-compatibility.json", "w"), separators=(',', ':'))

############################
# Markdown for human reading
############################

mdFile = MdUtils(file_name="README", title="Coherent Spark Runner Compiler Compatibility")

mdFile.new_paragraph("The Spark team developed [`nodegen-server`](https://github.com/orgs/Coherent-Partners/packages/container/package/nodegen-server) (also referred to as the Neuron runner) to create and run containerized applications designed explicitly for executing [Wasm](https://webassembly.org/) modules generated by Spark.")
mdFile.new_paragraph("This page details the compatibility between a version of the [`nodegen-server`](https://github.com/orgs/Coherent-Partners/packages/container/package/nodegen-server) against the Spark [Neuron compiler](https://docs.coherent.global/build-spark-services/neuron/release-history). The compiler version can be found from the Spark UI under the _[Service Documentation Version details](https://docs.coherent.global/navigation/service-documentation#version-details)_ or in the [_Execute API_ `response_meta`.](https://docs.coherent.global/spark-apis/execute-api/execute-api-v3#response_meta)")
# mdFile.new_paragraph("The runner includes configuration parameters to perform checks and whether or not to continue execution if a version of Neuron is not fully supported.")
mdFile.new_paragraph("[`nodegen-server`](https://github.com/orgs/Coherent-Partners/packages/container/package/nodegen-server) `1.31.0` is the first version that includes the capability and configuration for processing compatibility versions and the version compatibility mapping. Compiled  [Wasm](https://webassembly.org/) modules from `Neuron` `1.22.1` onwards embed the Neuron version that is also needed for the compatibility check.")
mdFile.new_paragraph("The releases include the download for a JSON file mapping the compatibility versions.")
mdFile.new_paragraph("")

if len(features_pd) > 0:
    mdFile.new_header(level=1, title="Compatibility features")
    mdFile.new_paragraph("List of features that require specific runner version(s).")
    mdFile.new_table(columns=features_pd.shape[1], rows=len(features_pd)+1, text=list(features_pd) + [item for sublist in features_pd.astype(str).values.tolist() for item in sublist], text_align='center')

mdFile.new_header(level=1, title="Compatibility versions")
mdFile.new_paragraph("List of all released runner versions and their corresponding __highest__ supported Neuron version.")
mdFile.new_table(columns=runner_versions_pd.shape[1], rows=len(runner_versions_pd)+1, text=list(runner_versions_pd) + [item for sublist in runner_versions_pd.astype(str).values.tolist() for item in sublist], text_align='center')

mdFile.create_md_file()