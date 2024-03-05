# # middleware.py

# from django.shortcuts import redirect
# from keycloak import KeycloakOpenID
# from django.conf import settings
# import requests  # Import requests module for making HTTP requests

# keycloak_openid = KeycloakOpenID(server_url=settings.KEYCLOAK_SERVER_URL,
#                                  realm_name=settings.KEYCLOAK_REALM,
#                                  client_id=settings.KEYCLOAK_CLIENT_ID,
#                                  client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)

# class KeycloakMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Check if the user is authenticated
#         print("is authenticated")
#         if request.user.is_authenticated:
#             # If the user is already authenticated, proceed with the request
#             return self.get_response(request)

#         # Check if the token is valid using Keycloak introspection endpoint
#         token = request.session.get('access_token')
#         if token:
#             introspection_url = f"{settings.KEYCLOAK_SERVER_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token/introspect"
#             introspection_data = {
#                 'token': token,
#                 'client_id': settings.KEYCLOAK_CLIENT_ID,
#                 'client_secret': settings.KEYCLOAK_CLIENT_SECRET,
#             }
#             introspection_response = requests.post(introspection_url, data=introspection_data)

#             if not introspection_response.json().get('active', False):
#                 # Redirect to Keycloak for authentication if the token is not valid
#                 return redirect(keycloak_openid.auth_url(request.build_absolute_uri()))

#         # Continue with the view logic for authenticated users
#         return self.get_response(request)
