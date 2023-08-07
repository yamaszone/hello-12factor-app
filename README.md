# [12-Factor App](https://12factor.net/) Demo

## Prerequisites
- [Docker Engine](https://docs.docker.com/engine/install/)
- [`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/)
- Local Kubernetes (K8s) cluster using one of the following:
  - [Docker Desktop Kubernetes](https://docs.docker.com/desktop/kubernetes/)
  - [kind Kubernetes](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
  - [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- K8s-based development using one of the following:
  - [`odo` CLI](https://odo.dev/docs/overview/installation)
  - [`skaffold` CLI](https://skaffold.dev/docs/install/)
  - [`tilt` CLI](https://docs.tilt.dev/install.html)

## Develop
- Startup local Kubernetes cluster following docs in the [**Prerequisites**]((#prerequisites))
- `./stack dev <tool>` # Launch app with hot-reloading. `tool` can be `odo`, `skaffold`, or `tilt`
  - See help: `odo -h` or `skaffold -h` or `tilt -h`
- Test
  - Request
    ```
    curl -s http://0.0.0.0:8000/hello?name=foo
    ```
  - Response
    ```
    {"greetings":"Hello, foo!"}
    ```

## Deploy
See `./stack -h`
