from cornice import Service
from colander import MappingSchema, SchemaNode, Int

class ScoreSchema(MappingSchema):
    score = SchemaNode(Int(), location="body", type='int')


hello = Service(name='hello', path='/', description="Simplest app")
scores = Service(name='scores', path='/scores')

SCORES = {}

@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@scores.post(schema=ScoreSchema)
def post_score(request):
    """Save score and return location in header."""

    request.response.status = 201
    request.response.headers['location'] = "10"
    SCORES["10"] = request.validated['score']
    return "ok"

@scores.get()
def get_scores(request):
  """Returns the current scores"""
  return {
    'scores': SCORES
  }
