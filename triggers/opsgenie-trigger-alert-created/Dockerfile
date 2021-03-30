FROM relaysh/core:latest-python
COPY "./handler.py" "/handler.py"
ENTRYPOINT []
CMD ["python3", "/handler.py"]

LABEL "org.opencontainers.image.title"="Opsgenie incident triggered"
LABEL "org.opencontainers.image.description"="This trigger fires when a Opsgenie incident is triggered for the first time."
LABEL "sh.relay.sdk.version"="v1"
