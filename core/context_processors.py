import json
from .models import Cart

def cart_context(request):
    cart_data = []
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        # We must format the data exactly like the JavaScript expects it
        for item in cart_items:
            cart_data.append({
                'id': str(item.item.id), # JavaScript expects strings for dataset attributes
                'name': item.item.name,
                'price': float(item.item.price),
                'image': item.item.image.url if item.item.image else '',
                'quantity': item.quantity
            })
    
    # Use json.dumps to convert the Python list to a JSON string
    return {'cart_json': json.dumps(cart_data)}