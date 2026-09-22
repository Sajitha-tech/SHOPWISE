from rest_framework import permissions

class AdminOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
    # safe methods:GET HEAD OPTIONS 
        if request.method in permissions.SAFE_METHODS:   
            return True
        return request.user.is_staff
    
    
