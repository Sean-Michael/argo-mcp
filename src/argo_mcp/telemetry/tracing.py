"""
Tracing helper functions

Handles tracer operations, called by other modules.
"""

from opentelemetry import trace


def get_tracer():
    """Creates a Tracer with app instrumentation scope"""
    return trace.get_tracer("argo-mcp")


def record_caller(span, sub: str, role: str):
    """Tag spans with the oidc subject and role"""
    span.set_attribute("caller.sub", sub)
    span.set_attribute("caller.role", role)
