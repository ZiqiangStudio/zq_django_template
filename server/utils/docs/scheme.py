from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from rest_framework_simplejwt.authentication import JWTAuthentication


class JWTTokenScheme(OpenApiAuthenticationExtension):
    target_class = JWTAuthentication
    name = "JwtTokenAuth"
    match_subclasses = True
    priority = 1

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
            bearer_format="JWT",
        )
