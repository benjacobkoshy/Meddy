from django.urls import path
from .views import home_page, EditAccountPage, ImageAddView, NotificationListView, NotificationMarkRead, NotificationMarkAllRead

urlpatterns = [
    path('home/',home_page,name="home_page"),
    path('edit_account/',EditAccountPage.as_view(),name="edit_account"),
    path('add_image/',ImageAddView.as_view(),name="add_image"),
    path('notifications/',NotificationListView.as_view(),name='notification'),
    path('notifications-mark-read/<int:notification_id>/',NotificationMarkRead.as_view(),name='notification_mark_read'),
    path('notifications-mark-all-read/',NotificationMarkAllRead.as_view(),name='notification-mark-all-read'),
    
]
