from datetime import date
from typing import Optional, List
from pydantic import BaseModel, root_validator, EmailStr
from basemodels.commonmodel import CommonModel
from basemodels.address import Address
from basemodels.contact import ContactBase
from termcolor import colored
from basemodels.jobposition import PositionBase
from basemodels.jobofferbase import JobofferBase
from basemodels.person import Person, PersonalAssess


class LmiaCase(BaseModel):
    area_index: int
    province_index: int
    unemploy_rate: float
    area_median_wage: float
    noc_outlook: int
    reason_failed_hire_canadian: Optional[str]
    provincial_median_wage: float
    is_in_10_days_priority: Optional[bool]
    top10_wages: float
    is_waived_from_advertisement: bool
    purpose_of_lmia: str
    stream_of_lmia: str
    has_another_employer: bool
    another_employer_name: Optional[str]
    number_of_tfw: int
    duration_number: float
    duration_unit: str
    duration_reason: str
    has_attestation: bool
    is_waived_from_advertisement: bool
    reason_for_waived: Optional[str]
    provide_details_even_waived: Optional[str]
    use_jobbank: Optional[bool]
    reason_not_use_jobbank: Optional[str]


class Position(BaseModel):
    why_hire: str
    who_current_fill: str
    how_did_you_find: str
    how_when_offer: str
    worked_working: bool
    worked_working_details: Optional[str]


class Joboffer(JobofferBase):
    license_request: bool
    license_description: Optional[str]
    union: bool
    payment_way: str
    ot_after_hours_unit: Optional[str]
    ot_after_hours: Optional[float]
    is_working: bool
    has_probation: bool
    probation_duration: Optional[str]
    offer_date: date
    duties_brief: str
    duties: str
    english_french: bool
    oral: Optional[str]
    writing: Optional[str]
    reason_for_no: Optional[str]
    other_language_required: bool
    reason_for_other: Optional[str]
    education_level: str
    specific_edu_requirement: Optional[str]
    skill_experience_requirement: Optional[str]
    other_requirements: Optional[str]

    @root_validator
    def checkProbation(cls, values):
        has_probation = values.get("has_probation", None)
        probation_duration = values.get("probation_duration")
        if has_probation and not probation_duration:
            raise ValueError(
                "Since has probation is true, but did not input probation duration"
            )
        return values

    @root_validator
    def checkLanguage(cls, values):
        english_french = values.get("english_french", None)
        oral = values.get("oral", None)
        writing = values.get("writing", None)
        reason_for_no = values.get("reason_for_no", None)
        if english_french and (not oral or not writing):
            raise ValueError(
                "Since English or French is true, but did not input oral or/and writting language requirement"
            )
        if not english_french and not reason_for_no:
            raise ValueError(
                "Since there is no English or French requirement, but did not input the reason"
            )
        return values

    @root_validator
    def checkOtherLanguageReason(cls, values):
        other_language_required = values.get("other_language_required", None)
        reason_for_other = values.get("reason_for_other", None)
        if other_language_required and not reason_for_other:
            raise ValueError(
                "Since required other language in job offer sheet,but did not input the reason"
            )
        return values


class Lmi(BaseModel):
    brief_benefit: str
    job_creation_benefit: Optional[str]
    skill_transfer_benefit: Optional[str]
    fill_shortage_benefit: Optional[str]
    other_benefit: Optional[str]
    canadian_lost_job: bool
    canadian_lost_job_info: Optional[str]
    safety_concerns: str

    @root_validator
    def checkLabourDisput(cls, values):
        canadian_lost_job = values.get("canadian_lost_job", None)
        canadian_lost_job_info = values.get("canadian_lost_job_info", None)
        if canadian_lost_job and not canadian_lost_job_info:
            raise ValueError(
                "Since Canadian will lost job because of hiring TFW,but did not input the details about it."
            )
        return values


class LmiaRcic(BaseModel):
    lmiacase: LmiaCase
    position: Position
    joboffer: Joboffer
    lmi: Lmi
    personalassess: PersonalAssess


class LmiaRcicE(CommonModel, LmiaRcic):
    lmiacase: LmiaCase
    position: Position
    joboffer: Joboffer
    lmi: Lmi
    personalassess: PersonalAssess

    def __init__(self, excels=None, output_excel_file=None,language:str|None=None):
        from basemodels.utils import excel_language_path
        path=excel_language_path(language)
        mother_excels = [path+"/er.xlsx", path+"/lmia.xlsx", path+"/pa.xlsx"]
        super().__init__(excels, output_excel_file, mother_excels, globals())
