SELECT pres_name, question_text, avg(answer)
from aba_app_answer, aba_app_question, aba_app_presentation
where aba_app_question.id = aba_app_answer.question_id and aba_app_presentation.id =16
group by aba_app_answer.question_id