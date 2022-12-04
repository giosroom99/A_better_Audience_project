select pres_name,AVG(review1),AVG(review2),AVG(review3)
from aba_app_reviews,aba_app_presentation
where aba_app_presentation.id = aba_app_reviews.presentation_id
group by presentation_id