from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='index'),


                  path('register', views.register_view, name='register'),
                  path('login', views.login_view, name='login'),
                  path('logout', views.logout_view, name='logout'),

                  # Presentation URL
                  path('presentations', views.presentation_views, name='presentations'),
                  path('create_presentation', views.create_presentation_views, name='create_presentation'),
                  path('update_pres/<int:id>', views.updatePresentation_view, name='update_presentation'),
                  path('delete_pres/<int:id>', views.deletePresentation_view, name='delete_presentation'),
                  path('detail_pres/<int:id>', views.PresentationDetail_view, name='detail_presentation'),
                  path('evaluate_pres/<int:id>', views.EvaluatePresentation_view, name='evaluate_presentation'),
                  #path('status/<int:id>', views.updatePresentation, name='changestatus'),

                  # Stage URL
                  path('stage', views.stage_view, name='stage'),
                  path('add_stage', views.add_stage_view, name='add_stage'),
                  path('update_stage/<int:id>', views.updateStage_view, name= 'update_stage'),
                  path('delete_stage/<int:id>', views.deleteStage_view, name='delete_stage'),
                  path('detail_stage/<int:id>', views.stageDetail_view, name='detail_stage'),
                  # path('status/<int:id>', views.presentationApproval_view, name='changestatus')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
