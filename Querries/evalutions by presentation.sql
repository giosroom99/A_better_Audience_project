"""  This Querry returns all evaluation given to a presentations.
    * The query select the pres_name from the Presentations table filter where the presentation_id is equal to
        X in the Presentations table.   X is determine by the user

    * The query select the criteria from the Criterias table filter where the criteria_id is equal to
        the criteraia in the Evalution table.

    * The query select the evalution from the Evaluations table filter on the same rules as the above rule
    "

--     ############ General ############
select pres_name,criteria,evaluation
from aba_app_evaluation,aba_app_presentation,aba_app_criteria
where aba_app_presentation.id =2 and
        aba_app_criteria.id =aba_app_evaluation.criteria_id
group by pres_name, criteria, evaluation, criteria_id


--     ############ Most recent added or edited Evalutions ############
select pres_name,criteria,evaluation,aba_app_evaluation.updated_at as "last edited "
from aba_app_evaluation,aba_app_presentation,aba_app_criteria
where aba_app_presentation.id =2 and
        aba_app_criteria.id =aba_app_evaluation.criteria_id
group by pres_name, criteria, evaluation, criteria_id
--to see the latest evalution
order by  "last edited " DESC



--     ############ Most recent edited with date Added ############
select pres_name,criteria,evaluation,aba_app_evaluation.created_at as "Added on",aba_app_evaluation.updated_at as "Last edited "
from aba_app_evaluation,aba_app_presentation,aba_app_criteria
where aba_app_presentation.id =2 and
      aba_app_criteria.id =aba_app_evaluation.criteria_id
group by pres_name, criteria, evaluation, criteria_id
--to see the latest evalution
order by  "Last edited " DESC