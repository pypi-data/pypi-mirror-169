from flask import Blueprint

blueprint = Blueprint(
    'siena_blueprint',
    __name__,
    url_prefix='/api/siena',
)
