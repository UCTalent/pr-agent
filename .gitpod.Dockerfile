# You can find the new timestamped tags here: https://hub.docker.com/r/gitpod/workspace-full/tags
FROM ghcr.io/tkhieu/gitpod-starter:main

RUN brew install awscli aws/tap/copilot-cli aws-sam-cli