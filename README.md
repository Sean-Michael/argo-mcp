# argo-mcp

A FastMCP/API Server for interacting with Argo Workflows through agents.

- Python + FastMCP
- OIDC auth (Keycloak/Asgardeo compatible)
- Role-based permission boundaries
- Approval gates
- OTel instrumentation


### Local Development Setup

First you need Argo Workflows installed.

To do that you also need a kubernetes cluster. 

I like KIND. 

```zsh
brew install kind
...
kind create cluster
```

Great, now for argo workflows. The easiest way is with helm.

```zsh
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

You have a choice here in how much pain you want to deal with to just setup something locally. If this is never going to leave your laptop and run in a port-forward, then `server` auth and SSL disabled is probably the way to go.. 

```zsh
helm install argo-workflows argo/argo-workflows \
  --namespace argo \
  --create-namespace \
  --set server.authModes="{server}" \
  --set server.secure=false
```

Once installed, you can access the UI without any pesky auth using port-forward:

```zsh
kubectl port-forward -n argo svc/argo-workflows-server 2746:
```

The app uses uv, you know the drill

```zsh
uv run fastapi dev server.py
```