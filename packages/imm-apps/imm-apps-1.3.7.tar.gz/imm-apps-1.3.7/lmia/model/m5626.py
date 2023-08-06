from .common import *
from basemodels.commonmodel import CommonModel, BuilderModel
from ..webform.webformmodel import WebformModel
from basemodels.finance import Finance
from basemodels.contact import Contacts
from basemodels.advertisement import (
    InterviewRecord,
    InterviewRecords,
    RecruitmentSummary,
)
import os
from basemodels.person import Person


class Emp5626(BaseModel):
    named: bool
    is_in_seasonal_industry: bool
    start_month: Optional[str]
    end_month: Optional[str]
    last_canadian_number: Optional[int]
    last_tfw_number: Optional[int]
    current_canadian_number: Optional[int]
    current_tfw_number: Optional[int]
    tp_waivable: bool
    waive_creteria: Optional[str]
    has_finished_tp: Optional[bool]
    finished_tp_result: Optional[str]
    activity1_title: Optional[str]
    activity1_description: Optional[str]
    activity1_outcome: Optional[str]
    activity1_comment: Optional[str]
    activity2_title: Optional[str]
    activity2_description: Optional[str]
    activity2_outcome: Optional[str]
    activity2_comment: Optional[str]
    activity3_title: Optional[str]
    activity3_description: Optional[str]
    activity3_outcome: Optional[str]
    activity3_comment: Optional[str]
    activity4_title: Optional[str]
    activity4_description: Optional[str]
    activity4_outcome: Optional[str]
    activity4_comment: Optional[str]
    activity5_title: Optional[str]
    activity5_description: Optional[str]
    activity5_outcome: Optional[str]
    activity5_comment: Optional[str]

    @root_validator
    def checkAnswers(cls, values):
        questions = [
            "tp_waivable",
            "has_finished_tp",
        ]
        explanations = [
            "waive_creteria",
            "finished_tp_result",
        ]
        qas = dict(zip(questions, explanations))
        for k, v in qas.items():
            if values.get(k) and not values.get(v):
                raise ValueError(
                    f"Since {k} is true, but you did not answer the question {v} in info-position sheet"
                )
        is_in_seasonal_industry = values.get("is_in_seasonal_industry", None)
        is_seasonal_vars = [
            values.get(var, None)
            for var in [
                "start_month",
                "end_month",
                "last_canadian_number",
                "last_tfw_number",
                "current_canadian_number",
                "current_tfw_number",
            ]
        ]
        if is_in_seasonal_industry and not all(v is not None for v in is_seasonal_vars):
            raise ValueError(
                "The position is in seasonal industry, but you didn't input all the information required"
            )

        return values


class Personal(Person):
    last_name: Optional[str]
    first_name: Optional[str]
    sex: Optional[str]
    dob: Optional[date]
    citizen: Optional[str]


class M5626Model(BaseModel, BuilderModel):
    lmiacase: LmiaCase
    general: General
    lmi: Lmi
    emp5626: Emp5626
    eraddress: List[ErAddress]
    contact: List[Contact]
    finance: List[Finance]
    joboffer: Joboffer
    personal: Personal
    personalassess: PersonalAssess
    position: Position
    advertisement: List[Advertisement]
    interviewrecord: List[InterviewRecord]
    rcic: Rcic
    recruitmentsummary: RecruitmentSummary

    def checkTFW(self):
        if self.emp5626.named and not all(
            [
                self.personal.first_name,
                self.personal.last_name,
                self.personal.sex,
                self.personal.citizen,
                self.personal.dob,
            ]
        ):
            raise ValueError(
                "Since TFW is name required, you haven't input all information required in info-personal sheet."
            )

    def make_web_form(self, output_json, upload_dir, rcic, *args, **kwargs):
        args = {
            "model_variable": "5626",
            "app": self,
            "output_json": output_json,
            "upload_dir": upload_dir,
            "rcic": rcic,
        }
        wf = WebformModel(**args)
        wf.save()

    def make_pdf_form(self):
        pass

    def context(self, *args, **kwargs):
        interview = InterviewRecords(self.interviewrecord)
        primary_contact = Contacts(self.contact).primary
        return {
            **self.dict(),
            "formatted_finance": [
                {
                    "year": f.year,
                    "formatted_revenue": f.formatted_revenue,
                    "formatted_net_income": f.formatted_net_income,
                    "formatted_retained_earning": f.formatted_retained_earning,
                }
                for f in self.finance
            ],
            "num_of_job_posts": Advertisements(self.advertisement).amount,
            "why_qualified": self.personalassess.why_qualified,
            "adv_summary": [
                {
                    "start_date": a.start_date,
                    "end_date": a.end_date,
                    "media": a.media,
                    "days": a.days,
                }
                for a in self.advertisement
            ],
            "high_wage": True
            if float(self.joboffer.hourly_rate) >= self.lmiacase.provincial_median_wage
            else False,
            "rs": {
                "resume_num": interview.resume_num,
                "canadian_num": interview.canadian_num,
                "unknown_num": interview.unknown_num,
                "foreigner_num": interview.foreigner_num,
                "total_canadian": interview.total_canadian,
                "total_interviewed_canadians": interview.total_interviewed_canadians,
                "canadian_records": interview.canadian_records,
            },
            "primary_contact": primary_contact,
            "within_2years": self.general.within_2years,
            "lmi_benefits": [
                self.lmi.job_creation_benefit,
                self.lmi.skill_transfer_benefit,
                self.lmi.fill_shortage_benefit,
                self.lmi.other_benefit,
            ],
            "duration": self.lmiacase.duration,
            "why_qualified": [
                item
                for item in [
                    self.personalassess.work_experience_brief,
                    self.personalassess.education_brief,
                    self.personalassess.competency_brief,
                    self.personalassess.language_brief,
                    self.personalassess.performance_remark,
                ]
                if item
            ],
            "employee_name": self.personal.full_name,
        }


class M5626ModelE(CommonModel, M5626Model):
    def __init__(self, excels=None, output_excel_file=None,language:str|None=None):
        from basemodels.utils import excel_language_path
        path=excel_language_path(language)        
        mother_excels = [
            path+"/recruitment.xlsx",
            path+"/pa.xlsx",
            path+"/er.xlsx",
            path+"/rep.xlsx",
            path+"/lmia.xlsx",
        ]
        super().__init__(excels, output_excel_file, mother_excels, globals())
