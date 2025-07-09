from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('book/',views.book,name='book'),
    path('menu/',views.menu,name='menu'),
    path('menu_items/<int:pk>/',views.display_menu_item,name='menu_items'),
    path('bookings/',views.booking_list,name='bookings'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('tables/',views.table_list_page,name='table'),
    path('bookings/<int:user_id>/',views.user_bookings,name='user_bookings'),
    path('delete/<int:booking_id>/',views.delete_booking,name='delete'),
    path('update/<int:booking_id>/',views.update,name="Update"),
]