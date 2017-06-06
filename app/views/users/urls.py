from django.conf.urls import url, include
import views as users_views
import messages.views
import benefit_forms.views
import retirement.views


urlpatterns = [
    url(r'^$', users_views.index, name='users_index'),
    url(r'^new$', users_views.new_user, name='users_new'),
    url(r'^(?P<user_id>[0-9]+)/edit$', users_views.edit_user, name="user_edit"),
    url(r'^(?P<user_id>[0-9]+)/account_settings$', users_views.account_settings, name="user_account_settings"),
    url(r'^(?P<user_id>[0-9]+)$', users_views.user_view, name="user_view"),
    url(r'^(?P<user_id>[0-9]+)/messages/', include(messages.urls)),
    url(r'^(?P<user_id>[0-9]+)/benefit_forms/', include(benefit_forms.urls)),
    url(r'^(?P<user_id>[0-9]+)/retirement/', include(retirement.urls)),
]