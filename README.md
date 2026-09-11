# [12-Factor App](https://12factor.net/) Demo

## Prerequisites
- [Docker Engine](https://docs.docker.com/engine/install/)
- [`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/)
- Local Kubernetes (K8s) cluster using one of the following:
  - [Docker Desktop Kubernetes](https://docs.docker.com/desktop/kubernetes/)
  - [kind Kubernetes](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
  - [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- K8s-based development:
  - [`skaffold` CLI](https://skaffold.dev/docs/install/)

## Develop
- Startup local Kubernetes cluster following docs in the [**Prerequisites**]((#prerequisites))
- `./stack dev` # Launch app with hot-reloading, via `skaffold debug --auto-sync=true`
  - See help: `skaffold -h`
  - Editing a `.py` file syncs it into the running container, where `uvicorn --reload` restarts the app
  - Changing `requirements.txt` needs a rebuild: press `r` at the skaffold prompt
- Expose the service: `./stack expose`
- Test
  - Request
    ```
    curl -s "localhost:8000/hello?name=foo"
    ```
  - Response
    ```
    {"greetings":"Hello, foo!"}
    ```

## Deploy
See `./stack -h`
