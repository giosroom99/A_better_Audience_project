


select pres_name, stage_name,pres_date,aba_app_presentation.stage_id
from aba_app_presentation, aba_app_stage
where aba_app_presentation.stage_id =10
group by aba_app_presentation.id
