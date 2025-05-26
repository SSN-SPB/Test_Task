FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code

COPY requirements.txt /code
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["flask_app.py"]

FROM builder as dev-envs

# RUN <<EOF
# apk update
# apk add git bash
# EOF
#
# RUN <<EOF
# addgroup -S docker
# adduser -S --shell /bin/bash --ingroup docker vscode
# EOF

# another version for Debian
RUN apk update && apk add --no-cache git bash

RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /