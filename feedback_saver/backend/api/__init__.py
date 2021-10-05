from .form import get_form, post_form

form_routes = [
    ("GET", "/feedback/{portal_id}", get_form, "get_form"),
    ("POST", "/feedback/{portal_id}", post_form, "post_form"),
]