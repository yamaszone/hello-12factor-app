docker_build('hello-12fa', '.')
k8s_yaml('deployments/app.yaml')
k8s_resource('hello-12fa', port_forwards=8000)
