FROM jetbrains/teamcity-agent

USER root

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/listss/*

RUN \ #Додадуть в домашці

ENV CROME_BIN /usr/bin/google-chrome-stable

EXPOSE 9223

ENTRYPOINT ["/run-agent.sh"]